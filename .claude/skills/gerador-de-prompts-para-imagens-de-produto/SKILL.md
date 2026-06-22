---
name: gerador-de-prompts-para-imagens-de-produto
description: Gera prompts especializados para imagens do produto principal da empresa — produto instalado em contexto de uso, mockups, ambientação, close-up de detalhes técnicos. Complemento direto do /gpt-image2-unity focado em fotografia de produto. Dispara quando: "quero imagem do produto", "prompt para foto de produto", "imagem de produto com IA", "foto do produto instalado".
---

# Gerador de Prompts para Imagens de Produto

## Contexto

Antes de gerar, ler:
- `_contexto/empresa.md` — o que é o produto, linhas/variantes, contextos de uso, ICP
- `marca/DESIGN.md` → seção `image_style.photography` — os estilos fotográficos da marca
- `_contexto/referencias.md` → pasta "Fotos do Produto" no Drive para referência de estilo real

**Produto:** conforme `_contexto/empresa.md`. Nunca inventar características — usar só o que está documentado.

---

## Coleta de Informações

**Obrigatório:**
- `[LINHA/VARIANTE]` — qual linha ou versão do produto aparece na cena
- `[TIPO DE CENA]` — produto instalado / detalhe técnico / ambiente de uso / obra/processo
- `[USO DA IMAGEM]` — capa carrossel / post estático / story / material técnico
- `[ESTILO]` — conforme `image_style.photography` no DESIGN.md (estilo_foto_1 / estilo_foto_2 / estilo_foto_3)

**Opcional:**
- `[AMBIENTE]` — tipo de espaço, contexto de uso, perfil de projeto
- `[PESSOAS]` — sem pessoas (padrão) / usuário do produto / profissional em operação

---

## Os 3 Estilos de Foto (do DESIGN.md)

Ler `marca/DESIGN.md` → `image_style.photography` e usar as descrições configuradas para cada estilo.
Os exemplos abaixo são placeholders — substituir pelo conteúdo real ao configurar a empresa.

### [estilo_foto_1] — ex.: dark_lifestyle
[Conforme configurado em DESIGN.md. Descrever: pessoas em ação no ambiente de uso, mood atmosférico.]

### [estilo_foto_2] — ex.: architectural_installation
[Conforme configurado em DESIGN.md. Descrever: produto instalado em projeto acabado, luz natural, clean e premium.]

### [estilo_foto_3] — ex.: product_closeup
[Conforme configurado em DESIGN.md. Descrever: macro/detalhe da superfície e estrutura do produto, foco técnico.]

---

## Templates de Prompt por Estilo

### [estilo_foto_2] — produto instalado (mais usado)
```
[DESCRIÇÃO DO PRODUTO, ex: high-performance product] installed in
[AMBIENTE, ex: modern high-end residence],
natural daylight, contemporary minimal interior, clean lines, no clutter,
professional architectural photography, wide to mid shot showing full product in context,
no text overlay, no watermarks, no people, photorealistic, portrait format
```

### [estilo_foto_1] — lifestyle
```
[SUJEITO, ex: professional reviewing] in front of
[PRODUTO] in [AMBIENTE],
moody atmospheric lighting, soft ambient side light, slightly desaturated tones,
candid or near-candid pose, environmental context visible,
professional lifestyle photography, no text overlay, photorealistic, portrait format
```

### [estilo_foto_3] — close-up técnico
```
extreme close-up of [DETALHE, ex: product cross-section showing internal structure],
[DETALHE TÉCNICO — ex.: material layers, sealing detail, joint],
neutral color grade true to product, technical and elegant simultaneously,
macro photography, sharp focus, studio lighting, white or neutral background,
no text overlay, photorealistic
```

---

## Output

```
PRODUTO: [linha/variante e tipo]
ESTILO: [nome do estilo conforme DESIGN.md]
USO: [onde vai ser usada]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROMPT PRINCIPAL:
[prompt completo otimizado para gpt-image-1]

VARIAÇÃO (ângulo diferente): [prompt alternativo]

ASPECT RATIO: [square / portrait / landscape]

COMANDO POWERSHELL (destino = pasta de produção do conteúdo):
# Carrossel:      conteudo/carrosseis/[periodo]/[dia-tema]/instagram/img-slideXX.png
# Post estático:  conteudo/post-estatico/[periodo]/[dia-tema]/img-post.png
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "[PROMPT]" "conteudo/post-estatico/[periodo]/[dia-tema]/img-post.png" "[RATIO]"

DICAS ESPECÍFICAS:
[O que ajustar se o resultado não estiver no nível esperado]
```
