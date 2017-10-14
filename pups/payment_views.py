from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import render
 
from pups.models import Sale
from pups.forms import SalePaymentForm
 
def charge(request):
    if request.method == "POST":
        form = SalePaymentForm(request.POST)
 
        if form.is_valid(): # charges the card
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()
 
    return render(request, "pups/charge.html", {'form': form})