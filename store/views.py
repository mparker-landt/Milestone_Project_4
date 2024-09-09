from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category, AuctionProduct, RentalProduct
from .forms import ProductForm, RentalForm, AuctionForm

# Create your views here.
def store(request):
    """ A view that renders the bag contents page """
    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'store/store.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'store/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'store/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('store'))


# Create your views here.
def rental(request):
    """ A view that renders the bag contents page """
    rentals = RentalProduct.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                rentals = rentals.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            rentals = rentals.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            rentals = rentals.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            rentals = rentals.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'rentals': rentals,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'store/store_rentals.html', context)

def rental_detail(request, rental_id):
    """ A view to show individual product details """

    rental = get_object_or_404(RentalProduct, pk=rental_id)

    context = {
        'rental': rental,
    }

    return render(request, 'store/rental_detail.html', context)

@login_required
def add_rental(request):
    """ Add a rental to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES)
        if form.is_valid():
            rental = form.save()
            messages.success(request, 'Successfully added rental!')
            return redirect(reverse('rental_detail', args=[rental.id]))
        else:
            messages.error(request, 'Failed to add rental. Please ensure the form is valid.')
    else:
        form = RentalForm()
        
    template = 'store/add_rental.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_rental(request, rental_id):
    """ Edit a rental in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    rental = get_object_or_404(RentalProduct, pk=rental_id)
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES, instance=rental)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated rental!')
            return redirect(reverse('rental_detail', args=[rental.id]))
        else:
            messages.error(request, 'Failed to update rental. Please ensure the form is valid.')
    else:
        form = RentalForm(instance=rental)
        messages.info(request, f'You are editing {rental.product.name}')

    template = 'store/edit_rental.html'
    context = {
        'form': form,
        'rental': rental,
    }

    return render(request, template, context)

@login_required
def delete_rental(request, rental_id):
    """ Delete a rental from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    rental = get_object_or_404(RentalProduct, pk=rental_id)
    rental.delete()
    messages.success(request, 'Rental deleted!')
    return redirect(reverse('rental'))


# Create your views here.
def auction(request):
    """ A view that renders the bag contents page """
    auctions = AuctionProduct.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                auctions = auctions.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            auctions = auctions.order_by(sortkey)
            
        # if 'category' in request.GET:
        #     categories = request.GET['category'].split(',')
        #     products = products.filter(category__name__in=categories)
        #     categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('store_auction'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            auctions = auctions.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'auctions': auctions,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'store/store_auction.html', context)

def auction_detail(request, auction_id):
    """ A view to show individual product details """

    auction = get_object_or_404(AuctionProduct, pk=auction_id)

    context = {
        'auction': auction,
    }

    return render(request, 'store/auction_detail.html', context)

@login_required
def add_auction(request):
    """ Add a rental to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save()
            messages.success(request, 'Successfully added auction!')
            return redirect(reverse('auction_detail', args=[auction.id]))
        else:
            messages.error(request, 'Failed to add auction. Please ensure the form is valid.')
    else:
        form = AuctionForm()
        
    template = 'store/add_auction.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_auction(request, auction_id):
    """ Edit a rental in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    auction = get_object_or_404(AuctionProduct, pk=auction_id)
    if request.method == 'POST':
        form = AuctionForm(request.POST, request.FILES, instance=auction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated auction!')
            return redirect(reverse('auction_detail', args=[auction.id]))
        else:
            messages.error(request, 'Failed to update auction. Please ensure the form is valid.')
    else:
        form = AuctionForm(instance=auction)
        messages.info(request, f'You are editing {auction.title}')

    template = 'store/edit_auction.html'
    context = {
        'form': form,
        'auction': auction,
    }

    return render(request, template, context)

@login_required
def delete_auction(request, auction_id):
    """ Delete a rental from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    auction = get_object_or_404(AuctionForm, pk=auction_id)
    auction.delete()
    messages.success(request, 'auction deleted!')
    return redirect(reverse('auction'))

