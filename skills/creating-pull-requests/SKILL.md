---
name: creating-pull-requests
description: >-
  Use quando o usuário pedir para criar/abrir PR, publicar branch pra review
  ou file pull request.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Criar Pull Requests

Use `gh` pra tudo que for GitHub. Não invente URL de PR sem ter criado.
Pra monitorar/babysit depois de aberto: skill `babysit-pr`.

## Antes de abrir

1. **Já existe PR pra esta branch?** `gh pr view` / `gh pr list --head $(git branch --show-current)`. Se existir, atualize e devolva a URL — não abra outro.
2. **Diff local vs base** (`origin/main` ou a default do repo): o conteúdo bate com o que o usuário pediu? Se não, pare e alinhe antes de publicar.
3. Rebase na `main` mais recente antes de abrir. Branch velha = conflito e review desperdiçada.
4. Abra **PR real**, não draft — draft não ganha cobertura do bot de review.

## Contexto (paralelo)

Rode junto:

1. `git status`
2. `git diff` (+ `git diff <base>...HEAD`)
3. Tracking remoto — precisa de `git push -u`?
4. `git log <base>..HEAD` — **todos** os commits da branch, não só o tip

## Título

Títulos costumam virar mensagem de merge. Siga a convenção do repo (olhe PRs merged recentes / `git log`).

**Regra:** curto, legível por humano, explica **por que importa** — não o mecanismo interno.

```text
❌ perf(server): negociar permessage-deflate no websocket
✅ perf(server): cortar tamanho de frame websocket em 70%+ com gzip
```

Conventional commits onde o projeto usa (`fix(web): …`, `feat(api): …`).

## Descrição

Comece pelo **problema** (a partir do pedido original do usuário), depois a **solução** em uma frase. **Não** abra com inventário de implementação.

```text
❌ Removido o carry-over implícito de workspace em todo entry point de
   "new thread" (cmd+n / cmd+shift+o, botões sidebar v1/v2, command palette).
   Threads novas herdam só o projeto do contexto; branch, worktree e env
   mode sempre vêm dos defaults. Apaguei buildContextualThreadOptions,
   startNewThreadInProjectFromContext e a maquinaria de seed-context da
   sidebar v1.

✅ O default de "new worktree" era ignorado ao abrir threads em worktrees
   existentes. Super anti-intuitivo. Agora as preferências valem sempre.
```

Corpo mínimo:

```bash
gh pr create --title "…" --body "$(cat <<'EOF'
<problema em 1–2 frases>

<como resolveu em 1–2 frases>

## Test plan
- [ ] …

---
Modelo/ambiente: <modelo> · <local|cloud>
EOF
)"
```

A nota de modelo/ambiente no final é obrigatória.

## Publicar (sequencial)

1. Branch nova só se precisar.
2. `git push -u origin HEAD` se a branch não estiver no remote (ou estiver atrás do tip).
3. `gh pr create` com título/corpo acima.
4. Devolva a **URL** do PR.

## Hard rules

- Nunca atualize `git config`.
- Nunca force-push em `main`/`master`; avise se pedirem.
- Sem flags interativas (`-i`).
- Não faça push “por hábito” fora do fluxo de PR (a menos que o usuário peça).
