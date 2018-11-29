from django.conf.urls import url, include

from pis_product.views import ProductItemList
from pis_product.views import ProductDetailList
from pis_product.views import AddNewProduct
from pis_product.views import AddProductItems
from pis_product.views import PurchasedItems
from pis_product.views import ExtraItemsView
from pis_product.views import ClaimedProductFormView
from pis_product.views import ClaimedItemsListView
from pis_product.views import StockItemList
from pis_product.views import AddStockItems
from pis_product.views import StockOutItems
from pis_product.views import StockDetailView


urlpatterns = [
    url(r'^items/list/$', ProductItemList.as_view(), name='items_list'),
    url(
        r'^item/(?P<pk>\d+)/detail/list/$',
        ProductDetailList.as_view(),
        name='item_details'
    ),
    url(
        r'^retailer/(?P<retailer_id>\d+)/add/$',
        AddNewProduct.as_view(),
        name='add_product'
    ),
    url(
        r'^item/(?P<product_id>\d+)/add/$',
        AddProductItems.as_view(),
        name='add_product_items'
    ),
    url(
        r'^items/purchased/$', PurchasedItems.as_view(),
        name='purchased_items'
    ),
    url(
        r'^items/extra/purchased/$', ExtraItemsView.as_view(),
        name='purchased_extra_items'
    ),
    url(
        r'^items/claimed/$', ClaimedProductFormView.as_view(),
        name='claimed_items'
    ),
    url(
        r'^items/claimed/list/$', ClaimedItemsListView.as_view(),
        name='claimed_items_list'
    ),
    url(
        r'^retailer/(?P<retailer_id>\d+)/add/$',
        AddNewProduct.as_view(),
        name='add_product'
    ),
    url(r'^stock/items/list/$', StockItemList.as_view(), name='stock_items_list'),
    url(
        r'^stock/item/(?P<product_id>\d+)/add/$',
        AddStockItems.as_view(),
        name='add_stock_items'
    ),
    url(
        r'^stock/item/(?P<product_id>\d+)/out/$',
        StockOutItems.as_view(),
        name='stock_out_items'
    ),
    url(
        r'^stock/item/(?P<product_id>\d+)/detail/$',
        StockDetailView.as_view(),
        name='stock_detail'
    ),
]