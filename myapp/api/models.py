from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String)
    wheel = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "wheel": self.wheel,    
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }