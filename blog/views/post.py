from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from blog.models.comment import Comment
from blog.models.post import Post,Tag
from django.shortcuts import render

from django import forms

class NameForm(forms.Form):
    tags = forms.CharField(label='Your name', max_length=100)

def PageObjects(request):
    print(request)
#   if request.method == 'POST':
#     form = NameForm(request.POST)
#     print(form)

#     if form.is_valid():
#       answer = form.cleaned_data['value']

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the username
        comments = Comment.objects.filter(post=self.kwargs['pk'])
        context['comments'] = comments
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostSearch(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['tag']
    allTags = Tag.objects.filter()
    names = []
    for tag in allTags:
        my_tuple = (tag.name,tag.name)
        names.append(tag)
    # form = NameForm()
    # return render(request, '/blog/search_post.html', {'form': form})
    template_name = 'blog/search_post.html'
    login_url = reverse_lazy('login')

    # def test_func(self):
    #     return Post.objects.get(id=self.kwargs['pk']).user == self.request.user


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('login')

    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')
    login_url = reverse_lazy('login')

    def test_func(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user
