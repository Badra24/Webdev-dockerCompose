from app.extension import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    projects = db.relationship("Project", backref="user")

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "email":self.email,
            "project" : [project.serialize() for project in self.projects]

        }