from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import UpdateView, DetailView, View

from following.models import Subscriber, FriendRequest
from profiles.forms import ProfileUpdateForm
from profiles.models import Profile


class BaseProfileView(LoginRequiredMixin, View):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/myprofile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile


class ProfileUpdateView(BaseProfileView, UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'profiles/profile_update.html'
    success_url = reverse_lazy('profile-my-detail')


class ProfileDetailView(BaseProfileView, DetailView):
    template_name = 'profiles/myprofile.html'


class UserProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/userprofile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            subscribe = Subscriber.objects.filter(from_user=self.request.user, to_user=self.get_object().user)
            if subscribe:
                context['is_subscribed'] = True
            friend_request = FriendRequest.objects.filter(from_user=self.request.user, to_user=self.get_object().user)
            if friend_request:
                context['is_friend_request'] = True

        return context
