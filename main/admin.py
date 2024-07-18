from django.contrib import admin
from .models import Products

# Register your models here.
@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'created', 'author')