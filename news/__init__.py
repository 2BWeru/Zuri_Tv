from flask import Flask
from .config import DevConfig

news = Flask(__name__ , instance_relative_config = True)   ##Initializing application

# Setting up configuration
news.config.from_object(DevConfig)
news.config.from_pyfile('config.py')


from news import views