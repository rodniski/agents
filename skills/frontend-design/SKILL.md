---
name: frontend-design
description: >-
  Use quando o usuário pedir UI/landing nova, redesign, direção estética,
  tipografia, motion, imagery, ou quiser evitar visual genérico de template/IA.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Frontend Design (Classicista)

Use esta skill quando a qualidade depende de **direção de arte, hierarquia, contenção, imagem e motion** — não de contagem de componentes.

**Meta:** interfaces deliberadas, premium, atuais. Composição nível award: uma ideia grande, imagery forte, copy escassa, espaçamento rigoroso, poucos motions memoráveis.

Julgamento = classicista (Renascimento / Grécia): proporção, ritmo, peso tipográfico, luz e sombra, silêncio que carrega significado. Execução = moderna (Astro, Svelte, GSAP, Three). Estética não é verniz; avançado sem forma não tem valor — forma sem clareza também falha.

Você é o design lead que o cliente já rejeitou quando veio “template”. Tome partido. Arrisque **uma** ousadia justificável.

## Modelo de trabalho (antes do código)

Escreva três coisas:

1. **Tese visual** — uma frase: humor, material, energia (ex.: “mármore frio + tipografia lapidar + motion de cortina”).
2. **Plano de conteúdo** — hero → suporte → detalhe → CTA final (landing) **ou** workspace → nav → contexto (app).
3. **Tese de interação** — 2–3 ideias de motion que mudam o *feeling* da página.

Cada seção: **um** emprego, **uma** ideia visual dominante, **uma** takeaway/ação.

Depois feche o sistema curto:

- **Cor:** 4–6 hex nomeados + papel (fundo / texto / acento / perigo)
- **Tipo:** no máx. 2 famílias (display + body); utility só com motivo
- **Layout:** uma frase + ASCII do fold
- **Assinatura:** o único gesto que a página será lembrada

Critique: se trocar o nome do cliente e ainda parecer o SaaS genérico que você faria pra qualquer brief, a assinatura é fraca — refaça **só ela**.

**UI não-trivial:** mock estático → URL → **aprovação** → só então código real.

Planeje em silêncio; mostre quando tiver confiança de encantar.

## Defaults belos

- Comece por **composição**, não por componentes.
- Prefira hero full-bleed / âncora visual full-canvas.
- Nome da marca/produto = texto mais alto.
- Copy curta o bastante pra scan em segundos.
- Whitespace, alinhamento, escala, crop e contraste **antes** de chrome.
- Sistema magro: 2 typefaces no máx.; **um** accent por default.
- Default **sem cards**. Use seções, colunas, divisores, listas, blocos de mídia.
- First viewport = **pôster**, não documento.

### Anti-defaults de IA (eixo livre ≠ licença pra isso)

```text
❌ Cream #F4F1EA + serif + terracota
❌ Roxo → indigo gradient
❌ Dark + neon/glow + pill + sombra em camadas + emoji
❌ Broadsheet: hairline, radius 0, colunas de jornal
❌ Badge/chip/sticker flutuando no hero
❌ Grid de 3 cards (ícone · título · lorem) como first impression
❌ Bento genérico “pra parecer moderno”
```

Brief manda um desses looks → obedeça. Senão, não gaste liberdade aí.

## Ramos e stack

| Ramo | Postura | Stack |
|------|---------|--------|
| **Landing / marca / Awwwards** | Teatro controlado, emoção, poster | Astro + Tailwind + **GSAP**; Three só se o 3D **for** a assinatura |
| **Produto labs** | Densidade, DS, operação | SvelteKit + tokens/bits-ui/Travertino |
| **App interno** | Clareza operacional | DS existente; zero hero de marketing |

Misturar ramo (Three no consultório / cards de feature no hero de campanha) = recomeçar o plano.

## Landings

**Sequência default:** Hero (marca, promessa, CTA, 1 visual dominante) → Suporte (1 feature/prova concreta) → Detalhe (atmosfera, fluxo, profundidade) → CTA final.

**Hero**

- Uma composição só. Full-bleed de verdade: edge-to-edge, sem gutter herdado, sem max-width emoldurando o hero; constranja só a coluna interna de texto/ação.
- Ordem: marca → headline → body → CTA.
- Sem hero-cards, stat strips, logo clouds, pill soup, dashboards flutuantes.
- Headline ~2–3 linhas no desktop; um olhar no mobile.
- Coluna de texto estreita, ancorada numa zona calma da imagem.
- Texto sobre imagem: contraste forte + tap targets claros.
- Header sticky/fix **conta no orçamento do viewport**. `100vh`/`100svh` → subtraia o chrome (`calc(100svh - header)`) ou overlay — não empurre o hero pra fora do fold.

**Litmus do fold**

- Se o first viewport ainda “funciona” sem a imagem → imagem fraca.
- Se a marca some sem a nav → hierarquia fraca.
- Orçamento: marca + 1 headline + 1 frase + CTAs + 1 dominante. Stats, agenda, endereço, “essa semana” → fora.

## Apps / produto

Default: contenção tipo Linear — superfície calma, tipo+espaço fortes, poucas cores, denso porém legível, chrome mínimo. Card **só** quando o card é a interação.

Organize: workspace primário · navegação · contexto/inspector · um accent pra ação/estado.

**Superfícies (roubado do ofício macOS, vale em produto web também):**
- Hierarquia por **níveis de fundo**, não por borda grossa.
- Light e dark **desenhados separados** — nunca inverter a palette (dark precisa de mais diferenciação entre camadas; `#000` puro costuma ser preguiça).
- Accent só em ação/foco/seleção — nunca fill de região grande.
- Progressive disclosure: empty state limpo; esconda filtro/toolbar até existir dado.

```text
❌ Mosaico de cards; borda grossa em tudo; gradient decorativo em UI rotina;
   vários accents competindo; ícone ornamental; hero de marketing em dashboard;
   dark = light invertido
✅ Heading operacional ("KPIs selecionados", "Último sync"); superfície limpa;
   se o painel vira layout plano sem perder sentido, tire o card
```

Copy de produto = utilitária (orientação, status, ação). Se a frase poderia estar num anúncio, reescreva. Operador lendo só headings/labels/números precisa entender na hora.

App **macOS nativo / native-feel desktop** → skill `macos-design` (SwiftUI, traffic lights, vibrancy, DnD, atalhos).

## Imagery

Imagem faz trabalho narrativo — textura decorativa **não** é âncora.

- Marca, venue, editorial, lifestyle: pelo menos uma imagem forte, com cara de real.
- Prefira foto in-situ a gradient abstrato ou 3D fake.
- Crop com zona tonal estável pro texto.
- Sem letreiro/logo/tipografia embutida brigando com a UI.
- Não gere imagem com frames de UI, splits, cards ou panels dentro.
- Vários momentos → várias imagens, não colagem.

## Tipografia e estrutura

Tipo carrega personalidade. Display com caráter (contido); body complementar; escala com pesos/larguras/espaçamento intencionais. O tratamento tipográfico deve ser memorável — não veículo neutro.

Estrutura **é** informação. Eyebrow, número, divisor, label só se codificam verdade do conteúdo. `01 / 02 / 03` só se for sequência real (processo, timeline). Senão é enfeite.

```text
❌ Inter / Roboto / Arial / system-ui como face do projeto
❌ Display gritando em todo heading
✅ ≤2 famílias; display no momento herói; body quieto e legível
```

## Motion

Motion = presença e hierarquia, não ruído. Em trabalho visualmente liderado, **≥2–3** gestos:

1. entrada no hero  
2. scroll-linked / sticky / profundidade  
3. hover, reveal ou transição de layout que afia affordance  

**Preferir GSAP** (landing). Three quando o objeto 3D é a assinatura. Em produto: motion mínimo (estado, feedback). **Android (Material):** use o sistema M3 — não invente cubic solto.

### Tags M3 Expressive (usar de propósito)

Vocabulário canônico — vale pra Compose/`MotionScheme`, web (GSAP/`linear()` spring) e pra falar de motion sem enrolação:

| Tag | Significado |
|-----|-------------|
| **standard** | Scheme utilitário, contido — app/produto denso |
| **expressive** | Scheme com mais personalidade/overshoot — hero, destaque, marca |
| **spatial** | Move posição/tamanho/shape — **pode** overshoot |
| **effects** | Cor, opacity, blur — **sem** overshoot (alpha não “pula” de 1.0) |
| **fast / default / slow** | Velocidade do spring pela **distância/área** (switch → fast; sheet → default; fullscreen → slow) |
| **emphasized** | Família de easing M3 “com caráter” (enter/exit/on-screen) |
| **standard easing** | Família utilitária (enter/exit/on-screen) |
| **duration short→extra-long** | 50–1000ms em degraus; duração sobe com a área atravessada |

**Regra de escolha:** (1) scheme `standard` vs `expressive` pelo ramo/gesto · (2) `spatial` vs `effects` pela propriedade · (3) `fast/default/slow` pelo tamanho do movimento.

```text
Android / Compose
  MaterialTheme.motionScheme → standard() | expressive()
  defaultSpatialSpec · fastEffectsSpec · slowSpatialSpec …

Landing / GSAP
  spatial  → spring (stiffness/damping) ou ease com leve overshoot no transform
  effects  → fade/tint sem bounce (power2/power3, sem elastic em opacity)
  expressive no hero; standard em UI de produto embutida na page

macOS / produto denso
  micro-feedback rápido (fast effects); painéis = default spatial; sem elastic em tudo
```

Pares clássicos de **curva** (ainda úteis quando não for spring):

| Momento | Easing (ideia M3) |
|---------|-------------------|
| Entra na tela | emphasized/standard **decelerate** |
| Sai da tela | emphasized/standard **accelerate** |
| Mexe já on-screen | emphasized/standard (begin & end on screen) |
| Sem estilo | linear (quase nunca em UI expressiva) |

Regras: perceptível num recording rápido · suave no mobile · rápido e contido · consistente · corta se for só ornamento · respeita `prefers-reduced-motion`.

```text
❌ pulse/glow/blur eterno em CSS; parallax em tudo; carousel sem narrativa;
   elastic em opacity; um único ease pra tudo; duration igual pra chip e pra fullscreen
✅ spring spatial no transform; effects limpo no fade; expressive no gesto-assinatura;
   fast no toggle, slow na transição de tela; timeline GSAP com easing caro e coerente
```

Detalhe de tokens/springs: `references/motion-m3-expressive.md`.

## Copy (design material)

Palavra existe pra entender e usar — não pra decorar.

- Linguagem de produto, não comentário de designer.
- Headline carrega significado; suporte = uma frase curta.
- Corte repetição entre seções. Se deletar 30% melhora, continue deletando.
- Nunca jogue prompt/comentário de design na UI.
- Cada seção: explicar **ou** provar **ou** aprofundar **ou** converter.

```text
❌ "Submit" · "Configurar webhook" · "Oops, algo deu errado"
✅ "Salvar alterações" · "Notificações" · "Não deu pra salvar — tenta de novo"
```

Voz ativa, sentence case, mesmo verbo botão↔toast (`Publicar` → `Publicado`). Erro = causa + próximo passo. Empty = convite à ação. Sem desculpa teatral.

## Ponytail ∩ estética

Menor solução que **funciona e fica linda**. Nativo feio perde pra componente próprio mínimo alinhado à marca. Lib+wrapper+timezone debate pra um input também perde. Estética não autoriza over-engineering — é critério no degrau.

## Processo e contenção

1. Tese visual + plano de conteúdo + tese de interação + tokens.  
2. Crítica de unicidade.  
3. Mock → aprovação (não-trivial).  
4. Build fiel; CSS sem seletor cancelando seletor (`.section` vs `.cta` em padding/margin). Mobile real; foco de teclado visível.  
5. **Chanel:** tire um acessório. Ousadia num lugar; resto quieto. Screenshot se der.  
6. Anote o que já tentou — memória evita repetir o mesmo risco.

Maximalismo pede execução elaborada; minimalismo pede precisão. Elegância = executar a visão escolhida bem. Não arriscar também é risco.

## Hard rules

- Sem cards por default; sem hero-cards.
- Sem hero em coluna central / boxed quando o brief pede full-bleed.
- Uma ideia dominante por seção.
- Headline não ofusca a marca em página branded.
- Sem filler copy.
- Sem split-hero a menos que o texto sente num lado calmo e unificado.
- ≤2 typefaces sem motivo claro; ≤1 accent sem sistema do produto mandar o contrário.
- Ramo/stack certos (`AGENTS.md`). Sem React/Convex inventado.
- Sem misturar estética de landing com app denso (nem o inverso).

## Rejeite estes fracassos

- Grid SaaS genérico como first impression  
- Imagem linda com marca fraca  
- Headline forte sem ação clara  
- Imagery ocupada atrás de texto  
- Seções repetindo o mesmo mood statement  
- Carousel sem propósito narrativo  
- App = pilha de cards em vez de layout  
- First viewport que sobrevive sem a imagem ou sem a marca  

## Litmus finais

- Marca/produto inconfundível no first screen?  
- Uma âncora visual forte?  
- Dá pra entender só com headings?  
- Cada seção tem um emprego?  
- Cards são necessários de verdade?  
- Motion melhora hierarquia/atmosfera?  
- Ainda parece premium sem sombras decorativas?  
- Parece inevitável pra **este** sujeito — ou o default que você faria pra qualquer um?
