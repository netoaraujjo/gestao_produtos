from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name="index"),
    path('sair/', views.sair, name='sair'),
] 