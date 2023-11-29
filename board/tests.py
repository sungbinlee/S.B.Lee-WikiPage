from django.test import TestCase
from django.urls import reverse
from board.models import Post


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_posts = 20
        for post_id in range(number_of_posts):
            Post.objects.create(
                title=f"Test Post {post_id}", content=f"Test content {post_id}"
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/board/")
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        response = self.client.get(reverse("board:post_list"))
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(len(response.context["post_list"]) == 15)


class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title="Test Post", content="Test content")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/board/1/")
        self.assertEqual(response.status_code, 200)

    def test_view_returns_correct_post(self):
        response = self.client.get(reverse("board:post_detail", kwargs={"pk": 1}))
        self.assertEqual(response.context["post"].title, "Test Post")
        self.assertEqual(response.context["post"].content, "Test content")
