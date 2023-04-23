from django.shortcuts import render
from products.models import Genre


def bag_view(request):
    genres_list = Genre.objects.all()

    context = {
        'genres_list': genres_list,
    }
    return render(request, 'bag/bag.html', context)
