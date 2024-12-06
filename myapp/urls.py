from django.urls import path
from .views import index, face_feed, login_user,register_user , logout_user, home, video_feed, gen_table

urlpatterns = [
    path('', home, name='home'),
    path('VideoFeed/', index, name='index'),
    path('faceDetect/', face_feed, name='face_feed'),
    path('login/', login_user, name='login'),
    path("register/", register_user, name="register"),
    path('logout/', logout_user, name='logout'),
    path('video_feed/', video_feed, name='video_feed'),
    path('t/', gen_table, name='gen_table'),
]
