from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='home'),
    # url(
    #         r'^book/(?P<pk>\d+)$',
    #         views.BookDetailView.as_view(),
    #         name='book-detail'
    #     ),
    # url(
    #         r'<slug:category_name_slug>/',
    #         views.BookDetailView.as_view(),
    #         name='book-detail'
    #     ),
    path(
            'book/<slug:slug>/',
            views.show_book,
            name='detail'
        ),
    path(
            'book/<slug:slug>/',
            views.show_book,
            name='cart_add'
        ),
    # url(
    #         r'^search/(?P<busqueda>[-a-zA-Z0-9_]+)/$',
    #         views.search,
    #         name='books'
    #     ),
    url(r'^books/$', views.SearchView.as_view(), name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
