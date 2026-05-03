# Unity Content — Sistema de Automação de Conteúdo para Redes Sociais

---

## O que é este projeto

Sistema de automação do processo de criação de conteúdo para redes sociais do Grupo Unity. Substitui o workflow editorial manual por um fluxo orquestrado de IA que vai da definição estratégica do tema até a entrega do pacote de conteúdo pronto para publicação.

**Objetivo:** Reduzir o tempo entre "temos algo para comunicar" e "post aprovado pronto para publicar", mantendo qualidade editorial e consistência visual de marca.

**Contexto:** Departamento de marketing interno, não agência. Cada empresa do grupo opera com seu próprio workspace independente — contextos isolados, rollout gradual, sem risco de embaralhamento entre marcas.

**Empresa piloto:** Construção a seco (drywall/steel frame).

---

## O que o sistema faz

1. Monta o calendário comercial do mês com base em janelas de oportunidade, datas sazonais e eventos de cultura pop relevantes para a marca
2. Para cada conteúdo do calendário, gera um briefing completo: gancho, copy base, formato recomendado e orientações visuais
3. A partir do briefing aprovado, gera o asset visual (carrossel PNG ou imagem avulsa)
4. Para conteúdo em vídeo, gera o roteiro cena a cena (Reels/TikTok/YouTube)
5. Entrega o pacote completo: visual + copy + hashtags por plataforma
6. Publica nas redes após aprovação final

**Aprovação humana obrigatória** em cada etapa crítica — o fluxo para e aguarda antes de avançar.

**Publicação automática** não entra no MVP — é manual por ora, vira automática na V2.

---

## O que o sistema não faz

- Não publica automaticamente no MVP (vem na V2)
- Não gera o vídeo final — apenas o roteiro; gravação e edição continuam sendo humanas
- Não faz gestão de comunidade (comentários, DMs)
- Não integra com o Figma (apenas Canva e geração HTML/PNG por enquanto)

---

## Peças existentes (não precisam ser construídas)

Este sistema não parte do zero. As seguintes ferramentas já existem como skills no Claude Code:

| Peça | Repositório | O que faz |
|---|---|---|
| Plataforma/OS | `ccos-unity` (dobralabs) | Orquestra skills, contexto persistente de marca, auto-sync com GitHub — **instalado e configurado** |
| Calendário estratégico | `calendario-comercial` | Janelas comerciais, cultura pop, sazonalidade, timing |
| Geração de carrossel | `carrossel-unity` | Texto + HTML + PNG via Playwright, 3 estilos, Instagram/TikTok |
| Copy de marca | `ogilvy-copy` | Framework Ogilvy — copy de longo prazo, construção de identidade |
| Copy de vendas | `schwartz-copy` | Framework Schwartz — copy de conversão por nível de consciência |
| Geração de imagem (default) | `gpt-image2-unity` | GPT Image 2 via OAuth ChatGPT — usa quota da assinatura, sem custo adicional de API |
| Geração de imagem (fallback) | `nanobanana-unity` | Google Gemini, grátis, rápido — entra quando quota do ChatGPT estiver no limite |
| Geração de imagem (contingência) | `image-gen-unity` | GPT Image 2 via FAL API — pagamento por uso: ~$0,06/imagem (média) até $0,22/imagem (alta qualidade); carrossel de até 10 cards pode chegar a $2,20 |
| Publicação social | `publicar-social-unity` | Instagram, TikTok, LinkedIn via Post for Me ou Meta Graph API |
| Triagem YouTube | `triagem-youtube-unity` | Análise editorial de temas — score, SEO, títulos otimizados |

**O que falta construir:** a skill `briefing-unity` que conecta todas essas peças em um fluxo único, mais os gates de aprovação e, futuramente, a skill de roteiro de vídeo.

---

## Arquitetura do fluxo

```
[CALENDARIO-COMERCIAL]
  Input: mês/período, empresa, produtos, eventos culturais (web search)
  Output: janelas comerciais, tema narrativo, produto a promover, timing
          │
          ▼
[GATE: APROVAÇÃO DO CALENDÁRIO]
  Humano revisa o plano do mês antes de gerar conteúdo
          │
          ▼
[BRIEFING-UNITY]  ← skill a construir
  Recebe: output do calendario + contexto da marca (CCOS) + biblioteca técnica (V1+)
  Entrega: gancho, copy base, formato recomendado, orientações visuais
          │
          ▼
[GATE: APROVAÇÃO DO BRIEFING]
  Humano valida gancho, tom e direção antes de gerar assets
          │
          ├── carrossel ──→ [CARROSSEL-UNITY] → PNG pronto
          ├── imagem ─────→ [GPT-IMAGE2-UNITY] → GPT Image 2 via ChatGPT (default)
          │                → [NANOBANANA-UNITY] → Gemini, grátis (fallback: quota esgotada)
          │                → [IMAGE-GEN-UNITY]  → GPT Image 2 via FAL API (contingência: até $2,20/carrossel)
          └── vídeo ──────→ [ROTEIRO-UNITY] → script cena a cena (V1)
          │
          ▼
[GATE: APROVAÇÃO DO CONTEÚDO FINAL]
  Humano valida visual + copy antes de publicar
          │
          ▼
[PUBLICAR-SOCIAL-UNITY]
  Instagram, TikTok, LinkedIn
  MVP: acionado manualmente após aprovação
  V2+: automático após aprovação
```

### Loop de inteligência (V3)

```
[PUBLICAÇÃO]
     ↓
[COLETA DE MÉTRICAS] ← APIs das redes
     ↓
[BASE DE PERFORMANCE] ← Supabase
  Registra: gancho, formato, tema, plataforma, data, métricas
     ↓
[AGENTE DE ANÁLISE] ← roda semanal/mensal
  Identifica padrões de melhor e pior performance
     ↓
[BRIEFING-UNITY]
  Prioriza ganchos e formatos com histórico positivo
```

---

## Stack

| Camada | Tecnologia | Status |
|---|---|---|
| Plataforma/OS | CCOS-Unity (Claude Code local) | ✅ Instalado e configurado |
| Calendário/contexto externo | calendario-comercial skill | ✅ Existe |
| Geração de carrossel | carrossel-unity (HTML → PNG via Playwright) | ✅ Existe |
| Copy | ogilvy-copy + schwartz-copy | ✅ Existe |
| Geração de imagem (default) | gpt-image2-unity (GPT Image 2 via OAuth ChatGPT) | ✅ Existe |
| Geração de imagem (fallback) | nanobanana-unity (Gemini, grátis) | ✅ Existe |
| Geração de imagem (contingência API) | image-gen-unity (GPT Image 2 via FAL API, pago) | ✅ Existe |
| Publicação social | publicar-social-unity (Post for Me ou Meta Graph API) | ✅ Existe |
| Briefing orchestrator | briefing-unity | ✅ Skill criada — aguarda validação com runs reais |
| Gates de aprovação | Fluxo conversacional (A/E/C) | ✅ Definidos na skill |
| Roteiro de vídeo | roteiro-unity | 🔜 V1 |
| Biblioteca técnica | Supabase pgvector + REST API | 🔄 Projeto paralelo |
| Base de performance | Supabase (tabela separada) | 🔜 V2 |
| Coleta de métricas | Python (Meta Insights + LinkedIn Analytics) | 🔜 V2 |
| Deploy remoto | n8n Cloud ou VPS | 🔜 V1 |
| Autenticação web | Supabase Auth | 🔜 V3 |

### Separação IA vs. Python

| Tarefa | Quem executa |
|---|---|
| Calendário comercial, briefing, copy, roteiro, análise de performance | IA — Claude via skills |
| Renderização HTML → PNG | Playwright (dentro do carrossel-unity) |
| Publicação via API, coleta de métricas, registro em banco | Python (V2+) |

**Evitar:**
- n8n no MVP — CCOS-Unity já orquestra no Claude Code
- Canva API no MVP — acesso restrito; carrossel-unity entrega o mesmo resultado

**Hierarquia de geração de imagem:**
1. `gpt-image2-unity` (default) — GPT Image 2 via OAuth ChatGPT; sem custo adicional, usa quota da assinatura; latência 60-180s
2. `nanobanana-unity` (fallback) — Gemini, grátis, rápido; entra quando quota do ChatGPT estiver no limite
3. `image-gen-unity` (contingência) — GPT Image 2 via FAL API; ativar só quando as opções acima não estiverem disponíveis; custo: ~$0,06/imagem (média) a $0,22/imagem (alta qualidade) — carrossel de até 10 cards pode custar até $2,20

---

## Integração com a Biblioteca Técnica

A Biblioteca de Conteúdos (projeto paralelo) já foi projetada para consumo por IA desde o início. Quando disponível, o `briefing-unity` vai consultá-la para enriquecer o conteúdo com dados técnicos reais.

**Arquitetura da biblioteca:** RAG de 4 camadas — Google Drive (arquivos) → Google Sheets (metadados) → Supabase pgvector (embeddings) → REST API (consumo por IA).

**Contrato de integração:**
- `briefing-unity` envia o gancho como query em texto
- API converte para embedding → busca semântica no pgvector
- Retorna `Titulo`, `Fabricante_Fonte`, `Resumo_IA`, `Tags`, `Norma_Ref` dos documentos mais relevantes

**Quando integrar:** assim que a Fase 7 da biblioteca estiver concluída (wrapper de consulta).

**No MVP:** enquanto a biblioteca não estiver pronta, o agente opera com o contexto fornecido no input. Conteúdo técnico fica mais raso, mas o fluxo funciona.

---

## Deploy e escalabilidade

**MVP:** roda localmente no Claude Code, máquina do operador. Sem infraestrutura. Sem custo fixo.

**V1+:** migra para n8n Cloud ou VPS — o time inteiro acessa de qualquer lugar sem replicar a instalação em cada máquina.

**Regra crítica para a migração:** construir o MVP já sem hardcode de paths locais, credenciais ou configurações que não funcionam em cloud. A transição é exportar os workflows e importar — funciona se tudo estiver parametrizado.

**Multi-empresa:** cada empresa do grupo tem seu próprio workspace CCOS independente — repo separado, contexto isolado, credenciais separadas, histórico independente. Rollout gradual: começa na empresa piloto, valida, replica para as demais sem risco de comprometer o que já funciona.

**V3 → aplicação web:** quando a escala justificar, o sistema evolui para uma aplicação web com autenticação (Supabase Auth), controle de acesso por empresa e interface para operadores não-técnicos.

---

## Plano em fases

### MVP — Conectar as peças que já existem

**O que construir:**
- ~~Skill `briefing-unity`~~ ✅ Criada com spec completa e gates definidos
- ~~Gates de aprovação conversacionais~~ ✅ Definidos na skill (A/E/C)
- ~~Instalar `calendario-comercial` no projeto~~ ✅ Instalada
- ~~Instalar `schwartz-copy` e `ogilvy-copy`~~ ✅ Instaladas
- Instalar skills de geração de imagem e publicação por ordem de fluxo — ver [MAPA-TECNICO.md](MAPA-TECNICO.md)

**Fluxo:**
```
/calendario → [aprova] → /briefing → [aprova] → /carrossel ou /gpt-image2 (→ /nanobanana → /image-gen) → [aprova] → /publicar-social
```

**Validação:** 10 conteúdos produzidos pelo fluxo. Mede tempo total vs. processo anterior, taxa de aprovação sem ajuste, qualidade percebida.

---

### V1 — Deploy remoto + biblioteca técnica

- Deploy em n8n Cloud ou VPS (acesso remoto para o time)
- Integração com a biblioteca técnica via Supabase RAG
- Skill `roteiro-unity` para conteúdo em vídeo
- Copy adaptado por plataforma
- Pacote completo: visual + copy + hashtags por plataforma

---

### V2 — Publicação automática + métricas

- Publicação automática após aprovação via publicar-social-unity
- Scripts Python: publicação, coleta de métricas, registro em Supabase
- Registro estruturado por post: gancho, formato, tema, plataforma, métricas

---

### V3 — Loop de inteligência

- Análise periódica de performance
- Retroalimentação do briefing-unity com padrões de sucesso
- Score de conteúdo antes da aprovação
- Sugestão proativa de conteúdo
- Dashboard de inteligência editorial

---

## Riscos e decisões em aberto

**Riscos conhecidos:**
- Canva API tem acesso restrito (programa de parceiros) — não entra no MVP, carrossel-unity resolve
- Meta muda permissões de API com frequência — monitorar
- TikTok API tem restrições para contas menores — verificar antes do V2
- YouTube upload via API requer verificação adicional da conta
- Biblioteca técnica ainda não implementada — MVP opera sem ela
- Qualidade do briefing depende do prompt engineering — validar nas primeiras 10 execuções

**Decisões ainda em aberto:**
- Canal de aprovação no V1: Slack, e-mail, WhatsApp ou interface web?
- Quem aprova? Operador central ou qualquer membro da equipe?
- Publicação: imediata após aprovação ou sempre agendada?
- Visão futura da web app: acesso por empresa isolado ou painel unificado do grupo?

---

## Skills a construir

```
briefing-unity  ← MVP
  Input: output do calendario-comercial + contexto CCOS + query biblioteca (V1+)
  Output: gancho, copy base, formato recomendado, orientações visuais

roteiro-unity  ← V1
  Input: briefing aprovado, plataforma alvo, duração estimada
  Output: roteiro estruturado cena a cena

coletor-metricas.py  ← V2, Python
  Input: IDs dos posts, janela de tempo
  Output: registro estruturado no Supabase

analista-performance  ← V3
  Input: base de posts com métricas
  Output: padrões de melhor performance + contexto para retroalimentar o briefing-unity
```

---

*Documento gerado em 2026-05-02. Última atualização: 2026-05-03 — briefing-unity criada, calendario-comercial instalada, roadmap de instalação em andamento.*
