from flask import render_template
from app import app
from ..requests import get_articles,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    article_news = get_articles('source')
    message = 'Hello World'
    print("inside views")
    print(article_news)
    return render_template('index.html',message = message, source = article_news)


@app.route('/article/<string:aurthor>')
def article(aurthor):

    '''
    View movie page function that returns the movie details page and its data
    '''
    article = get_article('aurthor')
    
    print(article)

    return render_template('article.html',article = article)
