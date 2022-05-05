from django.shortcuts import render, redirect
import datetime as d
import joblib

from . import data_entry, state


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def errorpage(request):
    return render(request, "error.html")


def pricing(request):
    return render(request, "pricing.html")


def predict(request):
    if request == "POST":
        model = joblib.load("../ml/models/model_jlib")

        form_data = request.POST.dict()

        name = form_data.get("Name")
        email = form_data.get("Email")
        f1 = float(form_data.get("lat"))
        f2 = float(form_data.get("long"))
        f3 = float(form_data.get("brightness"))
        f4 = float(form_data.get("frp"))
        f5 = int(form_data.get("time"))
        f6 = int(form_data.get("sat"))
        f7 = int(form_data.get("for_reserve"))
        f8 = int(form_data.get("ind_area"))
        f9 = int(form_data.get("for_area"))
        f10 = int(form_data.get("day"))
        f11 = int(form_data.get("month"))
        f12 = int(form_data.get("year"))

        feature_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")

        data_id = data_entry.insert_data(name, email, date, feature_list=feature_list)

        predict = model.predict([feature_list])

        data_entry.add_prediction_result(email, data_id, res=float(predict))

        # Update Dataset

        # Return Result

    return render(request, "prediction.html")


def result(request):
    print("RESULT")
    # return render(request, "result.html")
