from flask import Flask
from app.db.database import get_db
import random
import string

def generate_code(length=6):
    char=string.ascii_letters+string.digits
    return ''.join(random.choice(char) for _ in range(length))


def url_shorten(data):
    db=get_db()
    cursor=db.cursor()
    
    original_url=data["url"]
    code=generate_code()
    
    sql="INSERT INTO Shorten_url(short_url,Original_url) VALUES(%s,%s)"
    values=(code,original_url)
    
    cursor.execute(sql,values)
    
    db.commit()
    
    return{
        "message":"url added successfully"
    }
    
    

    
