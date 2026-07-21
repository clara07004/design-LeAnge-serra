---
name: estatico-leange
description: >
  Cria posts estáticos (card único) completos para Instagram com identidade visual da empresa.
  Gera a foto de fundo via gpt-image2-leange, monta o layout HTML com copy do briefing + logo +
  identidade visual, e renderiza em PNG via Playwright. Post pronto para publicar.
  Use quando o briefing definir formato "imagem" ou "post estático", ou quando o usuário
  pedir "cria o post", "gera o card", "post de imagem".
---

# /post-estatico-leange — Post Estático (Card Único)

## Dependências

- **Identidade visual:** `marca/DESIGN.md` — LER ANTES de montar qualquer HTML
- **Contexto do negócio:** `_contexto/empresa.md`
- **Tom de voz:** `_contexto/preferencias.md`
- **Motor de imagem:** `.claude/skills/gpt-image2-leange/gerar-imagem.py` + `credentials/openai_key.txt`
- **Fallback de imagem:** `.claude/skills/nanobanana-leange/` (Gemini, grátis)
- **Playwright CLI:** renderização via `npx.cmd playwright screenshot`
- **Node.js:** já instalado. PATH: `C:\Program Files\nodejs`
- **Browser do Playwright:** se o render falhar com `Executable doesn't exist`, instalar o navegador uma vez: `npx.cmd playwright install chromium`

## Comando de renderização (Windows)

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 "file:///CAMINHO/post-01.html" "CAMINHO/post-01.png"
```

Usar `npx.cmd` no PowerShell. Caminhos no `file:///` com barras normais `/`.

---

## Histórico de execuções

Antes de iniciar, verificar se existe `conteudo/post-estatico/[periodo]/[dia]/_aprovado.md`. Se existir, ler e usar como referência de qualidade mínima: reaproveitar o prompt de imagem aprovado como ponto de partida, reproduzir o ângulo de copy aprovado, evitar o que estiver marcado em "O que evitar".

---

## Input

- Briefing aprovado em `conteudo/post-estatico/[periodo]/[dia]/_briefing.md` (vindo do /briefing-leange)
- Ou: tema + copy fornecidos diretamente pelo usuário

---

## Workflow em 3 Fases

### Fase 1 — Copy e prompt de imagem

1. Ler `_contexto/empresa.md`, `_contexto/preferencias.md`, `marca/DESIGN.md`
2. Localizar o briefing aprovado — perguntar o caminho se não for informado
3. Do briefing, extrair:
   - **Headline principal** (frase de impacto, max 10 palavras)
   - **Tagline/categoria** (ex: "POUSADA PET LOVER · ALTO PADRÃO")
   - **Texto de apoio** (1-2 frases complementares)
   - **Objetivo do post** (autoridade, lançamento, prova social, etc.)

4. Construir o prompt da foto de fundo em inglês:
   - Cena concreta relacionada ao tema (pet nos espaços da pousada, natureza, suíte, gastronomia)
   - Estilo: `cinematic professional photography`, luz natural quente, alta qualidade
   - `no text overlay`, `no watermarks`, `no people` (a menos que o briefing peça)
   - Aspect ratio: `portrait` (1024×1536) para encaixar em 1080×1350

5. **CHECKPOINT:** mostrar copy extraída do briefing + prompt proposto para a foto.
   Aguardar confirmação antes de gerar a imagem.

---

### Fase 2 — Geração da foto de fundo

Definir caminho de saída:
```
conteudo/post-estatico/[periodo]/[dia]/img-post.png
```

Criar a pasta e executar via PowerShell:
```powershell
python ".claude/skills/gpt-image2-leange/gerar-imagem.py" "PROMPT" "conteudo/post-estatico/PERIODO/DIA/img-post.png" "portrait"
```

- Informar o usuário que leva 60-180 segundos
- Se falhar por API key ausente (exit code 2): orientar setup da key
- Se falhar por quota/erro (exit code 4): oferecer fallback Nanobanana
- Salvar o prompt usado em `conteudo/post-estatico/[periodo]/[dia]/prompt.txt`

**CHECKPOINT:** mostrar a foto gerada. Usuário aprova ou pede refinamento.
Se pedir refinamento: ajustar o prompt, gerar novamente. Só avançar com foto aprovada.

---

### Fase 3 — Montagem do post e renderização

1. Ler `marca/DESIGN.md` para aplicar cores, tipografia e logo corretos

2. Se `status: not-configured` ou algum campo obrigatório estiver `""`, interromper e avisar:
   > ⚠️ O DESIGN.md ainda não foi configurado com a identidade visual da empresa. Para continuar, rode `/setup`.
   
   A execução para. Sem cores improvisadas.

3. Montar o HTML do post (1080×1350px, inline CSS):

**Estrutura do layout (referência):**
```html
<!-- Foto de fundo — full-bleed sempre -->
<img src="./img-post.png" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center top;">

<!-- Overlay gradiente — direção segue onde o texto está posicionado -->
<!-- Texto na base: gradiente bottom→top (padrão) -->
<div style="position:absolute; inset:0; background: linear-gradient(to top,
  rgba(10,18,30,0.93) 0%,
  rgba(10,18,30,0.70) 40%,
  rgba(10,18,30,0.20) 70%,
  rgba(10,18,30,0.55) 100%
);"></div>

<!-- Topo: Logo com folga garantida (padding-top mínimo = spacing.section do DESIGN.md) -->
<!-- O HTML fica em conteudo/post-estatico/[periodo]/[dia]/ = 4 níveis até a raiz. NÃO improvisar a contagem. -->
<img src="../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
<!-- Rodapé: Tagline → linha separadora → Headline → Texto de apoio -->
```

4. Aplicar identidade visual do DESIGN.md:
   - Cores primárias e secundárias nos destaques de texto
   - Logo no topo, path `../../../../marca/logos/logo-branco.png` (4 níveis — o post fica em
     `conteudo/post-estatico/[periodo]/[dia]/`, não em pasta `instagram/` como o carrossel).
     `logo-branco.png` sobre a foto escura (padrão); `logo-cor.png` só se o fundo for claro
   - Tipografia do DESIGN.md como mínimos mobile: headline ≥ `heading.fontSize`, apoio ≥ `body.fontSize`, line-height ≤ `body.lineHeight`

5. Salvar o HTML em `conteudo/post-estatico/[periodo]/[dia]/post-01.html`

6. Renderizar via Playwright:
```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 "file:///CAMINHO/post-01.html" "CAMINHO/post-01.png"
```

7. **CHECKPOINT:** mostrar o post renderizado. Usuário aprova ou pede ajuste.
   - Se ajuste for de texto: editar HTML, re-renderizar
   - Se ajuste for na foto: voltar para Fase 2, gerar nova foto, re-renderizar
   - Só entregar como finalizado após aprovação explícita

8. **Após aprovação explícita:** salvar `conteudo/post-estatico/[periodo]/[dia]/_aprovado.md` com:
   ```markdown
   # Execução aprovada — [data]

   ## Copy aprovada
   - Ângulo: [ex: autoridade acolhedora / prova social]
   - Headline: "[headline aprovada]"
   - Ajustes feitos: [X foi corrigido para Y — ou "nenhum"]

   ## Prompt de imagem aprovado
   - img-post: "[prompt exato usado]"

   ## O que funcionou bem
   - [o que passou sem ajuste]

   ## O que evitar
   - [o que foi rejeitado ou exigiu muita correção]
   ```

---

## Output final

```
conteudo/post-estatico/[periodo]/[dia]/
  img-post.png     ← foto gerada pelo GPT Image
  prompt.txt         ← prompt da foto (referência para variações)
  post-01.html       ← layout montado
  post-01.png        ← post final renderizado (arquivo para publicar)
```

---

## Regras

- **Tamanho exato 1080×1350, sem exceção.** O HTML tem `width:1080px; height:1350px; overflow:hidden`
  e a renderização **não** usa `--full-page` (ela captura a altura do conteúdo e gera tamanho
  errado). Após renderizar, rodar a validação — se o PNG não for exatamente 1080×1350, corrigir o
  HTML e re-renderizar **antes** de seguir:
  ```powershell
  python ".claude/skills/publicar-social-leange/validar-dimensao.py" "CAMINHO/post-01.png" 1080 1350
  ```
  Tamanho errado = o Instagram redimensiona na publicação = texto deslocado/cortado.
- **Texto nunca cortado nem sobreposto — regra inviolável.** Todo texto cabe inteiro no canvas,
  com respiro nas bordas. Se não couber, **reduzir a quantidade de texto** (cortar palavras/linhas)
  — NUNCA reduzir a fonte abaixo da escala mobile do DESIGN.md, NUNCA comprimir padding/espaçamento
  até os elementos colidirem. No checkpoint, conferir visualmente: nada cortado nos cantos/bordas,
  nada sobreposto. Se houver, é reprovado — refazer.
- **Fundo de cor sólida é proibido.** O post estático SEMPRE tem foto de fundo gerada por IA. Cadeia de tentativas: GPT Image 2 → Nanobanana → image-gen-leange. Se um motor falhar, sinalizar ao usuário e tentar o próximo sem interromper o fluxo. Só parar se todos os três falharem.
- Copy aprovada no Checkpoint da Fase 1 não muda na Fase 3 sem nova confirmação
- Sempre mostrar o post renderizado antes de encerrar — nunca entregar sem aprovação
- Nunca embutir texto dentro do prompt da imagem (texto vai no HTML, não na foto)
- Nunca prometer prazos ou preços no texto do post
- Se o usuário pedir versão story (9:16): adaptar viewport para 1080×1920 e salvar em `post-01-story.png`
