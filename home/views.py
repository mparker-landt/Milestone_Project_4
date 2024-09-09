from django.shortcuts import render, redirect, reverse, get_object_or_404

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
            enquiry = form.save(commit=False)
            enquiry.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect(reverse('contact'))

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
def enquiries(request):
    """ A view to return the about us webpage """

    enquiries = Enquiry.objects.all()

    context = {
        'enquiries': enquiries,
    }

    return render(request, 'home/enquiries.html', context)


# Create your views here.
def faq(request):
    """ A view to return the about us webpage """

    return render(request, 'home/faq.html')


# Create your views here.
def privacy(request):
    """ A view to return the about us webpage """

    return render(request, 'home/privacy.html')