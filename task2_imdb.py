from task1_imdb import scrape_top_list
import pprint
whole_data=scrape_top_list()

def group_by_year(data_collection):
    # According to the year we have the data
    years_according=[]
    for i in data_collection:
        data_year=i
        if data_year not in years_according:
            years_according.append(data_year)
        movie_dic={i["year"]:[]for i in years_according}
        for i in data_collection:
            data_year=i["year"]
            for j in movie_dic:
                if str(j)==str(data_year):
                    movie_dic[j].append(i)
    return movie_dic

years=group_by_year(whole_data)
pprint.pprint(years)