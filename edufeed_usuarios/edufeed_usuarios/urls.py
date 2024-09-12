from django.contrib import admin
from django.urls import path
from appedu_usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.about, name='sobre'),
    path('login/', views.user_login, name='login'), 
]
