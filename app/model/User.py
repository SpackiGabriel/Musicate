from app import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    idprogress = db.Column(db.Integer, unique=True)
    idlevel = db.Column(db.Integer, unique=True)
    
    def toJson(self):
        return { 
            "id":self.id, 
            "name":self.name, 
            "email":self.email, 
            "password":self.password, 
            "idprogress":self.idprogress,
            "idlevel":self.idlevel
        }