from django.contrib import admin
from .models import Article, Category

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)