from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
    path('images/<int:image_id>/result/', views.record_result, name='record_result'),
]
