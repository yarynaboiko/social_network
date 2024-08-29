from django.urls import path
from profiles import views

urlpatterns = [
    path('update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('my-profile/', views.ProfileDetailView.as_view(), name='profile-my-detail'),

]