from django.shortcuts import render

# Create your views here.

# Create your views here.
# Create your views here.
def checkout(request):
    """ A view that renders the bag contents page """
    return render(request, 'checkout/checkout.html')