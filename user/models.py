from django.db import models
from django.contrib.auth.models import User


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Team = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    def __str__(self):
        return self.Designation
