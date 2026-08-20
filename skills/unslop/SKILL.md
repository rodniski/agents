---
name: unslop
description: >-
  Use quando o usuário pedir unslop, tirar slop, remover cara de IA, reescrever
  texto mais humano, limpar copy/README/changelog/docs/PR de patterns de LLM,
  ou disser que o texto “parece ChatGPT”.
metadata:
  harness: [claude, cursor, codex]
  platform: [darwin, linux]
---

# Unslop

Reescreve prosa pra soar humana. Preserva significado e tom pedido. Não inventa fatos.

Não use pra código, diffs ou contratos técnicos densos — só pra texto que o humano vai ler como escrita (copy, docs, changelog, PR body, email, post).

## Processo

1. Escaneia os patterns abaixo.
2. Reescreve. Mesmo significado, tom certo.
3. Coloca voz (ver Soul).
4. Self-audit: “O que ainda grita IA?” Corrige o que restar.
5. Entrega o texto limpo. Sem metacommentário tipo “aqui está a versão unslop”.

## Soul

Cortar pattern é metade. Texto estéril também denuncia máquina.

- Opine quando o gênero pedir. Reaja ao fato; não faça lista neutra de prós/contras.
- Varie ritmo. Frase curta. Depois uma mais longa que respira.
- Admita nuance. “Impressionante e meio inquietante” > “impressionante”.
- Use “eu” se couber. Não é amadorismo.
- Deixa um pouco de irregularidade. Estrutura perfeita demais parece template.
- Seja específico. Não “isso é preocupante” — “tem algo estranho em agentes rodando sozinhos às 3h”.

Docs técnicas e respostas de agente: priorize concreto e curto. Soul sem floreio.

## Patterns

### Conteúdo

| ❌ | ✅ |
|----|----|
| Puffery (“pivotal”, “testament to”, “evolving landscape”, “indelible mark”) | O que aconteceu, em fato |
| Name-drop de outlets sem contexto | Um outlet + o que disse |
| “-ing” decorativo (highlighting, ensuring, showcasing, fostering) | Apaga ou troca por causa/efeito real |
| Promo (“nestled”, “vibrant”, “breathtaking”, “groundbreaking”, “stunning”) | Descrição neutra |
| Atribuição vaga (“experts believe”, “industry reports suggest”) | Nomeia a fonte ou corta |
| “Despite challenges… continues to thrive” | Fato específico |

### Linguagem

| ❌ | ✅ |
|----|----|
| Vocabulário IA: additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstrato), pivotal, showcase, tapestry, testament, underscore, vibrant | Palavra comum |
| “serves as”, “stands as”, “boasts”, “features” | “é” / “tem” |
| “Not just X, but Y” | O ponto direto |
| Forçar trinca (rule of three) | O número natural de ideias |
| Ciclagem de sinônimo no mesmo parágrafo | Um termo, repete |
| False range (“from X to Y” sem escala) | Lista os tópicos |

### Estilo

| ❌ | ✅ |
|----|----|
| Em dash em todo canto | Ponto ou vírgula. Não trocar por parêntese/en dash como muleta |
| Dois-pontos no meio da frase como “conector dramático” | Só antes de lista/exemplo; senão reescreve |
| Bold em todo nome próprio/acrônimo | Bold raro, só âncora real |
| “**Label:** Label restated…” | Prosa; ou `**Nome.**` + detalhe novo |
| Title Case Em Heading | Sentence case |
| Emoji decorativo em heading/bullet | Sem emoji ornamental |
| Curly quotes | Straight quotes (`"` `'`) |

### Artefatos de chatbot

| ❌ | ✅ |
|----|----|
| “I hope this helps!”, “Let me know if…”, “Of course!”, “Certainly!”, “Found the smoking gun!” | Vai direto ao texto/pedido |
| “While specific details are limited…” | Acha fonte ou corta |
| “Great question! You’re absolutely right!” | Responde |

### Filler e jargão

| ❌ | ✅ |
|----|----|
| “In order to”, “due to the fact that”, “it is important to note that” | “To” / “because” / apaga |
| Hedge em cascata (“could potentially possibly…”) | “may” / afirmação |
| Fecho genérico (“the future looks bright”) | Plano ou fato |
| Metáfora abstrata: substrate, wedge, vector, locus, vantage, nexus, primitive (substantivo), harness/surface/bedrock/scaffolding (metáfora), modality, paradigm, gold-plating, ratchet, evacuate (código), endgame, north star, flywheel | Palavra concreta (“base”, “add”, “way”, “move out”…) |

### Fala clara

- Diz o mecanismo ou o número, não o feeling. “SQL you can read” → o que o reader faz/sabe (ex.: “`.toSQL()` devolve a string enviada ao banco”).
- Se a frase caberia igual em outro projeto, não diz nada deste — corta.
- Frase densa demais: parte em duas. Uma ideia por frase.
- Voz ativa. Nomeia o ator. Passiva só se o ator não importa.
- Advérbio fraco → verbo forte ou métrica.
- Preferir a palavra simples: utilize→use, leverage→use, facilitate→help, numerous→many, in the event that→if.

Checklist expandido: [references/patterns.md](references/patterns.md)
