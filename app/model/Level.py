from app import db

class Level(db.Model):
    __tablename__ = "level"
    
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    
    def toJson(self):
        return { 
            "id":self.id, 
            "level":self.level, 
            "xp":self.xp
        }

    def getId(self):
        return self.id
    
    def getLevel(self):
        return self.level
    
    def getXp(self):
        return self.xp