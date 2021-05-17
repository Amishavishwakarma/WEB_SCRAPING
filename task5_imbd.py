from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from bs4 import BeautifulSoup
import requests
import pprint
def get_movie_list_detail(top_movies):
    list_data_collection=[]
    for i in top_movies:
        url=i['url']
        # print(url)
        call=movie_detail_scrap(url)
        list_data_collection.append(call.copy())
    return (list_data_collection)
    # pprint.pprint(list_data_collection)


top_movies = scrape_top_list()
# a= get_movie_list_detail(top_movies[:10]) 
# print(get_movie_list_detail(top_movies[:10]))
# print(top_movies[:10])
# print (movie_detail_list)
# print(a)

