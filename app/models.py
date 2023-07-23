from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chats(models.Model):
    chat_message = models.CharField(max_length=10000)
    chat_time_stamp = models.DateTimeField(auto_now_add=True)