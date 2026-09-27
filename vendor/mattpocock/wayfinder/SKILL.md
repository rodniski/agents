---
name: wayfinder
description: >-
  Use quando o usuário pedir mapa de projeto, wayfind, wayfinder, chartar
  épico/ideia grande, fog of war, frontier de decisões, ou trabalho grande
  demais pra uma sessão — planejar o caminho, não executar o destino.
disable-model-invocation: true
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Wayfinder — mapas de projeto

Ideia grande demais pra uma sessão, ainda na neblina. Wayfinder **acha o caminho** até o **destino** — não carrega o destino de uma vez.

O mapa vive no **issue tracker do repo** (GitHub via `gh`). Cada ticket é uma **decisão** (ou investigação que destrava decisão), não uma fatia de build. Uma sessão resolve **no máximo um** ticket (exceto `research` em paralelo no chart).

Invocação típica: `/wayfinder`, “mapa isso”, “charta esse épico”, “trabalha o mapa #N”.

## Plan, don’t do

Default = **planejar**. Ticket fechado = decisão registrada. A vontade de “já implementar” costuma significar: mapa pronto → handoff (outra skill / outra sessão).

Notas do mapa podem autorizar execução pontual (`task`). Sem isso: decisões, não deliverables.

Se o esforço tocar auth, cookie, PII, admin, upload → consulta `secure-by-design` nas Notes do mapa.

## Referir pelo nome

Sempre cite o ticket pelo **título** (com link). Nunca muro de `#42, #43`. Número/URL vão **dentro** do nome linkado.

## Duas modos

### A — Chartar o mapa (ideia solta)

1. **Nomear o destino** — skill `grilling`: 1–2 linhas do que “chegou” significa (spec, decisão travada, mudança in-place…). Destino fixa o escopo.
2. **Fronteira em largura** — outra rodada de `grilling`, breadth-first: decisões abertas e primeiros passos *agora*, sem afundar num fio só.
3. Se **não há neblina** (caminho cabe numa sessão) → pare e pergunte como seguir; não force mapa.
4. **Criar o mapa** (`wayfinder:map`) com Destination, Notes, Decisions vazio, Not yet specified, Out of scope.
5. **Criar tickets** especificáveis agora (filhos) → **segunda passada** pra wiring de bloqueio.
6. Disparar `research` em paralelo (subagente) se houver.
7. Pare. Chart não resolve grilling/prototype na mesma sessão.

### B — Trabalhar o mapa (URL/# do mapa; ticket opcional)

1. Carregar o **mapa** (visão low-res — não todos os bodies).
2. Ticket: o que o user nomeou, senão o primeiro da **frontier** (aberto, desbloqueado, sem assignee).
3. **Claim** primeiro: `gh issue edit N --add-assignee @me`.
4. Resolver conforme o tipo (abaixo). Zoom: buscar bodies relacionados sob demanda.
5. **Resolver:** comentário de resolução → fechar issue → append em Decisions so far no mapa.
6. Graduar neblina → tickets novos; se algo passou do destino → Out of scope (fechar + uma linha), não “resolver na rota”.

Nunca mais de um ticket HITL por sessão. Expect concorrência: outros claims no tracker.

## Corpo do mapa

```markdown
## Destination
<1–2 linhas: o que é “chegar”>

## Notes
<domínio; skills a consultar (ex. secure-by-design, frontend-design); preferências>

## Decisions so far
- [Título do ticket fechado](url) — gist de uma linha da resposta

## Not yet specified
<!-- neblina in-scope, ainda sem pergunta afiada -->

## Out of scope
<!-- além do destino; nunca gradua -->
```

Tickets abertos **não** listam no mapa — vivem como child issues / query.

## Ticket

```markdown
## Question
<decisão ou investigação que este ticket resolve — cabe em ~uma sessão>
```

Label: `wayfinder:research` | `wayfinder:prototype` | `wayfinder:grilling` | `wayfinder:task`.

### Tipos

| Tipo | HITL/AFK | O que é |
|------|----------|---------|
| **research** | AFK | Fato externo (docs, API, wiki). Subagente. |
| **prototype** | HITL | Artefato barato pra reagir (outline, stub UI). Linka asset. |
| **grilling** | HITL | Conversa — default. Agente **não** responde no lugar do humano. |
| **task** | HITL/AFK | Trabalho manual que **desbloqueia** decisão (acesso, signup, dump de shape). Não entrega o destino. |

**Fog ou ticket?** Dá pra **enunciar** a pergunta com precisão agora? → ticket (mesmo bloqueado). Ainda vago? → Not yet specified. Não pré-fatie neblina em tickets fantasmas.

## Grilling

Tickets `grilling` (e o chart do destino) usam a skill **`grilling`**: rodadas, frontier, recomendação, fatos via tool — agente não responde no lugar do humano. Carregue `grilling` antes da conversa HITL.

## GitHub (`gh`) — operações

Labels a garantir no repo (criar se faltar):
`wayfinder:map`, `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, `wayfinder:task`.

```bash
# mapa
gh issue create --label wayfinder:map --title "…" --body "$(cat <<'EOF'
…
EOF
)"

# ticket filho — preferir sub-issue GitHub; senão task list no mapa + "Part of #N" no topo do filho
gh issue create --label wayfinder:grilling --title "…" --body "$(cat <<'EOF'
Part of #<map>

## Question
…
EOF
)"

# claim
gh issue edit <n> --add-assignee @me

# resolver
gh issue comment <n> --body "$(cat <<'EOF'
## Resolution
…
EOF
)"
gh issue close <n>

# frontier aproximada: abertos com label wayfinder:* sem assignee; filtrar blocked_by / "Blocked by:" no body
gh issue list --state open --label wayfinder:grilling --json number,title,assignees,labels
```

**Blocking:** dependência nativa GitHub se disponível (`issue_dependencies` / UI). Senão linha no body:

```markdown
Blocked by: #12, #15
```

Desbloqueado = todos os blockers closed. Frontier = aberto + desbloqueado + unclaimed.

Detalhe de API sub-issues/deps: `references/github-ops.md`.

## Fallback local

Sem remote GitHub (ou user pedir): mapa em `docs/wayfinder/<slug>-map.md` + tickets `docs/wayfinder/<slug>/<ticket>.md`. Mesma estrutura de seções. Claim = linha `Claimed-by: <nome>` no ticket.

## ❌ / ✅

```text
❌ Implementar o épico enquanto “charta”
❌ 12 tickets inventados na neblina
❌ Resolver 4 grillings numa sessão
❌ Citar só #88 #89 #90
❌ Mapa pra trabalho que cabe num PR pequeno

✅ Destino nomeado → frontier real → um ticket por sessão
✅ Decisions so far = índice; detalhe no ticket
✅ Research AFK em paralelo no chart; HITL um a um
✅ Título linkado; out of scope explícito
```
