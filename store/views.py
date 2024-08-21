from django.shortcuts import render

# Create your views here.
def store(request):
    """ A view that renders the bag contents page """
    return render(request, 'store/store.html')