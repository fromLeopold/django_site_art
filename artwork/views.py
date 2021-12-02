from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View

from artwork.forms import EntryForm, SiteLogForm, RegisterForm, CommentForm
from artwork.models import Entry


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            us1 = form.save()
            login(request, us1)
            messages.success(request, "Now you're a part of out community!")
            return redirect('login')
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
            return redirect('entry_view')
    else:
        form = SiteLogForm()

    return render(request, "artwork/login.html", {"form": form})


def site_logout(request):
    logout(request)
    return redirect('entry_view')


def main_artiwood(request):
    return render(request, 'artwork/main.html', {})


class EntryView(View):

    def get(self, request):
        entries = Entry.objects.all()
        content = {'entries': entries}
        return render(request, "artwork/page_get.html", content)


class CreateEntry(CreateView):
    form_class = EntryForm
    template_name = "artwork/creating_entry.html"
    success_url = reverse_lazy('entry_view')


class CreateComment(CreateView):
    form_class = CommentForm
    template_name = "artwork/add_comment.html"
    success_url = reverse_lazy('entry_view')
