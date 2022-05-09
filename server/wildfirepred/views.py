from django.shortcuts import render
import datetime as d
import joblib

from . import data_entry


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
    if request.method == "POST":

        print("ENTERED POST REQUEST")

        model = joblib.load("../ml/models/model_jlib")

        form_data = request.POST.dict()

        name = form_data.get("_name")
        email = form_data.get("email")
        f1 = float(form_data.get("lat"))
        f2 = float(form_data.get("long"))
        f3 = float(form_data.get("bright"))
        f4 = float(form_data.get("frp"))
        f5 = int(form_data.get("time"))
        f6 = int(form_data.get("sat"))
        f7 = int(form_data.get("forest"))
        f8 = int(form_data.get("ind"))
        f9 = int(form_data.get("area"))
        f10 = int(form_data.get("day"))
        f11 = int(form_data.get("month"))
        f12 = int(form_data.get("year"))

        feature_list = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

        print(feature_list)

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")

        data_id = data_entry.insert_data(name, email, date, feature_list=feature_list)

        predict = model.predict([feature_list])

        float_res = round(float(predict[0]), 2)

        str_res = str(float_res)

        print(type(str_res), type(float_res))

        data_entry.add_prediction_result(email, data_id, res=float(predict))

        # Update Dataset

        return render(request, "prediction.html", {"result": str_res})

    return render(request, "prediction.html")
