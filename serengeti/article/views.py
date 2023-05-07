from django.shortcuts import render,redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Category

# Create your views here.
def new(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(
                commit = False
            )

            article.author = request.user
            article.image = form.cleaned_data.get('image')
            article.save()
            return redirect('article:detail', id=article.id)

    return render(request, 'new.html', {'form': form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    categories = Category.objects.all()

    return render(request, 'detail.html', {'article': article, 'categories' : categories})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(isinstance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, isinstance=article)

        if form.is_valid():
            article = form.save()
            return redirect('article:detail', id=article.id)
        
    return render(request, ' edit.html', {'form': form, 'article': article})

def destroy(request, id):
    article = get_object_or_404(Article, pk=id)

    article.delete()

    return redirect('main:index.html')