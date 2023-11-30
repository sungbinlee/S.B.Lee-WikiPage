from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from board.models import Post
import pandas as pd
import re

# 데이터베이스에서 모든 게시물을 가져와 DataFrame에 저장
all_posts = Post.objects.order_by("id")
all_contents = pd.DataFrame(list(Post.objects.values().order_by("id")))

# 불용어 리스트 가져오기 출처: https://ahnsun98.tistory.com/35#google_vignette
file_path = "board/stopwords.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    file_content = f.read()

stop_words = file_content.split('\n')

# 불용어 제거(조사, 관사, 동사 etc.)
all_contents["content"] = all_contents["content"].apply(lambda x: re.sub(r'시켰습니다|으로써|적이며|라고|으로|합니다|입니다|에서|하고|하는|적인|로|을|를|은|는|이|가|한|에|과|의|와|들|$', '', x))

# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words, max_df=0.6, min_df=2)  # 전체 문서 에서 60% 이상 나온 단어 무시
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
