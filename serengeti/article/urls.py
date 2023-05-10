from django.urls import path
from .views import new, detail, edit, destroy_article, like, destroy_comment


app_name = 'article'

urlpatterns = [
    path("new/", new, name='new'),
    path("<int:id>", detail, name='detail'),
    path("edit/<int:id>", edit, name='edit'),
    path("destroy_article/<int:id>", destroy_article, name='destroy_article'),
    path("like/<int:id>", like, name='like'),
    path("destroy_comment/<int:id>", destroy_comment, name='destroy_comment'),
]


