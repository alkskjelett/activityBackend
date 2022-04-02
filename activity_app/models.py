from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    prize = models.IntegerField()
    passed = models.BooleanField(default=False)
    videoUrl = models.URLField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Question(models.Model):
    question = models.CharField(max_length=255, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    correctAnswer = models.CharField(max_length=255)
    firstWrongAnswer = models.CharField(max_length=255)
    secondWrongAnswer = models.CharField(max_length=255)
    thirdWrongAnswer = models.CharField(max_length=255)


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)