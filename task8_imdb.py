from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from task5_imbd import get_movie_list_detail
from bs4 import BeautifulSoup
# import requests
# import pprint
# import json
# import os
import requests,json,os,pprint,random,time


def cashing(top_movies):
    for i in top_movies:
        a=i["url"]
        id=a[27:36]
        # link=movie_detail_scrap(a)
        # with open(id+".json","w") as f:
        #     json.dump(link,f,indent=4)

        file_exist=os.path.exists(id+".json")
        if file_exist==True:
            with open(id+".json","r") as file1:
                data=file1.read()
                print( data)
        
        elif file_exist==False:
            data1=movie_detail_scrap(a)
            pprint.pprint(data1)
       




top_movies = scrape_top_list()
# movies_detail_list = get_movie_list_detail(top_movies[:10]) #  dekho kaise humne slicing ka use karke humne sirf pehli 10 movies input di. Yeh karna yaad rakhna :)
a=cashing(top_movies[:3]) # dekho kaise get_movie_list_details ki return value humne analyse_movies_language function mein de di 
print(a)




