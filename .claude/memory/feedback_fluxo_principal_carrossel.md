---
name: feedback-fluxo-principal-carrossel
description: Sequência de produção de carrossel confirmada — imagens aprovadas antes da montagem.
metadata:
  type: feedback
---

Fluxo confirmado de carrossel: gerar e aprovar as imagens **antes** de entrar no `/carrossel-leange`.

**Why:** o usuário prefere controle granular — aprovar cada foto antes da montagem. O fluxo
rápido (geração de imagem dentro do `/carrossel-leange`) tira esse controle.

**How to apply:**

```
/briefing-leange
    ↓ [aprovado]
/gerador-de-prompts-de-imagem   ← prompts para capa + todos os slides com foto
    ↓ [prompts aprovados]
/gpt-image2-leange               ← gera todas as imagens ANTES do carrossel-leange
    ↓ [imagens aprovadas]
/carrossel-leange                ← recebe imagens prontas, monta HTMLs + renderiza
    ↓ [slides aprovados]
/legenda-para-carrossel
```

**Não propor o fluxo rápido por padrão.**

**Fluxos alternativos válidos:**
- Post estático: `/gerador-de-prompts-para-imagens-da-pousada` → `/gpt-image2-leange` → `/estatico-leange` → `/legenda-para-post-estatico`
- Vídeo: `/hooks-para-instagram-reels` → `/roteiro-leange` → `/legenda-para-reel`
- Fundo de funil: `/banco-de-objecoes-do-avatar` → `/carrossel-de-quebra-de-objecao` → `/carrossel-leange` → `/legenda-para-carrossel`
- Repurposing: `/1-conteudo-em-7-formatos` após conteúdo aprovado

**Aprovação humana obrigatória em cada etapa.** Nunca avançar de fase, nunca salvar `_aprovado.md`,
nunca disparar `gerar-imagem.py` ou skill de produção sem comando explícito do usuário. Só usar o fluxo rápido se o usuário pedir explicitamente.
</content>
