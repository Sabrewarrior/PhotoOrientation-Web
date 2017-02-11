from rest_framework import serializers
from snippets.models import Correct, Incorrect, LANGUAGE_CHOICES, STYLE_CHOICES


class CorrectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correct
        fields = ('url_orig', 'url_pos', 'url_neg', 'url_hot', 'orient', 'pct', 'pred', 'prob')


class IncorrectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incorrect
        fields = ('url_orig', 'url_pos', 'url_neg', 'url_hot', 'orient', 'pct', 'pred', 'prob')
