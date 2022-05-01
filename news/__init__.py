from flask import Flask

news = Flask(__name__)   ##Initializing application

from news import views