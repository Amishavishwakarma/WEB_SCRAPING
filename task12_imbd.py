import requests
from bs4 import BeautifulSoup
def scrape_movie_cast(a):
    raw="https://www.imdb.com/title/"+a+"/fullcredits?ref_=tt_cl_sm#cast"
    req=requests.get(raw)
    html_content=req.content
    soup=BeautifulSoup(html_content,"html.parser")
    table_data=soup.find("table",class_="cast_list")
    actors=table_data.findAll("td",class_="")
    cast_list=[]
    for actor in actors:
        actor_dic={}
        imbd_id=actor.find('a').get('href')[6:15]
        name=actor.getText().strip()
        actor_dic['imdb_id']=str(imbd_id)
        actor_dic['name']=str(name)
        cast_list.append(actor_dic.copy())

    return (cast_list)
# a="tt0066763"
# scrape_movie_cast(a)