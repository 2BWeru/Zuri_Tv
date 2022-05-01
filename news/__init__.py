from flask import Flask
from .config import DevConfig

news = Flask(__name__)   ##Initializing application

# Setting up configuration
news.config.from_object(DevConfig)

from news import views