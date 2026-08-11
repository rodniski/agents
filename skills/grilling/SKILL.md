---
name: grilling
description: >-
  Use quando o usuário pedir para grelhar, grilling, stress-test de ideia/plano,
  entrevistar a decisão, ou quiser fechar entendimento antes de agir — sem
  implementar ainda.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Grilling

Entrevista o humano até haver **entendimento compartilhado**. Árvore de design: cada decisão ramifica nas que dependem dela.

Só **decisões** vão pro user. **Fatos** (filesystem, docs, API, código) você busca — ou manda subagente. Não pergunte o que dá pra olhar.

Não implemente, não abra PR, não “já codifica” até o user confirmar que a árvore fechou. Mapa de épico grande → skill `wayfinder` (que usa grilling nos tickets HITL).

## Rodadas + frontier

**Frontier** = perguntas cujos pré-requisitos **já** estão fechados — dá pra perguntar *agora* sem chutar resposta pendente.

Numa rodada:

1. Liste **toda** a frontier (não um fio só).
2. Numere cada pergunta + dê sua **recomendação**.
3. Espere as respostas.
4. Recalcule a frontier e vá à próxima rodada.

Pergunta que depende de outra ainda aberta **nesta** rodada → fica pra rodada seguinte.

Subagente buscando fato = pré-requisito em aberto só pros ramos que dependem dele; o resto da frontier você pergunta agora.

## Formato

```text
❓ **Q1** - **<título>**: <corpo; opções se couber>

➡️ <sua recomendação>
```

pt-BR. Direto. Sem preâmbulo de “ótimas perguntas”.

## Fim

Frontier vazia = todo ramo visitado, nada assumido em silêncio. Declare o entendimento em 3–6 linhas e **pare**. Só age depois do “fechou / pode seguir”.

## ❌ / ✅

```text
❌ Uma pergunta por vez sem mapa; perguntar fato que o repo responde;
   responder no lugar do user; já sair implementando

✅ Rodada com frontier inteira + recomendação; fatos via tool/subagente;
   decisões com o humano; stop até confirmar
```
