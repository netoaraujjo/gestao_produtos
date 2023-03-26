from django.urls import path
from . import views

app_name = "produtos"
urlpatterns = [
    path("", views.lista_produtos, name="lista_produtos"),
    path("detalhe/<int:id>/", views.detalhe_produto, name="detalhe_produto"),
    path("novo/", views.novo_produto, name="novo_produto"),
    path("editar/<int:id>/", views.editar_produto, name="editar_produto"),
    path("excluir/<int:id>/", views.excluir_produto, name="excluir_produto"),
]