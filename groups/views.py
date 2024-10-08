from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from groups.forms import GroupForm
from groups.models import Group


# Create your views here.
class GroupCreateView(CreateView):
    model = Group

    success_url = reverse_lazy('profile-my-detail')
    form_class = GroupForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
