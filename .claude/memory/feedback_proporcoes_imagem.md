---
name: feedback-proporcoes-imagem
description: Proporções de imagem por tipo de slide e relação com o canvas 1080×1350.
metadata:
  type: feedback
---

Proporção da imagem gerada por tipo de slide.

**Why:** imagem na proporção errada distorce ou corta mal no canvas do slide.

**How to apply:**

**Canvas final = SEMPRE 1080×1350** (4:5 retrato), tamanho exato do feed Instagram — capa, slides
internos e post estático. Isso é inegociável e independe da imagem de fundo.

**Imagem de fundo gerada por IA = SEMPRE `portrait` (1024×1536)** — capa e internos. Erro comum
(já corrigido nos docs): gerar a capa como `square` (1024×1024). Foto quadrada num canvas retrato
encaixa mal e força tentativas de "ajustar/diminuir" que cortam ou sobrepõem texto.

A imagem `portrait` 1024×1536 (2:3) é mais alta que o canvas 4:5, então `object-fit:cover` corta
um pouco do topo/base — esperado, preenche sem deformar. Posicionar via `object-position` quando o
assunto não estiver centrado.

**Render:** `--viewport-size=1080,1350` **sem** `--full-page` → PNG exatamente 1080×1350. Validar
com `validar-dimensao.py`. Nunca esticar (`object-fit:fill`) nem deixar barra vazia.
Ver [[feedback-fonte-mobile]].
</content>
