# Agent kit pessoal

Fonte canônica. Cursor, Claude Code e Codex redirecionam pra cá.

**Repo:** https://github.com/rodniski/agents (private)

```
~/.agents/
  AGENTS.md          # preferências universais
  own/               # skills minhas
  vendor/<fonte>/    # skills terceiras (taste-skill, emilkowalski, mattpocock) ou direto (unslop)
  skills/            # gerado: symlinks planos pra own/ e vendor/ (harness não desce em subpasta)
  bin/ensure-redirects
  README.md
```

## Nova máquina

```bash
git clone git@github.com:rodniski/agents.git ~/.agents
# ou: gh repo clone rodniski/agents ~/.agents
~/.agents/bin/ensure-redirects
```

## Garantir carga em toda conversa

```bash
~/.agents/bin/ensure-redirects
```

| Tool | Como carrega |
|------|----------------|
| **Claude Code** | `~/.claude/CLAUDE.md` → `~/.agents/AGENTS.md` (symlink; user-level always-on) |
| **Codex** | `~/.codex/AGENTS.md` → `~/.agents/AGENTS.md` |
| **Cursor** | Sem `CURSOR.md` / `AGENTS.md` global. Usa `~/.cursor/rules/gui-agents.mdc` (`alwaysApply`) com `@~/.agents/AGENTS.md` — link, não cópia. |

## Redirects

| Path | → |
|------|---|
| `~/.cursor/skills` | `~/.agents/skills` |
| `~/.claude/skills` | `~/.agents/skills` |
| `~/.claude/CLAUDE.md` | `~/.agents/AGENTS.md` |
| `~/.codex/AGENTS.md` | `~/.agents/AGENTS.md` |
| `~/.cursor/rules/gui-agents.mdc` | `@` → `~/.agents/AGENTS.md` (alwaysApply) |

Cursor também lê `~/.agents/skills/` nativamente; o symlink em `~/.cursor/skills` cobre compatibilidade.

## Auto-uso (Claude + Cursor)

Skills **sem** `disable-model-invocation` = o modelo pode (e deve) invocar sozinho quando a `description` casar.

Garantias deste kit:

1. Symlinks: `~/.claude/skills` e `~/.cursor/skills` → `~/.agents/skills`
2. `~/.agents/AGENTS.md` (sempre on via Claude `CLAUDE.md` + Cursor rule) lista o catálogo e manda **ler o SKILL.md antes de agir**
3. `description` = só **QUANDO** (gatilhos em pt-BR)

Se uma skill “não pega”: reforça gatilhos na `description`, ou invoca `/nome-da-skill`. Não use `disable-model-invocation: true` nestas skills de ofício (só em workflows destrutivos tipo deploy).

Depois de editar `AGENTS.md`: `~/.agents/bin/ensure-redirects`


### Header (obrigatório)

```yaml
---
name: babysit-pr
description: >-
  Use quando o usuário pedir para monitorar, acompanhar, watch ou babysit um PR.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---
```

| Campo | Regra |
|-------|--------|
| `name` | kebab-case |
| `description` | Só **QUANDO** usar (gatilhos). Não explique o que a skill “é”. |
| `metadata.harness` | Sempre incluir `claude`, `cursor`, `codex` (os que aplicam) |
| `metadata.platform` | `darwin`, `linux` conforme suporte |
| ~~`scope`~~ | **Não usar** |

Corpo: passos + exemplos ❌/✅. Sem prosa.

## Repo vs home

m4core (e outros) mantêm o próprio `AGENTS.md` / `.agents/skills/m4core-*`. Não misturar domínio de produto aqui. Em conflito: **repo/product vence** preferência pessoal.

## Backup do wipe

`~/.agent-home-backup-2026-08-11/`
