"""
Extrai contornos pixel-perfect da logo PNG e gera SVG vetorizado.
Separa por cor: bordô (vinho) e dourado.
"""
import cv2
import numpy as np
import json

# Load
img = cv2.imread('images/logo.png', cv2.IMREAD_UNCHANGED)
if img is None:
    raise SystemExit("Não consegui ler images/logo.png")

H, W = img.shape[:2]
print(f"Imagem: {W}x{H}, channels: {img.shape[2]}")

# Converter pra BGR puro (sem alpha)
if img.shape[2] == 4:
    # Imagem com alpha — usar alpha como mask
    rgba = img
    # Onde alpha é alto = pixel sólido
    alpha = rgba[:, :, 3]
    bgr = rgba[:, :, :3]
else:
    bgr = img
    alpha = np.ones((H, W), dtype=np.uint8) * 255

# Converter pra HSV pra detecção de cor mais robusta
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

# Bordô (#540c18 = vinho escuro) — Hue ~0 (vermelho), Sat alta, Value baixa
# OpenCV HSV: H 0-179, S 0-255, V 0-255
bordo_mask1 = cv2.inRange(hsv, (0, 80, 20), (15, 255, 150))
bordo_mask2 = cv2.inRange(hsv, (165, 80, 20), (179, 255, 150))
bordo_mask = cv2.bitwise_or(bordo_mask1, bordo_mask2)

# Dourado (#c69444 = dourado/mostarda) — Hue ~20-30 (amarelo-laranja)
dourado_mask = cv2.inRange(hsv, (12, 60, 100), (40, 255, 220))

# Aplicar alpha mask (só onde tem pixel)
bordo_mask = cv2.bitwise_and(bordo_mask, alpha)
dourado_mask = cv2.bitwise_and(dourado_mask, alpha)

# Salvar masks pra debug
cv2.imwrite('images/_mask_bordo.png', bordo_mask)
cv2.imwrite('images/_mask_dourado.png', dourado_mask)

print(f"Pixels bordô: {np.sum(bordo_mask > 0)}")
print(f"Pixels dourado: {np.sum(dourado_mask > 0)}")

# Encontrar contornos
def contours_for(mask, simplify_epsilon=0.5):
    # Limpar ruído com kernel maior pra suavizar bordas pixeladas
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # Blur leve pra suavizar antes do contour
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = [c for c in contours if cv2.contourArea(c) > 30]
    # MUITO menos simplificação = mais pontos = curvas mais lisas
    simplified = []
    for c in contours:
        c2 = cv2.approxPolyDP(c, simplify_epsilon, True)
        simplified.append(c2)
    return simplified

bordo_contours = contours_for(bordo_mask)
dourado_contours = contours_for(dourado_mask)

print(f"Contornos bordô: {len(bordo_contours)} ({[len(c) for c in bordo_contours]} pontos cada)")
print(f"Contornos dourado: {len(dourado_contours)} ({[len(c) for c in dourado_contours]} pontos cada)")

# Normalizar coords pro espaço 0-100 (viewBox SVG) com Y invertido pra Three.js
def normalize(contours):
    out = []
    for c in contours:
        pts = []
        for [pt] in c:
            x, y = pt
            # Centralizar e escalar pra 7 unidades (menor que antes)
            nx = (x - W/2) / max(W, H) * 7
            ny = -(y - H/2) / max(W, H) * 7
            pts.append([round(nx, 3), round(ny, 3)])
        out.append(pts)
    return out

data = {
    'imageSize': [W, H],
    'bordo': {
        'color': '#540c18',
        'paths': normalize(bordo_contours)
    },
    'dourado': {
        'color': '#c69444',
        'paths': normalize(dourado_contours)
    }
}

with open('images/logo_paths.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nSalvo em images/logo_paths.json")
print(f"  Bordô: {sum(len(p) for p in data['bordo']['paths'])} pontos totais")
print(f"  Dourado: {sum(len(p) for p in data['dourado']['paths'])} pontos totais")
