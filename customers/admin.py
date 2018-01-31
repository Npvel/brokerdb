from django.contrib import admin

from .models import Contract, Customer, Currency, Insurer

admin.site.register(Customer)
admin.site.register(Contract)
admin.site.register(Currency)
admin.site.register(Insurer)



# Register your models here.
