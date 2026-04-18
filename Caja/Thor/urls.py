from django.urls import path
from .views import caja, borrar_venta,editar_venta

urlpatterns = [
    path('', caja, name='caja'),
    path('borrar/<int:id>/', borrar_venta, name='borrar'),
    path('editar/<int:id>/', editar_venta, name='editar'),
]