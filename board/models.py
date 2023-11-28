from django.db import models


class Post(models.Model):
    # * 게시판은 게시글의 ID, 제목, 본문, 생성날짜로 구성되며 제목과 본문은 각각 텍스트 입니다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RelatedPost(models.Model):
    #  * 게시글은 연관 게시글이라는 항목을 가지고 있으며, 연관게시글은 게시글과 내용이 유사한 게시글 입니다.
    #  * 연관게시글이 보여지는 순서는 연관도가 높은것을 우선적으로 보여주도록 만들어주시면 더 좋습니다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="related_post")
    related_to = models.ForeignKey(Post, on_delete=models.CASCADE)
    similarity = models.FloatField(default=0.0)
