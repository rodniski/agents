# Wayfinder × GitHub — ops

Usar `gh` dentro do clone. Repo inferido do remote.

## Labels

```bash
for l in wayfinder:map wayfinder:research wayfinder:prototype wayfinder:grilling wayfinder:task; do
  gh label create "$l" --force 2>/dev/null || true
done
```

## Mapa

```bash
gh issue create --label wayfinder:map --title "<destino curto>" --body-file - <<'EOF'
## Destination
…

## Notes
…

## Decisions so far

## Not yet specified

## Out of scope
EOF
```

## Filho (task list fallback)

No mapa, sob uma seção opcional `## Tickets` (só se sub-issues não existirem):

```markdown
## Tickets
- [ ] #101
- [ ] #102
```

No filho, primeira linha: `Part of #MAP`.

## Sub-issues (quando a org/repo tiver)

Preferir a API de sub-issues do GitHub em vez de task list. Se `gh`/API falhar → fallback task list + `Part of`.

## Blocking nativo

`blocked_by` usa **database id** (`.id`), não o `#number`:

```bash
BLOCKER_ID=$(gh api "repos/{owner}/{repo}/issues/<blocker_number>" --jq .id)
gh api --method POST "repos/{owner}/{repo}/issues/<blocked_number>/dependencies/blocked_by" -f issue_id="$BLOCKER_ID"
```

Se a API de dependencies não existir no plano/repo → `Blocked by: #A, #B` no body do filho.

## Frontier

1. Listar children abertos do mapa (sub-issues ou task list).
2. Dropar com assignee.
3. Dropar com blocker aberto (`issue_dependencies_summary.blocked_by` ou issues abertos na linha `Blocked by:`).
4. Ordem = ordem do mapa / criação.

## Resolve → mapa

Depois de fechar o ticket, editar o mapa:

```bash
gh issue view <map> --json body --jq .body  # editar Decisions so far
gh issue edit <map> --body "…"
```

Append:

```markdown
- [<título>](https://github.com/<owner>/<repo>/issues/<n>) — <gist>
```

## Claim

```bash
gh issue edit <n> --add-assignee @me
```

Primeira escrita da sessão de work-through.
