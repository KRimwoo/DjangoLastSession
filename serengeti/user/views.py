from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserLoginForm, UserSignUpForm
from django.contrib.auth import login, logout
import os

# Create your views here.
def signin(request):

    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:index')
        
    return render(request, 'user/signin.html', {'form': form})

def signup(request):

    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            # 회원가입하면 바로 로그인
            login(request, user)
            return redirect('main:index')
    
    else: 
        form = UserSignUpForm()

    return render(request, 'user/signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('main:index')

def edit_profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    form = UserSignUpForm(instance=request.user)
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES, instance=request.user)
        image_path = ""
        if form.image:
            image_path = user.image.path
        if form.is_valid():
            #이미지 삭제(취소)가 있을 경우
            if 'image-clear' in request.POST:
                os.remove(image_path)
                user.image = None
            #이미지 변경이 있을 경우
            elif 'image' in request.FILES:
                if image_path != "":
                    os.remove(image_path)
                user.image = form.cleaned_data.get('image')
            form.save()
            return redirect('main:index')
        

    return render(request, 'user/useredit.html', {'form': form})