from flask import Flask
from datetime import timedelta
from flask_cors import CORS
from app.flaskextension import bcrypt, jwt
from app.routes.auth_routes import auth_bp
from app.routes.url_shortenroutes import urlshorten_bp
from app.routes.url_redirectroutes import main
from app.routes.url_statsroutes import stats_bp


def create_app():
    
    app=Flask(__name__)
    
    app.config["SECRET_KEY"]="abc"
    app.config["JWT_SECRET_KEY"]="abc123"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(minutes=20)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"]=timedelta(days=30)
    
    
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(
        app,
        supports_credentials=True,
        origins=["http://127.0.0.1:5500"]
    )
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(urlshorten_bp)
    app.register_blueprint(main)
    app.register_blueprint(stats_bp)
    
    
    return app