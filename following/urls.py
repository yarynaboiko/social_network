from django.urls import path
from following import views

urlpatterns = [
    path('subscribe/<int:profile_id>', views.SubscriberCreateView.as_view(), name='subscriber-create'),
    path('unsubscribe/<int:profile_id>', views.SubscriberDeleteView.as_view(), name='subscriber-delete'),
    path('friend_request/<int:profile_id>', views.FriendRequestCreateView.as_view(), name='friend-request-create'),
    path('friend_request/delete/<int:profile_id>', views.FriendRequestDeleteView.as_view(), name='friend-request-delete'),

]