from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Album, Genre


def all_products(request):
    albums = Album.objects.all()
    genres_list = Genre.objects.all()
    query = None
    genre = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'genre':
                sort_key = 'genre__name'
            if sort_key == 'name':
                sort_key = 'lower_name'
                albums = albums.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            albums = albums.order_by(sort_key)

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

    current_sort = f'{sort}_{direction}'
    context = {
        'albums': albums,
        'search_term': query,
        'genres_list': genres_list,
        'current_sort': current_sort
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    genres_list = Genre.objects.all()
    album = get_object_or_404(Album, pk=product_id)
    tracks = album.tracks.all()
    context = {
        'album': album,
        'tracks': tracks,
        'genres_list': genres_list,
    }
    return render(request, 'products/product_detail.html', context)
