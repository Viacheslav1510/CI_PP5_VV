from django.shortcuts import (render, redirect, reverse, get_object_or_404,
                              HttpResponse)
from django.contrib import messages

from products.models import Album


def bag_view(request):

    context = {

    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    album = get_object_or_404(Album, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Added {album.name} to your bag')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {album.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):

    album = get_object_or_404(Album, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    if quantity < 1:
        quantity = 1
    if quantity > 5:
        quantity = 5
    bag = request.session.get('bag', {})
    bag[item_id] = quantity
    messages.success(request, f'Updated {album.name} quantity')
    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):

    try:
        album = get_object_or_404(Album, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {album.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
