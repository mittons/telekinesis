from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('technology/', views.technology, name='technology'),
    path('travel/', views.travel, name='travel'),
    path('food/', views.food, name='food'),
    path('fashion/', views.fashion, name='fashion'),
    path('blogposttemplate/', views.blogposttemplate, name='blogposttemplate'),
    path('blogwysiwygtest/', views.blogwysiwygtest, name='blogwysiwygtest'),
]
