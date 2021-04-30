from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = "account"

urlpatterns = [
    url(r"^signup/$", views.user_signup, name="user_signup"),
    url(r"^login/$", views.user_login, name="user_login"),
    # url(r"^logout/$", login_required(views.user_logout), name="user_logout"),
]
