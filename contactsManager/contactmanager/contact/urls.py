from django.urls import path
from contact import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add/",views.add,name="add"),
    path("save_contact/",views.save_contact,name="save_contact")
]