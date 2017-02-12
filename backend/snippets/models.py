from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Database(models.Model):
    name = models.CharField(max_length=16)
    correct = models.BooleanField()

    class Meta:
        ordering = ('pk', 'name', 'correct')


class URLList(models.Model):
    db = models.ForeignKey('Database')
    url_orig = models.CharField(max_length=64)
    url_pos = models.CharField(max_length=64)
    url_neg = models.CharField(max_length=64)
    url_hot = models.CharField(max_length=64)
    orient = models.IntegerField()
    pct = models.IntegerField()
    pred = models.IntegerField()
    prob = models.IntegerField()

    class Meta:
        ordering = ('db', '-pct',)
