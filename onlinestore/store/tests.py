# TESTS:
# Author: DA PARRY (16700090) - 2015

from django.core.urlresolvers import resolve 
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from store.views import home_page, categories_page, about_page, contact_page, specific_category_page, specific_item_page
from store.models import Item, Category

# To run this file: python manage.py test store

# These tests are run on the homepage and detect 
# whether it runs correctly and contains the correct tags

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)

		self.assertIn(b'<title>Douglas & sons</title>', response.content)

# tests that the categories page runs correctly

class CategoriesPageTest(TestCase):
	def test_categories_page_returns_correct_html(self):
		request = HttpRequest()
		response = categories_page(request)

		self.assertIn(b'<h1 id="page header">Product Categories</h1>', response.content)

	# This test asserts that the correct images are displayed on the page

	def test_categories_images_appear_correctly(self):
		request = HttpRequest()
		response = categories_page(request)

		self.assertIn(b'<img', response.content)
		for i in range(1, 3):
			self.assertIn(b'src=\"/static/categories' + str(i) + '.jpg\"', response.content)

# These tests assert that the about page loads correctly

class AboutPageTest(TestCase):
	def test_about_page_returns_correct_html(self):
		request = HttpRequest()
		response = about_page(request)

		self.assertIn(b'<h1 id="page header">About Douglas & sons</h1>', response.content)

	# This test asserts that the correct images are displayed on the page	

	def test_abput_page_images_appear_correctly(self):
		request = HttpRequest()
		response = contact_page(request)

		self.assertIn(b'<img', response.content)
		for i in range(1, 3):
			self.assertIn(b'src=\"/static/about' + str(i) + '.jpg\"', response.content)

# These tests assert that the correct HTML and content loads on the page			

class ContactPageTest(TestCase):
	def test_contact_page_returns_correct_html(self):
		request = HttpRequest()
		response = contact_page(request)

		self.assertIn(b'<h1 id="page header">Contact Douglas & sons</h1>', response.content)

	def test_contact_page_images_appear_correctly(self):
		request = HttpRequest()
		response = contact_page(request)

		self.assertIn(b'<img', response.content)
		self.assertIn(b'src=\"/static/contact1.jpg\"', response.content)




