from django import forms
from webpage.models import CropInfo


class CropAddForm(forms.ModelForm):
    class Meta:
        model = CropInfo
        fields = ("crop", "min_price", "stock", "place", "description", "photo")
        # exclude = ("user", "highest_bid")

        labels = {
            "crop": "",
            "place": "",
            "min_price": "",
            "description": "",
            "photo": "",
            "stock": "",
        }

        widgets = {
            "crop": forms.TextInput(
                attrs={
                    "class": "form-control part1",
                    "placeholder": "Crop Name",
                }
            ),
            "place": forms.TextInput(
                attrs={
                    "class": "form-control place3",
                    "placeholder": "Address",
                }
            ),
            "min_price": forms.NumberInput(
                attrs={
                    "class": "form-control place2 part2",
                    "placeholder": "Base price",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control place2 part2",
                    "placeholder": "Description",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control place2 part3",
                    "placeholder": "Stock",
                }
            ),
        }


class BidForm(forms.Form):
    bid = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"style": "width:500px;"}),
    )
