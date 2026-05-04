---
name: carrossel-unity
description: >
  Cria carrosséis completos para Instagram e TikTok com a identidade visual da Unity.
  Gera o texto dos slides, cria os HTMLs estilizados, renderiza em PNG via Playwright
  e oferece versão TikTok ao final.
  Use quando o usuário mencionar "carrossel", "carousel", "slides instagram",
  "slides tiktok", "faz um carrossel", ou pedir pra transformar um tema em carrossel.
---

# /carrossel-unity — Criação de Carrossel

## Dependências

- **Identidade visual:** `marca/design-guide.md` — LER ANTES de criar qualquer HTML
- **Contexto do negócio:** `_contexto/empresa.md`
- **Tom de voz:** `_contexto/preferencias.md`
- **Playwright CLI:** renderização via `npx playwright screenshot`
- **Node.js:** já instalado (v24.15.0). PATH: `C:\Program Files\nodejs`
- **Geração de imagem (default):** `.claude/skills/gpt-image2-unity/gerar-imagem.py` + `credentials/openai_key.txt`
- **Geração de imagem (fallback):** `.claude/skills/nanobanana-unity/` (Gemini, grátis — se GPT falhar)

## Comando de renderização (Windows)

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 --full-page "file:///CAMINHO_ABSOLUTO/slide-XX.html" "CAMINHO_ABSOLUTO/slide-XX.png"
```

Usar `npx.cmd` (não `npx`) no PowerShell do Windows para contornar a política de execução de scripts.
Caminhos no `file:///` precisam usar barras normais `/`, não `\`.

## Input

O usuário fornece:
- Tema, ideia, texto livre, link ou arquivo de referência
- Número do episódio ou série (se aplicável)
- Foto pra capa (opcional)

---

## Workflow em 3 Fases

### Fase 1 — Texto

1. Ler `_contexto/preferencias.md` pra calibrar o tom de voz
2. Ler `_contexto/empresa.md` pra entender o contexto e o público
3. Se o input for um link, usar WebFetch pra buscar o conteúdo
4. Definir o ângulo do carrossel: educacional, oportunidade, contrário, provocativo ou inspiracional
5. Escrever 8-10 slides seguindo o fluxo:
   - **Slide 1 (Capa):** 3 opções de título (max 8 palavras cada) + subtítulo — o usuário escolhe antes de continuar
   - **Slides 2-3 (Contexto):** o que é / por que importa
   - **Slides 4-7 (Desenvolvimento):** um insight por slide, opinião clara
   - **Slide 8-9 (Implicação):** "o que isso muda pra quem tá lendo?"
   - **Slide final (CTA):** chamada pra ação + menção ao canal/marca

**Tom do texto:**
- Frases longas e naturais (2-4 frases por slide), não bullet points disfarçados
- Frases curtas e picotadas ficam com cara de IA — evitar
- Manter o curiosity gap entre slides, mas dentro de cada slide o texto deve fluir
- Seguir `_contexto/preferencias.md` (sem travessões, etc)
- Contexto: construção a seco (drywall/steel frame) — público técnico mas acessível

6. Salvar o texto em `conteudo/carrosseis/[tema]/carousel-text.md`

**CHECKPOINT:** mostrar o texto completo + as 3 opções de capa. Aguardar o usuário escolher a capa e aprovar o texto antes de seguir pra Fase 1.5.

---

### Fase 1.5 — Geração de Imagens (GPT Image 2)

Após o texto aprovado, identificar quais slides se beneficiam de uma imagem fotográfica de fundo ou de apoio:

**Slides que recebem imagem:**
- **Slide 1 (Capa):** sempre — imagem fotográfica que represente o tema principal
- **Slides de impacto (dados, fatos, revelações):** opcional — imagem contextual que reforce o conteúdo
- **Slides puramente tipográficos (listas, bullets, texto longo):** sem imagem — layout clean

Regra: **menos é mais**. Máximo de 3 imagens por carrossel de 8-10 slides.

#### Construir prompts para cada imagem

Para cada slide que receberá imagem, criar um prompt em inglês:
- Descrever a cena concreta relacionada ao conteúdo do slide (ex: "drywall installation in a modern apartment")
- Incluir: `professional photography`, iluminação (natural/artificial), enquadramento
- Incluir: `no text overlay`, `no watermarks`, `photorealistic`
- Incluir contexto de construção a seco quando relevante: `drywall`, `steel frame`, `dry construction`
- **Nunca:** obras com EPI incorreto, texto embutido na imagem, ilustrações genéricas
- Aspect ratio: `portrait` (1024×1536) para encaixar em 1080×1350 via CSS object-fit

Mostrar todos os prompts de uma vez antes de gerar qualquer imagem — usuário confirma ou ajusta.

#### Gerar as imagens (GPT Image 2 → fallback Nanobanana)

Para cada imagem, executar via PowerShell:
```powershell
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT" "conteudo/carrosseis/TEMA/instagram/img-slideXX.png" "portrait"
```

- Avisar o usuário que cada imagem leva 60-180s
- Se o script falhar (exit code ≠ 0):
  - Verificar se `credentials/openai_key.txt` existe — se não, pedir pro usuário adicionar
  - Se a key existe mas falhou (quota/erro): avisar e oferecer fallback Nanobanana
  - **Fallback Nanobanana:** usar `.claude/skills/nanobanana-unity/` com o mesmo prompt (se a skill estiver instalada)
  - Se Nanobanana também não estiver disponível: prosseguir sem imagem nesse slide, avisar o usuário

Salvar cada imagem em `conteudo/carrosseis/[tema]/instagram/img-slideXX.png`.

**CHECKPOINT:** mostrar as imagens geradas. Usuário aprova ou pede regeneração individual antes de seguir pra Fase 2.

---

### Fase 2 — Visual (HTMLs + PNGs)

1. Ler `marca/design-guide.md` pra aplicar a identidade visual
2. Se o design guide estiver vazio ou com `<!-- NOT CONFIGURED -->`, avisar:
   > "O design-guide.md ainda não tem cores e fontes definidas. Vou usar o layout padrão Unity agora. Pra personalizar, preenche `marca/design-guide.md` e chama /carrossel-unity de novo."
   
   **Layout padrão Unity (quando design guide vazio):**
   - Fundo: `#0D0D0D`
   - Cor de destaque: `#FFD600`
   - Tipografia: Bricolage Grotesque (títulos) + Instrument Serif (corpo)

3. Criar HTMLs (1080x1350px, inline CSS, Google Fonts como única dependência externa)

**Padrão visual dos slides:**
- Fundo: cor definida no design guide (ou `#0D0D0D` padrão)
- Tipografia: fontes do design guide (ou Bricolage Grotesque + Instrument Serif)
- Cor de destaque: cor do design guide (ou `#FFD600`)
- Variação visual: usar pelo menos 2 layouts diferentes entre os slides (ex: texto simples, destaque com número grande, card com borda, citação em destaque)
- Último slide: apenas branding e CTA, sem texto longo

**Slides com imagem gerada (Fase 1.5):**
- Referenciar com caminho relativo: `<img src="./img-slideXX.png">`
- Imagem como fundo ou elemento visual — usar `object-fit: cover` quando for background
- Sobrepor um overlay escuro semi-transparente (`rgba(0,0,0,0.45)`) para garantir legibilidade do texto
- Exemplo de background com imagem:
  ```html
  <div style="position:relative; width:1080px; height:1350px; overflow:hidden;">
    <img src="./img-slide01.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:rgba(0,0,0,0.45);"></div>
    <div style="position:relative;z-index:1; /* conteúdo do slide */ ">...</div>
  </div>
  ```
- Slides sem imagem: usar fundo sólido normalmente

4. Salvar HTMLs em `conteudo/carrosseis/[tema]/instagram/`
5. Renderizar cada HTML em PNG via PowerShell (comando acima)
   - Renderizar slide 1 primeiro e mostrar pro usuário antes de renderizar os demais

**CHECKPOINT:** mostrar slide 1 renderizado. Se aprovado, renderizar os demais.

Salvar PNGs em `conteudo/carrosseis/[tema]/instagram/`.

---

### Fase 3 — Versão TikTok (opcional)

Após finalizar o Instagram, perguntar:
> "Quer a versão TikTok também? (1080x1920, formato vertical para stories/reels)"

Se sim:
- Adaptar os HTMLs: height 1920px, ajustar padding, aumentar fonte levemente
- Renderizar com `--viewport-size=1080,1920`
- Salvar em `conteudo/carrosseis/[tema]/tiktok/`

---

## Output final

```
conteudo/carrosseis/[tema]/
  carousel-text.md          ← texto aprovado + legenda sugerida
  instagram/
    img-slide01.png          ← imagem gerada pelo GPT (capa)
    img-slide04.png          ← imagem gerada pelo GPT (slide de impacto, se houver)
    slide-01.html → slide-01.png
    slide-02.html → slide-02.png
    ...
  tiktok/ (se solicitado)
    img-slide01.png          ← mesma imagem, reutilizada
    slide-01.html → slide-01.png
    ...
```

## Regras

- Texto aprovado na Fase 1 não muda na Fase 2
- Sempre mostrar slide 1 antes de renderizar os demais
- Se o usuário pedir ajuste no visual, editar o HTML e re-renderizar apenas o slide alterado
- Sem travessões (—) no texto por padrão, a menos que `preferencias.md` indique o contrário
- Nunca prometer prazos ou preços nos slides (restrição da empresa piloto)
- Não usar referências a obras com EPI incorreto
