from flask import Flask, Blueprint
from app.services.url_redirectservice import url_redirect


main=Blueprint("main",__name__)

@main.route("/<short_code>",methods=["GET","POST"])
def Urlredirect(short_code):
    
    return url_redirect(short_code)