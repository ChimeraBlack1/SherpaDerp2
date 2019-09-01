"""fuckaround URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('', include('pages.urls')),
    path('invoice/', include('invoice.urls')),
    path('products/', include('products.urls')),
    path('itemreceipts/', include('itemreceipts.urls')),
    path('customers/', include('customers.urls')),
    path('quotes/', include('quotes.urls')),
    path('proposals/', include('proposals.urls')),
    path('salesorders/', include('salesorders.urls')),
    path('purchaseorders/', include('purchaseorders.urls')),
    path('accounts/', include('accounts.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
