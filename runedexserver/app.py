import json
import logging
import os

from flask import Flask
from flask import request

from runedexserver.database import database
from runedexserver.runemon import KEYS
from runedexserver.runemon import Runemon

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///runedex.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
database.app = app
database.init_app(app)
database.create_all()


@app.route("/submit", methods=["POST"])
def submit():
    auth = request.headers.get("RUNEDEX-AUTH", None)
    log.debug("RUNEDEX-AUTH: %s", auth)
    if auth is None or len(auth) != 128:
        log.info("RUNEDEX-AUTH did not pass checks: %s", auth)
        return "RUNEDEX-AUTH required", 400

    for npc in json.loads(request.data):
        npc["userAuth"] = auth
        if set(npc.keys()) != KEYS:
            log.info("DATA did not pass checks: %s", npc)
            return "Bad data", 400

        # SQLite3 can't store booleans - so we'll use strings instead
        for k, v in npc.items():
            if isinstance(v, bool):
                npc[k] = str(v)

        runemon = Runemon(**npc)
        database.session.add(runemon)
        database.session.commit()
        log.debug("NPC inserted: %s", runemon)
    return "OK"


@app.route("/fetch", methods=["GET"])
def fetch():
    auth = request.headers.get("RUNEDEX-AUTH", None)
    log.debug("RUNEDEX-AUTH: %s", auth)
    if auth is None or len(auth) != 128:
        log.info("RUNEDEX-AUTH did not pass checks")
        return "RUNEDEX-AUTH required", 400

    values = []
    for runemon in Runemon.query.filter_by(userAuth=auth).all():
        npc = runemon.to_dict()
        values.append(npc)

    result = json.dumps(values)
    log.debug("Fetch result: %s", result)
    return result
