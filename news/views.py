from flask import render_template
from news import news

# views
@news.route('/')
def index():
     '''
     View root page function that returns the index page and its data
     '''
     message = 'Welcome to Zuri_Tv'
     return render_template('index.html', message = message)