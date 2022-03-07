from django.shortcuts import render

from . import data_entry


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

        f1 = form_data.get("Feature1")
        f2 = form_data.get("Feature2")
        f3 = form_data.get("Feature3")

        feature_list = [f1, f2, f3]

        data_entry.insert_data(feature_list=feature_list)

        #Prediction ML Function Call

        #Return Result

    return render(request, "prediction.html")


def pricing(request):
    return render(request, "pricing.html")


def result(request):
    print("RESULT")
    # return render(request, "result.html")
