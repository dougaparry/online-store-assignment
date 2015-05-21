# Author: DA PARRY (16700090) - 2015
from django.conf.urls import include, url
from django.contrib import admin
from store import views

# A url pattern is matched by means of a regular expression to determine which
# view needs to be called when that URL is encountered

urlpatterns = [
    url(r'^obfuscate/', include(admin.site.urls)),
    url(r'^$', 'store.views.home_page', name='home'),
    url(r'^about', 'store.views.about_page', name='about'),
	url(r'^contact', 'store.views.contact_page', name='contact'),
	url(r'^categories$', 'store.views.categories_page', name='categories'),
	url(r'^categories/', 'store.views.specific_category_page', name='category_pages'),
	url(r'^[0-9]*$', 'store.views.specific_item_page', name='item_pages'),
]

