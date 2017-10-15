from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import stripe

from pups import stripe_settings
from pups.models import Puppy

stripe.api_key = stripe_settings.STRIPE_SECRET_KEY

def payment_form(request):

    context = { "stripe_key": stripe_settings.STRIPE_PUBLIC_KEY }
    return render(request, "pups/payment_form.html", context)

def checkout(request):

    """
    new_puppy = Puppy(
        name = "Blackjack",
        breed  = "Lab",
        age = "1",
        owner = 
    )
    """

    if request.method == "POST":
        token = request.POST.get("stripeToken")

        try:
            charge = stripe.Charge.create(
                amount = 50,
                currency = "usd",
                source = token,
                description = "The product charged to the user"
            )

            # new_puppy.charge_id = charge.id

        except stripe.error.CardError as ce:
            return False, ce

    else:
        # new_puppy.save()
        template = loader.get_template('pups/checkout.html')
        return HttpResponse(template.render({}, request))
        # return redirect("pups/thank_you_page")
        # The payment was successfully processed, the user's card was charged.
        # You can now redirect the user to another page or whatever you want
