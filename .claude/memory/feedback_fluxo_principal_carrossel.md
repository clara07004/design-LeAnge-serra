---
name: feedback-fluxo-principal-carrossel
description: Sequência de produção de carrossel confirmada — imagens aprovadas antes da montagem.
metadata:
  type: feedback
---

Fluxo confirmado de carrossel: gerar e aprovar as imagens **antes** de entrar no `/carrossel-unity`.

**Why:** o usuário prefere controle granular — aprovar cada foto antes da montagem. O fluxo
rápido (geração de imagem dentro do `/carrossel-unity`) tira esse controle.

**How to apply:**

```
/briefing-unity
    ↓ [aprovado]
/gerador-de-prompts-de-imagem   ← prompts para capa + todos os slides com foto
    ↓ [prompts aprovados]
/gpt-image2-unity               ← gera todas as imagens ANTES do carrossel-unity
    ↓ [imagens aprovadas]
/carrossel-unity                ← recebe imagens prontas, monta HTMLs + renderiza
    ↓ [slides aprovados]
/legenda-para-carrossel
```

**Não propor o fluxo rápido por padrão.**

**Fluxos alternativos válidos:**
- Post estático: `/gerador-de-prompts-para-imagens-de-produto` → `/gpt-image2-unity` → `/estatico-unity` → `/legenda-para-post-estatico`
- Vídeo: `/hooks-para-instagram-reels` → `/roteiro-unity` → `/legenda-para-reel`
- Fundo de funil: `/banco-de-objecoes-do-avatar` → `/carrossel-de-quebra-de-objecao` → `/carrossel-unity` → `/legenda-para-carrossel`
- Repurposing: `/1-conteudo-em-7-formatos` após conteúdo aprovado

**Aprovação humana obrigatória em cada etapa.** Nunca avançar de fase, nunca salvar `_aprovado.md`,
nunca disparar `gerar-imagem.py` ou skill de produção sem comando explícito do usuário. Só usar o fluxo rápido se o usuário pedir explicitamente.
</content>
