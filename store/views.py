from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Store

class IndexView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'stores'
    paginate_by = 8

    def get_queryset(self):
	    """
	    Return the last five published stores (not including those set to be
	    published in the future).
	    """
	    return Store.objects.order_by('-visit')
