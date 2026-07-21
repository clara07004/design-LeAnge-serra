---
name: carrossel-de-quebra-de-objecao
description: Cria a estrutura de um carrossel que nomeia e desmonta uma objeção específica do ICP — slide a slide, com o leitor no próprio ritmo. Diferente do /carrossel-leange (educativo/autoridade): este é focado em conversão e fundo de funil. Use após o /banco-de-objecoes-do-avatar para criar conteúdo para cada objeção mapeada. Dispara quando: "carrossel sobre [produto] vs [alternativa]", "como responder objeções em carrossel", "carrossel para quem está na dúvida", "conteúdo de fundo de funil".
---

# Carrossel de Quebra de Objeção

## Contexto

Antes de executar, ler:
- `_contexto/empresa.md` → objeções frequentes e contra-argumentos já mapeados
- `_contexto/preferencias.md` → restrições: comparativos com a concorrência sempre consultivos, nunca agressivos; sem promessas absolutas
- `marca/DESIGN.md` → identidade visual para o /carrossel-leange usar depois

**Fluxo recomendado:**
1. `/banco-de-objecoes-do-avatar` → mapeia todas as objeções
2. `/carrossel-de-quebra-de-objecao` → estrutura o carrossel para a objeção escolhida
3. `/carrossel-leange` → produz o carrossel visual com HTML + PNG

---

## O que essa skill faz

Cria a estrutura completa de um carrossel que ataca uma objeção específica — slide a slide, com profundidade suficiente para que o leitor, no próprio ritmo, seja levado da resistência à abertura.

O carrossel de quebra de objeção aproveita o que o vídeo não pode: o leitor controla o ritmo e pode reler os slides que mais o impactaram.

---

## Coleta de Informações

**Obrigatório:**
- `[A OBJEÇÃO]` — a resistência específica do avatar (ex: "pousada pet lover é mais cara", "meu pet vai estressar viajando", "prefiro deixar o pet em casa")
- `[AVATAR]` — persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)

**Opcional:**
- `[PROVA]` — caso real de cliente ou hóspede que tinha essa objeção
- `[O REFRAME]` — a perspectiva que desmonta a objeção
- `[CTA]` — a ação após o carrossel (padrão: consultar disponibilidade / falar com a pousada)
- `[NÚMERO DE SLIDES]` — padrão 8-10

---

## Os 3 Movimentos

**Movimento 1: Nomeação + Validação (Slides 1-3)**
Começa nomeando a objeção sem julgamento. Valida que ela faz sentido.
Quem se sente compreendido antes de ser convencido abre muito mais o ouvido.

**Movimento 2: O Reframe em camadas (Slides 4-7)**
Cada slide é uma camada do argumento:
- Por que a objeção existe (o diagnóstico)
- O que ela está protegendo (a raiz)
- O que muda quando você vê pelo outro ângulo (a virada)
- O que acontece quando você não age por causa dela (o custo)

**Movimento 3: Prova + Caso Concreto (Slides 8-9)**
- Quem tinha a mesma objeção
- O que pensava antes de decidir
- O que aconteceu depois que tomou a decisão

---

## Estrutura Slide a Slide

**Slide 1 — Cover: a objeção nomeada**
O título é a objeção do avatar — não uma pergunta retórica.
- "[A objeção exata como o avatar a formula]"
- Exemplo: "Pousada pet lover é mais cara. Faz sentido pensar assim."

**Slide 2 — Validação**
"Faz sentido pensar que [objeção]. Se eu estivesse escolhendo só por preço, pensaria o mesmo."

**Slide 3 — O diagnóstico**
Por que essa objeção existe — não como falha do avatar, mas como consequência do mercado.

**Slides 4-5 — O reframe**
- Objeção de preço → custo da diária vs. valor total (o que está incluído, a experiência completa, a tranquilidade de viajar com o pet)
- Objeção de percepção → hospedagem comum vs. a experiência pet lover de alto padrão
- Objeção de confiança → avaliações de hóspedes, depoimentos, fotos reais de pets, casos documentados
- Objeção de relevância → contexto específico da viagem do tutor e por que a pousada é a escolha mais coerente para ele e o pet

**Slide 6 — O custo da objeção não resolvida**
O que continua acontecendo enquanto o avatar não toma a decisão.
Não é ameaça — é clareza sobre o preço do status quo.

**Slides 7-8 — Prova com caso concreto**
Alguém que tinha a mesma objeção — com perfil, situação, a decisão que tomou e o resultado.

**Slide final — CTA com baixo atrito**
Não pressiona — convida o próximo passo natural.
"[ex.: Está planejando uma viagem com seu pet? Me chama para conversar.]" ou "Link na bio para falar com nossa equipe."

---

## Output

```
A OBJEÇÃO: "[como o avatar formula essa resistência]"
AVATAR: [persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ESTRUTURA DO CARROSSEL:

SLIDE 1 — COVER
Título: "[A objeção nomeada — ou a perspectiva que vai reframeá-la]"
Elemento visual: [texto em destaque + direção visual]

SLIDE 2 — VALIDAÇÃO
"[Por que faz sentido ter essa objeção — empatia antes de argumento]"

SLIDE 3 — O DIAGNÓSTICO
"[Por que essa objeção existe — a causa real]"

SLIDE 4 — O REFRAME (CAMADA 1)
"[A primeira mudança de perspectiva]"

SLIDE 5 — O REFRAME (CAMADA 2)
"[Aprofundamento do reframe — o argumento central com base real]"

SLIDE 6 — O CUSTO DA OBJEÇÃO
"[O que continua acontecendo enquanto a decisão não é tomada]"

SLIDE 7 — PROVA: QUEM TINHA A MESMA OBJEÇÃO
"[Apresentação do caso — perfil, situação, a objeção que tinha]"

SLIDE 8 — PROVA: O QUE ACONTECEU DEPOIS
"[Decisão que tomou e resultado concreto — com especificidade]"

SLIDE FINAL — CTA
"[Próximo passo natural — de baixo atrito, congruente com o argumento]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGENDA:
[Primeira linha: a objeção nomeada — filtra quem se identifica]
[Corpo: 2-3 frases que aprofundam o reframe sem revelar tudo]
[CTA: convite consultivo de baixo atrito]

PRÓXIMO PASSO:
Chamar /carrossel-leange com essa estrutura para produzir o visual.
```
