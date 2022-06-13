from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.cart_view, name='cart_list'),
    # url(
    #         r'^(?P<pk>\d+)/remove/$',
    #         views.order_remove,
    #         name='cart_remove'
    #     ),
    path(
            '<slug:slug>/remove/',
            views.order_remove,
            name='cart_remove'
        ),
    url(r'^order_create/$', views.order_create, name='order_create'),
]
