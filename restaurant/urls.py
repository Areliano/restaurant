
from django.urls import path

from . import views

#app_name = "rest"

urlpatterns = [
    path("", views.about, name="index"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("blog-single", views.blog-single, name="blog-single"),
    path("contact", views.contact, name="contact"),
    path("menu", views.menu, name="menu"),
    path("reservation", views.reservation, name="reservation")

]