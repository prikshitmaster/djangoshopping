from django.contrib import admin
from home.models.product import Contact, Emailcollection,  AdminProduct
from home.models.catorgry import Catorgry
# Register your models here.

class AdminProducts(admin.ModelAdmin):
    list_display = ['name' , 'prize' , 'catorgry']
admin.site.register(Contact)
admin.site.register(Emailcollection)
admin.site.register(AdminProduct , AdminProducts )
admin.site.register(Catorgry)

