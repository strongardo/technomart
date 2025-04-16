from itertools import product

from django.shortcuts import render, redirect
from catalog.models import Product
from .forms import FeedbackForm, SearchForm
from .models import Message


def home(request):
    products = Product.objects.filter(is_hit=True)
    return render(request, 'home.html', context={
        'hits': products
    })


def feedback_form(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        message = Message()
        message.name = form.cleaned_data['name']
        message.email = form.cleaned_data['email']
        message.text = form.cleaned_data['text']
        message.save()
    else:
        print(form.errors.as_text())
    return redirect('catalog_url')


def search_form(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        search_value = form.cleaned_data['search_value']
        products = Product.objects.filter(name__icontains=search_value)
        return render(request, 'catalog.html', context={
            'perfs': products
        })
    else:
        print(form.errors.as_text())
        return redirect("home.html")

