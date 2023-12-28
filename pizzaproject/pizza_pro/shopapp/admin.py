from django.contrib import admin
from .models import Item
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','image')
    
admin.site.register(Item) 

# Register your models here.
