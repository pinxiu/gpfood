from django.contrib import admin

from .models import Recipe


class IngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['dish_name']}),
        ('Author information', {'fields': ['author'], 'classes': ['collapse']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Instruction', {'fields': ['instruction'], 'classes': ['collapse']}),
    ]
    inlines = [IngredientInline]
    list_display = ('dish_name', 'author', 'pub_date', 'was_published_recently')
    list_filter = ['author', 'pub_date']
    search_fields = ['dish_name']

admin.site.register(Recipe, RecipeAdmin)
