from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('agregar_producto',views.agregar_producto,name="agregar_producto"),
    path('show_product/<str:pk>',views.show_product,name="show_product"),
    path('editar_producto/<str:pk>',views.editar_producto,name="editar_producto"),
    path('borrar_producto/<str:pk>',views.borrar_producto,name="borrar_producto"),
    path('search_categoria/',views.search_categoria, name='search_categoria'),
    path('search/',views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



