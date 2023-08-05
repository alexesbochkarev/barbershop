from django.contrib import admin

# Register your models here.

from .models import Group, Manufacturer, Product, Image

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}

class ProductImageInline(admin.StackedInline):
    model = Image
    extra = 1
    max_num = 4

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'vendor_code', 'pub_date', 'group', 'manufacturer', 'status',]
    inlines = [
         ProductImageInline,
     ]

admin.site.register(Group, GroupAdmin)
admin.site.register(Manufacturer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)