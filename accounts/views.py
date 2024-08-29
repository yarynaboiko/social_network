from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserLoginForm, UserRegisterForm
from profiles.models import Profile


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile-update')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user, name=form.cleaned_data['first_name'], surname=form.cleaned_data['last_name'])
        login(self.request, user)
        return redirect(reverse_lazy('profile-update'))