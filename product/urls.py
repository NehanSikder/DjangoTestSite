from django.contrib import admin
from django.urls import path
from product.views import product_create_view, home_view, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = 'product'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', product_create_view),
    path('<int:id>/delete/', ProductDeleteView.as_view(), name='product-delete'),    
    path('<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:id>/update/', ProductUpdateView.as_view(), name='product-update'),
]