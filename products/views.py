from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Album, Genre
from .forms import AlbumForm


def all_products(request):
    albums = Album.objects.all()
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
        'current_sort': current_sort
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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'How dare you? Only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[album.id]))
        else:
            messages.error(request, 'Failed to add product. \
                           Please ensure the form is valid.')
    else:
        form = AlbumForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'How dare you? Only store owners can do that.')
        return redirect(reverse('home'))

    album = get_object_or_404(Album, pk=product_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[album.id]))
        else:
            messages.error(request, 'Failed to update product. \
                            Please ensure the form is valid.')
    else:
        form = AlbumForm(instance=album)
        messages.info(request, f'You are editing {album.name}')

    template = 'products/update_product.html'
    context = {
        'form': form,
        'album': album,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'How dare you? Only store owners can do that.')
        return redirect(reverse('home'))

    album = get_object_or_404(Album, pk=product_id)
    if request.method == 'POST':
        album.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    template = 'products/delete-confirmation.html'
    context = {
        'album': album,
    }
    return render(request, template, context)
