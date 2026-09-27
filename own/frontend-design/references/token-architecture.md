# Arquitetura de tokens — filosofia portável

Como amarrar cor/tipo/elevação sem inventar sistema novo a cada tela. Dialeto muda; contrato de papéis não.

## Regra de ouro

**Retonalize valores. Não invente tokens de cor novos.**

Se o host já tem contrato canônico (shadcn, M3, Apple semantic colors): mude `--background`, `--primary`, `--muted`… Não crie `--surface-*`, `--info`, `--warning` “porque faltou nome”. Token novo de cor força reescrever componentes — exatamente o que a arquitetura evita.

Projeto greenfield sem DS: defina **poucos** tokens com os papéis abaixo e pare.

## Papéis (contrato)

| Papel | Exemplos de binding | Faz |
|-------|---------------------|-----|
| `background` | `--background` | Campo base |
| `surface` | `--card`, `--popover`, `--secondary` | Planos elevados / ilhas |
| `muted` | `--muted`, `--muted-foreground` | Recuo quente — não cinza morto sem decisão |
| `action` | `--primary` | CTA, foco, seleção |
| `accent` | `--accent` | Realce que equilibra a ação |
| `rare` | chart reservado / botão único | Gesto deliberado — não UI corrente |
| `border` | `--border` | Divisor real apenas |
| `elevation` | `--elevation-island`, shadow tokens | Profundidade sem filete |

Light e dark: **dois desenhos**, mesmos papéis, valores distintos.

## Dialeto vs vocabulário fechado

```text
Filosofia (esta ref)     → papéis, elevação por tom, retonalizar, contenção
Dialeto do projeto       → metáfora + hex/oklch concretos deste produto
Vocabulário fechado      → só onde o DS do repo manda
```

**labs / m4doc (m4core):** dialeto Travertino & Patina — bronze / verdigris / ouro / Fraunces·Outfit·Kode. Fonte: skill `m4core-labs-ui-travertino` + wiki do repo. Zero hex literal em `.svelte`.

**Outro projeto:** escolha outra metáfora (ardósia+latão, papel+tinta, concreto+cobre…). Preencha os **mesmos papéis**. Não copie bronze/verdigris por nostalgia.

## Tipo (papéis, não faces)

| Papel | Uso |
|-------|-----|
| Display / heading | Título, momento herói |
| Body / sans | Leitura corrida, UI |
| Mono / data | Código, IDs, números tabulares |

≤2 famílias sem motivo forte. Faces concretas = dialeto (Fraunces no labs; noutra marca, outras).

## Elevação

- Preferir tom (`surface` > `background`) a borda.
- Sombra: blur largo, spread negativo ou equivalente — não `0 1px 2px` que vira filete.
- Input “afundado” = `background` dentro de `surface`, não caixa com stroke.

## Checklist ao abrir um projeto

1. Existe DS/tokens? → retonalizar; ler skill/wiki do repo se houver.
2. Não existe? → definir papéis da tabela + metáfora numa frase.
3. Anotar o dialeto (material + ação + realce + raro) antes de codar UI.
4. Recusar hex/oklch solto em componente se o projeto já tem tokens.
5. Em m4core labs/m4doc → Travertino vence qualquer default desta skill.

## Anti-padrões

```text
❌ --surface-1/2/3 inventados em cima do shadcn
❌ muted = cinza frio “neutro” sem metáfora
❌ ouro/accent raro usado em texto corrido
❌ copiar bronze/verdigris pra projeto que não é labs
❌ dark = light invertido
✅ mesmos papéis · valores novos · metáfora explícita · repo DS vence
```
