
from django.urls import path
from .views import signin, signup, signout, edit_profile

app_name = 'user'

urlpatterns = [
    path("signin/", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("signout/", signout, name="signout"),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
