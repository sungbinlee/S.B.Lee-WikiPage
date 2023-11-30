from django.contrib import admin
from .models import Post, RelatedPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content"]
    list_display_links = ['title']


@admin.register(RelatedPost)
class RelatedPost(admin.ModelAdmin):
    list_display = ["id", "post", "related_to", "similarity"]

