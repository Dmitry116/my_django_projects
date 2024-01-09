from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import AboutUserView, RegisterView


app_name = 'myauth'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path(
        'login/',
         LoginView.as_view(
             template_name='myauth/login.html',
             redirect_authenticated_user=True,
         ),
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='myauth:login'), name='logout'),
    path('about_user/', AboutUserView.as_view(), name='about_user'),
]
