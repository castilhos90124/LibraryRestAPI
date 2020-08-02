from django.db import models

class Client(models.Model):

    name = models.CharField(
        max_length=40,
        null=False
    )

    fine = models.FloatField(null=False, blank= True, default=0.0)
    
    # books = books.all()
    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField(
        max_length=40,
        null=False
    )

    available = models.BooleanField(default=True)

    borrowed_since = models.DateField(null=True, blank= True)

    borrowed_to = models.ForeignKey(Client, related_name='books', null=True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



