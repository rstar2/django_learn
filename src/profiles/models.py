from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True)
    location = models.CharField(max_length=120, default="Here")
    job = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name
