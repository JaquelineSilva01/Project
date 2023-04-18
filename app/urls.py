from django.urls import path

from . import views

urlpatterns = [
    path('telaprincipal/', views.telaprincipal, name="telaprincipal"),
    path('inicio/', views.inicio, name="inicio"),
    path('causas/', views.causas, name="causas"),
    path('consequencias/', views.consequencias, name="consequencias"),
    path('solucoes/', views.solucoes, name="solucoes"),
    path('newpost/', views.newpost, name="newpost"),
    path('editar/<str:id>/', views.editar, name="editar"),
    path('atualizar_post/<str:id>/', views.atualizar_post, name="atualizar_post"),
    path('apagar_post/<str:id>/', views.apagar_post, name="apagar_post")
]