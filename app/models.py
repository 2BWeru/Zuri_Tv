from argparse import ArgumentDefaultsHelpFormatter


class Article:
    '''
    Article class to define news Objects
    '''

    def __init__(self,source,aurthor,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.aurthor = aurthor
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        

        
