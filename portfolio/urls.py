from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="portfolio"),
    path("insert-about", views.insert_about, name='insert_about'),
    path("about-info", views.get_about, name='about_info'),
]