"""Converte todas as JPG da pasta images/ pra WebP com qualidade 80."""
from PIL import Image
import os
import glob

IMAGES_DIR = 'images'
QUALITY = 82
total_jpg = 0
total_webp = 0
results = []

for jpg_path in sorted(glob.glob(os.path.join(IMAGES_DIR, '*.jpg'))):
    name = os.path.basename(jpg_path).rsplit('.', 1)[0]
    webp_path = os.path.join(IMAGES_DIR, f'{name}.webp')

    # Pula arquivos especiais
    if name.startswith('_'):
        continue

    jpg_size = os.path.getsize(jpg_path)
    total_jpg += jpg_size

    img = Image.open(jpg_path).convert('RGB')
    # Reduz pra max 1200px (suficiente pra qualquer card retina)
    if max(img.size) > 1200:
        img.thumbnail((1200, 1200), Image.LANCZOS)
    img.save(webp_path, 'WEBP', quality=QUALITY, method=6)

    webp_size = os.path.getsize(webp_path)
    total_webp += webp_size
    pct = (1 - webp_size / jpg_size) * 100
    results.append((name, jpg_size, webp_size, pct))
    print(f'{name:20} {jpg_size//1024:>4}KB → {webp_size//1024:>4}KB  ({pct:+.0f}%)')

print('=' * 60)
print(f'TOTAL: {total_jpg//1024}KB → {total_webp//1024}KB')
print(f'Economia: {(total_jpg-total_webp)//1024}KB ({(1-total_webp/total_jpg)*100:.0f}%)')
