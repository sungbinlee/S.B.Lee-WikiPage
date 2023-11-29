from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Post


class PostListview(ListView):
    model = Post
    paginate_by = 15


post_list = PostListview.as_view()


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


post_detail = PostDetailView.as_view()


# def post_detail(request, pk):
#     related_posts = [1,2,3,4]
#     context = {
#         "related_posts": related_posts,
#     }
#     return render(request, "board/post_detail.html", context)
