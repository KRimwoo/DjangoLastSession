from django.shortcuts import render,redirect, get_object_or_404
from django.conf import settings
from .forms import ArticleForm, CommentForm
from .models import Article, Category, Tag, Like, Comment
import os

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

    return render(request, 'article/new.html', {'form': form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    categories = Category.objects.all()
    tags = article.tag.all()
    comments = Comment.objects.filter(article=article)
    likes = [like.likedUser for like in Like.objects.filter(article=article)]

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article:detail', id=id)
    else:
        comment_form = CommentForm()

    return render(request, 'article/detail.html', {'article': article, 'categories' : categories, 'tags': tags, 'likes': likes, 'comments': comments, 'comment_form': comment_form})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        image_path = ""
        if article.image:
            image_path = article.image.path
        if form.is_valid():
            #이미지 삭제(취소)가 있을 경우
            if 'image-clear' in request.POST:
                os.remove(image_path)
                article.image = None
            #이미지 변경이 있을 경우
            elif 'image' in request.FILES:
                if image_path != "":
                    os.remove(image_path)
                article.image = form.cleaned_data.get('image')

            article = form.save(commit=False)
            article.save()
            form.save_m2m()
            return redirect('article:detail', id=article.id)
        
    return render(request, 'article/edit.html', {'form': form, 'article': article})


def destroy_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if article.image:
        os.remove(article.image.path)

    article.delete()

    return redirect('main:index')


def destroy_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    article_id = comment.article.pk
    comment.delete()
    return redirect('article:detail', id=article_id)


def like(request, id):
    #로그인 하지 않은 경우
    if request.user.is_anonymous:
        return redirect("user:signin")

    article = get_object_or_404(Article, pk=id)
    likes = Like.objects.filter(article=article)

    if likes.filter(likedUser=request.user).exists():
        likes.filter(likedUser=request.user).delete() #좋아요가 되어있는 상태에서 요청할 경우 좋아요 취소
    else:
        Like.objects.create(likedUser=request.user, article=article) #좋아요 객체 생성
    return redirect('article:detail', id)
