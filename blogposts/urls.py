from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:post_id>', views.post, name="post"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('create-post/', views.create_post, name="create-post"),
    path('edit-post/<int:post_id>', views.edit_post, name="edit-post"),
    path('delete-post/<int:post_id>', views.delete_post, name="delete-post"),
]
