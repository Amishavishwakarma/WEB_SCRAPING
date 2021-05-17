from task1_imdb import scrape_top_list
import pprint
whole_data=scrape_top_list()
def group_by_decade(data_collection):
    #movie decade 
    movie_decade={}
    list_year=[]
    for i in data_collection:
        modulus=i["year"]%10
        decade=i["year"]-modulus
        if decade not in list_year:
            list_year.append(decade)
        list_year.sort()
        for k in list_year:
            movie_decade[k]=[]
        for j in movie_decade:
            dec10=j+9
            for y in data_collection:
                m=y["year"]
                if m<=dec10 and m>=j:
                    movie_decade[j].append(y)
                
    return movie_decade

movie_decade_year=group_by_decade(whole_data)
pprint.pprint(movie_decade_year)