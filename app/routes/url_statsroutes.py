from flask import Flask, Blueprint
from app.services.url_statservice import url_stats


stats_bp=Blueprint("stats_bp",__name__)

@stats_bp.route("/stats/<short_code>",methods=["POST"])
def urlstats(short_code):
    return url_stats(short_code)