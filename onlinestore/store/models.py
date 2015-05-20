import datetime 
from django.db import models 
from django.utils import timezone
from django.core.files import File
from django.db.models import Count

class Category(models.Model): 
	category_text = models.CharField(max_length=200) 
	pub_date = models.DateTimeField('date published')
	category_description = models.CharField(max_length=200, default='')

	def __unicode__(self):
		return self.category_text

	def get_category_name(self):
		return self.category_text

class Item(models.Model): 
	category = models.ForeignKey(Category) 
	item_text = models.CharField(max_length=200) 
	item_description = models.CharField(default=' ',max_length =400)
	price = models.IntegerField(default=0)

	thumbnail = models.ImageField(upload_to="thumbs/", blank=True, null=True, default='')
	image_source = models.CharField(max_length=300, null=True) #For referencing purposes - in order to attribute to the orginal owner of the content

	def image(self):
		return '<a href="/mdia/{0}"><img src="/media/{0}"></a>'.format(self.thumbnail)
	
	image.allow_tags = True

	def __unicode__(self):
		return self.item_text


		
