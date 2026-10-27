"""카드뉴스 렌더러.
사용: python3 template/render.py <cards.html> <출력폴더>
cards.html 안의 각 class="s" 요소(section)(1080x1350)를 순서대로 01.jpg, 02.jpg ... 로 저장한다.
"""
import sys, os
from playwright.sync_api import sync_playwright
src, out = os.path.abspath(sys.argv[1]), sys.argv[2]
os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=1)
    pg.goto('file://' + src); pg.wait_for_timeout(800)
    els = pg.query_selector_all('.s')
    for i, el in enumerate(els, 1):
        el.screenshot(path=os.path.join(out, f'{i:02d}.png'))
    b.close()
from PIL import Image
for f in sorted(os.listdir(out)):
    if f.endswith('.png'):
        Image.open(os.path.join(out, f)).convert('RGB').save(os.path.join(out, f[:-4] + '.jpg'), quality=92)
        os.remove(os.path.join(out, f))
print('rendered', len([f for f in os.listdir(out) if f.endswith('.jpg')]))
