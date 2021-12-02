from django.conf.urls import url
from django.urls import path, include

from .views import EntryView, registration, site_login, site_logout, main_artiwood, CreateEntry, CreateComment

urlpatterns = [
    url('account/', include('django.contrib.auth.urls')),
    path('art-works', EntryView.as_view(), name="entry_view"),
    path("create/entry/", CreateEntry.as_view(), name="add_entry"),
    path("create/comment/", CreateComment.as_view(), name="add_comment"),
    path("register/", registration, name="register"),
    path('login/', site_login, name='login'),
    path('logout/', site_logout, name='logout'),
    path('', main_artiwood, name='main'),
]
