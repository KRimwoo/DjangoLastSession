from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import TextInput, FileInput
from django import forms
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        label = '유저이름'
    )
    pass

class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

        fields = [
            'username',
            'image',
        ]

        fields = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'background-color: skyblue',
                'placeholder': 'ID'
            }),
            'image': FileInput(attrs={
                'class': "form-control-file",
            }),
        }

        labels = {
            'username': 'ID',
            'image': '프로필 사진',
        }


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'image',)
        labels = {
            'username': 'ID',
            'image': '프로필 사진',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'background-color: skyblue',
                'placeholder': 'ID'
            }),
            'image': forms.FileInput(attrs={
                'class': "form-control-file",
            }),
        }
        
        labels = {
            'username': 'ID',
            'image': '프로필 사진',
        }