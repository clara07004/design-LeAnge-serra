---
name: hooks-para-carrossel
description: Cria o primeiro slide de carrosseis do Instagram — a combinação de headline e direção visual que força o swipe e maximiza salvamentos. Usado DENTRO do /carrossel-leange na Fase 1 para gerar 5 opções de capa antes de produzir os slides. Também pode ser chamado isoladamente para melhorar uma capa existente. Dispara quando: "preciso de uma capa para meu carrossel", "primeiro slide não tá bom", "como fazer capa que prende", "quero opções de primeiro slide".
---

# Hooks para Carrossel

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — ICP, posicionamento e objeções frequentes
- `_contexto/preferencias.md` — tom de voz e palavras proibidas

O "nicho" e o "avatar" são definidos em `_contexto/empresa.md`.

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
- `[AVATAR]` — a persona da LeAnge (persona **única**: tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)
- `[TOM]` — mais direto, mais conversacional, mais provocador
- `[NÚMERO DE SLIDES]` — calibra a promessa da capa

---

## Anatomia do Primeiro Slide

**Headline** — a frase principal. Decide se a pessoa para de rolar.
- Máximo 8-10 palavras para leitura instantânea
- Deve funcionar como uma promessa ou uma tensão
- Evitar ponto final — ponto final fecha, o carrossel precisa abrir

**Subheadline (opcional)** — 1 linha de contexto ou detalhe
- Máximo 15 palavras

**Indicador de carrossel** — sinalização visual de que tem mais conteúdo

---

## Os 7 Tipos de Capa que Funcionam

### 1. Promessa de resultado específico
O slide promete uma transformação concreta.
- "Como planejar a primeira viagem com seu cão sem estresse"
- "3 detalhes que transformam uma hospedagem comum em experiência pet lover"

### 2. Dor nomeada com precisão
A capa nomeia exatamente o que o avatar sente.
- "Por que 'aceita pet' não é a mesma coisa que 'feito para o seu pet'"
- "O motivo pelo qual seu cão fica ansioso quando você viaja sem ele"

### 3. Número + conteúdo acionável
Lista com número específico — cria expectativa de conteúdo completo.
- "5 coisas para checar antes de escolher uma pousada pet friendly"
- "3 critérios que separam uma pousada pet friendly de uma pet lover"

### 4. Afirmação polêmica ou contraintuitiva
Vai contra o que a maioria acredita.
- "Pet friendly não é o mesmo que pet lover. É outra categoria."
- "Deixar o pet solto não é bagunça — é liberdade com segurança"

### 5. Pergunta de identificação
Uma pergunta que o avatar responde "sim" mentalmente.
- "Você viaja e deixa seu pet, ou viaja com ele?"
- "Seu cão pode entrar no restaurante e na piscina onde você se hospeda?"

### 6. Antes/depois em uma linha
Mostra a transformação de forma compacta.
- "Antes: pet preso no quarto. Depois: solto no restaurante, na piscina e nas cachoeiras."
- "De 'aceita pet com restrições' para 'sem limite de porte, raça ou quantidade'. O que muda →"

### 7. Dado surpreendente
Um número que recontextualiza o problema.
- "Somos a única pousada onde o pet frequenta todos os espaços — sem exceção"
- "Sem limite de porte, raça ou quantidade: o conceito que nos torna únicos"

---

## Output

```
TEMA: [tema]
OBJETIVO: [objetivo]
AVATAR: [persona LeAnge — ver `_contexto/persona.md`]

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
