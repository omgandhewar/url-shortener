from flask import Flask, redirect
from app.db.database import get_db


def url_redirect(short_code):
    db=get_db()
    cursor=db.cursor()
    
    sql="SELECT Original_url,Count_click FROM Shorten_url WHERE short_url=%s"
    cursor.execute(sql,(short_code,))
    
    short_url=cursor.fetchone()
    
    if not short_url:
        return{
            "message":"url not available"
        }
    
    Original_url=short_url[0]
    Count_click=short_url[1]


    Count_click+=1
 
    sql="UPDATE Shorten_url SET Count_click=%s WHERE short_url=%s"
    cursor.execute(sql,(Count_click,short_code))
    
    db.commit()
    
    return redirect(Original_url)



