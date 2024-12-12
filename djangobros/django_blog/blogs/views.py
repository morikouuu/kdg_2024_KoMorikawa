from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog,Comment,Reply
from django.views.generic  import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from .models import  Comment

CommentForm = forms.modelform_factory(Comment, fields=('text', ))

# Create your views here
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})

class BlogDetailView(generic.DetailView):
    
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
        return context

def comment_create(request, pk):
    
    blog = get_object_or_404(Blog, pk=pk)
    form = CommentForm(request.POST or None)
    
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
        return redirect('blogs:detail', pk=blog.pk)

    context = {
        'form': form,
        'blog': blog
    }
    return render(request, 'blogs/comment_form.html', context)

def reply_create(request, comment_id):
    
    comment = get_object_or_404(Comment, pk=comment_id)
    blog = comment.blog
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent = comment
        reply.blog = blog
        reply.save()
        return redirect('blogs:detail', pk=comment.blog.pk)

    context = {
        'form': form,
        'blog': blog,
        'comment': comment,
    }
    return render(request, 'blogs/comment_form.html', context)




class CreateView(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blogs/blog_form.html'
    success_url = reverse_lazy('blogs:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)
    
class DeleteView(DeleteView):
    model = Blog

    success_url = reverse_lazy('blogs:index')

class UpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'blogs/blog_form.html'
    
    def get_success_url(self):
        return reverse_lazy('blogs:detail', kwargs={'blog_id': self.object.pk})
    

class CommentCreateView(CreateView):
    model = Comment
    fields = [
        'text']
    
    template_name = 'blogs/blog_form.html'
    
    def form_valid(self, form):
        blog = get_object_or_404(Blog, id=self.kwargs['pk'])
        form.instance.blog = blog  
        return super().form_valid(form)
    
    def get_success_url(self):
        
        return reverse_lazy('blogs:index')
    
class ReplyCreateView(CreateView):
    model = Comment
    fields = ['text']  
    template_name = 'blogs/comment_form.html'
    success_url = reverse_lazy('blogs:index')

    def form_valid(self, form):
        # overraide
        blog_id = self.kwargs['pk']
        blog = get_object_or_404(Blog, id=blog_id)
        parent = self.kwargs.get('pk')
        
        


        
        form.instance.blog = blog
        form.instance.parent = parent
        

        return super(ReplyCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogs:detail', kwargs={'blog_id': self.kwargs['blog_id']})

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blogs/comment_detail.html'
    def get_object(self):
        
        blog = get_object_or_404(Blog, pk=self.kwargs['blog_id'])
        
        comment = get_object_or_404(Comment, pk=self.kwargs['comment_id'], blog=blog)
        return comment

