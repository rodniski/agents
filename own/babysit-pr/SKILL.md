---
name: babysit-pr
description: >-
  Use quando o usuário pedir para monitorar, acompanhar, watch ou babysit um PR.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Babysit PR

Acompanhe um PR já aberto até ficar review-ready (ou até o pedido mandar parar/mergear).

## Loop

1. Identifique o PR (`gh pr view` / URL / branch atual).
2. Olhe **checks e comentários depois do último push**.
3. Valide cada apontamento de bot **no código** antes de agir.
4. Corrija erro real; descarte falso positivo com justificativa escrita no PR.
5. Separe quebra real de flaky de infra.
6. Sem novidade → **silêncio** (não spamme comentário).
7. Pare quando os bots de review estiverem **verdes no commit mais recente**.

## Merge

- Só se o pedido inicial mandou (ex.: “merge quando verde” ou “só reporta”).
- Sem instrução de merge: reporte o estado e pergunte.

## Hard rules

- Nunca atualize `git config`.
- Nunca force-push em `main`/`master`; avise se pedirem.
- Sem flags interativas (`-i`).
- Não abra PR novo daqui — pra criar/abrir use `creating-pull-requests`.
