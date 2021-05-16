from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def dynamic_lookup_view(request):
	obj = Product.objects.get(id=1)
	context = {
		"object" : obj
	}


# def render_initial_data(request):
# 	initial_data = {
# 		"title":"My this awesome title"
# 	}
# 	obj = Product.objects.get(id=1)
# 	form = ProductForm(request.POST or None, initial=obj)
# 	if form.is_valid():
# 		form.save()
# 	context = {
# 		'form':form
# 	}

# 	return render(request, "products/product_create.html")



def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
	'object': obj
	}
	return render(request, "product/product_detail.html", context)

# def product_create_view(request):
# 	my_form = RawProductForm(request.POST)
# 	if request.method == "POST":
# 		if my_form.is_valid():
# 			# the data is good
# 			print(my_form.cleaned_data)
# 			# Add more product
# 			Product.objects.create(**my_form.cleaned_data)

# 		else:
# 			print(my_form.errors)
# 	context = {
# 				"form": my_form
# 				}

# 	return render(request, "product/product_create.html", context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, "product/product_create.html", context)

# def product_create_view(request):
# #	print(request.GET['title'])
# 	# print(request.GET)
# 	# print(request.POST)
# 	if  request.method == 'POST':
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 	context = {}
# 	return render(request, "product/product_create.html", context)

