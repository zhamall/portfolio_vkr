from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),
    path("project/<int:id>/", views.project, name="project"),
]