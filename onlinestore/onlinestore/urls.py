
from django.conf.urls import include, url
from django.contrib import admin
from store import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'store.views.home_page', name='home'),
    url(r'^about', 'store.views.about_page', name='about'),
	url(r'^contact', 'store.views.contact_page', name='contact'),
	url(r'^categories$', 'store.views.categories_page', name='categories'),
	url(r'^categories/', 'store.views.specific_category_page', name='category_pages'),
	url(r'^[0-9]*$', 'store.views.specific_item_page', name='item_pages'),
]

