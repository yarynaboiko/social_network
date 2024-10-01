from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from posts.forms import PostForm
from posts.models import Post


# Create your views here.
class ProfilePostCreateView(CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    success_url = reverse_lazy('profile-my-detail')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)
