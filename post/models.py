from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=1000)
    date_created = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

