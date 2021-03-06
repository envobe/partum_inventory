"""partum_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pis_com.urls')),
    url(r'^product/', include('pis_product.urls', namespace='product')),
    url(r'^retailer/', include('pis_retailer.urls', namespace='retailer')),
    url(r'^sales/', include('pis_sales.urls', namespace='sales')),
    url(r'^ledger/', include('pis_ledger.urls', namespace='ledger')),
    url(r'^expense/', include('pis_expense.urls', namespace='expense')),
    url(r'^employee/', include('pis_employees.urls', namespace='employee')),
    url(r'^supplier/', include('pis_supplier.urls', namespace='supplier')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
