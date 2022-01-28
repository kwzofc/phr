from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.PHR)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')