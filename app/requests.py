from unicodedata import category
import urllib.request,json
from .models import Article



base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['NEWS_API_BASE_URL']


def get_articles(category):
    ''''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
                                                  

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_results(article_results_list)

   
    return article_results



def process_results(article_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    article_results = []
    for  article_item in article_list:
         source = article_item.get('source')
         aurthor = article_item.get('aurthor')
         title = article_item.get('title')
         description =  article_item.get('description')
         url = article_item.get('url')
         urlToImage = article_item.get('urlToImage')
         publishedAt = article_item.get('publishedAt')
         content=  article_item.get('content')
         
         
         
         if id:
             article_object = Article(source,aurthor,title,description,url,urlToImage,publishedAt,content)
             article_results.append(article_object)
     
    return article_results


def get_article(aurthor):
    get_article_details_url = base_url.format(aurthor)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)
        
        print(article_details_response)
        article_object = None
        
        if article_details_response:
            aurthor = article_details_response.get('aurthor')
            source = article_details_response.get('source')
            title = article_details_response.get('title')  
            description =  article_details_response.get('description')
            url = article_details_response.get('url')
            urlToImage = article_details_response.get('urlToImage')
            publishedAt = article_details_response.get('publishedAt')
            content =  article_details_response.get('content')


        article_details_response= Article(source,title,aurthor,description,url,urlToImage,publishedAt,content)
        
        
        
    return article_details_response

