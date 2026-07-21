---
name: gerador-de-prompts-de-imagem
description: Cria prompts precisos e estruturados para geração de imagem com IA — thumbnails, capas de carrossel, posts, stories. Melhora diretamente a qualidade das imagens geradas pelo /gpt-image2-leange. Use ANTES de executar o script gerar-imagem.py quando quiser um prompt mais elaborado do que o padrão. Dispara quando: "quero criar uma imagem com IA", "me ajuda a escrever um prompt", "preciso melhorar o prompt dessa imagem".
---

# Gerador de Prompts de Imagem

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — a pousada, contexto de uso e posicionamento da empresa
- `marca/DESIGN.md` → seção `image_style` — estilos fotográficos (dark_lifestyle, architectural_installation, product_closeup), paleta
- `_contexto/preferencias.md` — restrições visuais e tom de voz

**Regras fixas para qualquer prompt:**
- Sempre em inglês
- Sempre incluir: `no text overlay`, `no watermarks`, `photorealistic`
- Nunca: texto embutido, ilustrações genéricas
- Contexto preferencial: pets soltos e felizes, natureza, aconchego de refúgio, alto padrão acolhedor

**Ferramenta alvo:** `gpt-image-1` (OpenAI). Os prompts são otimizados para este modelo.

---

## Diagnóstico inicial

Confirmar antes de gerar:
1. Qual o objetivo da imagem? (capa carrossel, fundo post estático, story, imagem avulsa)
2. O que deve aparecer? (pet aproveitando os espaços, detalhe da suíte, cena na pousada, ambiente interno)
3. Qual a estética? (lifestyle quente/afetivo, ambiente clean/natural, close-up/detalhe)
4. Qual a proporção? (square 1:1, portrait 9:16, landscape 3:2)

---

## Anatomia de um prompt eficaz

```
[SUJEITO] + [AÇÃO/ESTADO] + [AMBIENTE/CONTEXTO] + [ESTILO] + [ILUMINAÇÃO] + [QUALIDADE] + [RESTRIÇÕES]
```

**Exemplos por camada (adaptar à pousada):**

**Sujeito:** "[pet] in cozy pousada suite", "[pet] in a contemporary pousada setting", "close-up of [pet] detail"

**Ambiente/Contexto:** "cozy Brazilian pousada", "high-end pet-friendly retreat", "modern minimal interior with natural light"

**Estilo:** "professional lifestyle photography", "cinematic still", "editorial travel photography"

**Iluminação:** "natural daylight flooding through windows", "soft ambient side light", "dramatic golden hour"

**Qualidade:** "ultra detailed", "8k resolution", "photorealistic", "sharp focus"

**Restrições fixas:** "no text overlay, no watermarks, no people, photorealistic"

---

## Prompts por caso de uso

### Capa de Carrossel (portrait 1024×1536)
```
[Cena da pousada relacionada ao tema — pet feliz e solto, natureza, suíte, piscina, cachoeira],
natural warm light, golden hour, [composição com área inferior disponível para texto],
professional lifestyle photography, cozy and affectionate atmosphere, pet-friendly inn context,
no text overlay, no watermarks, photorealistic, portrait format
```

### Post Estático — fundo full-bleed (portrait 1024×1536)
```
[Cena concreta da experiência — pet nos espaços, ambiente acolhedor, gastronomia],
cinematic professional photography, [iluminação natural quente], [enquadramento],
cozy pousada interior, warm natural tones, refuge atmosphere,
no text overlay, no watermarks, no people (unless specified), photorealistic, portrait format
```

### Imagem de pet aproveitando os espaços
```
[Cena, ex: happy dog relaxing in the suite] in [contexto da LeAnge Serra],
natural daylight, cozy interior design, warm and welcoming,
lifestyle pet-friendly inn photography, wide to mid shot showing the pet enjoying the space,
warm wood tones and natural light, no text overlay, photorealistic
```

---

## Modificadores por estilo (seção image_style do DESIGN.md)

| Estilo | Modificadores |
|---|---|
| dark_lifestyle | warm, atmospheric, golden hour, natural light, cozy and affectionate, pets and owners in action (never cold or desaturated) |
| architectural_installation | clean, premium, natural light dominant, warm and natural color grade, wide to mid shot, pet enjoying the space |
| product_closeup | macro detail, intimate and elegant, natural warm color grade, extreme close-up (pet's gaze, amenity, plated dish) |
| full_bleed_dark | dark tones, cinematic, dramatic lighting, for cover slides |
| off_white_textured | soft, clean, paper texture, warm off-white background |

---

## Output

```
OBJETIVO DA IMAGEM: [uso]
PROPORÇÃO: [square / portrait / landscape]
ESTILO: [estilo do DESIGN.md]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROMPT PRINCIPAL:
[prompt completo, pronto para usar no script gerar-imagem.py]

VARIAÇÃO A (mais minimalista): [...]
VARIAÇÃO B (mais impactante): [...]

ASPECT RATIO PARA O SCRIPT: [square / portrait / landscape]

COMANDO POWERSHELL (destino = pasta de produção do conteúdo; não existe conteudo/imagens/):
# Carrossel:    conteudo/carrosseis/[periodo]/[dia-tema]/instagram/img-slideXX.png
# Post estático: conteudo/post-estatico/[periodo]/[dia-tema]/img-post.png
python ".claude/skills/gpt-image2-leange/gerar-imagem.py" "[PROMPT]" "conteudo/carrosseis/[periodo]/[dia-tema]/instagram/img-slideXX.png" "[RATIO]"
```
