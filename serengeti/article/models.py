from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Article(models.Model):
    author = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )

    title = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now = True,
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    image = models.ImageField(upload_to="article/", blank=True)

    content = models.TextField()

    