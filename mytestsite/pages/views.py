from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	#return HttpResponse("<h1>Hello world!<h1>")
	return render(request, "home.html", {})

def contact_view(*args, **kwargs):
		return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_numer": 123,
		"This_is_true":True,
		"my_list": [123, 2, 3, "AWdWA", 2.32],
		"my_html":"<h1>Hello world</h1>",
		"title":"abc this is about us"
	}

	return render(request, "about.html", my_context)

def social_view(*args, **kwargs):
	return HttpResponse("<h1>Hello world!<h1>")