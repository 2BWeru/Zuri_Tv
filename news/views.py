from flask import render_template
from news import news


# views
@news.route('/')
def index():
     '''
     View root page function that returns the index page and its data
     '''
     message = 'Welcome to Zuri_Tv'
     title = 'Home - Welcome to The best Movie Review Website Online'
     return render_template('index.html', message = message)