from django.urls import path
from posts import views

urlpatterns = [
    path('create/', views.ProfilePostCreateView.as_view(), name='profile-post-create'),

]