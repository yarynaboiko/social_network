from django.urls import path
from groups import views

urlpatterns = [
    path('create-group/', views.GroupCreateView.as_view(), name='group-create'),
    path('update/<int:pk>', views.GroupUpdateView.as_view(), name='group-update'),
    path('<int:pk>', views.GroupDetailView.as_view(), name='group-detail'),
    path('<int:pk>/join', views.GroupMemberCreateView.as_view(), name='group-join'),
    path('<int:pk>/leave', views.GroupMemberDeleteView.as_view(), name='group-leave'),

]