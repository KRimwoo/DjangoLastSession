from django import forms
from .models import Article, Comment, Tag

class ArticleForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        label = "태그 선택",
        queryset = Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Article

        fields = [
            'title',
            'category',
            'content',
            'image',
            'tag',
        ]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = {
            'content',
        }

        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

        labels = {'content': '댓글 쓰기'}
