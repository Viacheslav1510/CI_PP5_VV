from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import ContactForm


def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


def contact_view(request):
    if request.method == 'POST':
        email = request.user.email
        contact_form = ContactForm(request.POST, initial={'email': email})
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.info(request, "Massage has been sent")
        return render(request, 'contact/message-received.html')
    else:
        email = request.user.email
        contact_form = ContactForm(initial={'email': email})
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form
    }

    return render(request, template, context)
