"""bookshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/page/', permanent=True)),
]

# urlpatterns += [
#     path('page/', views.index, name='index'),
# ]

# urlpatterns += [
#     path('page/', views.index, name='home'),
# ]

urlpatterns += [
    path('page/', include('catalog.urls')),
]

urlpatterns += [
    path('orders/', include('orders.urls')),
]

urlpatterns += [
    path('accounts/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
