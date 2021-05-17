from bs4 import BeautifulStoneSoup
from task1_imdb import scrape_top_list
from  task4_imbd import movie_detail_scrap
from task5_imbd import get_movie_list_detail
from task12_imbd import scrape_movie_cast
import pprint

top_movies=scrape_top_list()


def scrape_movie_with_casting(top_movies):
    for i in top_movies:
        url=i["url"]
        a=movie_detail_scrap(url)
        id=url[27:36]
        call=scrape_movie_cast(id)
        a["casting"]=call
        pprint.pprint(a)





casting=scrape_movie_with_casting(top_movies[:3])
print(casting)
