from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment


# Create your views here.
class ProfilePostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new_post.html'
    success_url = reverse_lazy('profile-my-detail')
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


class LikePushView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post_db = get_object_or_404(Post, pk=self.kwargs['post_id'])
        if request.user in post_db.likes.all():
            post_db.likes.remove(request.user)
        else:
            post_db.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER', 'profile-my-detail'))


class SharePushView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post_db = get_object_or_404(Post, pk=self.kwargs['post_id'])
        if request.user in post_db.shares.all():
            post_db.shares.remove(request.user)
        else:
            post_db.shares.add(request.user)

        return redirect(request.META.get('HTTP_REFERER', 'profile-my-detail'))


class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'posts/post_comment.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['post'] = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return context

    def form_valid(self, form):
        post_db = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.from_user = self.request.user
        form.instance.post = post_db
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-comments', kwargs={'post_id': self.kwargs['post_id']})


