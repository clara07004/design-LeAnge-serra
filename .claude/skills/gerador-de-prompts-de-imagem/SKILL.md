---
name: gerador-de-prompts-de-imagem
description: Cria prompts precisos e estruturados para geração de imagem com IA — thumbnails, capas de carrossel, posts, stories. Melhora diretamente a qualidade das imagens geradas pelo /gpt-image2-unity. Use ANTES de executar o script gerar-imagem.py quando quiser um prompt mais elaborado do que o padrão. Dispara quando: "quero criar uma imagem com IA", "me ajuda a escrever um prompt", "preciso melhorar o prompt dessa imagem".
---

# Gerador de Prompts de Imagem

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — produtos, contexto de uso e posicionamento da empresa
- `marca/DESIGN.md` → seção `image_style` — estilos fotográficos (dark_lifestyle, architectural_installation, product_closeup), paleta
- `_contexto/preferencias.md` — restrições visuais (sem EPI incorreto, sem obras improvisadas)

**Regras fixas para qualquer prompt:**
- Sempre em inglês
- Sempre incluir: `no text overlay`, `no watermarks`, `photorealistic`
- Nunca: obras com EPI incorreto, texto embutido, ilustrações genéricas
- Contexto preferencial: ambiente de uso do produto, arquitetura contemporânea, alto padrão

**Ferramenta alvo:** `gpt-image-1` (OpenAI). Os prompts são otimizados para este modelo.

---

## Diagnóstico inicial

Confirmar antes de gerar:
1. Qual o objetivo da imagem? (capa carrossel, fundo post estático, story, imagem avulsa)
2. O que deve aparecer? (esquadria instalada, detalhe de produto, cena de obra, ambiente interno)
3. Qual a estética? (moody/dark, clean/arquitetônica, close-up técnico)
4. Qual a proporção? (square 1:1, portrait 9:16, landscape 3:2)

---

## Anatomia de um prompt eficaz

```
[SUJEITO] + [AÇÃO/ESTADO] + [AMBIENTE/CONTEXTO] + [ESTILO] + [ILUMINAÇÃO] + [QUALIDADE] + [RESTRIÇÕES]
```

**Exemplos por camada (adaptar ao produto da empresa):**

**Sujeito:** "[produto] in modern apartment", "[produto] installed in contemporary project", "close-up of [produto] technical detail"

**Ambiente/Contexto:** "contemporary Brazilian residence", "high-end construction site", "modern minimal interior with natural light"

**Estilo:** "professional architectural photography", "cinematic still", "editorial architectural photography"

**Iluminação:** "natural daylight flooding through windows", "soft ambient side light", "dramatic golden hour"

**Qualidade:** "ultra detailed", "8k resolution", "photorealistic", "sharp focus"

**Restrições fixas:** "no text overlay, no watermarks, no people, photorealistic"

---

## Prompts por caso de uso

### Capa de Carrossel (portrait 1024×1536)
```
[Cena arquitetônica contemporânea relacionada ao tema do carrossel],
[iluminação natural ou dramática], [composição com área inferior disponível para texto],
professional architectural photography, dark moody atmosphere, high-end residential context,
[produto da empresa se aplicável ao tema],
no text overlay, no watermarks, photorealistic, portrait format
```

### Post Estático — fundo full-bleed (portrait 1024×1536)
```
[Cena concreta do produto ou ambiente de uso],
cinematic professional photography, [iluminação], [enquadramento],
contemporary architecture, premium materials, warm natural tones,
no text overlay, no watermarks, no people (unless specified), photorealistic, portrait format
```

### Imagem de produto instalado
```
[Nome do produto, ex: PVC casement window] installed in [contexto de projeto],
natural daylight from outside, contemporary interior design, minimal decor,
architectural installation photography, wide to mid shot showing full product in context,
warm wood tones and white walls, no text overlay, photorealistic
```

---

## Modificadores por estilo (seção image_style do DESIGN.md)

| Estilo | Modificadores |
|---|---|
| dark_lifestyle | moody, atmospheric, slightly desaturated, ambient natural light, soft side light, people in action |
| architectural_installation | clean, premium, natural light dominant, warm and natural color grade, wide to mid shot |
| product_closeup | macro detail, technical and elegant, neutral color grade, extreme close-up, surface texture |
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
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "[PROMPT]" "conteudo/carrosseis/[periodo]/[dia-tema]/instagram/img-slideXX.png" "[RATIO]"
```
