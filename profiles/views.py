from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import UpdateView, DetailView, View

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

