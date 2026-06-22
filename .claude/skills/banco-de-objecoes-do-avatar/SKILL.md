---
name: banco-de-objecoes-do-avatar
description: Mapeia todas as objeções que o ICP tem antes de contratar, comprar ou recomendar — organizadas por tipo (valor, tempo, confiança, relevância, urgência) e com respostas em formato de conteúdo para cada uma. Cria um banco que alimenta o /briefing-unity, o /carrossel-de-quebra-de-objecao e qualquer conteúdo de meio de funil. Dispara quando: "quais as objeções do meu avatar", "como responder objeções no conteúdo", "banco de objeções", "o que impede meu cliente de comprar".
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
Raiz real: o avatar não vê suficiente valor para justificar a escolha agora — ainda mede por preço de entrada, não por valor total (durabilidade, manutenção, conforto, resultado final).

### Tipo 2 — Produto / Percepção
"[ex.: produto parece de qualidade inferior à alternativa conhecida]", "meus clientes preferem o que já conhecem"
Raiz real: associação do produto com a versão popular de menor desempenho — não conhece a diferença entre a versão de entrada e a versão de alto desempenho.

### Tipo 3 — Confiança técnica
"[ex.: não sei se funciona nas condições do meu mercado]", "[ex.: dúvida sobre durabilidade a longo prazo]"
Raiz real: falta de prova técnica visível — laudos, certificações, casos documentados no contexto do cliente.

### Tipo 4 — Confiança em si mesmo
"Minha obra não é o perfil ideal", "meus clientes são conservadores"
Raiz real: o avatar acha que a solução é para outros perfis de obra/cliente — não vê o fit com seu contexto específico.

### Tipo 5 — Relevância
"[ex.: funciona para esse sistema/nicho mas não para o meu tipo de projeto]"
Raiz real: o conteúdo ou a oferta não está falando com o avatar no contexto exato onde ele atua.

### Tipo 6 — Urgência / Prioridade
"Vou ver isso no próximo projeto", "preciso primeiro fechar o projeto atual"
Raiz real: o avatar não sente que a dor dói o suficiente agora para mudar o padrão de especificação.

---

## Output

```
AVATAR: [arquiteto / construtor / proprietário]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANCO DE OBJEÇÕES:

TIPO 1 — VALOR / PREÇO
Objeção: "[como o avatar formula isso]"
Raiz real: [o que está por trás dessa objeção]
Resposta em conteúdo: [ângulo de carrossel/reel que aborda essa objeção]
Resposta em copy: [linha de argumento para legenda ou material técnico]

TIPO 2 — MATERIAL / PERCEPÇÃO
[mesma estrutura]

TIPO 3 — CONFIANÇA TÉCNICA
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

Skill recomendada para cada post: /carrossel-de-quebra-de-objecao ou /roteiro-unity
```
