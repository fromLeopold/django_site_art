from django.contrib.auth.models import User
from django.db.migrations import serializer
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from artwork.models import Entry


class EntrySerializer(ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field="first_name", read_only=True)

    class Meta:
        model = Entry
        fields = '__all__'
