from random import choice

from django.db import models

from enum import Enum
from enumfields import EnumField


class TimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(Enum):
    DRAFT = "draft", "진행 중"
    PUBLISHED = "published", "발행 완료"
    DELETED = "deleted", "삭제됨"

    def __init__(self, value, description):
        self.v = value
        self.description = description

    @property
    def value(self):
        return self.v

    @classmethod
    def random(cls):
        return choice(list(cls))


class PostQuerySet(models.QuerySet):
    def paginated(self, page: int, page_size: int = 20):
        """단순한 페이지네이션 구현"""
        limit = (page - 1) * page_size
        return self[limit : limit + page_size]

    def paginated_v2(self, page: int, page_size: int = 20):
        """커버링 인덱스를 이용"""
        index_only_scan = self.paginated(page, page_size)
        return self.filter(id__in=index_only_scan)


class Post(TimeMixin, models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    status = EnumField(Status, default=Status.DRAFT)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ["-id"]


e
