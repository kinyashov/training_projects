from django.contrib import admin
from .models import Product, Category, Price, Discount


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Discount)
