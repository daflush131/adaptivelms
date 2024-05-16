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
    learning_style = models.CharField(max_length=3, choices=LEARNING_STYLE_CHOICES, blank=True, null=True)

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

class Difficulty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lesson1 = models.PositiveSmallIntegerField(null=True)
    lesson2 = models.PositiveSmallIntegerField(null=True)
    lesson3 = models.PositiveSmallIntegerField(null=True)
    lesson4 = models.PositiveSmallIntegerField(null=True)

class PostTest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_score1 = models.PositiveSmallIntegerField(null=True)
    post_items1 = models.PositiveSmallIntegerField(null=True)
    post_score2 = models.PositiveSmallIntegerField(null=True)
    post_items2 = models.PositiveSmallIntegerField(null=True)
    post_score3 = models.PositiveSmallIntegerField(null=True)
    post_items3 = models.PositiveSmallIntegerField(null=True)
    post_score4 = models.PositiveSmallIntegerField(null=True)
    post_items4 = models.PositiveSmallIntegerField(null=True)
    post1_answers = models.JSONField(null=True)
    post2_answers = models.JSONField(null=True)
    post3_answers = models.JSONField(null=True)
    post4_answers = models.JSONField(null=True)

class ClusterResults(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clesson1 = models.JSONField(null=True)
    clesson2 = models.JSONField(null=True)
    clesson3 = models.JSONField(null=True)
    clesson4 = models.JSONField(null=True)
    