from django.urls import path
from webfront import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]