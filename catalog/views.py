from django.shortcuts import render
from django.views import generic
from .models import Book, Vote
from catalog.forms import FilterForm, VoteForm
from orders.forms import CartAddBookForm
from orders.cart import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    libros_mas_populares = Book.objects.order_by('-score')[:5]
    libros_mas_recientes = Book.objects.order_by('-date')[:5]

    context_dict = {}
    context_dict['libros_mas_populares'] = libros_mas_populares
    context_dict['libros_mas_recientes'] = libros_mas_recientes

    vote_count = {}
    for b in Book.objects.all():
        vote_count[b] = b.votes.count()

    list_sorted = []
    list_sorted = sorted(vote_count.items(), key=lambda x: x[1], reverse=True)[:5]

    libros_mas_votados = []
    for x, y in list_sorted:
        libros_mas_votados.append(x)

    context_dict['libros_mas_votados'] = libros_mas_votados

    return render(request, 'index.html', context_dict)


class BookDetailView(generic.DetailView):
    model = Book


def show_book(request, slug):

    context_dict = {}
    cart = Cart(request)

    try:
        book = Book.objects.get(slug=slug)

        context_dict['book'] = book

    except Book.DoesNotExist:

        context_dict['book'] = None

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request:
        form = CartAddBookForm(request.POST)
        vote_form = VoteForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cart.add(book, quantity=form.cleaned_data['quantity'])

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('cart_list'))

        if vote_form.is_valid():
            # process the data in form.cleaned_data as required
            Vote.objects.create(book=book, score=vote_form.cleaned_data['score'], user=request.user)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = CartAddBookForm()
        vote_form = VoteForm()

    context_dict['form'] = form
    context_dict['vote_form'] = vote_form

    return render(request, 'catalog/book_detail.html', context_dict)


class SearchView(generic.ListView):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')

        if query is None:
            query = ''

        return Book.objects.filter(title__icontains=query)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = FilterForm(initial={
            'search': self.request.GET.get('search', ''),
        })

        return context
