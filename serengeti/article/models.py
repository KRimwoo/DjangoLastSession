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

    tag = models.ManyToManyField('Tag', blank=True)



class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'comment'
    
    def __str__(self):
        return self.content + ' | ' + str(self.author)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name
    

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    likedUser = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'like'

    def __str__(self):
        return self.article.title + ' | ' + str(self.likedUser)