from random import choice

from factory import LazyFunction
from factory.django import DjangoModelFactory

from .models import Post, Status

_tokens = """이지러는 졌으나 보름을 갓 지난 달은 부드러운 빛을 흔붓이 흘리고 있다. 대화까지는 팔십 리의 밤길, 고개를 둘이나 넘고 개울을 하나 건너고 벌판과 산길을 걸어야 된다. 길은 지금 긴 산허리에 걸려 있다.
밤중을 지난 무렵인지 죽은 듯이 고요한 속에서 짐승 같은 달의 숨소리가 손에 잡힐 듯이 들리며, 콩 포기와 옥수수 잎새가 한층 달에 푸르게 젖었다. 산허리는 온통 메밀 밭이어서 피기 시작한 꽃이 소금을 뿌린 듯이 흐뭇한 달빛에 숨이 막힐 지경이다. 붉은 대공이 향기같이 애잔하고 나귀들의 걸음도 시원하다.
길이 좁은 까닭에 세 사람은 나귀를 타고 외줄로 늘어섰다. 방울소리가 시원스럽게 딸랑딸랑 메밀 밭께로 흘러간다. 앞장선 허생원의 이야기 소리는 꽁무니에 선 동이에게는 확적히는 안 들렸으나, 그는 그대로 개운한 제멋에 적적하지는 않았다.
""".split()


def _words(n: int):
    random_words = [choice(_tokens) for _ in range(n)]
    return LazyFunction(lambda: " ".join(random_words))


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = _words(4)
    content = _words(1000)
    status = LazyFunction(Status.random)
