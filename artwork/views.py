from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from artwork.forms import EntryForm
from artwork.models import Entry


def auth(request):
    return render(request, "artwork/oauth.html")


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
        return redirect("/")
