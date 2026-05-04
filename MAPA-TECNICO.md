# Mapa Técnico — Automação de Conteúdo para Redes Sociais
> Gerado em sessão de arquitetura em 2026-05-02. O sistema não parte do zero — orquestra peças já construídas.

---

## Definição do Problema

**O que:** Sistema semi-automático de criação de conteúdo para redes sociais, que substitui o processo manual atual por um fluxo orquestrado de coleta de contexto → geração de briefing com IA → aprovação humana → produção visual → publicação.

**Para quem:** Equipe de marketing de empresas do grupo (início pela empresa de construção a seco), com replicabilidade para outras marcas do grupo.

**Objetivo prático:** Reduzir o tempo entre "temos algo pra comunicar" e "post aprovado pronto pra publicar", mantendo a qualidade editorial e a consistência visual de marca.

---

## Tradução para Solução

**Tipo:** Automação de workflow editorial com IA generativa, rodando no Claude Code (CCOS-Unity como plataforma base).

**Como funciona em alto nível:**
1. Skill `calendario-comercial` monta o plano do mês com janelas de oportunidade, datas sazonais e cultura pop
2. Skill `briefing-unity` gera o briefing de cada conteúdo: gancho, copy base, formato recomendado, orientações visuais
3. Humano aprova o briefing antes de gerar os assets
4. Skills de produção visual (`carrossel-unity` ou `gpt-image2-unity`) geram o material
5. Humano aprova o conteúdo final
6. `publicar-social-unity` publica nas redes

**O que não faz ainda (evoluirá):**
- Não publica automaticamente no MVP — vem na V2
- Não coleta métricas no MVP — vem na V2
- Não gera vídeos finais (apenas roteiro) — gravação e edição continuam humanas
- Não integra com Figma
- Não faz gestão de comunidade (comentários, DMs)

---

## Peças Já Construídas

| Peça | Repositório | O que faz | Status |
|---|---|---|---|
| Plataforma/OS | `dobralabs/ccos-unity` | Orquestra skills no Claude Code, contexto persistente de marca, auto-sync GitHub | ✅ Pronto |
| Calendário estratégico | `calendario-comercial` skill | Define QUANDO e POR QUÊ — janelas comerciais, cultura pop, sazonalidade | ✅ Pronto |
| Geração de carrossel | `duduesh/carrossel-unity` | Texto + HTML + PNG via Playwright, 3 estilos, Instagram/TikTok; integra gpt-image2-unity para imagens fotográficas nos slides de capa e impacto (máx 3/carrossel) | ✅ Pronto |
| Copy de marca | `duduesh/ogilvy-copy` | Framework Ogilvy — copy de longo prazo, construção de identidade | ✅ Pronto |
| Copy de vendas | `duduesh/schwartz-copy` | Framework Schwartz — copy de conversão, 6 lead types, por nível de consciência | ✅ Pronto |
| Geração de imagem (default) | `duduesh/gpt-image2-unity` | gpt-image-1 via OpenAI API (key em credentials/openai_key.txt); ~$0,02–$0,10/imagem quality:high; latência 60-180s | ✅ Instalada |
| Geração de imagem (fallback) | `duduesh/nanobanana-unity` | Google Gemini, grátis, rápido — entra quando quota do ChatGPT estiver no limite | ✅ Pronto |
| Geração de imagem (contingência) | `duduesh/image-gen-unity` | GPT Image 2 via FAL API — pago por uso: ~$0,06–$0,22/imagem; carrossel de 10 cards = até $2,20 | ✅ Pronto |
| Publicação social | `duduesh/publicar-social-unity` | Instagram, TikTok, LinkedIn via Post for Me ou Meta Graph API | ✅ Pronto |
| Triagem YouTube | `duduesh/triagem-youtube-unity` | Análise editorial de temas — score, SEO, títulos otimizados (DataForSEO) | ✅ Pronto |

**O que falta construir:** skill `roteiro-unity` (V1). `briefing-unity` e gates de aprovação já estão definidos.

---

## Arquitetura Sugerida

### Fluxo principal (MVP → V2)

```
[CALENDARIO-COMERCIAL]  ← skill já existe
  Input: mês/período, empresa, produtos, eventos culturais (web search)
  Output: janelas comerciais, tema narrativo, produto a promover, timing
          │
          ▼
[GATE: APROVAÇÃO DO CALENDÁRIO]  ← a construir
  Humano revisa o plano do mês antes de gerar conteúdo
          │
          ▼
[BRIEFING-UNITY]  ← skill a construir (núcleo do MVP)
  Recebe: output do calendario + contexto da marca (CCOS) + biblioteca técnica (V1+)
  Entrega: gancho, copy base (ogilvy ou schwartz), formato recomendado, orientações visuais
          │
          ▼
[GATE: APROVAÇÃO DO BRIEFING]  ← a construir
  Humano valida gancho, tom e direção antes de gerar assets
          │
          ├── formato carrossel ──→ [CARROSSEL-UNITY]  ← já existe
          │                          Texto + imagens GPT (capa + impacto) + HTML + PNG
          │
          ├── formato imagem ────→ [GPT-IMAGE2-UNITY]  ← default (OAuth ChatGPT, sem custo adicional)
          │                       → [NANOBANANA-UNITY] ← fallback (Gemini, grátis, quota esgotada)
          │                       → [IMAGE-GEN-UNITY]  ← contingência (FAL API, pago — até $2,20/carrossel)
          │
          └── formato vídeo ─────→ [ROTEIRO-UNITY]  ← a construir (V1)
                                    Script cena a cena para Reels/TikTok/YouTube
          │
          ▼
[GATE: APROVAÇÃO DO CONTEÚDO FINAL]  ← a construir
  Humano valida visual + copy antes de publicar
          │
          ▼
[PUBLICAR-SOCIAL-UNITY]  ← já existe
  Instagram, TikTok, LinkedIn
  MVP: acionado manualmente | V2: automático após aprovação
```

### Loop de inteligência (V3)

```
[PUBLICAÇÃO]
     │
     ▼
[COLETA DE MÉTRICAS]  ← Python, APIs das redes
     │
     ▼
[BASE DE CONHECIMENTO DE PERFORMANCE]  ← Supabase
  Registra: gancho, formato, tema, plataforma, data, métricas
     │
     ▼
[AGENTE DE ANÁLISE]  ← roda semanal/mensal
  Identifica padrões de melhor e pior performance
     │
     ▼
[BRIEFING-UNITY]  ← recebe padrões como contexto
  Prioriza ganchos e formatos com histórico positivo
```

**Dependências:**
- Biblioteca técnica alimenta o briefing-unity com dados técnicos dos produtos
- Loop de inteligência só tem valor com ~20-30 posts com dados coletados
- Aprovações são gates obrigatórios — o fluxo para enquanto não há resposta

---

## Stack

| Camada | Tecnologia | Status |
|---|---|---|
| Plataforma/OS | **CCOS-Unity** (Claude Code local) | ✅ Existe |
| Calendário/contexto externo | **calendario-comercial** skill | ✅ Existe |
| Geração de carrossel | **carrossel-unity** (HTML → PNG via Playwright, 3 estilos; imagens via gpt-image2-unity integrado) | ✅ Existe |
| Copy de marca | **ogilvy-copy** skill | ✅ Existe |
| Copy de vendas | **schwartz-copy** skill | ✅ Existe |
| Geração de imagem (default) | **gpt-image2-unity** (gpt-image-1 via OpenAI API key; openai SDK 2.33.0 instalado) | ✅ Instalada |
| Geração de imagem (fallback) | **nanobanana-unity** (Gemini, grátis) | ✅ Existe |
| Geração de imagem (contingência) | **image-gen-unity** (GPT Image 2 via FAL API, pago) | ✅ Existe |
| Publicação social | **publicar-social-unity** (Post for Me $10/mês ou Meta Graph API) | ✅ Existe |
| Briefing orchestrator | **briefing-unity** | ✅ Skill criada — aguarda validação com runs reais |
| Gates de aprovação | Fluxo conversacional no Claude Code (A/E/C) | ✅ Definidos na skill |
| Roteiro de vídeo | **roteiro-unity** | 🔜 V1 |
| Biblioteca técnica | **Supabase pgvector + REST API** | 🔄 Projeto paralelo |
| Base de performance | **Supabase** (tabela separada da biblioteca) | 🔜 V2 |
| Coleta de métricas | **Python** — Meta Insights API + LinkedIn Analytics | 🔜 V2 |
| Deploy remoto | **n8n Cloud** ou **VPS** | 🔜 V1 |
| Autenticação futura | **Supabase Auth** | 🔜 V3 |

### Separação IA vs. Python

| Tarefa | Quem faz |
|---|---|
| Calendário, briefing, copy, roteiro, análise de performance | IA — Claude via skills |
| Renderização HTML → PNG | Playwright (dentro do carrossel-unity) |
| Publicação via API, coleta de métricas, registro em banco | Python (V2+) |

**Evitar:**
- n8n no MVP — CCOS-Unity já orquestra tudo no Claude Code
- Canva API no MVP — acesso restrito (programa de parceiros); carrossel-unity entrega o mesmo resultado

**Hierarquia de geração de imagem:**
1. `gpt-image2-unity` (default) — modelo gpt-image-1 via OpenAI API; API key em `credentials/openai_key.txt`; custo ~$0,02–$0,10/imagem (quality: high); latência 60-180s; usado diretamente pelo carrossel-unity e standalone
2. `nanobanana-unity` (fallback) — Gemini, grátis e rápido; entra quando a key OpenAI não estiver disponível ou a API falhar — **pendente instalação**
3. `image-gen-unity` (contingência) — GPT Image 2 via FAL API; ativar só quando as opções acima não estiverem disponíveis; custo: ~$0,06/imagem (média) a $0,22/imagem (alta qualidade) — carrossel de até 10 cards pode custar até $2,20 — **pendente instalação**

**Uso do gpt-image2 no carrossel:**
- Fase 1.5 do fluxo carrossel-unity: gera imagens fotográficas antes de criar os HTMLs
- Slides com imagem: capa (sempre) + até 2 slides de impacto (máx 3/carrossel)
- Imagens salvas como `img-slideXX.png` na pasta do carrossel; referenciadas por caminho relativo nos HTMLs
- Overlay `rgba(0,0,0,0.45)` aplicado no HTML para garantir legibilidade do texto sobre a foto

---

## Integração com a Biblioteca Técnica

**Projeto:** `C:\Users\gabri\OneDrive\Desktop\Unity - Projetos\Biblioteca de conteúdos`

**Arquitetura:** RAG de 4 camadas — Google Drive (arquivos originais) → Google Sheets (metadados/catálogo) → Supabase pgvector (embeddings de Resumo_IA) → REST API (consumo agnóstico por IA).

**Status:** Projeto documentado, scripts prontos, implementação pendente (todas as 8 fases a executar). Bloqueantes: ID do Drive Compartilhado, Organizador não definido, credenciais Supabase/OpenAI em aberto.

**Contrato de integração (já definido):**
- `briefing-unity` envia o gancho como query em texto
- API converte para embedding → busca semântica no pgvector
- Retorna `Titulo`, `Fabricante_Fonte`, `Resumo_IA`, `Tags`, `Norma_Ref` dos documentos relevantes
- REST API agnóstica — funciona com Claude, GPT ou qualquer modelo

**Quando integrar:** após a Fase 7 da biblioteca (wrapper de consulta). No MVP opera sem ela — conteúdo técnico fica mais raso mas o fluxo funciona.

**Observação:** o campo `Conteudo_Gerado` já está reservado no Google Sheets da biblioteca — deve ser preenchido pela automação com referência a qual conteúdo foi gerado a partir de cada documento consultado.

---

## Riscos e Travas

**Canva API**
- API do Canva tem acesso limitado (programa de parceiros) — não entra no MVP
- No MVP e V1: carrossel-unity entrega PNG pronto via HTML/CSS

**Qualidade do briefing**
- IA pode gerar ganchos genéricos sem contexto suficiente da marca
- Mitigação: prompt engineering cuidadoso + exemplos de conteúdos aprovados como referência (few-shot) no `briefing-unity`

**APIs de redes sociais**
- Meta muda limites e permissões com frequência — monitorar
- TikTok API tem restrições para contas menores — verificar antes do V2
- YouTube upload via API requer verificação adicional da conta

**Migração local → web**
- Construir o MVP sem hardcode de paths locais, credenciais ou configurações que não funcionam em cloud
- Transição simples: exportar workflows → importar no n8n Cloud (funciona se tudo estiver parametrizado)
- Assets em disco (imagens, PDFs) precisam migrar para cloud storage (S3 ou Google Drive) antes do V1

**Biblioteca técnica ausente no MVP**
- Conteúdo técnico fica mais raso até a integração
- Mitigação: operador fornece dados técnicos relevantes no input do briefing manualmente por ora

**CCOS — perfil empresa, não agência**
- O CCOS-Unity foi construído com cabeça de agência (clientes, contunity, propostas, cobrança)
- Usar o template `claude-md-empresa.md` como base do setup
- Remover skills irrelevantes: proposta comercial, gestão de clientes, cobrança
- Multi-empresa: cada marca do grupo = workspace CCOS independente (repo separado, contexto isolado)

---

## Gaps — Decisões em Aberto

**Decidido:**
- ✅ Um workspace CCOS independente por empresa do grupo — contextos isolados, rollout gradual
- ✅ MVP roda localmente no Claude Code, sem infraestrutura
- ✅ Publicação automática vem na V2, não no MVP
- ✅ Python assume tarefas determinísticas (publicação, métricas, banco) no V2+

**Ainda precisa de decisão antes do V1:**
- Canal de aprovação remota: Slack, e-mail, WhatsApp ou interface web própria?
- Quem aprova? Operador central ou qualquer membro da equipe pode aprovar?
- Publicação: imediata após aprovação ou sempre agendada?
- App web futura: acesso por empresa isolado ou painel unificado do grupo?

---

## Instalação das Skills no Projeto (MVP)

Skills instaladas por ordem de fluxo — instalar o que o próximo passo precisa, não tudo de uma vez.

```
/calendario → /briefing-unity → /schwartz-copy + /ogilvy-copy → /carrossel ou /gpt-image2 → /publicar-social
    [1]            [✅ OK]               [2a] e [2b]                    [3a] ou [3b]               [4]
                                                                    fallback: [3c] nanobanana
                                                                    contingência: [3d] image-gen
```

| # | Skill | Repositório de origem | Status |
|---|---|---|---|
| 1 | `calendario-comercial` | Local (`_modelo-cliente`) | ✅ Instalada |
| ✅ | `briefing-unity` | Criada neste projeto | ✅ Instalada |
| 2a | `schwartz-copy` | github.com/duduesh/schwartz-copy | ✅ Instalada |
| 2b | `ogilvy-copy` | github.com/duduesh/ogilvy-copy | ✅ Instalada |
| 3a | `carrossel-unity` | github.com/duduesh/carrossel-ratos | ✅ Instalada |
| 3b | `gpt-image2-unity` | github.com/duduesh/gpt-image2-ratos | ✅ Instalada |
| 3c | `nanobanana-unity` | github.com/duduesh/nanobanana-ratos | 🔜 Fallback |
| 3d | `image-gen-unity` | github.com/duduesh/image-gen-ratos | 🔜 Contingência |
| 4 | `publicar-social-unity` | github.com/duduesh/publicar-social-ratos | 🔜 Quando chegar na publicação |
| V1 | `triagem-youtube-unity` | github.com/duduesh/triagem-youtube-ratos | 🔜 V1 |

> Atualizar status conforme cada skill for instalada.

---

## Plano em Fases

### MVP — Orquestrar as peças que já existem
**Roda no CCOS-Unity (Claude Code local). Construção mínima.**

**O que construir:**
- Skill `briefing-unity`: recebe output do `calendario-comercial` + contexto da marca (CCOS) → gera briefing completo
- Gates de aprovação conversacionais (pontos de pausa no fluxo)

**Fluxo:**
```
/calendario → [aprova] → /briefing → [aprova] → /carrossel ou /gpt-image2 (→ /nanobanana → /image-gen) → [aprova] → /publicar-social
```

**Validação:** 10 conteúdos produzidos pelo fluxo. Mede: tempo total vs. processo anterior, taxa de aprovação sem ajuste, qualidade percebida.

---

### V1 — Deploy remoto + biblioteca técnica

- Deploy em n8n Cloud ou VPS (acesso remoto para o time)
- Integração com biblioteca técnica via Supabase RAG (depende da Fase 7 do projeto paralelo)
- Skill `roteiro-unity`: roteiro cena a cena para Reels/TikTok/YouTube
- Copy adaptado por plataforma (LinkedIn vs Instagram vs TikTok)
- Entrega de pacote completo: visual + copy + hashtags por plataforma

---

### V2 — Publicação automática + coleta de métricas

- Publicação automática após aprovação via `publicar-social-unity`
- Scripts Python: publicação, coleta de métricas (Meta Insights + LinkedIn Analytics), registro em Supabase
- Registro estruturado por post: gancho, formato, tema, plataforma, data, métricas
- Variações visuais por formato de plataforma (story, feed, reels)

---

### V3 — Loop de inteligência de conteúdo

- Análise periódica: agente lê histórico e identifica padrões de melhor performance
- Retroalimentação do `briefing-unity`: ganchos e formatos com histórico positivo ganham peso
- Score de conteúdo: briefings recebem previsão de performance antes da aprovação
- Sugestão proativa: sistema identifica janelas de oportunidade e sugere sem input manual
- Dashboard de inteligência editorial

---

## Skills — Mapa Completo

### Existentes

| Skill | Repo | Input | Output |
|---|---|---|---|
| `calendario-comercial` | interno | mês, empresa, produtos | janelas comerciais, tema, timing |
| `carrossel-unity` | duduesh/carrossel-unity | tema, estilo | PNGs 1080×1350 (Instagram) ou 1080×1920 (TikTok); imagens fotográficas geradas via gpt-image2-unity na capa e slides de impacto |
| `ogilvy-copy` | duduesh/ogilvy-copy | briefing de marca | copy de longo prazo, headlines, manifestos |
| `schwartz-copy` | duduesh/schwartz-copy | produto, audience, consciousness level | copy de conversão, 6 lead types |
| `gpt-image2-unity` | duduesh/gpt-image2-unity | prompt em inglês, aspect ratio (square/portrait/landscape) | imagem PNG via gpt-image-1 (OpenAI API key; openai SDK 2.33.0; ~$0,02–$0,10/img) |
| `nanobanana-unity` | duduesh/nanobanana-unity | prompt em inglês, aspect ratio | imagem PNG via Gemini (grátis, fallback) |
| `image-gen-unity` | duduesh/image-gen-unity | prompt, qualidade, aspect ratio, ref. opcional | imagem PNG via GPT Image 2 (FAL API, contingência paga) |
| `publicar-social-unity` | duduesh/publicar-social-unity | imagem/texto, plataformas, data/hora | URLs dos posts publicados + IDs |
| `triagem-youtube-unity` | duduesh/triagem-youtube-unity | lista de temas | score, títulos, keywords, tier ranking |

### A construir

```
roteiro-unity  ← V1
  Input: briefing aprovado, plataforma alvo, duração estimada
  Output: roteiro estruturado cena a cena (falas, cortes, orientações de câmera)

coletor-metricas.py  ← V2, Python
  Input: IDs dos posts, janela de tempo
  Output: registro estruturado no Supabase (gancho, formato, tema, métricas)

analista-performance  ← V3
  Input: base de posts com métricas (Supabase)
  Output: padrões de melhor performance + contexto para retroalimentar o briefing-unity
```

---

*Mapa gerado em sessão de arquitetura — 2026-05-02.*
*Para retomar: o ponto de entrada é construir o `briefing-unity` em cima do CCOS com perfil empresa (template `claude-md-empresa.md`), não agência.*
