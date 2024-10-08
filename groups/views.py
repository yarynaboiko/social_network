from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from groups.forms import GroupForm
from groups.mixins import UserIsAdminMixin
from groups.models import Group, GroupMember


# Create your views here.
class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'groups/new_group.html'
    form_class = GroupForm
    success_url = reverse_lazy('profile-my-detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        admin = GroupMember(user=self.request.user, group=form.instance, is_admin=True)
        admin.save()
        return super().form_valid(form)


class GroupUpdateView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    model = Group
    template_name = 'groups/update_group.html'
    form_class = GroupForm
    success_url = reverse_lazy('profile-my-detail')


class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_page.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            group = self.get_object()
            member = group.members.all().filter(user = self.request.user).first()
            if member:
                context['member'] = member
                if member.is_admin:
                    context['is_admin'] = True

        return context


class GroupMemberCreateView(LoginRequiredMixin, CreateView):
    model = GroupMember
    fields = []
    context_object_name = 'group_member'

    def get_success_url(self):
        return reverse_lazy('group-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        form.instance.user = self.request.user
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        form.instance.group = group
        form.instance.save()
        return super().form_valid(form)


class GroupMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = GroupMember

    def get_object(self):
        group = get_object_or_404(Group, pk=self.kwargs['pk'])
        return get_object_or_404(GroupMember, user=self.request.user, group=group)

    def get_success_url(self):
        return reverse_lazy('group-detail', kwargs={'pk': self.kwargs['pk']})