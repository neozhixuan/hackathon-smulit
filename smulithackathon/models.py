from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Business(models.Model):
    businesstype = models.CharField(blank = True, null = True,  max_length = 50)
    employees = models.IntegerField(blank = True, null = True)
    salary = models.IntegerField(blank = True, null = True)
    profit = models.IntegerField(blank = True, null = True)
    encryption = models.CharField(blank = True, null = True,  max_length = 50)

    def __str__ (self):
        return f"{self.businesstype}, {self.encryption}"