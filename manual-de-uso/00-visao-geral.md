# O que é este repositório — Visão Geral

## A ideia central

Este repositório é um **sistema operacional de criação de conteúdo**. Ele transforma o Claude Code num produtor de conteúdo configurado para a empresa: lê o contexto do negócio, aplica a identidade visual da marca, gera imagens via IA, monta layouts HTML e entrega posts prontos para publicar no Instagram, TikTok e LinkedIn.

O nome técnico é **CCOS — Claude Code OS**. A analogia é precisa: assim como um sistema operacional orquestra programas e recursos de hardware, o CCOS orquestra skills de IA, APIs externas e arquivos de contexto para produzir conteúdo.

---

## Como o sistema funciona

O Claude Code lê arquivos Markdown como se fossem instruções de comportamento. Quando você abre uma conversa neste diretório, o Claude automaticamente lê:

- `CLAUDE.md` — regras gerais de comportamento (o "manual interno" do sistema)
- `_contexto/empresa.md` — quem é a empresa, o que vende, para quem
- `_contexto/preferencias.md` — como a marca fala, o que evitar
- `_contexto/estrategia.md` — foco atual, prioridades do período
- `_contexto/referencias.md` — onde estão as referências visuais no Google Drive

Tudo isso acontece em silêncio. O Claude não anuncia que leu. Ele simplesmente aplica esse conhecimento em cada resposta e decisão.

---

## A diferença entre skills e motores

O sistema tem dois tipos de componentes:

**Skills de produção** — o que você chama diretamente. São 19 skills organizadas em grupos:

*Ideação e pesquisa:*
- `/gerador-de-angulos-para-um-tema` — 10 lentes criativas para um tema
- `/gerador-de-angulos-de-conteudo` — ângulos segmentados por audiência
- `/banco-de-objecoes-do-avatar` — mapa de objeções do ICP com respostas em conteúdo

*Planejamento:*
- `/calendario-comercial` — define o que e quando postar no mês
- `/briefing-unity` — briefing completo de um post específico

*Hooks e capas:*
- `/hooks-para-carrossel` — 5 opções de capa para carrossel
- `/hooks-para-instagram-reels` — 7 opções de hook para Reel

*Produção de conteúdo:*
- `/carrossel-unity` — carrossel completo (texto + imagens + PNGs)
- `/carrossel-de-quebra-de-objecao` — carrossel de conversão que desmonta uma objeção
- `/estatico-unity` — post estático (card único)
- `/roteiro-unity` — roteiro de vídeo para Reels/TikTok

*Legendas:*
- `/legenda-para-carrossel` — legenda orientada a saves
- `/legenda-para-reel` — legenda que complementa o vídeo
- `/legenda-para-post-estatico` — legenda para post estático (4 tipos)

*Imagem:*
- `/gerador-de-prompts-de-imagem` — prompt otimizado para gpt-image-1
- `/gerador-de-prompts-para-imagens-de-produto` — prompts para os estilos fotográficos de produto

*Distribuição:*
- `/1-conteudo-em-7-formatos` — adapta 1 conteúdo para 7 canais

**Motores** — componentes internos chamados pelas skills de produção. Você raramente os chama diretamente:
- `/gpt-image2-unity` — gera imagens via OpenAI (gpt-image-1)
- `/nanobanana-unity` — gera imagens via Gemini (fallback gratuito)
- `/image-gen-unity` — gera imagens via FAL API (fallback pago)
- `/ogilvy-copy` — escreve copy de marca e autoridade
- `/schwartz-copy` — escreve copy de resposta direta (conversão)

A analogia: skills são os programas que você abre. Motores são as bibliotecas que esses programas chamam internamente.

---

## O princípio de aprovação humana

O sistema foi projetado com uma regra central: **nenhum asset caro é produzido sem aprovação humana explícita**.

Isso existe por um motivo prático: gerar uma imagem via OpenAI custa crédito. Renderizar um carrossel de 10 slides leva 10-15 minutos. Se o briefing ou o prompt estiverem errados, esse tempo e dinheiro são desperdiçados.

Por isso, todo fluxo tem **checkpoints obrigatórios** onde o sistema para, mostra o que vai fazer e aguarda sua confirmação antes de avançar. Você nunca é surpreendido por uma cobrança ou resultado que não aprovou.

```
[Claude gera o calendário]
          ↓
    VOCÊ APROVA
          ↓
[Claude gera o briefing]
          ↓
    VOCÊ APROVA
          ↓
[Claude mostra o prompt da imagem]
          ↓
    VOCÊ APROVA
          ↓
[Claude gera a imagem — só aqui gasta crédito]
          ↓
[Claude monta o HTML e renderiza]
          ↓
    VOCÊ APROVA
          ↓
[Post salvo e pronto para publicar]
```

---

## O que o sistema produz

No final de cada fluxo, os arquivos ficam salvos em `conteudo/`:

```
conteudo/
  calendarios/         ← calendários mensais aprovados
  briefings/           ← briefings aprovados
  carrosseis/          ← carrosséis: texto + HTMLs + PNGs
  imagens/             ← posts estáticos: foto + HTML + PNG
```

Os arquivos PNG em `conteudo/` são os arquivos finais — prontos para subir no Instagram, TikTok ou LinkedIn.

---

## Pré-requisitos para o sistema funcionar

1. **Python 3.x instalado** — para o script de geração de imagem
2. **Node.js instalado** — para o Playwright (renderização de HTML em PNG)
3. **API Key da OpenAI** — para geração de imagens (custo ~$0,02-$0,10 por imagem)
4. **Arquivos de contexto configurados** — `_contexto/empresa.md`, `preferencias.md`, `estrategia.md`
5. **DESIGN.md configurado** — `marca/DESIGN.md` com `status: configured`

Se algum desses itens estiver faltando, o sistema avisa antes de tentar executar.

---

## Onde fica cada tipo de informação

| O que você precisa saber | Onde está |
|---|---|
| Contexto da empresa | `_contexto/empresa.md` |
| Tom de voz e restrições | `_contexto/preferencias.md` |
| Foco atual e estratégia | `_contexto/estrategia.md` |
| Pastas do Google Drive | `_contexto/referencias.md` |
| Identidade visual completa | `marca/DESIGN.md` |
| Regras do sistema | `CLAUDE.md` |
| Credenciais de API | `credentials/` |
| Conteúdo gerado | `conteudo/` |
| Skills disponíveis | `.claude/skills/` |
