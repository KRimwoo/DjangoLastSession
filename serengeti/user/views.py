from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignUpForm, UserEditForm
from django.contrib.auth import login, logout

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

    form = UserSignUpForm()

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            # 회원가입하면 바로 로그인
            login(request, user)
            return redirect('main:index')


    return render(request, 'user/signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('main:index')

def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'user/useredit.html', {'form': form})