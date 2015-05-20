from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox() 

	def tearDown(self):
        self.browser.quit()

    def page_loads_correctly(self):
    	self.browser.get('http://localhost:8000')

    	#check that title and header mention 'Douglas & sons'
    	self.assertIn('Douglas & sons', self.browser.title)

if __name__ == '__main__':
	unittest.main()


