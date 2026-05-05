---
name: estatico-unity
description: >
  Cria posts estáticos (card único) completos para Instagram com identidade visual da empresa.
  Gera a foto de fundo via gpt-image2-unity, monta o layout HTML com copy do briefing + logo +
  identidade visual, e renderiza em PNG via Playwright. Post pronto para publicar.
  Use quando o briefing definir formato "imagem" ou "post estático", ou quando o usuário
  pedir "cria o post", "gera o card", "post de imagem".
---

# /post-estatico-unity — Post Estático (Card Único)

## Dependências

- **Identidade visual:** `marca/design-guide.md` — LER ANTES de montar qualquer HTML
- **Contexto do negócio:** `_contexto/empresa.md`
- **Tom de voz:** `_contexto/preferencias.md`
- **Motor de imagem:** `.claude/skills/gpt-image2-unity/gerar-imagem.py` + `credentials/openai_key.txt`
- **Fallback de imagem:** `.claude/skills/nanobanana-unity/` (Gemini, grátis)
- **Playwright CLI:** renderização via `npx.cmd playwright screenshot`
- **Node.js:** já instalado. PATH: `C:\Program Files\nodejs`

## Comando de renderização (Windows)

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 --full-page "file:///CAMINHO/post-01.html" "CAMINHO/post-01.png"
```

Usar `npx.cmd` no PowerShell. Caminhos no `file:///` com barras normais `/`.

---

## Input

- Briefing aprovado em `conteudo/[semana]/[post].md` (vindo do /briefing-unity)
- Ou: tema + copy fornecidos diretamente pelo usuário

---

## Workflow em 3 Fases

### Fase 1 — Copy e prompt de imagem

1. Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `marca/design-guide.md`
2. Localizar o briefing aprovado — perguntar o caminho se não for informado
3. Do briefing, extrair:
   - **Headline principal** (frase de impacto, max 10 palavras)
   - **Tagline/categoria** (ex: "ESQUADRIAS DE PVC · ALTO PADRÃO")
   - **Texto de apoio** (1-2 frases complementares)
   - **Objetivo do post** (autoridade, lançamento, prova social, etc.)

4. Construir o prompt da foto de fundo em inglês:
   - Cena concreta relacionada ao tema (arquitetura, produto aplicado, ambiente)
   - Estilo: `cinematic professional photography`, iluminação dramática, alta qualidade
   - `no text overlay`, `no watermarks`, `no people` (a menos que o briefing peça)
   - Restrição: nunca obras com EPI incorreto
   - Aspect ratio: `portrait` (1024×1536) para encaixar em 1080×1350

5. **CHECKPOINT:** mostrar copy extraída do briefing + prompt proposto para a foto.
   Aguardar confirmação antes de gerar a imagem.

---

### Fase 2 — Geração da foto de fundo

Definir caminho de saída:
```
conteudo/imagens/[tema]/foto-fundo.png
```

Criar a pasta e executar via PowerShell:
```powershell
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT" "conteudo/imagens/TEMA/foto-fundo.png" "portrait"
```

- Informar o usuário que leva 60-180 segundos
- Se falhar por API key ausente (exit code 2): orientar setup da key
- Se falhar por quota/erro (exit code 4): oferecer fallback Nanobanana
- Salvar o prompt usado em `conteudo/imagens/[tema]/prompt.txt`

**CHECKPOINT:** mostrar a foto gerada. Usuário aprova ou pede refinamento.
Se pedir refinamento: ajustar o prompt, gerar novamente. Só avançar com foto aprovada.

---

### Fase 3 — Montagem do post e renderização

1. Ler `marca/design-guide.md` para aplicar cores, tipografia e logo corretos

2. Se design-guide estiver vazio ou com `<!-- NOT CONFIGURED -->`, avisar e usar padrão:
   - Fundo overlay: `rgba(10,18,30,0.85)`
   - Cor de destaque: `#FFD600`
   - Tipografia: Poppins Bold (headline) + Montserrat (tagline)

3. Montar o HTML do post (1080×1350px, inline CSS):

**Estrutura do layout (referência):**
```html
<!-- Foto de fundo -->
<img src="./foto-fundo.png" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center top;">

<!-- Overlay gradiente (garante legibilidade do texto) -->
<div style="position:absolute; inset:0; background: linear-gradient(to bottom,
  rgba(10,18,30,0.55) 0%,
  rgba(10,18,30,0.20) 35%,
  rgba(10,18,30,0.70) 60%,
  rgba(10,18,30,0.93) 100%
);"></div>

<!-- Topo: Logo em caixa branca -->
<!-- Rodapé: Tagline → linha separadora → Headline → Texto de apoio -->
```

4. Aplicar identidade visual do design-guide:
   - Cores primárias e secundárias nos destaques de texto
   - Logo da empresa no topo (fundo branco/claro para contraste)
   - Tipografia definida no design-guide

5. Salvar o HTML em `conteudo/imagens/[tema]/post-01.html`

6. Renderizar via Playwright:
```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 --full-page "file:///CAMINHO/post-01.html" "CAMINHO/post-01.png"
```

7. **CHECKPOINT:** mostrar o post renderizado. Usuário aprova ou pede ajuste.
   - Se ajuste for de texto: editar HTML, re-renderizar
   - Se ajuste for na foto: voltar para Fase 2, gerar nova foto, re-renderizar
   - Só entregar como finalizado após aprovação explícita

---

## Output final

```
conteudo/imagens/[tema]/
  foto-fundo.png     ← foto gerada pelo GPT Image
  prompt.txt         ← prompt da foto (referência para variações)
  post-01.html       ← layout montado
  post-01.png        ← post final renderizado (arquivo para publicar)
```

---

## Regras

- Copy aprovada no Checkpoint da Fase 1 não muda na Fase 3 sem nova confirmação
- Sempre mostrar o post renderizado antes de encerrar — nunca entregar sem aprovação
- Nunca embutir texto dentro do prompt da imagem (texto vai no HTML, não na foto)
- Nunca prometer prazos ou preços no texto do post
- Sem EPI incorreto em cenas de obra
- Se o usuário pedir versão story (9:16): adaptar viewport para 1080×1920 e salvar em `post-01-story.png`
