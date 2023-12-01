from django.db import models
from django.urls import reverse


class Post(models.Model):
    # * 게시판은 게시글의 ID, 제목, 본문, 생성날짜로 구성되며 제목과 본문은 각각 텍스트 입니다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("board:post_detail", args=[self.pk])

    class Meta:
        ordering = ['-id']
