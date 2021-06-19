from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def customer(request):
    return render(request, "home.html")


def courier(request):
    return render(request, "home.html")
