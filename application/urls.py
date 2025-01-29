from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "application"

urlpatterns = [
    path("", views.user_list, name="user_list"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chat/<int:user_id>/', views.chat, name='chat'),
]