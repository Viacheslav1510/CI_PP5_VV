from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Album


@login_required
def wishlist(request):
    """
    View wishlist for logged in user
    """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        wishlist = Wishlist.objects.filter(user=profile)
    context = {
        'wishlist': wishlist,
        'profile': profile,
    }
    template = 'wishlist/wishlist.html'

    return render(request, template, context)
