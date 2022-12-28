from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:post_id>', views.post, name="post"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]