from app import app
import urllib.request,json
from .models import news


News = news.News

# Getting api key
# api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(country):
    ''''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(country)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        # print(type(get_news_response))                                            

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
           
    
    return news_results



def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for  news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        aurthor = news_item.get('aurthor')
        description =  news_item.get('description')
        content =  news_item.get('content')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        language = news_item.get('language')
        publishedAt = news_item.get('publishedAt')

        if description:
             news_object = News(id,title,aurthor,description,content,url,urlToImage,language,publishedAt)
             news_results.append(news_object)
            #  print(f"INSIDE PROCess NEWS{news_results} : {type(news_results)}")
    

    # print("INSIDE PROCESS NEWS")
    # print(news_results)

    return news_results


def get_articles(id):
    get_articles_details_url = base_url.format(id)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response:
            id = articles_details_response.get('id')
            name = articles_details_response.get('name')
            description =  articles_details_response.get('description')
            country =  articles_details_response.get('country')
            url = articles_details_response.get('url')
            language = articles_details_response.get('language')
            category = articles_details_response.get('category')
            

            articles_object = News(id,name,description,country,url,language,category)

    return articles_object
