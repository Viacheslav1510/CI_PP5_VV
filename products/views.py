from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Album, Genre


def all_products(request):
    albums = Album.objects.all()
    genres_list = Genre.objects.all()
    query = None
    genre = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            albums = albums.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

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
        'search_term': query,
        'genres_list': genres_list,
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
