from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'color', 'horsepower')
    list_filter = ('brand', 'color', 'year', 'transmission', 'fuel')
    search_fields = ('brand', 'model')
    list_editable = ('price',)
    ordering = ('-id',)