from django.db import models

class Book(models.Model):

    name = models.CharField(
        max_length=40,
        null=False
    )

    available = models.BooleanField(default=True)

    borrowed_since = models.DateField(null=True, blank= True)

class Client(models.Model):

    name = models.CharField(
        max_length=40,
        null=False
    )

    fine = models.FloatField(null=True, blank= True)

