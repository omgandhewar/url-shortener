from app.db.database import get_db

def url_stats(short_code):
    db=get_db()
    cursor=db.cursor()
    
    sql="SELECT Original_url,Count_click FROM Shorten_url WHERE short_url=%s"
    cursor.execute(sql,(short_code,))
    
    url=cursor.fetchone()
    
    Original_url=url[0]
    Count_click=url[1]
    
    
    return{
        "Original_url":Original_url,
        "click_count":Count_click
    }
    