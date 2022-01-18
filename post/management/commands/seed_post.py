from django.core.management import BaseCommand

from post.factories import PostFactory
from post.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        size = 2_000
        for i in range(size):
            print(i, "/", size)

            posts = PostFactory.build_batch(1_000)
            Post.objects.bulk_create(posts)
