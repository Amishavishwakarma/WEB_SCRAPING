from task1_imdb import scrape_top_list
from bs4 import BeautifulSoup
import requests



def movie_detail_scrap(url1):
    page=requests.get(url1)
    soup=BeautifulSoup(page.text,"html.parser")
    #here We scrap movie name
    tittle_div=soup.find('div',class_="title_wrapper").h1.get_text()
    movie_name=''
    for i in tittle_div:
        if "(" not in i:
            movie_name=(movie_name + i).strip()
        else:
            break    
    #for run time and gener
    sub_div=soup.find('div',class_="subtext")
    #this is for runtime
    run_time=sub_div.find('time').get_text().strip()
    runtime_hours=int(run_time[0])*60
    if "min" in sub_div:
        runtime_minutes=int(run_time[3:]).strip('min')
        movie_runtime=runtime_hours+runtime_minutes
    else:
        movie_runtime=runtime_hours

    #Movie gener
    gener=sub_div.find_all("a")
    gener.pop()
    movie_gener=[i.get_text() for i in gener]
    summary=soup.find('div',class_="plot_summary")
    #this is for movie bio and movie director
    movie_bio=summary.find('div',class_="summary_text").get_text().strip()
    #here i scrap the director name
    director=summary.find('div',class_="credit_summary_item")
    director_list=director.find_all('a')
    movie_director=[i.get_text().strip() for i in director_list]

    #language details
    extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
    lists_of_divs=extra_details.find_all('div')
    for div in lists_of_divs:
        tag_h4=div.find_all('h4')
        for text in tag_h4:
            if 'Language:' in text:
                tag_anchor=div.find_all('a')
                movie_language=[language.get_text() for language in tag_anchor]
    
    #find the poster 
    movie_poster_link=soup.find('div',class_="poster").a['href']
    movie_poster="https://www.imdb.com"+movie_poster_link
    
    #created dic for all
    movie_detail_dic={"name":" ","director":" ","bio":" ","runtime":" ","gener":" ","language":" ","poster_link":" "}
    movie_detail_dic["name"]=movie_name
    movie_detail_dic["director"]=movie_director
    movie_detail_dic["bio"]=movie_bio
    movie_detail_dic["runtime"]=movie_runtime
    movie_detail_dic["gener"]=movie_gener
    movie_detail_dic["language"]=movie_language
    
    movie_detail_dic["poster_link"]=movie_poster

    return movie_detail_dic



url=scrape_top_list()
# url1=url[0]["url"]
# print(movie_detail_scrap(url1))
# print(len(url))
# j=1
# for i in url:
#     print(j,movie_detail_scrap(i['url']))
#     j=j+1

