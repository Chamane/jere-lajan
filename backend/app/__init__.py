from flask import Flask
from .config import Config
from .extensions import db, jwt, swagger
from .routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    swagger.init_app(app)
    
    # Add blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    return app