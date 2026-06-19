from app.db.database import get_db
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, get_jwt, create_refresh_token
from flask_bcrypt import generate_password_hash, check_password_hash
from app.flaskextension import bcrypt, jwt


def user_signup(data):
    db=get_db()
    cursor=db.cursor()
    
    name=data.get("username")
    email=data.get("email")
    password=data.get("password")
    
    sql="SELECT * FROM users WHERE username=%s"
    cursor.execute(sql,(name,))
    
    user_obj=cursor.fetchone()
    
    if user_obj:
        return{
            "success":False,
            "message":"user already exists"
        }
    
    hashed_password=bcrypt.generate_password_hash(password).decode("utf-8")
    
    sql="INSERT INTO users(username,email,password) VALUES(%s,%s,%s)"
    values=(name,email,hashed_password)
    
    cursor.execute(sql,values)
    
    db.commit()
    
    return{
        "success":True,
        "message":"user added successfully"
    }
    
    
    
def login_user(data):
    db=get_db()
    cursor=db.cursor()
    
    email=data.get("email")
    password=data.get("password")
    
    if not email or not password:
        return{
            "success":False,
            "mesasge":"email and password are required"
        }
    
    sql="SELECT id,email,password FROM users WHERE email=%s"
    cursor.execute(sql,(email,))
    
    user_obj=cursor.fetchone()
    
    if not user_obj:
        return{
            "success":False,
            "message":"Invalid email"
        },422
        
    hashed_password=user_obj[2]
        
    if not bcrypt.check_password_hash(hashed_password,password):
        return{
            "success":False,
            "message":"Invalid password"
        },422
        
        
    token=create_access_token(identity=str(user_obj[0]))
    refresh_token=create_refresh_token(identity=email)
    
    return{
        "success":True,
        "message":"login succesfully",
        "token":token,
        "refresh_token":refresh_token
    }      
    
    
def user_refreshtoken():
    
    current_user=get_jwt_identity
    
    access_token=create_refresh_token()
    
    return{
        "access_token":access_token
    }
    
    
@jwt.token_in_blocklist_loader
def check_in_blocklist_token(jwt_header,jwt_payload):
    db=get_db()
    cursor=db.cursor()
    
    jti=jwt_payload["jti"]
    
    sql="SELECT jti FROM token_id WHERE jti=%s"
    cursor.execute(sql,(jti,))
    
    user_obj=cursor.fetchone()
    
    return user_obj is not None


def user_logout():
    db=get_db()
    cursor=db.cursor()
    
    jti=get_jwt()["jti"]
    
    sql="INSERT INTO token_id(jti) VALUES(%s)"
    values=(jti,)
    
    cursor.execute(sql,values)
    
    db.commit()
    
    return{
        "message":"logout successfully"
    }
    
    