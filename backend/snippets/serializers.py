from rest_framework import serializers
from snippets.models import Database, URLList, LANGUAGE_CHOICES, STYLE_CHOICES


class DatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Database
        fields = ('name', 'correct')


class URLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLList
        fields = ('db', 'url_orig', 'url_pos', 'url_neg', 'url_hot', 'orient', 'pct', 'pred', 'prob')
