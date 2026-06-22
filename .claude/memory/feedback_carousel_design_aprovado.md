---
name: feedback-carousel-design-aprovado
description: Padrões CSS/tipográficos aprovados e catálogo de componentes para carrossel — adaptar cores para a empresa configurada.
metadata:
  type: feedback
---

Catálogo de padrões CSS, componentes e estrutura **aprovados** para carrossel. Consultar **antes
de inventar componente novo**. Ao aplicar, substituir `[COR_PRIMÁRIA]` pela cor primária real
de `marca/DESIGN.md`, as fontes pelos nomes reais e a tagline pelo texto da empresa.

**Why:** a empresa constrói identidade visual no feed — o público precisa reconhecer um post
da marca antes de ler o nome. Inventar componente fora do catálogo aprovado quebra esse reconhecimento.

**How to apply:** manter rigorosamente header, gradiente, paleta, escala e componentes aprovados.
Inovação visual nesse nível **não** está autorizada — só no conteúdo (ângulo, narrativa, dado técnico).

---

## Canvas e base (extraído dos HTMLs de junho)

```css
body { width:1080px; height:1350px; overflow:hidden; background:#060a18; }
/* container raiz: position:relative; width:1080px; height:1350px; overflow:hidden; */
/* padding do conteúdo: 64px 80px 72px */
```

## Header padrão (todos os slides)

```html
<div style="display:flex;align-items:center;gap:10px;flex-shrink:0;">
  <img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
  <span style="width:1.5px;height:22px;background:[COR_PRIMÁRIA];margin:0 10px;display:inline-block;"></span>
  <span style="font-family:'Montserrat',sans-serif;font-size:16px;font-weight:700;color:[COR_PRIMÁRIA];letter-spacing:0.14em;text-transform:uppercase;">[TAGLINE]</span>
</div>
```
> Logo no header dos slides de junho = `height:48px`. (O DESIGN.md cita "mínimo 80px digital" —
> divergência real entre regra e prática; usar 48px no header até a Clara decidir. Ver [[feedback-logo-path-html]].)

## Overlay de gradiente para texto na base (mais comum)

```html
<div style="position:absolute;inset:0;background:linear-gradient(to top,
  rgba(6,10,24,0.97) 0%, rgba(6,10,24,0.88) 40%, rgba(6,10,24,0.50) 65%, rgba(6,10,24,0.12) 100%);"></div>
<div style="position:absolute;top:0;left:0;width:100%;height:200px;
  background:linear-gradient(to bottom, rgba(6,10,24,0.72) 0%, transparent 100%);"></div>
```
**Direção do gradiente segue a posição do conteúdo.** Texto na base → bottom→top. Texto à
esquerda → left→right. Nunca overlay sólido cobrindo a imagem.

## Glow blob de profundidade (canto)

```html
<div style="position:absolute;bottom:-60px;left:-60px;width:280px;height:280px;
  border-radius:50%;background:rgba([R_PRIMÁRIA],[G_PRIMÁRIA],[B_PRIMÁRIA],0.18);filter:blur(55px);"></div>
```

## Divider de seção

```html
<div style="width:48px;height:3px;background:[COR_PRIMÁRIA];border-radius:2px;margin-bottom:24px;"></div>
```

## Headline padrão (slide escuro)

```css
font-family:'Poppins'; font-size:88px; font-weight:700; color:#FFFFFF;
line-height:1.06; letter-spacing:-0.022em;
```

## Lista numerada (icon circle + texto)

```html
<div style="display:flex;align-items:flex-start;gap:24px;">
  <div style="width:48px;height:48px;border-radius:50%;background:rgba([R_PRIMÁRIA],[G_PRIMÁRIA],[B_PRIMÁRIA],0.25);
    border:1.5px solid rgba([R_PRIMÁRIA],[G_PRIMÁRIA],[B_PRIMÁRIA],0.55);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:4px;">
    <span style="font-family:'Montserrat';font-size:16px;font-weight:700;color:[COR_PRIMÁRIA];">01</span>
  </div>
  <div style="font-family:'Poppins';font-size:44px;font-weight:400;color:rgba(255,255,255,0.86);line-height:1.40;">Texto do passo.</div>
</div>
```

## Dissolve suave em split foto + texto

```html
<img src="./img-slideXX.png" style="position:absolute;top:0;left:0;width:100%;height:580px;object-fit:cover;">
<div style="position:absolute;top:0;left:0;width:100%;height:580px;
  background:linear-gradient(to bottom, rgba(6,10,24,0.10) 0%, rgba(6,10,24,0.30) 55%, rgba(6,10,24,1.0) 100%);"></div>
```

---

## Catálogo de elementos gráficos (DESIGN.md → graphic_elements)

| Componente | Descrição | Cor |
|---|---|---|
| **Text highlight box** | Retângulo sólido atrás de palavra-chave (nome de linha, spec, prova) | `[COR_PRIMÁRIA]` (fundo claro) / Branco (fundo escuro). Padding 4–8px, quase reto |
| **Hand-drawn loop** | Oval/loop orgânico circundando sujeito ou produto | `[COR_PRIMÁRIA]`, traço fino imperfeito (não geométrico) |
| **White bracket frame** | Colchete decorativo aberto nos cantos do headline | Branco puro |
| **Floating card** | Card branco arredondado flutuante + soft shadow | Radius 16–24px, sombra ambiente suave |
| **Sound wave lines** | 2–3 linhas curvas paralelas flanqueando elemento (acústica/térmica) | Azul ou branco conforme fundo |
| **Icon circle** | Círculo azul cheio com ícone de linha branco | Fill azul `[COR_PRIMÁRIA]`, ícone branco outline |
| **Accent blob** | Forma orgânica aparecendo pelo canto (transição p/ CTA) | `[COR_PRIMÁRIA]`, só a borda aparece |
| **Pill CTA** | Cápsula só com borda (outline), texto pequeno | Branco (fundo escuro) / Azul (fundo claro), radius 9999px |
| **Spec bar** | Barra base com specs técnicos reais do produto | `[Spec1: valor] \| [Spec2: valor] \| [Categoria: nome]` |

---

## Mapa de fotos do Drive testadas

Pasta de fotos: ver ID em `_contexto/referencias.md` → "Fotos do Produto". Priorizar <300KB.

> Preencher este mapa à medida que as fotos forem testadas em carrosseis reais.
> Manter o padrão: tema → ID do arquivo no Drive.

| Tema/Uso | ID do arquivo no Drive |
|---|---|
| [Tema 1 — ex.: Conforto / luz] | `[ID_FOTO]` |
| [Tema 2 — ex.: Especificação] | `[ID_FOTO]` |
| [Tema 3 — ex.: CTA / alto padrão] | `[ID_FOTO]` |
| [Tema 4 — ex.: Fachada] | `[ID_FOTO]` |

> Confirmar que os IDs ainda apontam para a foto certa antes de baixar.
> Baixar via MCP Drive e salvar como `img-slideXX.jpg`.

Relacionados: [[feedback-fonte-mobile]] · [[feedback-logo-path-html]] · [[feedback-proporcoes-imagem]] · [[feedback-design-direcao]]
</content>
