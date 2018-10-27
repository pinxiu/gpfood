from django.contrib import admin

from .models import History


class HistoryInline(admin.TabularInline):
    model = History
    extra = 3