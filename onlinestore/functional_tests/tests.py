# FUNCTIONAL TESTS:
# Author: DA PARRY (16700090) - 2015

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#to run this file: $ python manage.py  test functional_tests

class HomePageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the homepage loads correctly	
	def test_home_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Douglas & sons', self.browser.title)

		#test to ensure that the footer element loads correctly and contains the correct text
		footer_element = self.browser.find_element_by_id("footer")
		self.assertTrue(footer_element.text, 'Copyright &copy; 2015 Douglas & sons')

	# The following tests assert that the carousel elements load correctly
	def test_carousel(self):
		self.browser.get(self.live_server_url)
		carousel = self.browser.find_element_by_id("myCarousel")
		self.assertEqual(carousel.get_attribute('class'),
			'carousel slide')

		#test to determine the correct filepath location for the carousel image
		carousel_images = self.browser.find_elements_by_class_name('carouselImage')
		for image in carousel_images:
			self.assertIn( "/static/DS_banner_faded.png", image.get_attribute('src'))

	# The following tests assert that the 'cards' load correctly with the
	# correct information retrieved from the view
	def test_cards(self):
		self.browser.get(self.live_server_url)

		#test to determine the corretc filepath location for the image
		item_images = self.browser.find_elements_by_class_name('item_image')
		for image in item_images:
			self.assertIn("static", image.get_attribute('src'))

		#test to ensure that that the pricing element displays an R followed by numbers
		price_tag = self.browser.find_elements_by_class_name('pull-right')
		for price in price_tag:
			self.assertRegex(price.text, '^[R][0-9]')

class CategoriesPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# The following tests assert that the link works correctly from the home page
	# and that the categories page loads correctly 
	def test_categories_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Categories').click()
		page_header = self.browser.find_element_by_id('page header').text
		self.assertIn('Product Categories', page_header)

		# tests that the images are serving up the correct file path
		images = self.browser.find_elements_by_class_name("categories_images")
		for image in images:
			self.assertIn('/static/categories', image.get_attribute('src'))

class AboutPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# the following tests assert that the link works correctly 
	# and that the about page loads correctly	
	def test_about_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('About').click()
		page_header = self.browser.find_element_by_id('page header').text
		self.assertIn('About Douglas & sons', page_header)

class ContactPageTests(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	# the following tests assert that the link works correctly 
	# and that the contact page loads correctly	
	def test_contact_page_loads_correctly(self):
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_link_text('Contact').click()
		page_header = self.browser.find_element_by_id('page header').text
		self.assertIn('Contact Douglas & sons', page_header)
