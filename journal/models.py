from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def as_json(self):
        return dict(pk=self.id, body=self.body, timestamp=self.timestamp.isoformat())

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.body


class Profile(models.Model):
    user = models.OneToOneField(User)
    display_picture = models.CharField(max_length=1000, null=True, blank=True)


class Group(models.Model):
    title = models.CharField(max_length=500)
    users = models.ManyToManyField(User)
