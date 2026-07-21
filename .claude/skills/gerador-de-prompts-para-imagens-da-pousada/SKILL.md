---
name: gerador-de-prompts-para-imagens-da-pousada
description: Gera prompts especializados para imagens da experiência da pousada — pets aproveitando os espaços, suítes, gastronomia, natureza, ambientação e close-up de detalhes. Complemento direto do /gpt-image2-leange focado em fotografia da pousada. Dispara quando: "quero imagem da pousada", "prompt para foto do espaço", "imagem do pet na pousada com IA", "foto da suíte".
---

# Gerador de Prompts para Imagens de Produto

## Contexto

Antes de gerar, ler:
- `_contexto/empresa.md` — o que é a pousada, unidades/experiências, contextos de uso, ICP
- `marca/DESIGN.md` → seção `image_style.photography` — os estilos fotográficos da marca
- `_contexto/referencias.md` → pasta "Fotos da Pousada" no Drive para referência de estilo real

**Pousada:** conforme `_contexto/empresa.md`. Nunca inventar características — usar só o que está documentado.

---

## Coleta de Informações

**Obrigatório:**
- `[EXPERIÊNCIA/ESPAÇO]` — qual experiência ou espaço da LeAnge Serra aparece na cena
- `[TIPO DE CENA]` — pet aproveitando os espaços / detalhe da suíte / ambiente de uso / cena na pousada
- `[USO DA IMAGEM]` — capa carrossel / post estático / story / material da pousada
- `[ESTILO]` — conforme `image_style.photography` no DESIGN.md (estilo_foto_1 / estilo_foto_2 / estilo_foto_3)

**Opcional:**
- `[AMBIENTE]` — tipo de espaço, contexto de uso, perfil da estadia
- `[PESSOAS]` — sem pessoas (padrão) / hóspede com o pet / equipe da pousada

---

## Os 3 Estilos de Foto (do DESIGN.md)

Ler `marca/DESIGN.md` → `image_style.photography` e usar as descrições configuradas para cada estilo.
Os exemplos abaixo são placeholders — substituir pelo conteúdo real ao configurar a empresa.

### [estilo_foto_1] — ex.: dark_lifestyle
[Conforme configurado em DESIGN.md. Descrever: pessoas em ação no ambiente de uso, mood atmosférico.]

### [estilo_foto_2] — ex.: architectural_installation
[Conforme configurado em DESIGN.md. Descrever: pet aproveitando os espaços da pousada, luz natural, clean e premium.]

### [estilo_foto_3] — ex.: product_closeup
[Conforme configurado em DESIGN.md. Descrever: macro/detalhe de um ambiente ou objeto da pousada, foco no detalhe.]

---

## Templates de Prompt por Estilo

### [estilo_foto_2] — pet nos espaços da pousada (mais usado)
```
[DESCRIÇÃO DA CENA, ex: pet relaxando] in
[AMBIENTE, ex: cozy high-end pousada suite],
natural daylight, contemporary minimal interior, clean lines, no clutter,
professional lifestyle photography, wide to mid shot showing the space in context,
no text overlay, no watermarks, no people, photorealistic, portrait format
```

### [estilo_foto_1] — lifestyle
```
[SUJEITO, ex: guest relaxing with a dog] in
[AMBIENTE, ex: pousada lounge],
moody atmospheric lighting, soft ambient side light, slightly desaturated tones,
candid or near-candid pose, environmental context visible,
professional lifestyle photography, no text overlay, photorealistic, portrait format
```

### [estilo_foto_3] — close-up de detalhe
```
extreme close-up of [DETALHE, ex: cozy suite decor detail],
[DETALHE — ex.: texture, materials, warm cozy details],
neutral color grade, warm and elegant simultaneously,
macro photography, sharp focus, studio lighting, white or neutral background,
no text overlay, photorealistic
```

---

## Output

```
EXPERIÊNCIA: [unidade/experiência e tipo de cena]
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
python ".claude/skills/gpt-image2-leange/gerar-imagem.py" "[PROMPT]" "conteudo/post-estatico/[periodo]/[dia-tema]/img-post.png" "[RATIO]"

DICAS ESPECÍFICAS:
[O que ajustar se o resultado não estiver no nível esperado]
```
