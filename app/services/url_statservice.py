from app.db.database import get_db

def url_stats(short_code):
    db=get_db()
    cursor=db.cursor()
    
    sql="SELECT short_url,Original_url,Count_click FROM Shorten_url WHERE short_url=%s"
    cursor.execute(sql,(short_code,))
    
    url=cursor.fetchone()
    
    short_url=url[0]
    Original_url=url[1]
    Count_click=url[2]
    
    
    return{
        "Original_url":Original_url,
        "short_url":short_url,
        "click_count":Count_click
    }
    