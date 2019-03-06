from django.urls import path
from post import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/update', views.update, name='update'),
    path('<int:post_id>/delete', views.update, name='delete'),
    path('register/', views.registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]