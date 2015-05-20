from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class PageTest(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_home_page_loads_correctly(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Douglas & sons', self.browser.title)

	def test_categories_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Product Categories', self.browser.find_element_by_id('page header')



