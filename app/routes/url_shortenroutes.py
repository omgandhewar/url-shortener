from flask import Flask, request, Blueprint
from flask_jwt_extended import jwt_required
from app.db.database import get_db
from app.services.url_shortenservice import url_shorten, getuser_url


urlshorten_bp=Blueprint("urlshorten_bp",__name__)

@urlshorten_bp.route("/urlshorten",methods=["POST"])
@jwt_required()
def urlshorten():
    data = request.get_json()

    if not data:
        return {"message": "Invalid JSON"}, 400
    return url_shorten(data)

@urlshorten_bp.route("/geturl",methods=["GET"])
@jwt_required()
def get_url():
    return getuser_url()

