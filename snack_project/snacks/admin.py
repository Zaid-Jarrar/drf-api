from django.contrib import admin
from .models import Snack
# Register your models here.

@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'updated']
    # search_fields = ('title',)