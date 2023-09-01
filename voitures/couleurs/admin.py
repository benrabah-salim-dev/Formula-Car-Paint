from django.contrib import admin
from .models import Brand, Model, Color, BaseColor, ColorFormula, BaseColorFormula

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year')
    search_fields = ('name', 'brand__name')
    list_filter = ('brand',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code', 'color_code', 'car_model')
    search_fields = ('name', 'hex_code', 'color_code', 'car_model__name')
    list_filter = ('car_model__brand',)

@admin.register(BaseColor)
class BaseColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'color_code')
    search_fields = ('name', 'color_code')

@admin.register(ColorFormula)
class ColorFormulaAdmin(admin.ModelAdmin):
    list_display = ('color', 'color_code')
    search_fields = ('color__name', 'color_code')

@admin.register(BaseColorFormula)
class BaseColorFormulaAdmin(admin.ModelAdmin):
    list_display = ('formula', 'base_color', 'amount_in_grams')
    search_fields = ('formula__color__name', 'base_color__name')
