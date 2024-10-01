from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView

from accounts.models import User
from following.models import Subscriber, FriendRequest, Friend
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
        if form.instance.from_user == form.instance.to_user:
            return redirect('profile-user-detail', pk=self.kwargs['profile_id'])
        
        form.instance.save()
        return super().form_valid(form)


class FriendRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = FriendRequest

    def get_object(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['profile_id'])
        return get_object_or_404(FriendRequest, from_user=self.request.user, to_user=profile.user)

    def get_success_url(self):
        return reverse_lazy('profile-user-detail', kwargs={'pk': self.kwargs['profile_id']})


class FriendRequestListView(LoginRequiredMixin, ListView):
    model = FriendRequest
    template_name = 'following/friend-request-list.html'
    context_object_name = 'friend_requests'

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user = self.request.user, accepted=False)


class FriendCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_request = get_object_or_404(FriendRequest, pk=self.kwargs['request_id'], to_user=self.request.user)
        friend_request.accepted = True
        friend_request.save()
        friend = Friend.objects.create(from_user=friend_request.from_user, to_user=self.request.user)
        return HttpResponseRedirect(reverse('friend-request-list'))


class FriendRequestDeclineView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        friend_request = get_object_or_404(FriendRequest, pk=self.kwargs['request_id'], to_user=self.request.user)
        friend_request.delete()
        return HttpResponseRedirect(reverse('friend-request-list'))
