# Author: DA PARRY (16700090) - 2015
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from store.models import Category, Item

'''
This view function creates a list, the size of the number of items stored in the database
This list stores each item object returned from the database
Finally, the function renders the home page when requested, sending the item-object-list as a variable
'''
def home_page(request):
	item_list = list()
	count = Item.objects.count()
	for itemID in range(1, count +1):
		item_list.append(Item.objects.get(id=itemID))

	return render(request, 'home.html', {'content': item_list})

'''
The following 2 functions renders the about template and the contact template when called upon by the corresponding url matcher
'''
def about_page(request):
	return render(request, 'about.html')

def contact_page(request):
	return render(request, 'contact.html')

'''
This view function creates a list, the size of the number of categories stored in the database
This list stores each category object returned from the database
Finally, the function renders the category page when requested, sendiing the category object list as a variable
'''
def categories_page(request):
	name_list = list()
	count = Category.objects.count()
	for catID in range(1, count + 1):
			name_list.append(Category.objects.get(id=catID))

	return render(request, 'categories.html', {'content': name_list})

'''
This view function creates a list, the size of the number of categories stored in the database
This list stores each category object returned from the database
Finally, the function renders the specific category page when requested, 
sending the category-object-list, the number of items in this category as well as a list of items
in the category as variables
'''
def specific_category_page(request):
	url = request.build_absolute_uri()
	splits = url.split('/')
	categoryName = splits[4]

	categoryObject = Category.objects.get(category_text=categoryName)
	numItems = Item.objects.filter(category=categoryObject.id).count

	item_list = Item.objects.filter(category=categoryObject.id)

	return render(request, 'category.html', {'categoryForTemplate': categoryObject, 'numItems': numItems, 'items': item_list})

'''
This function renders the page for a specific Item
sending the item object as a variable to the rendered page
'''
def specific_item_page(request):
	url = request.build_absolute_uri()
	splits = url.split('/')
	itemID = splits[3]

	itemObject = Item.objects.get(id=itemID)
	return render (request, 'item.html', {'content': itemObject})


