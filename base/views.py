from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def articles(request):
    return render(request, "articles.html")

def asteroids(request):
    return render(request, "asteroids.html")

def stars(request):
    return render(request, "stars.html")

def pulsars(request):
    return render(request, "pulsars.html")

def dwarf(request):
    return render(request, "dwarf.html")

def galaxy(request):
    return render(request, "galaxy.html")

def astropy(request):
    return render(request, "astropy.html")

def videos(request):
    return render(request, "videos.html")

def comets(request):
    return render(request, "comets.html")

def flare(request):
    return render(request, "flare.html")

def meteors(request):
    return render(request, "meteors.html")

def natural(request):
    return render(request, "natural.html")

def nebulae(request):
    return render(request, "nebulae.html")

def oort(request):
    return render(request, "oort.html")

def planets(request):
    return render(request, "planets.html")

def quasars(request):
    return render(request, "quasars.html")

def white(request):
    return render(request, "white.html")

def introduction(request):
    return render(request, "introduction.html")

def dark(request):
    return render(request, "dark.html")
