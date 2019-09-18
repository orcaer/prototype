from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
        url(r"signup/$", views.SignUp.as_view(), name='signup'),
        url(r"login/$", LoginView.as_view(template_name='users/login.html'), name='login'),
        url(r"logout/$", LogoutView.as_view(template_name='users/logout.html'), name='logout')
]
