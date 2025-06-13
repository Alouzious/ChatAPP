from django.urls import path
from chat import views

app_name = 'chat'
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('registered_users/', views.registered_users, name='registered_users'),


]