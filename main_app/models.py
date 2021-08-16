import datetime

from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} -> {self.datetime}"
