from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from website import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "webpage"

urlpatterns = [
    url("^$", views.home, name="home"),
    url("^farmer_portal/$", views.farmer_portal, name="farmer_portal"),
    # url("^buyer_portal/$", views.buyer_portal, name="buyer_portal"),
    url(
        r"^crop_list/$",
        login_required(views.crop_list_view.as_view()),
        name="crop_list",
    ),
    url(
        r"^crop_list/(?P<pk>\d+)/$",
        login_required(views.crop_detail_view.as_view()),
        name="crop_detail",
    ),
    url(r"bid_update/(?P<id>\d+)/$", views.bid_update, name="bid_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()