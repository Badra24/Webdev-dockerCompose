from flask import Flask
from app.extension import db,migrate,jwt
from app.config import Config




def create_app(class_config=Config):
    # initialize and configure app
    app = Flask(__name__)
   
    app.config.from_object(class_config)

    # initialize db and migration
    db.init_app(app)
    migrate.init_app(app, db)

    # initialize jwt
    jwt.init_app(app)

    # register blueprint
    from app import auth, projects, tasks, views

    app.register_blueprint(auth.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(tasks.bp)
    app.register_blueprint(views.bp)

    with app.app_context():
        db.create_all()

    return app
