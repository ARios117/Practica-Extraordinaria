from .cart import Cart

def cart_info(request):

    cart = Cart(request)

    units = 0
    
    if cart.cart:

        units = len(cart)
        total_price = cart.get_total_price()

    else:

        units = None
        total_price = None
    
    return {
        'num_items': units,
        'total_price': total_price
    }
