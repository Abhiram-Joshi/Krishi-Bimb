from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r"^signup/$", views.user_signup, name="user_signup"),
    url(r"^login/$", views.user_login, name="user_login"),
    url(r"^logout/$", views.user_logout, name="user_logout"),
]
