from django.shortcuts import render
from .models import Album


def all_products(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'products/products.html', context)
