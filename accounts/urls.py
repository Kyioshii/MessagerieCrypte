from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]