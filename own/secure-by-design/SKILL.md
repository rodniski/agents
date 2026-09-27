---
name: secure-by-design
description: >-
  Use quando o usuário for criar/alterar feature, auth, API, upload, cookies,
  webhooks, admin, dados clínicos/PII, ou pedir pra nascer seguro / threat model
  / review de segurança antes do ship — não pra triagem de incidente já ocorrido
  (aí é secops-triage).
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Secure by Design

Segurança **antes** do ship. Enquanto desenha e implementa: trust boundaries, menor privilégio, fail-closed. Incidente já rolando → skill `secops-triage`.

**Contexto Gui / Med4U:** web (SvelteKit/Connect), BFF Go, domínio gRPC, mobile nativo, dados clínicos. Segredo e PHI **nunca** no client nem no git.

## Quando acionar (checklist mental)

Puxe esta skill se a mudança toca em **qualquer** item:

- Auth, sessão, cookie, JWT, refresh, logout  
- Nova rota/RPC pública ou com scope novo  
- Upload, download, export, link assinado  
- Admin, impersonation, bypass, feature flag perigosa  
- Webhook, fila, worker com side-effect  
- PII / clínico / audit log  
- CORS, CSP, iframe, postMessage  
- Secrets, CI, terraform, IAM, NetworkPolicy  

## Método (curto)

1. **Trust boundary** — quem é o caller? browser, mobile, outro serviço, admin? O que **não** se confia nele?
2. **Assets** — o que protege (token, PHI, ação destrutiva, money/ops)?
3. **Abuse cases** — 3–5 jeitos de quebrar (IDOR, replay, escalate scope, path traversal, SSRF, mass assign).
4. **Controles** — o que o desenho já tem vs o que falta **neste PR**.
5. **Fail-closed** — sem auth/config → nega / não sobe; nunca “abre pra funcionar”.
6. Só então implementa. Review final: os abuse cases ainda fecham?

## Padrões do teu stack (suco)

### Borda (BFF / Connect)

- Auth na borda; **zero domínio** no BFF, mas **100% de gate** (JWT + scope).
- Cookie httpOnly no web; mobile Bearer. Sem token no `localStorage` se o modelo for BFF-dono-do-cookie.
- RS256/JWKS — sem HS256 simétrico na borda.
- Scope por serviço/RPC; privilégio extra **no handler**, não “ADM libera tudo” sem querer.
- Erro pro client: genérico (`Unavailable` / 401 / 403). Detalhe só no log **sem PII**.
- CORS: origin explícita + credentials; nunca `*` com cookie.

### Domínio / gRPC interno

- Metadata de serviço (`*-service-token` + user-id de máquina). Caller externo não chega aqui.
- Validar input de novo na borda do domínio (BFF pode bugar).
- Sem falar com Tasy/Oracle direto do front/BFF — só helix/plataforma.

### Web (SvelteKit)

- XSS: sem `{@html` com dado de usuário; escape default.
- CSRF: cookie SameSite + fluxo Connect; cuidado com `None` sem Secure.
- Upload: type/size allowlist; não servir user content como HTML executável.
- Secrets só server-side / env; nunca `PUBLIC_*` com chave privada.
- Links de download GED/assinados: expiry curto + authz no resource ID (IDOR clássico).

### Mobile

- Token no Keychain/Keystore, não em log.
- Certificate pinning só se o time já tiver ops pra rotacionar — senão não invente.
- Mesmos scopes do proto; UI esconder ≠ authz.

### Dados / log

- Audit: quem/quando/quê (ID), não payload clínico completo.
- Log: `request_id`, nunca password/token/`cd_medico` em stack de erro se policy proíbe.

### Infra (quando a feature exige)

- SA de workload com menor privilégio; NetworkPolicy default deny onde o repo já usa.
- Secret no Secret Manager / Infisical — não no repo, não no PR.

## Threat model mínimo (colar no PR se a feature for sensível)

```markdown
### Threat model (mínimo)
- Boundary: …
- Assets: …
- Abuse cases: …
- Controles neste PR: …
- Residual / follow-up: …
```

## ❌ / ✅

```text
❌ “Auth no front resolve”; secret em VITE_/PUBLIC_; CORS *;
   confiar só no BFF sem validar no domínio; logar JWT; scope aberto “depois aperta”

✅ Gate na borda + validate no domínio; cookie/JWKS certos; allowlist;
   fail-closed; abuse cases listados; PII fora do client e do log
```

## Relação com outras skills

| Momento | Skill |
|---------|--------|
| Construindo feature sensível | **secure-by-design** (esta) |
| Alerta/incidente já aconteceu | `secops-triage` |
| UI/landing | `frontend-design` (estética) + esta se houver auth/dado |
| PR | `creating-pull-requests` — linkar o threat model mínimo se P1/P2 de risco |
