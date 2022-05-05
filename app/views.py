from unicodedata import category
from flask import render_template
from  app import app
from .requests import  get_news
from .requests import get_articles,get_articles



# views
@app.route('/')
def index():
     '''
     View root page function that returns the index page and its data
     '''
     # Getting popular movie
     popular_news = get_news(category)
     # gb_news = get_news("gb")
     # br_news = get_news("br")
     # print(f"INSIDE VIEWS.PY{popular_news}")
     message = 'Welcome to Zuri_Tv'
     print(popular_news)
     # title = 'Home - Welcome to The best Movie Review Website Online'
     return render_template('index.html', message = message, popular = popular_news)

