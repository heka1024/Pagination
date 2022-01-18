# 페이지네이션
`Django`에서 페이지 넘버 기반 페이지네이션 성능을 개선하는 방법을 담고 있는 레포지토리입니다.
`PostgreSQL` 상에서 커버링 인덱스를 이용해 성능을 개선합니다.

# 실험 준비 방법
## 파이썬 패키지 설치
```bash
poetry init
```
을 통해 파이썬 패키지를 설치할 수 있습니다. 의존성은 `pyproject.toml`에서 확인할 수 있습니다.

## 데이터베이스 준비
```bash
docker-compose -f docker-compose.dev.yml up -d
```
도커를 통해 실험과 동일한 환경의 DB를 준비할 수 있습니다.

```bash
poetry run python manage.py seed_post
```
위 커맨드 실행을 통해 데이터베이스에 200만개의 게시글을 생성할 수 있습니다.

# 실험 방법
콘솔 등에서
- `Post.objects.paginated(100000)`
- `Post.objects.paginated_v2(100000)`

을 실행해서 성능을 확인할 수 있습니다. 200만개 기준으로 `paginated_v2`(커버링 인덱스 이용)이
약 1.8배정도 더 뛰어난 성능을 보였습니다.