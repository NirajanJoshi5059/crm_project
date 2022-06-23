from django.contrib import admin
from customer.models import Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','email','phone','date_created',)


# admin.site.register(Customer)