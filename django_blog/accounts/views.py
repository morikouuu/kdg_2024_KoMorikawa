
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import CustomUser
from blogs.models import Blog
from blogs.models import Likes
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        # ログイン中のユーザーのプロフィールを返す
        return CustomUser.objects.get(pk=self.request.user.pk)
    
    def get_context_data(self, **kwargs):
        # デフォルトのコンテキストデータを取得
        context = super().get_context_data(**kwargs)
        # 現在ログイン中のユーザーのお気に入りデータを追加
        context['favorites'] = Likes.objects.filter(user_id=self.request.user).select_related('target')
        return context
    
class AuthorView(generic.DetailView):
    model = CustomUser
    template_name = 'accounts/author.html'
    context_object_name = 'author'

    
    
    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, pk=user_id)
    
    def get_context_data(self, **kwargs):
         # デフォルトのコンテキストデータを取得
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(author=self.get_object())
        return context