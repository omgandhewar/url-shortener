from flask import Flask, Blueprint
from app.services.url_redirectservice import url_redirect


main=Blueprint("main",__name__)

@main.route("/urlredirect/<short_code>",methods=["POST"])
def Urlredirect(short_code):
    return url_redirect(short_code)