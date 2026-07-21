---
name: banco-de-objecoes-do-avatar
description: Mapeia todas as objeções que o ICP tem antes de contratar, comprar ou recomendar — organizadas por tipo (valor, tempo, confiança, relevância, urgência) e com respostas em formato de conteúdo para cada uma. Cria um banco que alimenta o /briefing-leange, o /carrossel-de-quebra-de-objecao e qualquer conteúdo de meio de funil. Dispara quando: "quais as objeções do meu avatar", "como responder objeções no conteúdo", "banco de objeções", "o que impede meu cliente de comprar".
---

# Banco de Objeções do Avatar

## Contexto

Antes de mapear, ler:
- `_contexto/empresa.md` → seção "Objeções frequentes e contra-argumentos" (ponto de partida) e seção ICP (avatares)
- `_contexto/estrategia.md` → gaps prioritários a resolver com conteúdo
- `_contexto/preferencias.md` → restrições de compliance (não prometer superioridade universal sem contexto)

**Avatares da empresa:** conforme seção ICP em `_contexto/empresa.md`.

Gerar o banco focado no avatar informado, ou criar seções separadas para cada perfil.

---

## Os 6 Tipos de Objeção

### Tipo 1 — Valor / Preço
"[ex.: é mais caro que a alternativa padrão]", "não sei se o custo justifica"
Raiz real: o avatar não vê suficiente valor para justificar a escolha agora — ainda mede por preço da diária, não por valor total (a experiência completa, o conforto do pet, a tranquilidade, o que está incluído).

### Tipo 2 — Experiência / Percepção
"[ex.: parece uma hospedagem comum com preço de pet lover]", "meu pet se vira em qualquer lugar"
Raiz real: associação da pousada pet lover com hospedagem comum de menor padrão — não conhece a diferença entre uma opção de entrada e a experiência de alto padrão.

### Tipo 3 — Confiança
"[ex.: não sei se meu pet vai se adaptar]", "[ex.: dúvida se a estrutura dá conta do meu pet]"
Raiz real: falta de prova social visível — avaliações de hóspedes, depoimentos, fotos reais de pets no contexto do tutor.

### Tipo 4 — Confiança em si mesmo
"Meu perfil de viagem não é o ideal", "meu pet é muito agitado"
Raiz real: o avatar acha que a solução é para outros perfis de tutor/pet — não vê o fit com seu contexto específico.

### Tipo 5 — Relevância
"[ex.: funciona para esse perfil/nicho mas não para o meu tipo de viagem]"
Raiz real: o conteúdo ou a oferta não está falando com o avatar no contexto exato onde ele atua.

### Tipo 6 — Urgência / Prioridade
"Vou ver isso na próxima viagem", "preciso primeiro resolver a viagem atual"
Raiz real: o avatar não sente que a dor dói o suficiente agora para mudar o hábito atual.

---

## Output

```
AVATAR: [persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANCO DE OBJEÇÕES:

TIPO 1 — VALOR / PREÇO
Objeção: "[como o avatar formula isso]"
Raiz real: [o que está por trás dessa objeção]
Resposta em conteúdo: [ângulo de carrossel/reel que aborda essa objeção]
Resposta em copy: [linha de argumento para legenda ou material da pousada]

TIPO 2 — EXPERIÊNCIA / PERCEPÇÃO
[mesma estrutura]

TIPO 3 — CONFIANÇA
[mesma estrutura]

TIPO 4 — CONFIANÇA EM SI MESMO
[mesma estrutura]

TIPO 5 — RELEVÂNCIA
[mesma estrutura]

TIPO 6 — URGÊNCIA / PRIORIDADE
[mesma estrutura]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OBJEÇÕES PRIORITÁRIAS (as que mais travam o avatar):
1. [Objeção mais crítica] — sinal: [como identificar que o avatar está nessa]
2. [Segunda mais crítica]
3. [Terceira]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PLANO DE CONTEÚDO PARA RESPONDER AS OBJEÇÕES:
(posts específicos para criar — um por objeção prioritária)
1. Objeção [X]: [título/ângulo de carrossel ou reel que responde sem soar defensivo]
2. Objeção [Y]: [...]
3. Objeção [Z]: [...]

Skill recomendada para cada post: /carrossel-de-quebra-de-objecao ou /roteiro-leange
```
