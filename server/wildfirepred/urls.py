from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="Home"),
    path("about", views.about, name="About"),
    path("contact_us", views.contact, name="Contact"),
    path("faqs", views.faq, name="FAQ"),
    path("predict", views.predict, name="Prediction"),
    path("pricing", views.pricing, name="Pricing"),
    path("error", views.errorpage, name="Error"),
]
