from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length= 115)

    def __str__(self) -> str:
        return self.name
    