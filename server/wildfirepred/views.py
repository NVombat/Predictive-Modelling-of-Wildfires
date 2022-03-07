from django.shortcuts import render, redirect
import datetime as d

from . import data_entry, state


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def predict(request):
    if request == "POST":
        form_data = request.POST.dict()

        name = form_data.get("Name")
        email = form_data.get("Email")
        f1 = form_data.get("Feature1")
        f2 = form_data.get("Feature2")
        f3 = form_data.get("Feature3")

        feature_list = [f1, f2, f3]

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")

        data_entry.insert_data(name, email, date, feature_list=feature_list)

        # Prediction ML Function Call

        # Return Result

    return render(request, "prediction.html")


def pricing(request):
    return render(request, "pricing.html")


def result(request):
    print("RESULT")
    # return render(request, "result.html")
