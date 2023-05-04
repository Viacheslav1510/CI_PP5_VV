from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


def contact_view(request):

    template = 'contact/contact.html'
    context = {}

    return render(request, template, context)