from django.db import models
from django.contrib.auth.models import User

class Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    p1_checked = models.BooleanField(default=False)
    p2_checked = models.BooleanField(default=False)
    p3_checked = models.BooleanField(default=False)
    p4_checked = models.BooleanField(default=False)
# Create your models here.
