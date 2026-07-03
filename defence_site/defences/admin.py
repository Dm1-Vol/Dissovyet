from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Defence

@admin.register(Defence)
class DefenceAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'defence_type', 'defence_date', 'status']
    list_filter = ['defence_type', 'status']
    search_fields = ['author', 'title']