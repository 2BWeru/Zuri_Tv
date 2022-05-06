import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1,'sports', 'bbc','Todays top headlines','lllllllllll','wwww.news.com','oooooooooooooo','eng','21Jun')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))




if __name__ == '__main__':
    unittest.main()
