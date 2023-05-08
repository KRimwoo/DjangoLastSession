from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Tag)