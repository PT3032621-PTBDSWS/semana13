from flask import Flask
from .models import db
from .routes import main
from config import Config

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(Config)

    # init db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # register blueprints
    app.register_blueprint(main)

    return app
