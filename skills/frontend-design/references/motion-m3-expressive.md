# Motion M3 Expressive — referência rápida

Fonte: [Applying easing and duration](https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration) · Material Components Android Motion · `MotionScheme` (Compose).

## Duas camadas

1. **Physics / springs** (Expressive moderno) — stiffness + damping; duração emerge da física.
2. **Curves** (easing + duration) — ainda válidas; pares enter/exit/on-screen.

Prefira springs pra UI espacial. Curves quando o host for CSS/GSAP sem física ou pra fades simples.

## MotionScheme

| Scheme | Uso |
|--------|-----|
| `standard()` | Produto, utilitário, Android app denso |
| `expressive()` | Destaque, hero, interações “com alma” |

Cada scheme expõe specs **spatial** e **effects** em **fast / default / slow**.

## Springs (6 slots)

Escolha velocidade pela **área/distância**, tipo pela **propriedade**:

| Slot | damping | stiffness | Quando |
|------|---------|-----------|--------|
| fast spatial | 0.9 | 1400 | switch, botão, chip (mexeu pouco) |
| fast effects | 1.0 | 3800 | cor/opacity no mesmo escopo |
| default spatial | 0.9 | 700 | sheet, drawer, painel parcial |
| default effects | 1.0 | 1600 | effects no mesmo escopo |
| slow spatial | 0.9 | 300 | fullscreen / grande travessia |
| slow effects | 1.0 | 800 | effects fullscreen |

**Spatial** pode overshoot. **Effects** (damping 1) não oscila — obrigatório pra alpha/cor.

Dois springs no mesmo gesto é normal: shape com spatial + tint com effects.

## Curves — easing

| Token | Curva (default) | Uso |
|-------|-----------------|-----|
| emphasized | path M3 | motion “com caráter”, begin/end on screen |
| emphasized decelerate | `cubic-bezier(0.05, 0.7, 0.1, 1)` | **entra** na tela |
| emphasized accelerate | `cubic-bezier(0.3, 0, 0.8, 0.15)` | **sai** da tela |
| standard | `cubic-bezier(0.2, 0, 0, 1)` | utilitário on-screen |
| standard decelerate | `cubic-bezier(0, 0, 0, 1)` | entra utilitário |
| standard accelerate | `cubic-bezier(0.3, 0, 1, 1)` | sai utilitário |
| linear | `cubic-bezier(0, 0, 1, 1)` | sem estilo |

## Curves — duration

Sobe com a área: short1…4 (50–200) · medium1…4 (250–400) · long1…4 (450–600) · extraLong1…4 (700–1000).

## Mapa rápido pra GSAP / web

| Intenção M3 | GSAP / CSS |
|-------------|------------|
| fast spatial | `duration: 0.15–0.25`, `ease: "power3.out"` ou spring stiff |
| default spatial | `0.3–0.45`, spring médio / `power3.inOut` |
| slow spatial | `0.5–0.8`, spring macio |
| effects (fade) | sem elastic; `power2.out` / opacity only |
| expressive hero | spring com leve overshoot só em transform/scale |
| enter | decelerate (out) |
| exit | accelerate (in) |

CSS moderno: `linear()` pode aproximar spring (tokens Expressive); senão GSAP `ease: "elastic"` com cuidado — **nunca** em opacity.

## Android / Kotlin

```kotlin
// theme
MaterialTheme(
  motionScheme = MotionScheme.expressive() // ou .standard()
) { … }

// uso
val spatial = MaterialTheme.motionScheme.defaultSpatialSpec
val effects = MaterialTheme.motionScheme.fastEffectsSpec
```

Mobile do Gui = Material Design nativo: **respeite MotionScheme**; não hardcode duration mágica por componente.

## Anti-padrões

- Um ease + 300ms pra tudo  
- Overshoot em opacity/color  
- Expressive scheme em tela operacional densa (cansa)  
- Standard scheme num hero Awwwards que pediu presença  
- CSS `animation: pulse infinite` como “motion design”
