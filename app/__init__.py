from flask import Flask
from app.routes.url_shortenroutes import urlshorten_bp
from app.routes.url_redirectroutes import main
from app.routes.url_statsroutes import stats_bp


def create_app():
    
    app=Flask(__name__)
    
    app.config["SECRET_KEY"]="abc"
    
    app.register_blueprint(urlshorten_bp)
    app.register_blueprint(main)
    app.register_blueprint(stats_bp)
    
    
    return app