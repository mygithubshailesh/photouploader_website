from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery,name='gallery'),
    path('photo/<str:pk>/', views.viewphotos,name='photo'),
    path('add/', views.addphoto,name='add'),

]