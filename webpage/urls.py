from django.conf.urls import url
from . import views

app_name = "webpage"

urlpatterns = [
    url("^$", views.home, name="home"),
]