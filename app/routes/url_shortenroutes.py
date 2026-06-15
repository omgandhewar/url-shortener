from flask import Flask, request, Blueprint
from app.db.database import get_db
from app.services.url_shortenservice import url_shorten


urlshorten_bp=Blueprint("urlshorten_bp",__name__)

@urlshorten_bp.route("/urlshorten",methods=["GET","POST"])
def urlshorten():
    return url_shorten(request.get_json())

