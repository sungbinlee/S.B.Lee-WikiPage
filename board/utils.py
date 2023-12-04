from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from board.models import Post
import pandas as pd
import re


class PostAnalyzer:

    def __init__(self):
        self.all_contents = pd.DataFrame(list(Post.objects.values().order_by("id")))
        self.load_stopwords()
        self.data_preprocessing()
        self.calculate_tfidf()
        self.create_indices()

    def load_stopwords(self):
        file_path = "board/stopwords.txt"
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        self.stop_words = file_content.split('\n')

    def data_preprocessing(self):
        pattern = r'(시켰습니다|됩니다|으로써|적이며|라고|으로|합니다|입니다|에서|롭게|하면|하고|하는|적인|시킬|로|할|을|를|은|는|이|가|한|에|과|의|와|들)(?=[^가-힣])'
        self.all_contents["content"] = self.all_contents["content"].apply(lambda x: re.sub(pattern, '', x))

    def calculate_tfidf(self):
        self.tfidf_vectorizer = TfidfVectorizer(stop_words=self.stop_words, max_df=0.6, min_df=2)
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.all_contents["content"])
        self.cosine_similarities = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def create_indices(self):
        self.indices = pd.Series(self.all_contents.index, index=self.all_contents["id"]).drop_duplicates()

    def get_related_posts(self, post_id):
        mapped_post_id = self.indices[post_id]
        similarity = list(enumerate(self.cosine_similarities[mapped_post_id]))
        similarity = sorted(similarity, key=lambda x: x[1], reverse=True)
        related_posts = [
            {
                "post": self.indices[self.indices == post[0]].index[0],
                "similarity": post[1]
            }
            for post in similarity if post[1] > 0
        ]
        return related_posts[1:]

    def extract_word_associations(self, threshold=0.05):
        associations = []
        feature_names = self.tfidf_vectorizer.get_feature_names_out()
        rows, cols = self.cosine_similarities.shape
        for i in range(rows):
            for j in range(cols):
                if i != j and self.cosine_similarities[i][j] >= threshold:
                    word_i = feature_names[i]
                    word_j = feature_names[j]
                    associations.append((word_i, word_j))
        return associations
