from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Vacature(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default =timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reactions = []

    def __str__(self):
        return self.title

    def add_reaction(self, reaction1):
        self.reactions.append(reaction1)

    def get_absolute_url(self):
        return reverse('vacature-detail', kwargs={'pk': self.pk})

class Reaction(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
