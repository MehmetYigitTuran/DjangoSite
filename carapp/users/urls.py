from . import views
from django.urls import path, include

# http://127.0.0.1:8000/
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]