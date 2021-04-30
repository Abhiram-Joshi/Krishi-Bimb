from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone",)

    widgets = {
        "phone": forms.TextInput(
            attrs={
                "id": "inputPhone",
                "class": "form-control",
                "placeholder": "Phone Number",
            }
        ),
    }

    labels = {
        "phone": "",
    }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )

        help_texts = {
            "username": None,
            "email": None,
        }

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "id": "inputUserame",
                    "class": "form-control",
                    "placeholder": "Username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "id": "inputEmail",
                    "class": "form-control",
                    "placeholder": "Email",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "id": "inputPassword",
                    "class": "form-control",
                    "placeholder": "Password",
                }
            ),
        }
        labels = {
            "username": "",
            "email": "",
            "password": "",
        }


class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "id": "user",
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
        label="",
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "passw",
                "class": "form-control",
                "placeholder": "Password",
            }
        ),
        label="",
    )
