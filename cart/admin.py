from django.contrib import admin

from .models import Cart

class IngredientInline(admin.TabularInline):
    model = Cart.ingredients.through
    extra = 3


class RecipeInline(admin.TabularInline):
    model = Cart.recipes.through
    extra = 3


class CartAdmin(admin.ModelAdmin):
	# fields = ['customer']
    # fieldsets = [
    #     (None,               {'fields': ['dish_name']}),
    #     ('Author information', {'fields': ['author'], 'classes': ['collapse']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #     ('Instruction', {'fields': ['instruction'], 'classes': ['collapse']}),
    # ]
    inlines = [IngredientInline, RecipeInline]
    exclude = ('recipes', 'ingredients',)
    # list_display = ('customer_name')
    # list_filter = ['recipes']

admin.site.register(Cart, CartAdmin)
