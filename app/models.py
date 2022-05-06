
class News:
    '''
    Article class to define news Objects
    '''

    def __init__(self,id,title,author,description,content,url,urlToImage,language,publishedAt):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.content = content
        self.url = url
        self.urlToImage = urlToImage
        self.language = language
        self.publishedAt = publishedAt
        
