from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery,name='gallery'),
    path('photo/<str:pk>/', views.viewphotos,name='photo'),
    path('add/', views.addphoto,name='add'),
    path('signup/',views.signup,name="signup"),
    path('login/',views.user_login,name="login")

]