from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name = "entry"),
    path("new/", views.new, name= "new"),
    path("edit/", views.edit, name= "edit" ),
    path("randompage/", views.randomPage, name= "randompage"),
    path("submitchanges/", views.submitChanges, name="submitchanges"),
    path("search/", views.search, name="search")
]
