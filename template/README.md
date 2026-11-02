# 카드뉴스 제작 규칙
- 디자인 기준: `cards_01_example.html` (1080x1350, 파란 톤, 하단 로고). 클래스·색·폰트를 그대로 재사용한다.
- 새 글: `posts/YYYY-MM-DD-<slug>/cards.html` 작성 → 로고 경로는 `../../template/logo_wide_light.png` 처럼 상대경로.
- 렌더: `python3 template/render.py posts/<id>/cards.html posts/<id>` → 01.jpg~NN.jpg (5~8장)
- `posts/<id>/manifest.json`: {"id","caption","fb_caption","link","files":[{"media_type":"IMAGE","image_url":"https://raw.githubusercontent.com/jay8707/insta-assets/main/posts/<id>/01.jpg"},...]}
- 승인 링크: https://hook.eu1.make.com/pe5e9s5uf16n1ihpiwohai2m77bw8wbl?post=<id>&token=<토큰> (클릭 시 인스타 캐러셀 + 페이스북 글 게시, 같은 id는 한 번만)

## 업로드 방식 (예약 작업용 — git push 금지)
- 예약 작업 환경에는 GitHub 인증이 없으므로 git push를 쓰지 않는다.
- Make 시나리오 "카드뉴스 파일 GitHub 업로드"(ID 8316814)를 scenarios_run(responsive=true)으로 실행하고 data에 {post_id, cards_html, manifest_json}을 텍스트로 넘긴다.
- Make가 posts/<ID>/cards.html·manifest.json을 커밋하면 GitHub Actions(.github/workflows/render.yml)가 1~3분 안에 01.jpg~ 를 렌더해 커밋한다.
- 확인: https://raw.githubusercontent.com/jay8707/insta-assets/main/posts/<ID>/01.jpg 가 200이 될 때까지 기다린다(최대 5분).
