from django.urls import path
from . import views
from .views import upload_video,video_list,video_detail

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/",upload_video,name='upload_video'),
    path('videos/',video_list,name='video_list'),
    path('videos/<int:pk>/',video_detail,name='video_detail'),
]