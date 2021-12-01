from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Entry, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


class EntryForm(forms.ModelForm):
    class Meta:
        model: Entry
        fields = ("title", "picture", "description")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={"class": "form-control", "autocomplete": "off"}))
    username = forms.CharField(label="User  name",
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SiteLogForm(AuthenticationForm):
    username = forms.CharField(label="User  name",
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={"class": "form-control", "autocomplete": "off"}))
