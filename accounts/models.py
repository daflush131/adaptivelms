# accounts/models.py

from django.db import models
from django.contrib.auth.models import User


class ILSResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first = models.CharField(max_length=10, blank=True)
    second = models.CharField(max_length=10, blank=True)
    third = models.CharField(max_length=10, blank=True)
    fourth = models.CharField(max_length=10, blank=True)


class UserProfile(models.Model):
    LEARNING_STYLE_CHOICES = [
        ('ACT', 'Active'),
        ('REF', 'Reflective'),
        ('SNS', 'Sensing'),
        ('INT', 'Intuitive'),
        ('VIS', 'Visual'),
        ('VRB', 'Verbal'),
        ('SEQ', 'Sequential'),
        ('GLO', 'Global'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=100, blank=True)
    yearandsection = models.CharField(max_length=10, blank=True)
    learning_style = models.CharField(max_length=3, choices=LEARNING_STYLE_CHOICES, blank=True, null=True)
    cluster = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.user.username

class PreTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score1 = models.PositiveSmallIntegerField(null=True)
    items1 = models.PositiveSmallIntegerField(null=True)
    score2 = models.PositiveSmallIntegerField(null=True)
    items2 = models.PositiveSmallIntegerField(null=True)
    score3 = models.PositiveSmallIntegerField(null=True)
    items3 = models.PositiveSmallIntegerField(null=True)
    score4 = models.PositiveSmallIntegerField(null=True)
    items4 = models.PositiveSmallIntegerField(null=True)
    l1_answers = models.JSONField(null=True)
    l2_answers = models.JSONField(null=True)
    l3_answers = models.JSONField(null=True)
    l4_answers = models.JSONField(null=True)

class PostTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_score1 = models.PositiveSmallIntegerField()
    post_score2 = models.PositiveSmallIntegerField()
    post_score3 = models.PositiveSmallIntegerField()
    post_score4 = models.PositiveSmallIntegerField()