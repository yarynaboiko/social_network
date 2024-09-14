from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from accounts.models import User
from following.models import Subscriber, FriendRequest
from profiles.models import Profile


# Create your views here.
class SubscriberCreateView(LoginRequiredMixin, CreateView):
    model = Subscriber
    fields = []
    context_object_name = 'subscriber'

    def get_success_url(self):
        return reverse_lazy('profile-user-detail', kwargs={'pk': self.kwargs['profile_id']})

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        profile = get_object_or_404(Profile, pk=self.kwargs['profile_id'])
        form.instance.to_user = profile.user
        form.instance.save()
        return super().form_valid(form)


class SubscriberDeleteView(LoginRequiredMixin, DeleteView):
    model = Subscriber

    def get_object(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['profile_id'])
        return get_object_or_404(Subscriber, from_user=self.request.user, to_user=profile.user)

    def get_success_url(self):
        return reverse_lazy('profile-user-detail', kwargs={'pk': self.kwargs['profile_id']})


class FriendRequestCreateView(LoginRequiredMixin, CreateView):
    model = FriendRequest
    fields = []

    def get_success_url(self):
        return reverse_lazy('profile-user-detail', kwargs={'pk': self.kwargs['profile_id']})

    def form_valid(self, form):
        form.instance.from_user = self.request.user
        profile = get_object_or_404(Profile, pk=self.kwargs['profile_id'])
        form.instance.to_user = profile.user
        form.instance.save()
        return super().form_valid(form)


class FriendRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = FriendRequest

    def get_object(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['profile_id'])
        return get_object_or_404(FriendRequest, from_user=self.request.user, to_user=profile.user)

    def get_success_url(self):
        return reverse_lazy('profile-user-detail', kwargs={'pk': self.kwargs['profile_id']})
