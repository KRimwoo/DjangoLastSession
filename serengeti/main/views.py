from django.shortcuts import render
from article.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.

def base(request):
    categories = Category.objects.all()
    return (request, 'main/base.html', {'articles':articles, 'categories':categories})

def index(request):
    category_id = request.GET.get('category')
    if category_id:
        articles = Article.objects.filter(category__id = category_id).order_by('-created_at')
    else:
        articles = Article.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_range = range(1, paginator.num_pages + 1)
    return render(request, 'main/index.html', {'categories': categories, 'page_obj': page_obj, 'page_range': page_range})

