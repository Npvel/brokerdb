from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=150)
    company = models.OneToOneField('companies.Company')

    def __str__(self):
        return self.name


class Contract(models.Model):
    number = models.CharField(max_length=10)
    sign_date = models.DateField()
    end_date = models.DateField()
    customer = models.ForeignKey('Customer')
    insurer = models.ForeignKey('Insurer')

    @property # декаратор
    def active(self):
        return self.end_date > timezone.now().date()

    def __str__(self):
        return '{} {} {}'.format(self.number, self.customer, self.insurer)


class CreditLimit(models.Model):
    contract = models.ForeignKey('Contract')
    debitor = models.ForeignKey('companies.Company')
    request_date = models.DateField()
    requested_amount = models.IntegerField()
    currency = models.ForeignKey('Currency')
    approved_date = models.DateField()
    approved_amount = models.IntegerField()
    expiration_date = models.DateField(null=True)
    guarantor = models.ForeignKey('companies.Company', null=True, related_name="granted_limits")
    guarantor_comment = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return 'CreditLimit {} {} {}'.format(self.contract.pk, self.insurer, self.approved_amount) 


class Insurer(models.Model):
    name = models.CharField(max_length=150)
    company = models.OneToOneField('companies.Company')

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name

