from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, set_access_cookies
from app.services.auth_service import user_signup, login_user, user_logout, user_refreshtoken


auth_bp=Blueprint("auth",__name__)


@auth_bp.route("/signup",methods=["POST"])
def signup():
    return user_signup(request.get_json())

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    print("LOGIN ROUTE HIT")
    result=login_user(request.get_json())
    
    if not result["success"]:
         return jsonify(result),401
     
    response=jsonify({
        "message":result["message"]
    })
    
    set_access_cookies(response, result["token"])
    
    return response

@auth_bp.route("/refresh",methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    return user_refreshtoken(request.get_json())

@auth_bp.route("/logout",methods=["POST"])
@jwt_required(refresh=True)
def logout():
    return user_logout(request.get_json())