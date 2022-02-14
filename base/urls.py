from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("articles/", views.articles, name = "articles"),
    path("astropy/", views.astropy, name = "astropy"),
    path("videos/", views.videos, name = "videos"),
    path("asteroids/", views.asteroids),
    path("stars/", views.stars),
    path("pulsars/", views.pulsars),
    path("dwarf/", views.dwarf),
    path("galaxy/", views.galaxy),
    path("comets/", views.comets),
    path("flare/", views.flare),
    path("meteors/", views.meteors),
    path("natural/", views.natural),
    path("nebulae/", views.nebulae),
    path("oort/", views.oort),
    path("planets/", views.planets),
    path("quasars/", views.quasars),
    path("white/", views.white),
    path("introduction/", views.introduction),
    path("dark/", views.dark),
]