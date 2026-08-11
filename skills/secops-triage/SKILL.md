---
name: secops-triage
description: >-
  Use quando o usuário pedir triagem de alerta de segurança, IOC, incidente,
  análise de log/JSON suspeito, playbook de resposta, contain, ou mapear MITRE.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# SecOps Triage

Triagem de alerta → impacto → playbook **proposto**. Não é cosplay de SOC: é resposta curta, ancorada em evidência, sem queimar produção nem vazar PII.

**Ambiente default (Gui / Med4U):** GCP + **GKE** (+ serviços Go no m4core). AWS/outro cloud só se o alerta/evidência for daquele provedor.

## Hard rules (antes de tudo)

- **Blast radius:** nunca execute contain destrutivo (delete, drain, firewall, revoke em massa, force-push, wipe) sem ordem explícita (“pode aplicar”). Até lá: **proponha** comandos.
- **PII / clínico:** nada de dado de paciente, token, cookie, JWT completo, secret, connection string no relatório. Redija (`user=***`, `ip=10.x.x.x` se sensível).
- **Sem inventar IOC.** Se não está no log/payload, marque como hipótese.
- **Repo AGENTS / policy do projeto vencem** esta skill em domínio de produto.
- Output em **pt-BR**. Comandos em code fence prontos pra copiar.

## Fluxo

1. **Parse** — extraia IOC e fatos: IPs, hashes, users, pods, SA, project, namespace, user-agent, paths, ARNs/IDs GCP.
2. **Contexto** — o que é o asset? (BFF, helix, auth, node pool, bucket, CI). Criticidade: público / PHI path / só interno.
3. **Impacto** — severidade = criticidade × explorabilidade × evidência (confirmado vs suspeito).
4. **MITRE** — mapeie tática/técnica (ID + nome). Uma primária; secundárias só se couber.
5. **Contain (proposto)** — menor ação que corta o sangramento. CLI do cloud certo (`gcloud`/`kubectl` default).
6. **Evidência + próximo passo** — o que preservar (logs, imagem, timeline); quem/o que escalar; rollback se aplicarem o contain.

## Severidade (régua rápida)

| Sev | Quando |
|-----|--------|
| **P1** | Exploração ativa em path com auth/PHI, RCE, credencial cloud comprometida |
| **P2** | Acesso indevido confirmado sem exploração ampla; secret exposto ainda válido |
| **P3** | Tentativa bloqueada / IOC sem impacto confirmado / misconfig sem exploit |
| **P4** | Ruído, falso positivo provável, hygiene |

Na dúvida entre dois níveis, suba **um** e diga o que confirmaria o downgrade.

## MITRE

Sempre cite `Txxxx` (+ subtécnica se clara). Exemplos frequentes no teu mundo:

- Credencial / token — *Valid Accounts*, *Steal Application Access Token*
- Lateral em cluster — *Container Administration Command*, *Deploy Container*
- Persistência K8s — *Account Manipulation*, CronJob/Workload suspeito
- Exfil — *Exfiltration Over Web Service*, bucket/egress anômalo
- Supply chain / CI — *Supply Chain Compromise*, *Compromise Software Supply Chain*

Não force matriz inteira. 1–3 técnicas bem ligadas à evidência.

## Contain — padrões (suco)

Sempre como **proposta**; adapte IDs reais do alerta.

**GKE / kubectl**

```bash
# isolar workload (exemplo)
kubectl -n <ns> cordon <node>           # só se node comprometido
kubectl -n <ns> delete pod <pod>        # recreata; combine com imagePin/deny
kubectl -n <ns> scale deploy/<app> --replicas=0   # contain agressivo
kubectl -n <ns> get sa,secret,netpol -o wide
```

**GCP**

```bash
# desativar chave / conter identidade (exemplo)
gcloud iam service-accounts keys list --iam-account=<sa>
gcloud iam service-accounts keys delete <KEY_ID> --iam-account=<sa>
# revisar audit
gcloud logging read 'severity="ERROR" OR protoPayload.authenticationInfo.principalEmail="<user>"' --limit=50 --format=json
```

**App / bff (m4core)**

- Revogar sessão/JWT via fluxo do auth-service (não inventar HS256).
- Cortar egress / negar SA do pod via NetworkPolicy — propor YAML, não aplicar sozinho.
- Secret no log → rotacionar + invalidar; nunca republicar o valor.

**GitHub / CI**

- Revogar PAT/Actions secret exposto; invalidar caches; auditar runs do workflow.

## Formato de saída (obrigatório)

```markdown
### Resumo do alerta
- Sev: P?
- Asset: …
- Evidência (fatos): …
- Hipóteses (se houver): …

### MITRE
- Primária: Txxxx — Nome
- Secundárias: …

### Contenção imediata (proposta)
\`\`\`bash
# só comandos — sem prosa dentro do fence
\`\`\`

### Não faça
- …

### Evidência / follow-up
- Preservar: …
- Confirmar: …
- Escalar se: …
```

Sem emoji obligatory. Sem inventário novelístico — igual skill de PR: problema → ação.

## ❌ / ✅

```text
❌ Rodar kubectl delete em prod porque o JSON “parecia ruim”
❌ Colar JWT/secret/PHI no resumo
❌ Playbook AWS genérico pra incidente GKE
❌ Dez técnicas MITRE de enfeite

✅ Sev + asset + IOC redigidos + 1–2 MITRE justificados
✅ Contain mínimo proposto; “posso aplicar?” se for destrutivo
✅ gcloud/kubectl alinhados ao alerta; rollback e evidência explícitos
```
