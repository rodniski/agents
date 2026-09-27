---
name: macos-design
description: >-
  Use quando o usuário pedir app macOS, desktop nativo, UI estilo Apple,
  system utility, “native feel”, sidebar + traffic lights, ou ferramenta
  que precise parecer que pertence ao Mac.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# macOS Design

App nativo **não é site numa janela**. É ferramenta de sistema: aparece quando precisa, some do caminho depois. O conteúdo do usuário é o astro; chrome existe pra servir.

Nativo de verdade → **SwiftUI** (stack mobile/desktop do Gui). Web/Electron/Tauri/artefato → simule o chrome e a linguagem; não invente um site responsivo com casca de Mac.

Antes de codar, leia o que couber em `references/`:
- sempre → `layout-and-composition.md`
- atalhos, painéis, toasts, DnD → `interaction-patterns.md`
- light/dark, cor, tipo, blur, sombra → `visual-design.md`

## Filosofia

- Destino ≠ ferramenta. Landing Awwwards é teatro; Mac app é **contenção operacional**.
- Progressive disclosure: UI secundária só quando há conteúdo pra justificar.
- Teclado é first-class. Sem atalho na ação primária = incompleto.
- Feedback imediato em toda mudança de estado. Sem feedback = usuário assume falha.
- Drag-and-drop pra dentro **e** pra fora — não negociável pro “native feel”.

## Preflight

1. Top bar (~50px) = ações globais + **zona de drag**; sparse.
2. Sidebar só se nav ≥3 destinos; senão full-width utility.
3. Traffic lights integrados no top bar/sidebar (nunca flutuando torto).
4. Empty state limpo; esconda filtros/toolbars até existir conteúdo.
5. Light **e** dark desenhados separados — **não inverter** a palette.
6. Search proeminente (top bar, floating ou ⌘K).
7. Micro-transição em todo state change.
8. Onboarding breve: ensina **fazendo** o atalho, não lendo um wizard.

## Layout Apple (default)

```text
┌─ traffic + top bar (drag) ─────────────────────┐
│ sidebar (nav) │        conteúdo (dados)         │
└─────────────────────────────────────────────────┘
```

Conteúdo no centro. Detail = painel que desliza (mantém contexto), não “nova página web”. Skip sidebar em utility de uma missão.

## Visual (essência)

| Tema | Regra |
|------|--------|
| Light/dark | Design independente. Dark precisa **mais** separação entre superfícies; light colapsa tons. Evite `#000` puro — cinzas Apple (`#1C1C1E`…) |
| Hierarquia | Por **níveis de fundo**, não por borda grossa. Borda 0.5px low-opacity se precisar |
| Accent | Só highlight/ação/foco — nunca fill de área grande |
| Tipo | SF / `-apple-system`. Body ~13px (menor que web). Tracking apertado em título |
| Vibrancy | Blur+saturate em sidebar/toolbar/popover — **não** na área de conteúdo |
| Sombra | Camadas + `0 0 0 0.5px` (definição sem borda visível) — isso **é** o look |
| Radius | Janela 10 · panel 12 · card 8 · botão/input 6 |
| Grid | Base 8px. Top bar 48–52. Botão/input ~28 de altura |

## Interação (essência)

- Atalhos padrão: ⌘N ⌘F ⌘W ⌘, Esc Enter; hints visuais tipo `<kbd>` ao lado da ação.
- Search: floating (utility visual) · ⌘K palette (app complexo) · inline no top bar (browser de conteúdo).
- Optimistic UI: atualiza local → toast → async; falha reverte + erro.
- Toast leve 2–3s. Floating action bar no preview (pill + blur).
- Onboarding: um modal; dismiss = executar o atalho ensinado.

## ❌ / ✅

```text
❌ Site com border-radius e três dots vermelho/amarelo/verde no canto
❌ Inverter light→dark; borda 2px em tudo; accent como background de seção
❌ Sidebar pra 1–2 destinos; empty state com toolbar cheia de filtro inútil
❌ Ação primária sem atalho; DnD só “upload web”

✅ Chrome integrado + drag zone limpa; superfícies em camadas; vibrancy certo
✅ Light e dark pensados à parte; conteúdo opaco; painéis com blur
✅ Utility hiperfocada ou shell Finder-like; teclado + DnD nos dois sentidos
✅ SwiftUI nativo quando for app Mac de verdade
```

## Hard rules

- Não misture com skill `frontend-design` de landing Awwwards — ramos diferentes.
- Web artifact: simule traffic lights, SF stack, vibrancy, radius Apple — mas admita que é simulação.
- Respeite `prefers-color-scheme` e accent do sistema quando o host permitir.
- Referências longas (tokens, CSS, padrões) → pasta `references/`; não duplique prosa aqui.
