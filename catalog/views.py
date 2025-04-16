from django.shortcuts import render
from .models import Product
from .forms import Filter_form


def catalog(request):
    products = Product.objects.all()
    form = Filter_form(request.GET)
    if form.is_valid():
        manufacturers = form.cleaned_data["manufacturer"]
        minprice = form.cleaned_data["minprice"]
        maxprice = form.cleaned_data["maxprice"]
        if manufacturers:
            products = products.filter(manufacturer__in=manufacturers)
        if minprice:
            products = products.filter(price__gte=minprice)
        if maxprice:
            products = products.filter(price__lte=maxprice)
        return render(request, 'catalog.html', context={
                'perfs': products
            })
