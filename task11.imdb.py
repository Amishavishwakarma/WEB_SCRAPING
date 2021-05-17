from bs4 import BeautifulStoneSoup
from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from task5_imbd import get_movie_list_detail
import json


top_movies=scrape_top_list()
movie_detail=get_movie_list_detail(top_movies[:10])

def analyse_movies_genre(movie_detail):
    gener_list=[]
    for movie in movie_detail:
        # json_dic=json.loads(movie)
        gener=movie['gener']
        for i in gener:
            if i not in gener_list:
                gener_list.append(i)

    analyse_gener={gener_type:0 for gener_type in gener_list }
    for gener_type in gener_list:
        for movie in movie_detail:
            # json_dic=json.loads(movie)
            if gener_type in movie["gener"]:
                analyse_gener[gener_type]+=1

    print(analyse_gener)
analyse_movies_genre(movie_detail)