from django.urls import path
from .views import index, face_feed, login_user,register_user , logout_user, home, video_feed, gen_table, user_feedback,delete_user

urlpatterns = [
    path('', home, name='home'),
    path('VideoFeed/', index, name='index'),
    path('faceDetect/', face_feed, name='face_feed'),
    path('login/', login_user, name='login'),
    path("register/", register_user, name="register"),
    path('logout/', logout_user, name='logout'),
    path('video_feed/', video_feed, name='video_feed'),
    path("feedback/", user_feedback, name='feedback'),
    path("delete/<int:id>/", delete_user , name="delete_user"),
    path('t/', gen_table, name='gen_table'),
]
