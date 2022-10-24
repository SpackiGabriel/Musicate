from app import db

class Progress(db.Model):
    __tablename__ = "progress"

    id = db.Column(db.Integer, primary_key=True)
    sheetmodule = db.Column(db.Integer)
    ciphermodule = db.Column(db.Integer)

    def getId(self):
        return self.id
    
    def getSheetModule(self):
        return self.sheetmodule
    
    def getCipherModule(self):
        return self.ciphermodule