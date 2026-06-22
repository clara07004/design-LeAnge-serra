# CCOS — Sistema de Automação de Conteúdo

Sistema de automação do processo de criação de conteúdo para redes sociais. Substitui o workflow editorial manual por um fluxo orquestrado de IA — da definição estratégica do tema até a entrega do pacote de conteúdo pronto para publicação.

**Objetivo:** Reduzir o tempo entre "temos algo para comunicar" e "post aprovado pronto para publicar", mantendo qualidade editorial e consistência visual de marca.

**Empresa:** [Preencher após rodar `/setup` — cada empresa opera com seu próprio workspace]

---

## O que o sistema faz

1. Monta o calendário comercial do mês com base em janelas de oportunidade, datas sazonais e cultura pop
2. Gera um briefing completo para cada conteúdo: gancho, copy base, formato recomendado e orientações visuais
3. A partir do briefing aprovado, gera o asset visual (carrossel PNG ou imagem avulsa)
4. Para conteúdo em vídeo, gera o roteiro cena a cena (Reels / TikTok / YouTube)
5. Entrega o pacote completo: visual + copy + hashtags por plataforma
6. Publica nas redes após aprovação final

**Aprovação humana obrigatória** em cada etapa crítica — o fluxo para e aguarda antes de avançar.

---

## O que o sistema não faz (ainda)

- Publicação automática no MVP — vem na V2
- Geração do vídeo final — apenas o roteiro; gravação e edição continuam sendo humanas
- Gestão de comunidade (comentários, DMs)
- Integração com Figma — por ora apenas Canva e geração HTML/PNG

---

## Fluxo principal

```
[CALENDARIO-COMERCIAL]
  Input: período + lê contexto da empresa (frequência, plataformas, objetivo)
  Output: mapa de oportunidades proporcional à frequência de postagem
          │
          ▼
[GATE: APROVAÇÃO DO CALENDÁRIO]
          │
          ▼
[BRIEFING-UNITY]
  Recebe: tema do calendário + contexto da marca
  Entrega: objetivo, mensagem, formato recomendado, orientações visuais
          │
          ▼
[GATE: APROVAÇÃO DO BRIEFING]
          │
          ├── carrossel ──→ [CARROSSEL-UNITY]
          │                  motor: gpt-image2-unity (foto) + Playwright (render)
          │
          ├── imagem ─────→ [ESTATICO-UNITY]
          │                  motor: gpt-image2-unity (foto) + Playwright (render)
          │                  fallback foto: nanobanana-unity → image-gen-unity
          │
          └── vídeo ──────→ [ROTEIRO-UNITY]
                             motor: ogilvy-copy (orgânico) ou schwartz-copy (tráfego)
          │
          ▼
[GATE: APROVAÇÃO DO CONTEÚDO FINAL]
          │
          ▼
[PUBLICAR-SOCIAL-UNITY]
  Instagram, TikTok, LinkedIn
  MVP: acionado manualmente | V2: automático após aprovação
```

---

## Skills instaladas

### Skills de produção (acionadas diretamente no fluxo)

| Skill | O que faz |
|---|---|
| `calendario-comercial` | Mapa de oportunidades do período — lê contexto da empresa, frequência de postagem e objetivo; output proporcional à frequência |
| `briefing-unity` | Briefing completo de um tema: objetivo, mensagem, formato recomendado, orientações visuais |
| `carrossel-unity` | Carrossel completo: texto + imagens GPT + HTML + PNG via Playwright (Instagram/TikTok) |
| `estatico-unity` | Post card único completo: foto de fundo GPT + layout HTML + PNG via Playwright |
| `roteiro-unity` | Roteiro de vídeo para Reels/TikTok — Ogilvy para orgânico, Schwartz para tráfego pago |
| `publicar-social-unity` | Publica conteúdo aprovado no Instagram, TikTok, LinkedIn |
| `triagem-youtube-unity` | Score editorial, SEO e títulos otimizados via DataForSEO |

### Motores (usados internamente pelas skills de produção)

| Motor | O que faz |
|---|---|
| `gpt-image2-unity` | Gera foto de fundo via gpt-image-1 (OpenAI API); ~$0,02–$0,10/img; latência 60–180s |
| `nanobanana-unity` | Fallback de imagem via Google Gemini (grátis) |
| `image-gen-unity` | Contingência de imagem via FAL API (pago; ~$0,06–$0,22/img) |
| `ogilvy-copy` | Copy de marca e conteúdo orgânico (motor do roteiro orgânico) |
| `schwartz-copy` | Copy de resposta direta (motor do roteiro de tráfego pago) |

---

## A construir

```
coletor-metricas.py  ← V2, Python
  Input:  IDs dos posts, janela de tempo
  Output: registro estruturado no Supabase

analista-performance  ← V3
  Input:  base de posts com métricas (Supabase)
  Output: padrões de melhor performance → retroalimenta briefing-unity
```

---

## Stack

| Camada | Tecnologia | Status |
|---|---|---|
| Plataforma / OS | CCOS (Claude Code local) | ✅ Existe |
| Calendário | `calendario-comercial` skill | ✅ Existe |
| Geração de carrossel | `carrossel-unity` (HTML → PNG via Playwright) | ✅ Existe |
| Post card único | `estatico-unity` (foto GPT + HTML → PNG via Playwright) | ✅ Novo |
| Roteiro de vídeo | `roteiro-unity` (Ogilvy / Schwartz como motor) | ✅ Novo |
| Copy | `ogilvy-copy` + `schwartz-copy` | ✅ Existe |
| Motor de imagem | `gpt-image2-unity` / `nanobanana-unity` / `image-gen-unity` | ✅ Existe |
| Publicação social | `publicar-social-unity` | ✅ Existe |
| Briefing orchestrator | `briefing-unity` | ✅ Em validação |
| Gates de aprovação | Fluxo conversacional no Claude Code | ✅ Definidos |
| Biblioteca técnica | Supabase pgvector + REST API | 🔄 Projeto paralelo |
| Base de performance | Supabase | 🔜 V2 |
| Coleta de métricas | Python (Meta Insights + LinkedIn Analytics) | 🔜 V2 |
| Deploy remoto | n8n Cloud ou VPS | 🔜 V1 |
| Autenticação web | Supabase Auth | 🔜 V3 |

---

## Loop de inteligência (V3)

```
[PUBLICAÇÃO]
     ↓
[COLETA DE MÉTRICAS]  ← Python, APIs das redes
     ↓
[BASE DE PERFORMANCE]  ← Supabase
     ↓
[AGENTE DE ANÁLISE]  ← roda semanal / mensal
     ↓
[BRIEFING-UNITY]  ← recebe padrões como contexto
```

---

## Integração com a Biblioteca Técnica

Projeto paralelo que alimenta o `briefing-unity` com dados técnicos reais sobre os produtos.

**Arquitetura:** RAG de 4 camadas — Google Drive (arquivos) → Google Sheets (metadados) → Supabase pgvector (embeddings) → REST API (consumo por IA).

**Contrato de integração:**
- `briefing-unity` envia o gancho como query em texto
- API converte para embedding → busca semântica no pgvector
- Retorna `Titulo`, `Fabricante_Fonte`, `Resumo_IA`, `Tags`, `Norma_Ref`

**No MVP:** enquanto a biblioteca não estiver pronta, o operador fornece os dados técnicos manualmente no input. O fluxo funciona — o conteúdo técnico fica mais raso por ora.

---

## Roadmap

| Fase | O que entrega |
|---|---|
| **MVP** | ✅ Fluxo completo validado. Skills de produção: `calendario`, `briefing`, `carrossel`, `estatico-unity`, `roteiro-unity`. Motores: `gpt-image2`, `nanobanana`, `ogilvy`, `schwartz`. Infraestrutura: Node.js + Playwright + Python + openai SDK. |
| **V1** | Deploy remoto (n8n Cloud / VPS) + biblioteca técnica |
| **V2** | Publicação automática + coleta de métricas + registro no Supabase |
| **V3** | Loop de inteligência + score de conteúdo + sugestão proativa + dashboard |

---

## Variáveis de ambiente

Copie `.env.example` para `.env` e preencha os valores:

```bash
cp .env.example .env
```

| Variável / Arquivo | Serviço | Notas |
|---|---|---|
| `credentials/openai_key.txt` | OpenAI API | [platform.openai.com](https://platform.openai.com) → API Keys; usado pelo gpt-image2-unity e carrossel-unity |
| `GEMINI_API_KEY` | Google Gemini | Grátis — [aistudio.google.com](https://aistudio.google.com) — usado pelo nanobanana-unity (fallback) |
| `META_APP_ID` | Meta / Facebook | [developers.facebook.com](https://developers.facebook.com) |
| `META_APP_SECRET` | Meta / Facebook | |
| `META_ACCESS_TOKEN` | Meta Graph API | ⚠️ Expira em 60 dias — renovar via Graph API Explorer |
| `IMGBB_API_KEY` | imgbb | Hospedagem de imagens para Instagram |
| `FAL_KEY` | FAL API | Pago — usar apenas como contingência (image-gen-unity) |

---

## Multi-empresa

Cada empresa opera com seu próprio workspace CCOS independente — repositório separado, contexto isolado, credenciais separadas, histórico independente. Rollout gradual: começa na empresa piloto, valida, replica para as demais sem risco de comprometer o que já funciona.

---

*Última atualização: 2026-05-05 — `estatico-unity` e `roteiro-unity` criadas. Arquitetura revisada: gpt-image2-unity e copy agents (ogilvy/schwartz) são motores internos, não skills de produção direta. `/setup` reescrito com confirmação obrigatória, coleta de frequência de postagem e regra verbal > documento. `/iniciar` removido (redundante). `calendario-comercial` atualizado para output proporcional à frequência. Template base — replicar por empresa.*
