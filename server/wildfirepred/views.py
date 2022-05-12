from django.shortcuts import render
import datetime as d
import joblib

from . import data_entry
from .errors import (
    UserDoesNotExistError,
    ResultUpdationError,
    FileInsertionError,
    InvalidDataIDError,
)


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
        try:
            model = joblib.load("../ml/models/model_jlib")
        except Exception:
            print("Could Not Load Model Successfully")

        try:
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

        except Exception:
            print("Unable To Fetch Form Data")

        feature_list = [f1, f2, f3, f6, f4, f5, f7, f8, f9, f12, f11, f10]

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")

        try:
            data_id = data_entry.insert_data(
                name, email, date, feature_list=feature_list
            )

            predict = model.predict([feature_list])
            float_res = round(float(predict[0]), 2)
            str_res = str(float_res)

            data_entry.add_prediction_result(email, data_id, res=float_res)

            data_entry.update_dataset(feature_list)

        except UserDoesNotExistError as udne:
            print("Error:", str(udne))
        except ResultUpdationError as rue:
            print("Error:", str(rue))
        except FileInsertionError as fie:
            print("Error:", str(fie))
        except InvalidDataIDError as ide:
            print("Error:", str(ide))

        return render(request, "prediction.html", {"result": str_res})

    return render(request, "prediction.html")
