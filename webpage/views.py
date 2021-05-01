from django.shortcuts import render
from .forms import CropAddForm, BidForm
from django.contrib.auth.decorators import login_required
from .models import CropInfo
from django.views.generic import ListView, DetailView

# Create your views here.


def home(request):
    return render(request, "home.html")


@login_required
def farmer_portal(request):

    status = False

    if request.method == "POST":
        form = CropAddForm(request.POST)

        if form.is_valid():
            status = True
            instance = form.save(commit=False)
            instance.user = request.user
            instance.photo = request.FILES["photo"]
            instance.save()

        else:
            print(form.errors)
            print(form.non_field_errors)
            status = False
            form = CropAddForm()

    else:
        form = CropAddForm()

    context = {
        "form": form,
        "status": status,
        "user": request.user,
    }

    return render(request, "farmer_portal.html", context)


@login_required
def buyer_portal(request):
    return render(request, "buyer_portal.html")


class crop_list_view(ListView):
    model = CropInfo
    template_name = "crop_list.html"
    context_object_name = "list"


class crop_detail_view(DetailView):
    model = CropInfo
    template_name = "buyer_portal.html"
    context_object_name = "crop"


@login_required
def bid_update(request, id):

    placed = False

    if request.method == "POST":

        form = BidForm(request.POST)

        if form.is_valid():
            model = CropInfo.objects.get(id=id)

            highest_bid = CropInfo.objects.get(id=id).highest_bid
            bid = form.cleaned_data["bid"]

            if int(bid) > int(highest_bid):
                model.highest_bid = bid
                placed = True

            else:
                placed = False

            if placed == True:
                # model.id = id
                # model.user = request.user
                model.crop = CropInfo.objects.get(id=id).crop
                model.place = CropInfo.objects.get(id=id).place
                model.photo = CropInfo.objects.get(id=id).photo

                model.save()

            return render(
                request,
                "place_bid.html",
                {
                    "placed": placed,
                    "form": BidForm(),
                    "highest_bid": CropInfo.objects.get(id=id).highest_bid,
                },
            )

        else:
            print(form.errors)

    else:
        form = BidForm()

    return render(
        request,
        "place_bid.html",
        {
            "form": form,
            "placed": placed,
            "highest_bid": CropInfo.objects.get(id=id).highest_bid,
        },
    )
