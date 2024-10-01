from django.urls import path
from following import views

urlpatterns = [
    path('subscribe/<int:profile_id>', views.SubscriberCreateView.as_view(), name='subscriber-create'),
    path('unsubscribe/<int:profile_id>', views.SubscriberDeleteView.as_view(), name='subscriber-delete'),
    path('friend_request/<int:profile_id>', views.FriendRequestCreateView.as_view(), name='friend-request-create'),
    path('friend_request/delete/<int:profile_id>', views.FriendRequestDeleteView.as_view(), name='friend-request-delete'),
    path('friend_request/', views.FriendRequestListView.as_view(), name='friend-request-list'),
    path('friend_request/<int:request_id>/accept', views.FriendCreateView.as_view(), name='friend-request-accept'),
    path('friend_request/<int:request_id>/decline', views.FriendRequestDeclineView.as_view(), name='friend-request-decline'),

]