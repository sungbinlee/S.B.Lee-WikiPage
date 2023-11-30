from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Post
from board.post_suggestions import get_related_posts, indices


class PostListview(ListView):
    model = Post
    paginate_by = 15


post_list = PostListview.as_view()


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.object.id
        response = get_related_posts(indices.get(post_id))
        related_posts_ids = [i["post"] for i in response]
        related_posts = Post.objects.filter(id__in=related_posts_ids)

        related_posts_with_similarity = []
        for item in response:
            post = related_posts.get(id=item['post'])
            related_posts_with_similarity.append({'post': post, 'similarity': round(item['similarity'] * 100, 2)})
        context['related_posts'] = related_posts_with_similarity
        return context


post_detail = PostDetailView.as_view()
