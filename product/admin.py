from django.contrib import admin
from product.models import Product, Order, Tag

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','price','category','description','date_created',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ('customer','product','status','date_created',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display= ('name',)
