from runedexserver.database import database

KEYS = {
    "userAuth",
    "id",
    "name",
    "combatLevel",
    "hitpointsLevel",
    "attackLevel",
    "strengthLevel",
    "defenceLevel",
    "magicLevel",
    "rangedLevel",
    "maxHit",
    "attackStyle",
    "attackSpeed",
    "attackBonus",
    "stabBonus",
    "slashBonus",
    "crushBonus",
    "magicBonus",
    "rangedBonus",
    "strengthBonus",
    "rangedStrengthBonus",
    "magicStrengthBonus",
    "stabDefence",
    "slashDefence",
    "crushDefence",
    "magicDefence",
    "rangedDefence",
    "isSlayerTask",
    "isSlayerBossTask",
    "isPoisonImmune",
    "isCannonImmune",
    "isDemonbaneVulnerable",
    "isDragonbaneVulnerable",
    "vampyreTier",
}


class Runemon(database.Model):
    unique_key = database.Column(database.Integer, primary_key=True)
    unique_id_for_user_auth = database.UniqueConstraint("userAuth", "id", name="unique_id_for_user_auth")

    userAuth = database.Column(database.String)

    id = database.Column(database.Integer)
    name = database.Column(database.String)
    combatLevel = database.Column(database.Integer)
    hitpointsLevel = database.Column(database.Integer)
    attackLevel = database.Column(database.Integer)
    strengthLevel = database.Column(database.Integer)
    defenceLevel = database.Column(database.Integer)
    magicLevel = database.Column(database.Integer)
    rangedLevel = database.Column(database.Integer)
    maxHit = database.Column(database.Integer)
    attackStyle = database.Column(database.Integer)
    attackSpeed = database.Column(database.Integer)

    attackBonus = database.Column(database.Integer)
    stabBonus = database.Column(database.Integer)
    slashBonus = database.Column(database.Integer)
    crushBonus = database.Column(database.Integer)
    magicBonus = database.Column(database.Integer)
    rangedBonus = database.Column(database.Integer)
    strengthBonus = database.Column(database.Integer)
    rangedStrengthBonus = database.Column(database.Integer)
    magicStrengthBonus = database.Column(database.Integer)

    stabDefence = database.Column(database.Integer)
    slashDefence = database.Column(database.Integer)
    crushDefence = database.Column(database.Integer)
    magicDefence = database.Column(database.Integer)
    rangedDefence = database.Column(database.Integer)

    isSlayerTask = database.Column(database.String)
    isSlayerBossTask = database.Column(database.String)
    isPoisonImmune = database.Column(database.String)
    isCannonImmune = database.Column(database.String)
    isDemonbaneVulnerable = database.Column(database.String)
    isDragonbaneVulnerable = database.Column(database.String)

    vampyreTier = database.Column(database.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            combatLevel=self.combatLevel,
            hitpointsLevel=self.hitpointsLevel,
            attackLevel=self.attackLevel,
            strengthLevel=self.strengthLevel,
            defenceLevel=self.defenceLevel,
            magicLevel=self.magicLevel,
            rangedLevel=self.rangedLevel,
            maxHit=self.maxHit,
            attackStyle=self.attackStyle,
            attackSpeed=self.attackSpeed,
            attackBonus=self.attackBonus,
            stabBonus=self.stabBonus,
            slashBonus=self.slashBonus,
            crushBonus=self.crushBonus,
            magicBonus=self.magicBonus,
            rangedBonus=self.rangedBonus,
            strengthBonus=self.strengthBonus,
            rangedStrengthBonus=self.rangedStrengthBonus,
            magicStrengthBonus=self.magicStrengthBonus,
            stabDefence=self.stabDefence,
            slashDefence=self.slashDefence,
            crushDefence=self.crushDefence,
            magicDefence=self.magicDefence,
            rangedDefence=self.rangedDefence,
            isSlayerTask=self.isSlayerTask,
            isSlayerBossTask=self.isSlayerBossTask,
            isPoisonImmune=self.isPoisonImmune,
            isCannonImmune=self.isCannonImmune,
            isDemonbaneVulnerable=self.isDemonbaneVulnerable,
            isDragonbaneVulnerable=self.isDragonbaneVulnerable,
            vampyreTier=self.vampyreTier,
        )
