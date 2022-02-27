from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('add/', views.add,name="add"),
    path('cook/', views.cook,name="cook"),
    path('cook/recom', views.recom,name="recom"),
]
