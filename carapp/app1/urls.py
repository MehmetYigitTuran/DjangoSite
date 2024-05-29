from . import views
from django.urls import path, include

# http://127.0.0.1:8000/

urlpatterns = [
    path("", views.index),
    #path("index", views.index),
    path('blogs/', views.blogs, name="blogs"),
    path('comments/<int:car_id>/', views.comments, name='comments'),
    path('cars/', views.list_of_cars, name='list_of_cars'),
    path('types/', views.car_types, name='car_types'),
    path('search/', views.search, name='search'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/', views.list_of_cars, name='list_of_cars'),
    path('types/', views.car_types, name='car_types'),
    path('search/', views.search, name='search'),
    path('users/', include('users.urls')),
]