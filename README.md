# Unity Content

Sistema de automação do processo de criação de conteúdo para redes sociais do Grupo Unity. Substitui o workflow editorial manual por um fluxo orquestrado de IA — da definição estratégica do tema até a entrega do pacote de conteúdo pronto para publicação.

**Objetivo:** Reduzir o tempo entre "temos algo para comunicar" e "post aprovado pronto para publicar", mantendo qualidade editorial e consistência visual de marca.

**Empresa piloto:** Construção a seco (drywall / steel frame).

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
  Input: mês/período, empresa, produtos, eventos culturais
  Output: janelas comerciais, tema narrativo, produto a promover, timing
          │
          ▼
[GATE: APROVAÇÃO DO CALENDÁRIO]
  Humano revisa o plano do mês antes de gerar conteúdo
          │
          ▼
[BRIEFING-UNITY]  ✅ skill criada — aguarda validação com runs reais
  Recebe: output do calendario + contexto da marca (CCOS) + biblioteca técnica (V1+)
  Entrega: gancho, copy base, formato recomendado, orientações visuais
          │
          ▼
[GATE: APROVAÇÃO DO BRIEFING]
          │
          ├── carrossel ──→ [CARROSSEL-UNITY] → imagens GPT + HTML + PNG
          ├── imagem ─────→ [GPT-IMAGE2-UNITY] → default (OpenAI API key)
          │                → [NANOBANANA-UNITY] → fallback (Gemini, grátis)
          │                → [IMAGE-GEN-UNITY]  → contingência (FAL API, pago)
          └── vídeo ──────→ [ROTEIRO-UNITY] → script cena a cena (V1)
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

## Skills existentes

O sistema não parte do zero — as seguintes ferramentas já existem como skills no Claude Code (CCOS-Unity):

| Skill | Repositório | O que faz |
|---|---|---|
| Plataforma / OS | `dobralabs/ccos-unity` | Orquestra skills, contexto persistente de marca, auto-sync GitHub |
| Calendário estratégico | `calendario-comercial` | Janelas comerciais, cultura pop, sazonalidade, timing |
| Geração de carrossel | `duduesh/carrossel-unity` | Texto → imagens GPT → HTML → PNG via Playwright; imagens fotográficas na capa e slides de impacto (máx 3/carrossel) |
| Copy de marca | `duduesh/ogilvy-copy` | Framework Ogilvy — copy de longo prazo, construção de identidade |
| Copy de vendas | `duduesh/schwartz-copy` | Framework Schwartz — copy de conversão por nível de consciência |
| Imagem (default) | `duduesh/gpt-image2-unity` | gpt-image-1 via OpenAI API (key em `credentials/openai_key.txt`); ~$0,02–$0,10/img; latência 60–180s |
| Imagem (fallback) | `duduesh/nanobanana-unity` | Google Gemini — grátis, rápido; entra quando quota do ChatGPT esgota |
| Imagem (contingência) | `duduesh/image-gen-unity` | GPT Image 2 via FAL API — ~$0,06–$0,22/imagem; carrossel até $2,20 |
| Publicação social | `duduesh/publicar-social-unity` | Instagram, TikTok, LinkedIn via Post for Me ou Meta Graph API |
| Triagem YouTube | `duduesh/triagem-youtube-unity` | Score editorial, SEO e títulos otimizados via DataForSEO |

**Status de instalação:** `calendario-comercial` ✅, `briefing-unity` ✅, `schwartz-copy` ✅, `ogilvy-copy` ✅, `carrossel-unity` ✅, `gpt-image2-unity` ✅. Demais skills sendo instaladas por ordem de fluxo — ver [MAPA-TECNICO.md](MAPA-TECNICO.md).

---

## Skills a construir

```
roteiro-unity  ← V1
  Input:  briefing aprovado, plataforma alvo, duração estimada
  Output: roteiro estruturado cena a cena (falas, cortes, orientações de câmera)

coletor-metricas.py  ← V2, Python
  Input:  IDs dos posts, janela de tempo
  Output: registro estruturado no Supabase

analista-performance  ← V3
  Input:  base de posts com métricas (Supabase)
  Output: padrões de melhor performance + contexto para retroalimentar o briefing-unity
```

---

## Stack

| Camada | Tecnologia | Status |
|---|---|---|
| Plataforma / OS | CCOS-Unity (Claude Code local) | ✅ Existe |
| Calendário | `calendario-comercial` skill | ✅ Existe |
| Geração de carrossel | `carrossel-unity` (HTML → PNG via Playwright) | ✅ Existe |
| Copy | `ogilvy-copy` + `schwartz-copy` | ✅ Existe |
| Geração de imagem | `gpt-image2-unity` / `nanobanana-unity` / `image-gen-unity` | ✅ Existe |
| Publicação social | `publicar-social-unity` | ✅ Existe |
| Briefing orchestrator | `briefing-unity` | ✅ Criada — aguarda validação |
| Gates de aprovação | Fluxo conversacional (A/E/C) | ✅ Definidos na skill |
| Roteiro de vídeo | `roteiro-unity` | 🔜 V1 |
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
| **MVP** | ✅ Skills instaladas: `calendario`, `briefing`, `copy`, `carrossel`, `gpt-image2`. Node.js + Playwright + Python + openai SDK prontos. Bloqueante: API key OpenAI em `credentials/`. Próximo: 1ª run real. Validação: 10 conteúdos. |
| **V1** | Deploy remoto (n8n Cloud / VPS) + biblioteca técnica + `roteiro-unity` |
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

Cada empresa do Grupo Unity opera com seu próprio workspace CCOS independente — repositório separado, contexto isolado, credenciais separadas, histórico independente. Rollout gradual: começa na empresa piloto, valida, replica para as demais sem risco de comprometer o que já funciona.

---

*Última atualização: 2026-05-04 — `gpt-image2-unity` instalada (gpt-image-1 via OpenAI API); `carrossel-unity` atualizada para gerar imagens fotográficas nos slides via GPT com fallback Nanobanana. openai SDK 2.33.0 instalado. Falta: API key OpenAI em `credentials/openai_key.txt`.*
