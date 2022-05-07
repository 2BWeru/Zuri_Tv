import unittest
from app.models import article
Article = article.Article



class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article({"id:null","name:BBC"},"Elizabeth Wolfe, Ryan Young, Jaide Timm-Garcia and Paradise Afshar, CNN", 'Vehicle found in search for missing Alabama inmate and corrections officer - CNN','US Marshals found an orange 2007 Ford Edge associated with Vicky White and inmate Casey White in a tow lot in Williamson County, Tennessee.',' "https://www.cnn.com/2022/05/06/us/vicky-white-casey-white-alabama-manhunt-friday/index.html','"https://cdn.cnn.com/cnnnext/dam/assets/220501071557-vicki-white-casey-white-super-tease.jpg','2022-05-06T18:20:00Z',"(CNN)The escape vehicle used by Vicky White and Casey White, the missing former Alabama corrections officer and inmate, has been found, the US Marshals office said. \r\nThe orange 2007 Ford Edge SUV wa… [+6195 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))




if __name__ == '__main__':
    unittest.main()
