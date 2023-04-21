from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Album


def all_products(request):
    albums = Album.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            albums = albums.filter(queries)

    context = {
        'albums': albums,
        'search_term': query
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
