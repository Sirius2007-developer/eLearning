from django.http import HttpResponse
from django.shortcuts import render
from .models import Gallery, Category, Course, Team, Test, Carousel
from .forms import NewsletterForm, ContactForm
from django.db.models import Q
# Create your views here.
def index(request):
    carousel = Carousel.objects.all()
    test = Test.objects.all()
    team = Team.objects.all()
    course = Course.objects.all()
    categ = Category.objects.all()
    context = {
        "course": course,
        "categ": categ,
        "team": team,
        "test": test,
        "carousel": carousel,
    }
    return render(request, "index.html", context=context)

def a404(request):
    return render(request, "404.html", context={})

def about(request):
    team = Team.objects.all()
    context = {
        "team": team,
    }
    return render(request, "about.html", context=context)

def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>So'rovingiz muvafaqqiyatli amalga oshirildi!")
    context = {
        "contact": contact,
    }
    return render(request, "contact.html", context=context)

def courses(request):
    test = Test.objects.all()
    course = Course.objects.all()
    categ = Category.objects.all()
    context = {
        "course": course,
        "categ": categ,
        "test": test,
    }
    return render(request, "courses.html", context=context)

def team(request):
    team = Team.objects.all()
    context = {
        "team": team,
    }
    return render(request, "team.html", context=context)

def testimonial(request):
    test = Test.objects.all()
    context = {
        "test": test,
    }
    return render(request, "testimonial.html", context=context)

def base(request):
    letter = NewsletterForm(request.POST or None)
    if request.method == "POST" and letter.is_valid():
        letter.save()
        return HttpResponse("<h2>Emailingiz muvafaqqiyatli yuborildi!</h2>")
    gallery = Gallery.objects.all()
    context = {
        "gallery": gallery,
        "letter": letter,
    }
    return render(request, "base.html", context=context)


def carouseldetailview(request, id):
    try:
        caro = Carousel.objects.get(id=id)
        context = {
            "caro": caro,
        }
    except caro.DoesNotExists:
        raise caro.Http404("No information found")
    return render(request, "carodetail.html", context=context)

def coursedetailview(request, id):
    try:
        cour = Course.objects.get(id=id)
        context = {
            "cour": cour,
        }
    except cour.DoesNotExists:
        raise cour.Http404("No information found")
    return render(request, "coursedetail.html", context=context)

def read(request):
    return render(request, "read.html", context={})

































