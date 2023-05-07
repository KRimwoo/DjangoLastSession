from django.urls import path
from .views import new, detail, edit, destroy


app_name = 'article'

urlpatterns = [
    path("new/", new, name='new'),
    path("<int:id>", detail, name='detail'),
    path("edit/<int:id>", edit, name='edit'),
    path("destroy/<int:id>", destroy, name='destroy'),
]


