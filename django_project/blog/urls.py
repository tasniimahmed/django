from django.urls import path
from . import views


urlpatterns = [
    #fadi y3ni home, b3den page el http response, b3den esmha
    #.about we .home esm el fns el fe view
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),

]