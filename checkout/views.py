from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MwN0BBBWQhjq9UyATE3hTvpSODH77g6PQ67n5wxc7DkSdfXFsj8AHmaFJjaQ9yyRIhiEENhRSiybhh9tBS1AKLd00R9wtw6Sq',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
