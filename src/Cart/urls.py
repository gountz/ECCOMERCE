from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('Cart', views.cart, name="cart"), 
    path('add_product/<int:pk>/', views.add_product, name='add_product'),
    path('remove_product/<int:pk>/', views.remove_product, name='remove_product'),
    path('decrement_product/<int:pk>/', views.decrement_product, name='decrement_product'),
    path('clear/', views.clear_cart, name='clear_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)