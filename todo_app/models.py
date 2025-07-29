from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
