from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = None
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    company = models.BooleanField(default='False')
    opleidingen = models.TextField(default='None')
    regio = models.TextField(default='None')
    werkervaring = models.TextField(default='None')
    telefoon = PhoneNumberField(default='None', null=False, blank=False)
    talen = models.TextField(default='None')

    def __str__(self):
        self.username = self.user.username
        return '{} Profile'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    