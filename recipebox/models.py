from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def url(self):
        return f"/author/{self.id}"


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    total_time = models.DurationField()
    instructions = models.TextField(default='')
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.title

    def url(self):
        return f"/recipe/{self.id}"


class Unit(models.Model):
    name = models.CharField(max_length=20)
    abbr = models.CharField(max_length=6)

    def __str__(self):
        return self.name
