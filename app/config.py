
class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=694a4a1c592845af94f1d1cfeca4f8d0'
    

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

