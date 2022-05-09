from flask import render_template,url_for
from . import main
from ..requests import get_articles,get_article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    articles_news = get_articles('source')
    message = 'Hello World'
    return render_template('index.html',message = message, articles = articles_news)


@main.route('/article/<article_id>')
def article(aurthor):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article_news = get_article('source')
    
    print(article)

    return render_template('article.html',article = article_news)
