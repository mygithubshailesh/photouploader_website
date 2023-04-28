from django.contrib import admin
from .models import Photo,Category 
# Register your models here.

@admin.register(Category)
class PostModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name']

@admin.register(Photo)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Category','Image','description']


