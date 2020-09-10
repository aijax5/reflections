from django.contrib import admin

from blog.models.comment import Comment
from blog.models.post import Post
from blog.models.post import Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
