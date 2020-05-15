from django.urls import path
from webfront import views

urlpatterns = [
    path('', views.index, name='index'),
    path('style.css', views.styles, name='styles')
]