from django.shortcuts import render, redirect


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def predict(request):
    return render(request, "prediction.html")


def pricing(request):
    return render(request, "pricing.html")
