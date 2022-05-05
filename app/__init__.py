from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

# Initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):
    # Most flask extensions need to be initialized before we can start using them. 
    # We do that in our __init__.py file 
    # Initializing application

    app = Flask(__name__)
    bootstrap.init_app(app)
    

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # Registering the blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .requests import configure_requests
    configure_requests(app)

    return app


        