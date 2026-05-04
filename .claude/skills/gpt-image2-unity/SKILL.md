---
name: gpt-image2-unity
description: >
  Geração de imagens via GPT Image 2 (gpt-image-1 da OpenAI) para conteúdo da Unity.
  Default do fluxo de geração de imagem — usa API key OpenAI.
  Use quando o usuário pedir uma imagem, foto, visual ou arte para post,
  ou quando o briefing-unity recomendar formato "imagem".
  Fallback: nanobanana-unity (Gemini, grátis). Contingência: image-gen-unity (FAL API, pago).
---

# /gpt-image2-unity — Geração de Imagem com GPT Image 2

## Dependências

- **Python:** 3.x instalado
- **openai SDK:** `python -m pip install openai` (já instalado)
- **API Key OpenAI:** `credentials/openai_key.txt` ou variável `OPENAI_API_KEY`
- **Script:** `.claude/skills/gpt-image2-unity/gerar-imagem.py`
- **Contexto:** `_contexto/empresa.md`, `_contexto/preferencias.md`
- **Design:** `marca/design-guide.md`

---

## Setup (primeira vez)

1. Acessar [platform.openai.com](https://platform.openai.com) → API Keys → Create new key
2. Salvar em `credentials/openai_key.txt` (nunca commitar — já no .gitignore)
3. Créditos mínimos: ~$1 cobre dezenas de imagens em qualidade standard

---

## Input

O usuário fornece (pelo menos um):
- Descrição do que precisa: produto, cena, ambiente, emoção
- Contexto: plataforma destino (Instagram feed, story, TikTok, LinkedIn)
- Referência de estilo (opcional): foto, cor, mood
- Briefing aprovado (se vier do fluxo /briefing-unity)

---

## Workflow

### Fase 1 — Construir o prompt

1. Ler `_contexto/empresa.md` para entender o contexto (construção a seco / drywall / steel frame)
2. Ler `_contexto/preferencias.md` para tom de voz e restrições visuais
3. Ler `marca/design-guide.md` para cores, estilo e elementos obrigatórios

4. Construir um prompt em inglês otimizado para gpt-image-1:
   - Descrever a cena principal com detalhes visuais concretos
   - Incluir estilo fotográfico: `professional photography`, `architectural photography`, etc.
   - Incluir iluminação, ambiente, enquadramento
   - Incluir restrições: `no text overlay`, `no watermarks`, `clean background`
   - Restrição da empresa: sem imagens de obras com EPI incorreto
   - Manter coerência com a identidade visual (cores do design guide se relevante)

5. Definir o aspect ratio conforme a plataforma:
   - Instagram feed (1:1): `square` → 1024×1024
   - Instagram/TikTok story ou reels (9:16): `portrait` → 1024×1536
   - LinkedIn capa ou banner (3:2 landscape): `landscape` → 1536×1024

6. **CHECKPOINT:** Mostrar o prompt proposto ao usuário antes de gerar.
   Aguardar confirmação ou ajustes.

---

### Fase 2 — Gerar a imagem

Definir o caminho de saída:
```
conteudo/imagens/[tema]/imagem-01.png
```

Executar via PowerShell:
```powershell
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT_AQUI" "conteudo/imagens/TEMA/imagem-01.png" "ASPECT_RATIO"
```

- Latência esperada: 60-180 segundos — informar o usuário antes de executar
- Se o script retornar erro de API key (exit code 2): guiar o usuário no setup
- Se o script retornar outro erro (exit code 4): checar o prompt (sem conteúdo proibido)

---

### Fase 3 — Entregar e revisar

1. Mostrar a imagem gerada ao usuário
2. Perguntar: "Ficou bom? Se quiser ajustar, posso refinar o prompt e gerar de novo."
3. Se aprovado: confirmar o caminho do arquivo salvo
4. Se rejeitado: coletar feedback, ajustar o prompt, gerar novamente

---

## Fallback

Se a geração falhar (quota, erro de API, indisponibilidade):

```
gpt-image2-unity FALHOU → tentar nanobanana-unity (Gemini, grátis)
nanobanana-unity FALHOU → tentar image-gen-unity (FAL API, pago — confirmar com usuário antes)
```

Avisar o usuário antes de acionar o fallback e perguntar se quer continuar.

---

## Output

```
conteudo/imagens/[tema]/
  imagem-01.png       ← PNG gerado (1024×1024, 1024×1536 ou 1536×1024)
  prompt.txt          ← prompt usado (salvar para referência futura)
```

Salvar o prompt usado em `prompt.txt` na mesma pasta — serve como referência para variações.

---

## Regras

- Sempre mostrar o prompt pro usuário antes de gerar (evita desperdício de crédito)
- Nunca gerar imagens com pessoas sem EPI em obras (restrição da empresa)
- Nunca gerar imagens com texto embutido (fica pixelado, texto vai no carrossel/overlay)
- Preferir cenas reais e fotográficas para construção a seco — evitar ilustrações genéricas
- Salvar sempre o prompt usado para facilitar variações
- Custo aproximado por imagem: $0.02-$0.10 (quality: high) — informar se o usuário perguntar
