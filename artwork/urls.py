from django.conf.urls import url
from django.urls import path, include

from .views import auth, EntryView, AddEntry

urlpatterns = [
    path('', auth, name="authorize"),
    path('accounts/profile/', EntryView.as_view(), name="entry_view"),
    path("create/", AddEntry.as_view(), name="add_entry"),
]