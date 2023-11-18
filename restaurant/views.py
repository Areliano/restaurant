from django.shortcuts import render

# Create your views

def index(request):
    return render(request, 'index.html', {"link":"index"})


def about(request):
    return render(request, "about.html", {"link":"about"})


def blog(request):
    return render(request, "blog.html", {"link":"blog"})


#def blog-single(request):
  #  return render(request, "blog-single.html", {"link":"blog-single"})


def contact(request):
    return render(request, "contact.html", {"link":"contact"})


def index(request):
    return render(request, "index.html", {"link":"index"})


def menu(request):
    return render(request, "menu.html", {"link":"menu"})


def reservation(request):
    return render(request, "reservation.html", {"link":"reservation"})
