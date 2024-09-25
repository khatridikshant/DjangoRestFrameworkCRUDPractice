from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length= 115)
    gender = models.CharField(max_length=10, default="unknown")
    realm = models.CharField(max_length=50, default = "unknown")

    def __str__(self) -> str:
        return self.name
    