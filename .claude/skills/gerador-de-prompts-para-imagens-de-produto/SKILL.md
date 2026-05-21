---
name: gerador-de-prompts-para-imagens-de-produto
description: Gera prompts especializados para imagens do produto Ecoframe — esquadrias PVC instaladas em contexto arquitetônico, mockups, ambientação, close-up de detalhes técnicos. Complemento direto do /gpt-image2-unity focado em fotografia de produto. Dispara quando: "quero imagem do produto", "prompt para foto de esquadria", "imagem de produto com IA", "foto de janela PVC instalada".
---

# Gerador de Prompts para Imagens de Produto Ecoframe

## Contexto

Antes de gerar, ler:
- `_contexto/empresa.md` — linhas de produto (iTEC, euroTEC, TECplus100, MAXXI), contextos de uso
- `marca/DESIGN.md` → seção `image_style.photography` — os três estilos de foto da marca
- `_contexto/referencias.md` → pasta "Fotos do Produto" no Drive para referência de estilo real

**Produto Ecoframe:** esquadrias em PVC de alta performance para obras em Steel Frame, Drywall e arquitetura contemporânea. Linhas: iTEC, euroTEC, TECplus100, MAXXI (fornecedor Primeira Linha).

---

## Coleta de Informações

**Obrigatório:**
- `[LINHA DE PRODUTO]` — iTEC / euroTEC / TECplus100 / MAXXI / genérico PVC
- `[TIPO DE CENA]` — produto instalado / detalhe técnico / ambiente de uso / obra em andamento
- `[USO DA IMAGEM]` — capa carrossel / post estático / story / material técnico
- `[ESTILO]` — architectural_installation / dark_lifestyle / product_closeup

**Opcional:**
- `[AMBIENTE]` — residencial alto padrão / comercial / Steel Frame em construção / interior moderno
- `[PESSOAS]` — sem pessoas (padrão) / arquiteto revisando / proprietário apreciando

---

## Os 3 Estilos de Foto da Ecoframe (do DESIGN.md)

### dark_lifestyle
Pessoas em ação no ambiente de uso do produto.
- Mood: moody, atmosférico, slightly desaturated
- Iluminação: ambient natural, soft side light
- Sujeitos: arquiteto revisando projeto em obra de Steel Frame, construtora instalando esquadrias, proprietário apreciando janelas prontas
- Enquadramento: often cropped tight, subject off-center, environmental context visible

### architectural_installation
Foto real do produto instalado em projeto acabado.
- Mood: clean, premium, natural light dominant
- Iluminação: bright window light, natural diffuse
- Foco: fachada acabada com esquadrias de PVC, interior com janelas instaladas, detalhe de canto e perfil
- Enquadramento: wide to mid shot — mostra o ambiente completo com produto integrado

### product_closeup
Macro/detalhe da superfície e estrutura do produto.
- Mood: técnico e elegante simultaneamente
- Foco: seção transversal perfil PVC mostrando câmaras internas, detalhe do sistema de vedação, textura superficial do PVC
- Enquadramento: close-up extremo

---

## Templates de Prompt por Estilo

### architectural_installation (mais usado)
```
[LINHA DE PRODUTO, ex: high-performance PVC casement windows] installed in 
[AMBIENTE, ex: modern Brazilian high-end residence, steel frame construction], 
natural daylight flooding in from outside, contemporary minimal interior design,
warm wood tones, white walls, clean lines, no clutter,
professional architectural photography, wide to mid shot showing full product in context,
no text overlay, no watermarks, no people, photorealistic, portrait format
```

### dark_lifestyle
```
[SUJEITO, ex: architect reviewing construction plans] in front of 
[PRODUTO, ex: floor-to-ceiling PVC windows] in [AMBIENTE, ex: modern apartment under construction],
moody atmospheric lighting, soft ambient side light, slightly desaturated tones,
candid or near-candid pose, environmental context visible, 
professional lifestyle photography, no text overlay, photorealistic, portrait format
```

### product_closeup
```
extreme close-up of [DETALHE, ex: PVC window frame cross-section showing multi-chamber profile],
[DETALHE TÉCNICO, ex: internal chambers, weatherstrip detail, corner joint],
neutral color grade true to product, technical and elegant simultaneously,
macro photography, sharp focus, studio lighting, white background or neutral surface,
no text overlay, photorealistic
```

---

## Output

```
PRODUTO: [linha e tipo]
ESTILO: [architectural_installation / dark_lifestyle / product_closeup]
USO: [onde vai ser usada]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROMPT PRINCIPAL:
[prompt completo otimizado para gpt-image-1]

VARIAÇÃO (ângulo diferente): [prompt alternativo]

ASPECT RATIO: [square / portrait / landscape]

COMANDO POWERSHELL:
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "[PROMPT]" "conteudo/imagens/[TEMA]/foto-produto.png" "[RATIO]"

DICAS ESPECÍFICAS:
[O que ajustar se o resultado não estiver no nível esperado]
```
