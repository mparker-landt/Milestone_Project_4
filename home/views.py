from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

# Create your views here.
def about(request):
    """ A view to return the about us webpage """

    return render(request, 'home/about.html')