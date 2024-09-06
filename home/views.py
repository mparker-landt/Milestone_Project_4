from django.shortcuts import render, get_object_or_404

from .models import Enquiry
from .forms import EnquiryForm

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
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EnquiryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EnquiryForm()

    template = 'home/contact.html'
    context = {
        'form': form,
        # 'orders': orders,
        # 'on_profile_page': True
    }

    return render(request, template, context)

# Create your views here.
def contact_success(request):
    """ A view to return the about us webpage """

    return render(request, 'home/contact_success.html')


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