from django.shortcuts import render
from products.models import Album, Genre


def index(request):
    albums = Album.objects.all()
    genres_list = Genre.objects.all()

    context = {
        'albums': albums,
        'genres_list': genres_list,
    }
    return render(request, 'home/index.html', context)
