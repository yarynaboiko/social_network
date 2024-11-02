from django.urls import path
from posts import views

urlpatterns = [
    path('create/', views.ProfilePostCreateView.as_view(), name='profile-post-create'),
    path('<int:post_id>/like', views.LikePushView.as_view(), name='post-like'),
    path('<int:post_id>/share', views.SharePushView.as_view(), name='post-share'),
    path('<int:post_id>/comments', views.PostCommentView.as_view(), name='post-comments'),

]