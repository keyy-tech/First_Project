from itertools import product

from django.shortcuts import render, redirect
from invApp.models import Product
from invApp.forms import ProductForm


# Create your views here.
#
# Home View
def home_view(request):
    return render(request, "invApp/home.html")


# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    return render(request, "invApp/product_form.html", {"form": form})


# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "invApp/product_list.html", {"products": products})


# Update View
def product_update_view(request, product_id):
    products = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=products)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    return render(request, "invApp/product_form.html", {"form": form})


# Delete View
def product_delete_view(request, product_id):
    products = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        products.delete()
        return redirect("product_list")
    return render(request, "invApp/product_list.html", {"product": products})
