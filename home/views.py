from django.shortcuts import render
from products.models import Album, Genre


def index(request):
    genres_list = Genre.objects.all()

    context = {
        'genres_list': genres_list,
    }
    return render(request, 'home/index.html', context)
