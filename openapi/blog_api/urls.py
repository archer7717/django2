
from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="posts"),
    path('about/',views.about, name='about'),
    path('deciptikon/',views.about, name='deciptikon')
]