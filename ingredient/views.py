from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Ingredient


class IndexView(generic.ListView):
    template_name = 'ingredient/index.html'
    context_object_name = 'ingredients'

    def get_queryset(self):
	    return Ingredient.objects.order_by('ingredient_name')[:5]


class DetailView(generic.DetailView):
    model = Ingredient
    template_name = 'ingredient/detail.html'


class EditView(generic.DetailView):
    model = Ingredient
    template_name = 'ingredient/edit.html'


def create(request):
	return redirect(reverse('ingredient:index'))

def send_to_cart(request, pk):
	return redirect(reverse('ingredient:index'))


def delete(request, pk):
	ingredient = get_object_or_404(Ingredient, pk=pk)
	ingredient.delete()
	return redirect(reverse('ingredient:index'))

