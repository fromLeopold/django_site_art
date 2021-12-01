from django.conf.urls import url
from django.urls import path, include

from .views import EntryView, AddEntry, registration

urlpatterns = [

    path('', EntryView.as_view(), name="entry_view"),
    path("create/", AddEntry.as_view(), name="add_entry"),
    path("register/", registration, name="register"),
    path("login/", name="login"),
]
