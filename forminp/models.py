from django.db import models
from phone_field import PhoneField

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length = 20)
    blood_group = models.CharField(max_length=5)
    area = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)

    def __str__(self):
        return self.name + " " + self.blood_group
    