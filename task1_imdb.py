import requests
from bs4 import BeautifulSoup
import pprint


def scrape_top_list():
    url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
    req=requests.get(url)
    html_content=req.content
    soup=BeautifulSoup(html_content,"html.parser")
    table=soup.find("table",{"data-caller-name":"imdb-featured-india"})

    movie=[]
    for i in table.find_all("a"):
        title=i.text.strip()
        movie.append(title)
        if '' in movie:
            movie.remove('')

    # print(len(movie))

    year=[]
    for i in table.find_all("span",{"class":"secondaryInfo"}):
        title=i.text.strip()
        year.append(title)

    rating=[]
    for i in table.find_all("td",{"class":"ratingColumn imdbRating"}):
        title=i.text.strip()
        rating.append(title)
   

    url=[]
    url1=[]
    for link in table.find_all("a"):
        data = link.get('href')
        link_text="https://www.imdb.com"+str(data)
        url.append(link_text)
        if link_text not in url1:
            url1.append(link_text)

    #Whole collection of data
    data_collection=[]
    web_data={ "name":" ","position":" ","year":" ","rating":" ","url":" "}
    for i in range(0,len(movie)):
        web_data["position"]=int(i+1)
        web_data["name"]=movie[i]
        year[i]=year[i][1:5]
        web_data["year"]=int(year[i])
        web_data["rating"]=float(rating[i])
        web_data["url"]=url1[i]
        data_collection.append(web_data.copy())
    # pprint.pprint(data_collection)
    return data_collection

# whole_data=scrape_top_list()
# pprint.pprint(whole_data)