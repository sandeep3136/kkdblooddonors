from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length = 20)
    blood_group = models.CharField(max_length=5)
    area = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)

    class Meta:
        unique_together = ["name", "contact"]
    def __str__(self):
        return self.name + " " + self.blood_group
    