# Manual de Uso — CCOS (Claude Code OS)

Documentação completa do sistema de produção de conteúdo.

---

## Por onde começar

| Situação | Vá para |
|---|---|
| Nunca usei esse sistema antes | [00 — Visão Geral](00-visao-geral.md) |
| Quero entender o que cada arquivo faz | [01 — Estrutura do Repositório](01-estrutura-do-repositorio.md) |
| Preciso configurar as credenciais e o contexto | [02 — Configuração Inicial](02-configuracao-inicial.md) |
| Quero produzir conteúdo agora | [03 — Fluxo Completo](03-fluxo-completo.md) |
| Quero saber o que cada skill faz (referência técnica) | [04 — Referência de Skills](04-referencia-de-skills.md) |
| Quero saber como e quando usar cada skill + sequências | [06 — Guia de Skills](06-guia-de-skills.md) |
| Encontrei um erro | [05 — Resolução de Problemas](05-resolucao-de-problemas.md) |

---

## Os 6 arquivos do manual

### [00 — Visão Geral](00-visao-geral.md)
O que é o CCOS, como o sistema funciona, a diferença entre skills e motores, por que existem checkpoints de aprovação, o que o sistema produz e quais os pré-requisitos.

### [01 — Estrutura do Repositório](01-estrutura-do-repositorio.md)
Cada pasta, arquivo e skill explicados individualmente. Inclui o mapa completo de arquivos e a função de cada um.

### [02 — Configuração Inicial](02-configuracao-inicial.md)
Passo a passo completo para deixar o sistema pronto: instalação de dependências, configuração de credenciais de API, preenchimento dos arquivos de contexto e checklist de verificação.

### [03 — Fluxo Completo](03-fluxo-completo.md)
Como usar o sistema para gerar conteúdo do zero ao post pronto. Cobre o fluxo completo (calendário → briefing → produção → publicação) e os atalhos para entrar no meio do fluxo.

### [04 — Referência de Skills](04-referencia-de-skills.md)
Descrição detalhada de cada skill: para que serve, quando usar, o que precisa como input, o que entrega como output, e tabelas de referência rápida.

### [05 — Resolução de Problemas](05-resolucao-de-problemas.md)
Erros comuns e soluções: API key não encontrada, Playwright não instalado, DESIGN.md não configurado, token da Meta expirado, e perguntas frequentes.

### [06 — Guia de Skills](06-guia-de-skills.md)
Como usar e quando usar cada uma das 19 skills — com fluxos sequenciais completos para carrossel educativo, carrossel de quebra de objeção, post estático, Reel, planejamento mensal e escala de conteúdo para vários canais. Inclui tabela de referência rápida por situação.

---

## Fluxo resumido

```
1. /gerador-de-angulos-para-um-tema   →  10 ângulos para o tema escolhido
        ↓ escolhe 1
2. /calendario-comercial              →  mapa estratégico do mês
        ↓ aprova
3. /briefing-leange                    →  briefing do post específico
        ↓ aprova
4. /hooks-para-carrossel              →  5 opções de capa (se for carrossel)
   /hooks-para-instagram-reels        →  7 opções de hook (se for reel)
        ↓ escolhe 1
5. /carrossel-leange                   →  carrossel completo (slides + imagens + PNGs)
   /estatico-leange                    →  post estático (foto IA + layout + PNG)
   /roteiro-leange                     →  roteiro de vídeo
        ↓ aprova
6. /legenda-para-carrossel            →  legenda final
   /legenda-para-reel
   /legenda-para-post-estatico
        ↓ opcional
   /1-conteudo-em-7-formatos          →  distribui para outros canais
        ↓
   /publicar-social-leange             →  publica no Instagram/TikTok/LinkedIn
```

**Aprovação humana obrigatória em cada etapa — nada avança sem sua confirmação.**

Você pode entrar no fluxo em qualquer passo. Se já tem o tema e o ângulo, comece no passo 3.

---

## Onde está cada coisa

| O que você procura | Onde está |
|---|---|
| Contexto da empresa | `_contexto/empresa.md` |
| Tom de voz da marca | `_contexto/preferencias.md` |
| Estratégia e prioridades | `_contexto/estrategia.md` |
| Identidade visual | `marca/DESIGN.md` |
| API key OpenAI | `credentials/openai_key.txt` |
| Token Meta (Instagram) | `credentials/meta.txt` |
| Posts gerados | `conteudo/` |
| Histórico aprovado | `conteudo/[tipo]/[tema]/_aprovado.md` |
