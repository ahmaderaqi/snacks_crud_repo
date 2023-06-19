from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView,SnackDetailsView,SnacksListView,SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns = [
    
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('things',SnacksListView.as_view(), name="snacks"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snacks_detail"),
    path('create/',SnackCreateView.as_view(), name="snack_create"),
    path('update/<int:pk>',SnackUpdateView.as_view(), name="snack_update"),
    path('delete/<int:pk>',SnackDeleteView.as_view(), name="snack_delete"),
    
]