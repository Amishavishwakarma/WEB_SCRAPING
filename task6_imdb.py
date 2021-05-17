from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from task5_imbd import get_movie_list_detail
from bs4 import BeautifulSoup
import requests
import pprint


def analyse_movies_language(movie_detail):
    dic={}
    # pprint.pprint(movie_detail_list)
    for i in movie_detail:
        for lan in i["language"]:
            print(lan)
            if lan not in dic:
                dic[lan]=1
            else:
                dic[lan]+=1
    print(dic)


top_movies = scrape_top_list()
movies_detail = get_movie_list_detail(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
language_analysis = analyse_movies_language(movies_detail) # dekho kaise get_movie_list_details ki return value humne analyse_movies_language function mein de di 
print(language_analysis)