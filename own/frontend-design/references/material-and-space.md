# Material e espaço — filosofia portável

Taste estrutural do Gui. Vale em **todo** projeto. Cor/metáfora mudam; esta camada não.

## Tese

Interface é **matéria organizada no espaço**, não chrome empilhado. Luz, tom e silêncio carregam hierarquia. Avançado sem forma não tem valor; forma sem clareza também falha.

Metáfora do projeto (mármore, ardósia, papel, tinta…) = dialeto. A estrutura abaixo = língua.

## Espaço

- Elevação por **tom** e sombra intencional — não por filete/borda decorativa.
- **Ilhas, não cards.** Superfície sobe porque é mais clara (ou mais diferenciada no dark), não porque ganhou box.
- Borda só como **divisor real** (separar regiões), nunca como moldura de status.
- Silêncio é hierarquia: whitespace, alinhamento e escala **antes** de ícone/badge/glow.
- Um nível de elevação a mais só quando o conteúdo precisa de plano próprio.
- Dark e light **desenhados separados** — nunca inverter a palette. Dark pede mais distância entre camadas.

```text
❌ Card com border+shadow em tudo · mosaico de caixas · filete 1px fingindo profundidade
✅ Planos por tom · sombra larga/suave só quando a ilha precisa · layout plano se ainda legível
```

## Material

Todo projeto escolhe **um material dominante** + **pátina/metais com papel**:

| Papel | Função | Regra |
|-------|--------|-------|
| Pedra / fundo | Campo onde a UI vive | Croma baixo; nunca “cinza SaaS” sem decisão |
| Superfície | Ilha / painel / popover | Tom acima do fundo; sem borda de status |
| Ação | CTA, foco, seleção | Um metal/cor dominante |
| Realce | Estado frio / contraste da ação | Equilibra a ação; não compete |
| Gesto raro | Pico deliberado (entrar, celebrar) | Nunca cor corrente de UI |

Nomes concretos (bronze, verdigris, ouro…) pertencem ao **dialeto do produto** — não a esta filosofia. Em labs/m4doc o dialeto é Travertino; noutro repo invente outro material **em cima desta tabela**.

## Contenção (Chanel)

- Uma ousadia por composição; resto quieto.
- Um accent dominante. Segundo accent só com sistema do produto mandando.
- Se deletar um acessório e melhorar: delete.
- Landing = teatro controlado. App = densidade e fidelidade ao DS. Não misturar.

## Litmus de espaço

- Sem as bordas, a hierarquia ainda se lê?
- O first viewport sobrevive sem chrome ornamental?
- Cada superfície justifica o plano extra?
- O material escolhido aparece na UI — ou só no moodboard?
