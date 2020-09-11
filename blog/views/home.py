from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models.post import Post,Tag

NUM_OF_POSTS = 5


def home(request, username=None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        # post_list = Post.objects.filter(user=user)
        username = "tag1"
        b1 = Tag.objects.get(name = username)
        posts = Post.objects.filter(tag=b1)
    else:
        # post_list = Post.objects.all()
        posts = Post.objects.filter()

    # post_list = post_list.order_by('-pub_date')

    # paginator = Paginator(post_list, NUM_OF_POSTS)  # Show NUM_OF_PAGES posts per page
    # page = request.GET.get('page')

    # posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts,
                                              'first_name': first_name,
                                              'last_name': last_name,
                                              'home_page':True,})
