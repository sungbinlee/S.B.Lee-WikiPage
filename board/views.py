from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Post
from board.post_suggestions import get_related_posts, indices, extract_word_associations
from django.core.paginator import Paginator
import networkx as nx
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
from matplotlib import font_manager as fm
matplotlib.use('Agg')


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

        paginator = Paginator(related_posts_with_similarity, 6)
        page_number = self.request.GET.get('page')
        context['related_posts'] = paginator.get_page(page_number)
        return context


post_detail = PostDetailView.as_view()


def association_map_view(request):
    association_data = extract_word_associations(threshold=0.1)

    G = nx.Graph()

    for edge in association_data:
        G.add_edge(edge[0], edge[1])

    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 한국어 폰트 경로
    font_prop = fm.FontProperties(fname=font_path, size=14)

    plt.figure(figsize=(18, 14))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, font_weight='bold', node_color='skyblue', font_size=12, font_family='AppleGothic')

    # 이미지를 BytesIO로 변환하여 base64로 인코딩
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 인코딩된 이미지를 HTML에 넣기 위해 base64로 변환
    graph = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    context = {'graph': graph, 'association_data': association_data}
    return render(request, 'board/association_map.html', context)
