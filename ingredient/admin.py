from django.contrib import admin

from .models import Ingredient

from price.admin import HistoryInline


class IngredientAdmin(admin.ModelAdmin):
    inlines = [HistoryInline]


admin.site.register(Ingredient, IngredientAdmin)
