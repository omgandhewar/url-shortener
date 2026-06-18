from flask import Flask
from flask_jwt_extended import get_jwt_identity
from app.db.database import get_db
import random
import string

def generate_code(length=6):
    char=string.ascii_letters+string.digits
    return ''.join(random.choice(char) for _ in range(length))


def url_shorten(data):
    db=get_db()
    cursor=db.cursor()
    
    current_user=get_jwt_identity()
    
    original_url=data["url"]
    code=generate_code()
    
    sql="INSERT INTO Shorten_url(user_id,short_url,Original_url) VALUES(%s,%s,%s)"
    values=(current_user,code,original_url)
    
    cursor.execute(sql,values)
    
    db.commit()
    
    return{
        "message":"url added successfully"
    }
    
def getuser_url():
    db=get_db()
    cursor=db.cursor()
    
    current_user=get_jwt_identity()
    
    sql="SELECT short_url,Count_click FROM shorten_url WHERE user_id=%s"
    cursor.execute(sql,(current_user,))
    
    user_obj=cursor.fetchall()
    
    return{
        "mesage":user_obj
    }
    
    

    
