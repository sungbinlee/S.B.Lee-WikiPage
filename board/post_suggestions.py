from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from board.models import Post
import pandas as pd

# 데이터베이스에서 모든 게시물을 가져와 DataFrame에 저장
all_posts = Post.objects.order_by("id")
all_contents = pd.DataFrame(list(Post.objects.values().order_by("id")))

# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer(max_df=0.6, min_df=2)  # 전체 문서 에서 60% 이상 나온 단어 무시
tfidf_matrix = tfidf_vectorizer.fit_transform(all_contents["content"])

# 게시물 간 유사도 계산
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

# 게시물 ID를 DataFrame 인덱스로 매핑하는 인덱스 생성
indices = pd.Series(all_contents.index, index=all_contents["id"]).drop_duplicates()


def get_related_posts(post_id, cosine_similarities=cosine_similarities):
    similarity = list(enumerate(cosine_similarities[post_id]))
    similarity = sorted(similarity, key=lambda x: x[1], reverse=True)
    # 유사도가 0보다 큰 게시물들의 인덱스를 찾아서 관련 게시물로 반환
    related_posts = [
        {
            "post": indices[indices == post[0]].index[0],
            "similarity": post[1]
        }
        for post in similarity if post[1] > 0
    ]
    return related_posts[1:]
