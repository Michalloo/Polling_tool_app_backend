from django.conf.urls import url
from PollingToolApp import views

urlpatterns = [
    url(r"^show-answers/$", views.responseApi),
    url(r"^add-answer/$", views.responseApi),
]
