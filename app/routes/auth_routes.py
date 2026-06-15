from flask import Flask, request, Blueprint

auth_bp=Blueprint("auth",__name__)

auth_bp.route("/login",methods=["POST"])
def login():
    return login_user(request.get_json())