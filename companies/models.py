from django.db import models
from django.utils import timezone

class Company(models.Model):
    short_legal_name = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=250)
    house = models.CharField(max_length=50)
    registration_date = models.DateField()
    status = models.CharField(max_length=50)
    ceo = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    ogrn = models.CharField(max_length=13)
    okpo = models.CharField(max_length=10)
    kpp = models.CharField(max_length=9)
    modified = models.DateField(default=timezone.now)

    def __str__(self):
        return self.short_legal_name



