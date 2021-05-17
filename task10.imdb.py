from bs4 import BeautifulStoneSoup
from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from task5_imbd import get_movie_list_detail

top_movies=scrape_top_list()
movie_detail=get_movie_list_detail(top_movies[:10])
def analyse_language_and_directors(movie_detail):
    director_dic={}
    for movie in movie_detail:
        for director in movie["director"]:
            director_dic[director]={}
    for i in range(len(movie_detail)):
        for director in director_dic:
            if director in movie_detail[i]["director"]:
                for language in movie_detail[i]["language"]:
                    director_dic[director][language]=0
    for i in range(len(movie_detail)):
        for director in director_dic:
            if director in movie_detail[i]["director"]:
                for language in movie_detail[i]['language']:
                    director_dic[director][language]=+1
    print(director_dic)


director_by_language=analyse_language_and_directors(movie_detail)
print(director_by_language)

