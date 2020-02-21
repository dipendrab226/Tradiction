from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'm0/home.html')


def about_dibs(request):
    return render(request, 'm0/aboutDibs.html')


def about_kevin(request):
    return render(request, 'm0/aboutZike.html')


def about_brian(request):
    return render(request, 'm0/aboutBrian.html')


def about_may(request):
    return render(request, 'm0/aboutMay.html')


def about_sanjay(request):
    return render(request, 'm0/aboutSanjay.html')


def about_ben(request):
    return render(request, 'm0/aboutBen.html')
