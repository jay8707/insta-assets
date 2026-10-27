# 카드뉴스 제작 규칙
- 디자인 기준: `cards_01_example.html` (1080x1350, 파란 톤, 하단 로고). 클래스·색·폰트를 그대로 재사용한다.
- 새 글: `posts/YYYY-MM-DD-<slug>/cards.html` 작성 → 로고 경로는 `../../template/logo_wide_light.png` 처럼 상대경로.
- 렌더: `python3 template/render.py posts/<id>/cards.html posts/<id>` → 01.jpg~NN.jpg (5~8장)
- `posts/<id>/manifest.json`: {"id","caption","fb_caption","link","files":[{"media_type":"IMAGE","image_url":"https://raw.githubusercontent.com/jay8707/insta-assets/main/posts/<id>/01.jpg"},...]}
- 승인 링크: https://hook.eu1.make.com/pe5e9s5uf16n1ihpiwohai2m77bw8wbl?post=<id>&token=<토큰> (클릭 시 인스타 캐러셀 + 페이스북 글 게시, 같은 id는 한 번만)
