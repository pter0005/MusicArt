# MusicArt — Escola de Música

Landing page institucional da MusicArt, escola de música em Arujá-SP.

## 📁 Estrutura

```
musicart-site/
├── index.html          ← arquivo principal
├── favicon.svg         ← ícone da aba do navegador
├── README.md           ← este arquivo
└── images/             ← fotos otimizadas (JPG + WebP)
    ├── antonio.jpg / .webp
    ├── gabriel.jpg / .webp
    ├── ana-julia.jpg / .webp
    ├── felipe.jpg / .webp
    └── nicolas.jpg / .webp
```

## 🚀 Como abrir localmente

Só dar **double-click** no `index.html` que abre no navegador. Tudo funciona sem servidor.

## 🌐 Como subir no GitHub Pages (gratuito)

1. Crie um repositório no GitHub (ex: `musicart-site`)
2. Suba todos os arquivos da pasta (commit + push)
3. No GitHub: **Settings → Pages → Source: main branch / root**
4. Em ~1 minuto seu site fica no ar em `https://seu-usuario.github.io/musicart-site`

Depois é só apontar um domínio próprio (ex: `musicart.com.br`) pra esse endereço, comprado em Registro.br (~R$40/ano).

## ⚡ Performance

- **Imagens em WebP + JPG fallback** (`<picture>` element) — economia de ~35%
- **Lazy loading** em todas as imagens (`loading="lazy"`)
- **Particulas reduzidas em mobile** (metade da quantidade)
- **`prefers-reduced-motion` respeitado** (acessibilidade)
- Total da página: ~800KB (já com todas as fotos)

## 🎨 Identidade visual

- Cores: bordô `#540c18`, dourado `#c69444`, branco, nude
- Tipografia: Cormorant Garamond (títulos) + Raleway (texto)
- Logo: SVG inline (não depende de arquivo externo)

## 📝 Conteúdo a editar

Procurar e substituir no `index.html`:

| Onde | O quê |
|------|-------|
| Cards dos professores | `*texto de apresentação*` → bio real do Antonio e Gabriel |
| Seção depoimentos | Trocar pelos depoimentos reais |
| Stats do hero | "8 instrumentos" e "+50 alunos" — ajustar números |
| Footer | Adicionar redes sociais reais (Instagram, YouTube) |

## 🔧 Migrando pro Claude Code

Se quiser continuar editando com Claude Code (CLI no terminal):

1. Instale Node.js: https://nodejs.org
2. Instale Claude Code: `npm install -g @anthropic-ai/claude-code`
3. Faça login: `claude login`
4. Abra o terminal nesta pasta: `cd musicart-site`
5. Rode: `claude`

A partir daí, é só pedir mudanças em linguagem natural.

## 📞 Contato

WhatsApp: (11) 91241-0875
Endereço: R. Raymundo Fernandes, 696 - Parque Rodrigo Barreto, Arujá - SP
