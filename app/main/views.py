from unicodedata import category
from flask import render_template
from . import main
from ..requests import  get_news,get_articles




# views
@main.route('/')
def index():
     '''
     View root page function that returns the index page and its data
     '''
     message = 'Welcome to Zuri_Tv'
     # Getting popular movie
     

     news= get_news()
     # headlines = get_headlines()
     return render_template('index.html',user = news)

     
     print(popular_news)
     # title = 'Home - Welcome to The best Movie Review Website Online'
     # return render_template('index.html', message = message, popular = popular_news)


@main.route('/news/<int:id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    
    article = get_articles(id)
    title = f'{articles.title}'

    return render_template('articles.html',title = title,articles = articles,id=id)


