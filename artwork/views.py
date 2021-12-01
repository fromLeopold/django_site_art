from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from artwork.forms import EntryForm, SiteLogForm, RegisterForm
from artwork.models import Entry


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            us1 = form.save()
            login(request, us1)
            messages.success(request, "Now you're a part of out community!")
            return redirect('main_animals')
        else:
            messages.error(request, "Ooops, something goes wrong:(")
    else:
        form = RegisterForm()
    return render(request, "artwork/registration.html", {"form": form})


def site_login(request):
    if request.method == "POST":
        form = SiteLogForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_animals')
    else:
        form = SiteLogForm()

    return render(request, "animals/site_login.html", {"form": form})


def site_logout(request):
    logout(request)
    return redirect('main_animals')


class EntryView(View):

    def get(self, request):
        entries = Entry.objects.all()
        content = {'entries': entries}
        return render(request, "artwork/page_get.html", content)


class AddEntry(PermissionRequiredMixin, View):
    permission_required = 'blog.add_post'

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = self.request.user
            form.save()
        return redirect("authorize")
