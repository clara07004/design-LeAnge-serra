---
name: gpt-image2-leange
description: >
  Geração de imagens via GPT Image 2 (gpt-image-1 da OpenAI) para conteúdo da LeAnge.
  Default do fluxo de geração de imagem — usa API key OpenAI.
  Use quando o usuário pedir uma imagem, foto, visual ou arte para post,
  ou quando o briefing-leange recomendar formato "imagem".
  Fallback: nanobanana-leange (Gemini, grátis). Contingência: image-gen-leange (FAL API, pago).
---

# /gpt-image2-leange — Geração de Imagem com GPT Image 2

## Dependências

- **Python:** 3.x instalado
- **openai SDK:** `python -m pip install openai` (já instalado)
- **API Key OpenAI:** `credentials/openai_key.txt` ou variável `OPENAI_API_KEY`
- **Script:** `.claude/skills/gpt-image2-leange/gerar-imagem.py`
- **Contexto:** `_contexto/empresa.md`, `_contexto/preferencias.md`
- **Design:** `marca/DESIGN.md`

---

## Setup (primeira vez)

1. Acessar [platform.openai.com](https://platform.openai.com) → API Keys → Create new key
2. Salvar em `credentials/openai_key.txt` (nunca commitar — já no .gitignore)
3. Créditos mínimos: ~$1 cobre dezenas de imagens em qualidade standard

---

## Input

O usuário fornece (pelo menos um):
- Descrição do que precisa: cena, ambiente, pet, emoção
- Contexto: plataforma destino (Instagram feed, story, TikTok, LinkedIn)
- Referência de estilo (opcional): foto, cor, mood
- Briefing aprovado (se vier do fluxo /briefing-leange)

---

## Workflow

### Fase 1 — Construir o prompt

1. Ler `_contexto/empresa.md` para entender o contexto (pousada pet lover LeAnge Serra — Miguel Pereira)
2. Ler `_contexto/preferencias.md` para tom de voz e restrições visuais
3. Ler `marca/DESIGN.md` para cores, estilo e elementos obrigatórios. Se `status: not-configured` ou algum campo obrigatório estiver `""`, interromper:
   > ⚠️ O DESIGN.md ainda não foi configurado com a identidade visual da empresa. Para continuar, rode `/setup`.

4. Construir um prompt em inglês otimizado para gpt-image-1:
   - Descrever a cena principal com detalhes visuais concretos
   - Incluir estilo fotográfico: `professional photography`, `lifestyle photography`, etc.
   - Incluir iluminação, ambiente, enquadramento
   - Incluir restrições: `no text overlay`, `no watermarks`, `clean background`
   - Manter coerência com a identidade visual (cores do design guide se relevante)

5. Definir o aspect ratio conforme o **canvas final** do conteúdo (não a "plataforma" genérica):
   - Carrossel e post estático Instagram (canvas 1080×1350, 4:5 retrato): `portrait` → 1024×1536
   - Story / Reels (9:16): `portrait` → 1024×1536
   - LinkedIn banner (3:2 landscape): `landscape` → 1536×1024
   - `square` (1024×1024) **só** se o canvas final for realmente 1:1 — nunca para carrossel/post (são 4:5)

6. **CHECKPOINT:** Mostrar o prompt proposto ao usuário antes de gerar.
   Aguardar confirmação ou ajustes.

---

### Fase 2 — Gerar a imagem

O caminho de saída é a **pasta de produção do conteúdo** que chamou este motor (a skill
chamadora informa). Não existe pasta `conteudo/imagens/` — a imagem vai direto para a pasta final:
- Carrossel: `conteudo/carrosseis/[periodo]/[dia-tema]/instagram/img-slideXX.png`
- Post estático: `conteudo/post-estatico/[periodo]/[dia-tema]/img-post.png`

Executar via PowerShell:
```powershell
python ".claude/skills/gpt-image2-leange/gerar-imagem.py" "PROMPT_AQUI" "conteudo/carrosseis/PERIODO/DIA/instagram/img-slide01.png" "ASPECT_RATIO"
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
gpt-image2-leange FALHOU → tentar nanobanana-leange (Gemini, grátis)
nanobanana-leange FALHOU → tentar image-gen-leange (FAL API, pago — confirmar com usuário antes)
```

Avisar o usuário antes de acionar o fallback e perguntar se quer continuar.

---

## Output

```
conteudo/[tipo]/[periodo]/[dia-tema]/    ← pasta de produção do conteúdo (definida pela skill chamadora)
  img-slideXX.png / img-post.png         ← PNG gerado (1024×1024, 1024×1536 ou 1536×1024)
```

Salvar o prompt usado na própria pasta do conteúdo (`_prompts-imagens.md` no carrossel,
`_prompt.md` no post estático) — serve como referência para variações.

---

## Regras

- Sempre mostrar o prompt pro usuário antes de gerar (evita desperdício de crédito)
- Nunca gerar imagens com texto embutido (fica pixelado, texto vai no carrossel/overlay)
- Preferir cenas reais e fotográficas da experiência da pousada (pets soltos, natureza, aconchego) — evitar ilustrações genéricas
- Salvar sempre o prompt usado para facilitar variações
- Custo aproximado por imagem: $0.02-$0.10 (quality: high) — informar se o usuário perguntar
