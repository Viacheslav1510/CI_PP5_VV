from django.shortcuts import render


def bag_view(request):

    context = {

    }
    return render(request, 'bag/bag.html', context)
