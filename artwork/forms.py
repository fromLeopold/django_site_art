from django import forms

from .models import Entry, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


class EntryForm(forms.ModelForm):
    class Meta:
        model: Entry
        fields = ("title", "picture", "descroption")
