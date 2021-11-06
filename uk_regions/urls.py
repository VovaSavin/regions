from django.urls import path

from . import views

urlpatterns = [
    path("all-regions/", views.ListReDicKoatuuRegionAPI.as_view()),
    path("all-regions/districts/<int:pk>", views.DistrictsAPI.as_view()),
    path("all-regions/cities/<int:pk>", views.RegionCenterAPI.as_view()),
]
