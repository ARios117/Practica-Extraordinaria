from django.shortcuts import render
from .cart import Cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.models import Book
from .models import Order, OrderItem
from decimal import Decimal
from .forms import OrderCreateForm


# @login_required
# def cart_add(request, book_slug):
#     """ add the book with slug " book_slug " to the
#     shopping cart . The number of copies to be bought
#     may be obtained from the form CartAddBookForm """
#     cart = Cart(request)
#     # your code goes here
#     # process the form to get units
#     # then call to cart . add

#     book = get_object_or_404(Book, slug=book_slug)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request:
#         form = CartAddBookForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             cart.add(book, quantity=form.cleaned_data['units'])

#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('all-borrowed'))

#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = CartAddBookForm()

#     return redirect('cart_list')

@login_required
def cart_view(request):

    cart = Cart(request)

    items = []

    for item in cart:
        items.append(item)

    context_dict = {}

    context_dict['items'] = items
    context_dict['total_price'] = cart.get_total_price()

    return render(request, 'orders/cart.html', context_dict)


@login_required
def order_remove(request, slug):

    cart = Cart(request)

    book = get_object_or_404(Book, slug=slug)

    cart.remove(book)

    return HttpResponseRedirect(reverse('cart_list'))


@login_required
def order_create(request):

    context_dict = {}
    cart = Cart(request)

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = OrderCreateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            order = Order(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                postal_code=form.cleaned_data['postal_code'],
                city=form.cleaned_data['city']
            )
            order.save()

            for b, v in cart.cart.items():
                book = Book.objects.get(id=b)
                orderItem = OrderItem(
                    order=order,
                    book=book,
                    price=Decimal(v['price']),
                    quantity=v['quantity']
                )
                orderItem.save()

            context_dict['order_id'] = order.id

            cart.clear()

            # redirect to a new URL:
            return render(request, 'orders/created.html', context_dict)

    # If this is a GET (or any other method) create the default form.
    else:
        form = OrderCreateForm()

    context_dict['form'] = form

    return render(request, 'orders/order_create.html', context_dict)
