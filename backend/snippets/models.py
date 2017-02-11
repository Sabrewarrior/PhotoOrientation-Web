from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Correct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url_orig = models.URLField()
    url_pos = models.URLField()
    url_neg = models.URLField()
    url_hot = models.URLField()
    orient = models.IntegerField()
    pct = models.IntegerField()
    pred = models.IntegerField()
    prob = models.IntegerField()

    class Meta:
        ordering = ('pct',)


class Incorrect(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url_orig = models.URLField()
    url_pos = models.URLField()
    url_neg = models.URLField()
    url_hot = models.URLField()
    orient = models.IntegerField()
    pct = models.IntegerField()
    pred = models.IntegerField()
    prob = models.IntegerField()

    class Meta:
        ordering = ('pct',)