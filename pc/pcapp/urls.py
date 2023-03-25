from django.urls import path
from pcapp import views

urlpatterns = [
    path('', views.index, name='index')

]
