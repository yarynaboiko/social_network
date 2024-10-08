from django.urls import path
from posts import views

urlpatterns = [
    path('create-group/', views.ProfilePostCreateView.as_view(), name='group-create'),

]