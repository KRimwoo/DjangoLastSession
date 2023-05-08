from django.shortcuts import render,redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Category, Tag, Like, Comment

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
            form.save_m2m()
            return redirect('article:detail', id=article.id)

    return render(request, 'new.html', {'form': form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    categories = Category.objects.all()
    tags = article.tag.all()
    comments = Comment.objects.filter(article=article)
    likes = len(Like.objects.filter(article=article))

    return render(request, 'detail.html', {'article': article, 'categories' : categories, 'tags': tags, 'likes': likes, 'comments': comments})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(isinstance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, isinstance=article)

        if form.is_valid():
            article = form.save()
            return redirect('article:detail', id=article.id)
        
    return render(request, ' edit.html', {'form': form, 'article': article})


def create_comment(request, id):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.blog = get_object_or_404(Article, pk=id)
    comment.author = request.user
    comment.save()
    return redirect('detail', id)


def new_comment(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'new_comment.html', {'article': article})

def destroy(request, id):
    article = get_object_or_404(Article, pk=id)

    article.delete()

    return redirect('main:index.html')


def like(request, id):
    #로그인 하지 않은 경우
    if request.user.is_anonymous:
        return redirect("user:signin")
    #이미 좋아요 누른 경우
    if Like.objects.filter(likedUser=request.user, blog_id=blog_id):
        return redirect("detail", blog_id)
    #좋아요
    like = Like()
    like.blog = get_object_or_404(Blog, pk=blog_id)
    like.likedUser = request.user
    like.save()
    return redirect('detail', blog_id)
