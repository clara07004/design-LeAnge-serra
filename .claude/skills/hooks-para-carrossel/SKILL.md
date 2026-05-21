---
name: hooks-para-carrossel
description: Cria o primeiro slide de carrosseis do Instagram — a combinação de headline e direção visual que força o swipe e maximiza salvamentos. Usado DENTRO do /carrossel-unity na Fase 1 para gerar 5 opções de capa antes de produzir os slides. Também pode ser chamado isoladamente para melhorar uma capa existente. Dispara quando: "preciso de uma capa para meu carrossel", "primeiro slide não tá bom", "como fazer capa que prende", "quero opções de primeiro slide".
---

# Hooks para Carrossel

## Contexto Ecoframe

Antes de gerar, ler:
- `_contexto/empresa.md` — ICP, posicionamento premium técnico, objeções frequentes
- `_contexto/preferencias.md` — tom técnico acessível, palavras proibidas

O "nicho" da Ecoframe é esquadrias em PVC de alta performance para construção a seco.
O "avatar" principal é: arquitetos/especificadores, construtores Steel Frame, proprietários de alto padrão.

---

## O que essa skill faz

Cria capas de carrossel que param o scroll e forçam o swipe — combinando headline de impacto com direção visual clara.

A capa tem dois trabalhos simultâneos:
1. Parar o scroll (competir com tudo que está no feed)
2. Prometer o que vem nos slides seguintes (criar razão para swipe)

---

## Coleta de Informações

**Obrigatório:**
- `[TEMA DO CARROSSEL]` — sobre o que é o conteúdo
- `[OBJETIVO]` — educar, vender, construir autoridade, gerar salvamentos

**Opcional:**
- `[AVATAR]` — qual dos três perfis (arquiteto / construtor / proprietário)
- `[TOM]` — mais direto, mais conversacional, mais provocador
- `[NÚMERO DE SLIDES]` — calibra a promessa da capa

---

## Anatomia do Primeiro Slide

**Headline** — a frase principal. Decide se a pessoa para de rolar.
- Máximo 8-10 palavras para leitura instantânea
- Deve funcionar como uma promessa ou uma tensão
- Evitar ponto final — ponto final fecha, o carrossel precisa abrir

**Subheadline (opcional)** — 1 linha de contexto ou especificação
- Máximo 15 palavras

**Indicador de carrossel** — sinalização visual de que tem mais conteúdo

---

## Os 7 Tipos de Capa que Funcionam

### 1. Promessa de resultado específico
O slide promete uma transformação concreta.
- "Como especificar esquadrias que eliminam reclamações pós-obra"
- "3 mudanças que elevam o conforto acústico sem aumentar o custo"

### 2. Dor nomeada com precisão
A capa nomeia exatamente o que o avatar sente.
- "Por que sua esquadria de alumínio não resolve o problema do ruído"
- "O motivo pelo qual obras de Steel Frame perdem em isolamento térmico"

### 3. Número + conteúdo acionável
Lista com número específico — cria expectativa de conteúdo completo.
- "5 erros que comprometem o desempenho termoacústico da obra"
- "3 critérios que arquitetos de alto padrão usam para especificar esquadrias"

### 4. Afirmação polêmica ou contraintuitiva
Vai contra o que a maioria acredita.
- "PVC não é uma alternativa ao alumínio. É uma categoria diferente."
- "A janela mais cara pode ser a mais cara de manter"

### 5. Pergunta de identificação
Uma pergunta que o avatar responde "sim" mentalmente.
- "Você especifica alumínio por desempenho ou por hábito?"
- "Seu cliente sabe o que está perdendo sem vedação de alto padrão?"

### 6. Antes/depois em uma linha
Mostra a transformação de forma compacta.
- "Antes: obra com ruído externo constante. Depois: isolamento acústico real."
- "De esquadria padrão para sistema de alto desempenho. O que muda →"

### 7. Dado surpreendente
Um número que recontextualiza o problema.
- "Uma esquadria mal vedada pode aumentar em 30% o gasto de ar-condicionado"
- "87% das infiltrações em Steel Frame têm origem nas esquadrias"

---

## Output

```
TEMA: [tema]
OBJETIVO: [objetivo]
AVATAR: [arquiteto / construtor / proprietário]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CAPA 1 — [Tipo]
HEADLINE: [texto]
SUBHEADLINE (opcional): [texto]
DIREÇÃO VISUAL: [fundo, elemento central, cor de destaque, indicador de swipe]
Por que funciona: [1 linha]

CAPA 2 — [Tipo]
[mesma estrutura]

[repetir para 5 capas]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMENDAÇÃO:
Capa [X] para o objetivo de [objetivo] porque [razão específica].
```
