from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Create your views here.
def about(request):
    """ A view to return the about us webpage """

    return render(request, 'home/about.html')


# Create your views here.
def contact(request):
    """ A view to return the about us webpage """

    return render(request, 'home/contact.html')


# Create your views here.
def cookies(request):
    """ A view to return the about us webpage """

    return render(request, 'home/cookies.html')


# Create your views here.
def faq(request):
    """ A view to return the about us webpage """

    return render(request, 'home/faq.html')


# Create your views here.
def privacy(request):
    """ A view to return the about us webpage """

    return render(request, 'home/privacy.html')

# Create your views here.
def returns(request):
    """ A view to return the about us webpage """

    return render(request, 'home/returns.html')

# Create your views here.
def returnstart(request):
    """ A view to return the about us webpage """

    return render(request, 'home/returnstart.html')

# Create your views here.
def stories(request):
    """ A view to return the about us webpage """

    return render(request, 'home/stories.html')

# Create your views here.
def warranty(request):
    """ A view to return the about us webpage """

    return render(request, 'home/warranty.html')