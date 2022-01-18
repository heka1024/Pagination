from django.test import TestCase

from post.models import Post, Status


class PostTest(TestCase):
    def test_잘_생성된다(self):
        post = Post.objects.create(title="안녕", content="세상!")
        assert Post.objects.count() == 1
        assert post.status == Status.DRAFT
