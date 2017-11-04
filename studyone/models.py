from datetime import datetime

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import  get_all_styles
from pygments import highlight

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([item[1][0], item[0]] for item in get_all_styles())
sex_choices = (
    (1, 'Male'),
    (2, 'Female'),
    (3, '保密')
)

class users(models.Model):
    usersname = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    sex=models.IntegerField(choices=sex_choices, default=1)
    createOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usersname

class article(models.Model):
    title = models.CharField(max_length=20, default="")
    context = models.TextField(null=True)
    users = models.ForeignKey(to='users', null=True)
    createOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, max_length=100, default='')
    code = models.TextField()
    lineons = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField(null=True)


    class Meta:
        ordering = ('created',)
