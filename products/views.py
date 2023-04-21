from django.shortcuts import render, get_object_or_404
from .models import Album


def all_products(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    album = get_object_or_404(Album, pk=product_id)
    tracks = album.tracks.all()
    context = {
        'album': album,
        'tracks': tracks,
    }
    return render(request, 'products/product_detail.html', context)
