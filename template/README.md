# 카드뉴스 제작 규칙

## 디자인 테마 (매일 바뀜) — 2026-11 이후 이 방식이 기준
- cards.html <head>는 이 두 줄만 쓴다(스타일을 직접 쓰지 않는다):
  `<link rel="stylesheet" href="../../template/base.css">`
  `<link rel="stylesheet" href="../../template/themes/<테마>.css">`
- 테마 5종: blue(밝은 회청+파랑) · night(짙은 남색+시안 네온) · paper(크림+주황, 명조 제목) · mint(진초록 표지+연민트) · pop(노랑+검정 굵은 테두리)
- 고르는 법: 테마 순서 [blue, night, paper, mint, pop]에서 (그해 1월 1일부터 센 날짜 번호) % 5 번째. 전날과 같은 테마가 되면 다음 것으로.
- 미리보기: template/themes/preview.png, 테마별 예시: examples/<테마>/cards.html
- 마크업 클래스(공통): section.s(1080x1350) / 첫 장은 section.s.cover / 마지막 장은 section.s.cta / div.grid(장식) / .tag / .no / h1·h2 / span.b(강조) / p.lead / .list > .item(.x .v) > i / .two > .big > .num + .cap / .chips > div > span / .foot > img(src="../../template/logo_wide_light.png") + span.page / .btn / .contact / p.note / CTA 제목 강조는 span.hl
- 모양도 매번 다르게: 같은 글에서도 장마다 .list / .big 숫자 강조 / .chips / 체크리스트를 섞고, 전날과 다른 조합을 쓴다.
- manifest.json에 "theme":"<테마>"를 넣는다.

## (예전 방식) 아래는 카드뉴스 01 기준 — 참고용
- 디자인 기준: `cards_01_example.html` (1080x1350, 파란 톤, 하단 로고). 클래스·색·폰트를 그대로 재사용한다.
- 새 글: `posts/YYYY-MM-DD-<slug>/cards.html` 작성 → 로고 경로는 `../../template/logo_wide_light.png` 처럼 상대경로.
- 렌더: `python3 template/render.py posts/<id>/cards.html posts/<id>` → 01.jpg~NN.jpg (5~8장)
- `posts/<id>/manifest.json`: {"id","caption","fb_caption","link","files":[{"media_type":"IMAGE","image_url":"https://raw.githubusercontent.com/jay8707/insta-assets/main/posts/<id>/01.jpg"},...],"fb_photos":[{"type":"url","url":"(files와 같은 이미지 주소)"},...]}
- 승인 링크: https://hook.eu1.make.com/pe5e9s5uf16n1ihpiwohai2m77bw8wbl?post=<id>&token=<토큰> (클릭 시 인스타 캐러셀 + 페이스북 글 게시, 같은 id는 한 번만)

## 업로드 방식 (예약 작업용 — git push 금지)
- 예약 작업 환경에는 GitHub 인증이 없으므로 git push를 쓰지 않는다.
- Make 시나리오 "카드뉴스 파일 GitHub 업로드"(ID 8316814)를 scenarios_run(responsive=true)으로 실행하고 data에 {post_id, cards_html, manifest_json}을 텍스트로 넘긴다.
- Make가 posts/<ID>/cards.html·manifest.json을 커밋하면 GitHub Actions(.github/workflows/render.yml)가 1~3분 안에 01.jpg~ 를 렌더해 커밋한다.
- 확인: https://raw.githubusercontent.com/jay8707/insta-assets/main/posts/<ID>/01.jpg 가 200이 될 때까지 기다린다(최대 5분).
