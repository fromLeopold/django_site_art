from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from artwork.models import Entry
from artwork.permissions import IsAuthorOrStaffOrReadOnly
from artwork.serializers import EntrySerializer


def auth(request):
    return render(request, "artwork/oauth.html")


class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthorOrStaffOrReadOnly]
    filter_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['author', 'title']

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()



