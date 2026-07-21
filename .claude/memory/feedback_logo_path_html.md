---
name: feedback-logo-path-html
description: Caminho correto do logo nos HTMLs de carrossel (5 níveis) e versão por fundo.
metadata:
  type: feedback
---

Logo presente em **todo slide, sem exceção**. Slide sem logo = slide rejeitado.

**Why:** identidade de marca constante no feed. Path errado faz o logo não renderizar (imagem
quebrada) na hora do Playwright gerar o PNG.

**How to apply:**

Para HTMLs em `conteudo/carrosseis/*/instagram/`, o path correto tem **5 níveis** de `../`:

```html
<img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
```

Contagem: `instagram/` → dia → mês → carrosseis → conteudo → raiz (onde está `marca/`).
**4 níveis (`../../../../marca/...`) aponta para `conteudo/marca/`, que não existe → logo quebra.**

- Slide escuro (foto + gradiente): `logo-branco.png`
- Fundo claro (off-white): `logo-cor.png`

**Path por tipo de conteúdo (a contagem muda com a profundidade da pasta):**
- Carrossel — HTML em `conteudo/carrosseis/[periodo]/[dia]/instagram/` → **5 níveis** `../`
- Post estático — HTML em `conteudo/post-estatico/[periodo]/[dia]/` → **4 níveis** `../`
- Dashboard de calendário — em `conteudo/calendarios/[periodo]/` → **3 níveis** `../`

**Tamanho do logo (padrão de fato levantado nos HTMLs):**
- Slides internos: **48px** é o valor dos carrosséis mais recentes e consistentes (julho dia-01,
  junho dia-04 e dia-05). Os mais antigos (dia-02, dia-03) usam 40–44px → usar **48px** daqui pra frente.
- Slide CTA final (T7): logo maior para presença de branding. **Padrão recomendado: 64px**
  (intermediário; o 90px do dia-05 ficou grande demais, o 52px do dia-02 ficou tímido). Aplicar
  em CTAs novos — os HTMLs já renderizados não foram alterados.
- Post estático: 48px.

**Divergência com o DESIGN.md:** ele diz "logo mínimo 80px digital" — provavelmente referente à
versão vertical principal da marca em outros contextos, não à altura no header dos slides
(onde a prática é 48px). A Clara decide se reconcilia o número no DESIGN.md.
</content>
