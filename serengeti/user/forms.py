from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms import CharField, TextInput, FileInput
from .models import User

class UserLoginForm(AuthenticationForm):
    username = CharField(
        widget=TextInput(attrs={
            'class': 'form-control'
        }),
        label = '유저이름'
    )
    pass

class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

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


