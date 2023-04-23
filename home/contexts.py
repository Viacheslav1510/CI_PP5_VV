from products.models import Genre


def genres_contents(request):
    genres_list = Genre.objects.all()

    context = {
        'genres_list': genres_list,
    }

    return context
