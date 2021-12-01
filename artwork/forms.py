from django import forms

from .models import Entry, Comment


class Comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

class Entry(forms.ModelForm):
    class Meta:
        model: Entry
        fields = ("title", "picture")
