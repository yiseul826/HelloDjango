from django.db import models

# Create your models here.
from django.utils import timezone


class Board(models.Model):
    # id = models.IntegerField() # but, id는 자동생성되므로, 생략가능
    title = models.CharField(max_length=100)
    userid = models.CharField(max_length=18)
    regdate = models.DateTimeField(default=timezone.localtime)
    views = models.IntegerField(default=0)
    thumbup = models.IntegerField(default=0)
    contents = models.TextField()
