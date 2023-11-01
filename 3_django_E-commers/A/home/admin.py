from django.contrib import admin
from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category)


#Bootstrap
#https://getbootstrap.com/docs/5.1/components/dropdowns/

#Split button


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ('category',)