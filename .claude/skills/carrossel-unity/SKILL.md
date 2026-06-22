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

- **Identidade visual:** `marca/DESIGN.md` — LER ANTES de criar qualquer HTML
- **Contexto do negócio:** `_contexto/empresa.md`
- **Tom de voz:** `_contexto/preferencias.md`
- **Playwright CLI:** renderização via `npx playwright screenshot`
- **Node.js:** já instalado (v24.15.0). PATH: `C:\Program Files\nodejs`
- **Browser do Playwright:** se o render falhar com `Executable doesn't exist`, instalar o navegador uma vez: `npx.cmd playwright install chromium`
- **Geração de imagem (default):** `.claude/skills/gpt-image2-unity/gerar-imagem.py` + `credentials/openai_key.txt`
- **Geração de imagem (fallback):** `.claude/skills/nanobanana-unity/` (Gemini, grátis — se GPT falhar)

## Comando de renderização (Windows)

```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot --viewport-size=1080,1350 "file:///CAMINHO_ABSOLUTO/slide-XX.html" "CAMINHO_ABSOLUTO/slide-XX.png"
```

**NÃO usar `--full-page`.** Com `--full-page`, o Playwright captura a altura do *conteúdo*
(não do viewport) — se o HTML errar a altura ou o texto transbordar, o PNG sai com tamanho
errado (ex.: 1080×1080 ou 1080×1500). Sem `--full-page`, o `--viewport-size=1080,1350` garante
**exatamente 1080×1350** sempre. Esse é o tamanho exato do feed do Instagram (retrato 4:5) e é
**inegociável** — todo slide, capa e internos.

Usar `npx.cmd` (não `npx`) no PowerShell do Windows para contornar a política de execução de scripts.
Caminhos no `file:///` precisam usar barras normais `/`, não `\`.

**Após renderizar, rodar AS DUAS validações (ambas obrigatórias — gate de qualidade):**

```powershell
# 1) Dimensão do PNG — o canvas tem que ser exatamente 1080×1350
python ".claude/skills/publicar-social-unity/validar-dimensao.py" "CAMINHO_ABSOLUTO/instagram" 1080 1350

# 2) Overflow interno — nenhum texto pode ultrapassar as bordas do canvas
node ".claude/skills/publicar-social-unity/validar-overflow.js" "CAMINHO_ABSOLUTO/instagram"
```

- `validar-dimensao.py` confere só o tamanho do canvas — **não enxerga texto cortado dentro dele**.
- `validar-overflow.js` renderiza cada slide e acusa qualquer elemento de texto que sangre para
  fora de 1080×1350 (caso clássico: spec bar / rodapé horizontal cortado no canto). Ele aponta o
  slide, o trecho exato e quantos px transbordam.

Se **qualquer uma** das duas falhar (exit 1), **não seguir** — corrigir o HTML e re-renderizar o
slide afetado, depois rodar as duas de novo. Só avança quando ambas derem OK. Nunca "deixar passar"
um corte de poucos pixels — o feed mobile amplia o canto e o erro fica evidente.

## Histórico de execuções

Antes de iniciar, verificar se existe `conteudo/carrosseis/[periodo]/[dia]/_aprovado.md`. Se existir, ler e usar como referência de qualidade mínima: reaproveitar prompts de imagem aprovados como ponto de partida, reproduzir o ângulo de copy aprovado, evitar o que estiver marcado em "O que evitar".

---

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
- Contexto: usar o perfil de público definido em `_contexto/empresa.md` (setor, linguagem técnica vs. acessível)
- **Um ponto por slide.** Quando o texto estiver em excesso, cortar o parágrafo final — nunca reduzir o tamanho da fonte para encaixar

6. Salvar o texto em `conteudo/carrosseis/[periodo]/[dia]/carousel-text.md`

**CHECKPOINT:** mostrar o texto completo + as 3 opções de capa. Aguardar o usuário escolher a capa e aprovar o texto antes de seguir pra Fase 1.5.

---

### Fase 1.5 — Geração de Imagens (GPT Image 2)

Após o texto aprovado, identificar quais slides se beneficiam de uma imagem fotográfica de fundo ou de apoio:

**Slides que recebem imagem:**
- **Slide 1 (Capa):** SEMPRE — obrigatório, sem exceção. Cadeia de tentativas: GPT Image 2 → Nanobanana → image-gen-unity. Se um motor falhar, sinalizar ao usuário e tentar o próximo sem interromper o fluxo. Só parar se todos os três falharem.
- **Slides de impacto (dados, fatos, revelações):** opcional — imagem contextual que reforce o conteúdo
- **Slides puramente tipográficos (listas, bullets, texto longo):** sem imagem — layout clean

Regra: **menos é mais** para slides intermediários. Máximo de 2 imagens adicionais além da capa (total: até 3 por carrossel).

**Imagem única por slide.** Nunca usar a mesma imagem em dois slides diferentes — cada slide que recebe foto deve ter seu próprio arquivo `img-slideXX.png`.

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
python ".claude/skills/gpt-image2-unity/gerar-imagem.py" "PROMPT" "conteudo/carrosseis/PERIODO/DIA/instagram/img-slideXX.png" "portrait"
```

- Avisar o usuário que cada imagem leva 60-180s
- Se o script falhar (exit code ≠ 0):
  - Verificar se `credentials/openai_key.txt` existe — se não, pedir pro usuário adicionar
  - Se a key existe mas falhou (quota/erro): avisar e oferecer fallback Nanobanana
  - **Fallback Nanobanana:** usar `.claude/skills/nanobanana-unity/` com o mesmo prompt (se a skill estiver instalada)
  - Se Nanobanana também não estiver disponível: prosseguir sem imagem nesse slide, avisar o usuário

Salvar cada imagem em `conteudo/carrosseis/[periodo]/[dia]/instagram/img-slideXX.png`.

**CHECKPOINT:** mostrar as imagens geradas. Usuário aprova ou pede regeneração individual antes de seguir pra Fase 2.

---

### Fase 2 — Visual (HTMLs + PNGs)

1. Ler `marca/DESIGN.md` para aplicar a identidade visual
2. Se `status: not-configured` ou algum campo obrigatório estiver `""`, interromper e avisar:
   > ⚠️ O DESIGN.md ainda não foi configurado com a identidade visual da empresa. Para continuar, rode `/setup`.
   
   A execução para. Sem cores improvisadas.
3. Criar HTMLs (1080x1350px, inline CSS, Google Fonts como única dependência externa)

**Padrão visual dos slides:**
- Fundo: cor definida em `colors.canvas` no DESIGN.md
- Tipografia: usar os valores de `typography` do DESIGN.md como mínimos mobile — não reduzir abaixo deles
  - `display.fontSize` (~100px): destaque/accent na capa
  - `heading.fontSize` (~70px): título principal dos slides internos
  - `body.fontSize` (~28px): corpo de texto
  - `body.lineHeight` (máx 1.3): acima disso o bloco fica arejado demais
- **Texto nunca cortado nem sobreposto — regra inviolável.** Cada slide cabe inteiro em 1080×1350
  com respiro nas bordas. Se o texto não couber, **cortar texto** (menos palavras/linhas) — NUNCA
  reduzir a fonte abaixo da escala mobile, NUNCA comprimir padding/espaçamento até os elementos
  colidirem. No checkpoint de cada slide, conferir: nada cortado nos cantos/bordas, nada sobreposto.
- **Barras horizontais (spec bar / rodapé de specs) — ponto de falha recorrente.** Uma fileira de
  itens com `display:flex` + `white-space:nowrap` **não quebra linha**: se a soma (textos + gaps +
  padding lateral) passar de 1080px, o último item sangra para fora e é cortado no canto inferior
  direito — sem erro visível na dimensão do PNG. Para garantir que cabe:
  - usar `justify-content:space-between` (não `gap` grande fixo) + `flex-wrap:nowrap` + `overflow:hidden` no container da barra;
  - manter padding lateral enxuto (≤56px) e `letter-spacing` baixo (≤0.04em) em texto uppercase;
  - no máximo ~4 itens curtos; se precisar de mais, encurtar os rótulos (ex.: "Vento 1.820 Pa", não "Resistência ao vento ensaiada 1.820 Pa");
  - **sempre** confirmar com `validar-overflow.js` depois de renderizar — nunca confiar só no olho.
- **Tamanho exato 1080×1350 em todos os slides** (capa e internos). `overflow:hidden` no body +
  render sem `--full-page` + validação de dimensão (ver "Comando de renderização"). Slide fora de
  1080×1350 = refazer, nunca redimensionar na publicação.
- Cor de destaque: cor definida em `colors.accent` no DESIGN.md
- **Layout diferente por slide.** Cada slide tem estrutura visual distinta — não repetir o mesmo template
- **Sem espaço morto.** Quando a imagem não precisa respirar, centralizar o conteúdo verticalmente
- **Capa = slide mais impactante.** O slide visualmente mais cinematográfico vai para posição 01
- **CTA com composição dinâmica.** Usar diagonal ou split no último slide — não é layout estático como os slides informativos
- **Logo com folga garantida.** Nunca coberta pelo conteúdo. Quando o conteúdo for centralizado verticalmente, usar mínimo de `padding-top` equivalente a `spacing.section` do DESIGN.md (ref: 160px quando logo está em `top: 64px` com altura ~68px)
- Último slide: apenas branding e CTA, sem texto longo

**Logo e header — path obrigatório (não improvisar a contagem de `../`):**

Os HTMLs ficam em `conteudo/carrosseis/[periodo]/[dia]/instagram/`, que está a **5 níveis** da
raiz do projeto. O path do logo é **sempre** com 5 `../`:

```html
<img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">
```

Contagem: `instagram/` → dia → periodo → carrosseis → conteudo → raiz (onde está `marca/`).
**4 níveis (`../../../../`) aponta para `conteudo/marca/`, que não existe → logo quebra no Playwright.**
Logo branco em slide escuro; `logo-cor.png` em fundo claro. Header padrão completo em `.claude/memory/feedback_carousel_design_aprovado.md`.

**Elementos proibidos nos slides:**
- Sem labels de seção ("VIDA ÚTIL", "MATERIAIS")
- Sem eyebrows ("COMPARATIVO TÉCNICO", "SAIBA MAIS")
- Sem badges de série ("PARTE 1 DE 2", "EP. 03")
- Sem slide-tags no rodapé ("Tema · Parte 1")
- Em slides comparativos (A vs. B): hierarquia via cor, nunca via redução de opacidade — os dois lados devem estar 100% legíveis

**Slides com imagem gerada (Fase 1.5):**
- Referenciar com caminho relativo: `<img src="./img-slideXX.png">`
- Full-bleed sempre: `position:absolute; inset:0; width:100%; height:100%; object-fit:cover`
- **Gradiente segue a direção do conteúdo:** texto na base → gradiente bottom→top; texto à esquerda → gradiente left→right. Nunca overlay sólido cobrindo a imagem
- **Dissolve suave:** usar `linear-gradient` no elemento de overlay para que a transição foto→fundo nunca apareça como corte brusco. Em composições de duas fotos empilhadas, ambas devem dissolver no ponto de encontro
- Exemplo de background com imagem (texto na base):
  ```html
  <div style="position:relative; width:1080px; height:1350px; overflow:hidden;">
    <img src="./img-slide01.png" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;">
    <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.90) 0%, rgba(0,0,0,0.40) 50%, rgba(0,0,0,0.10) 100%);"></div>
    <div style="position:relative;z-index:1; /* conteúdo do slide */ ">...</div>
  </div>
  ```
- Slides sem imagem: usar fundo sólido normalmente

4. Salvar HTMLs em `conteudo/carrosseis/[periodo]/[dia]/instagram/`
5. Renderizar cada HTML em PNG via PowerShell (comando acima)
   - Renderizar slide 1 primeiro e mostrar pro usuário antes de renderizar os demais

**CHECKPOINT:** mostrar slide 1 renderizado. Se aprovado, renderizar os demais.

Salvar PNGs em `conteudo/carrosseis/[periodo]/[dia]/instagram/`.

**Após aprovação explícita dos slides finais:** salvar `conteudo/carrosseis/[periodo]/[dia]/_aprovado.md` com:
```markdown
# Execução aprovada — [data]

## Copy aprovada
- Ângulo: [ex: educacional / provocativo]
- Headline da capa: "[headline aprovada]"
- Ajustes feitos: [X foi corrigido para Y — ou "nenhum"]

## Prompts de imagem aprovados
- Slide 1 (capa): "[prompt exato usado]"
- Slide [N]: "[prompt exato usado]" (se houver)

## O que funcionou bem
- [o que passou sem ajuste]

## O que evitar
- [o que foi rejeitado ou exigiu muita correção]
```

---

### Fase 3 — Versão TikTok (opcional)

Após finalizar o Instagram, perguntar:
> "Quer a versão TikTok também? (1080x1920, formato vertical para stories/reels)"

Se sim:
- Adaptar os HTMLs: height 1920px, ajustar padding, aumentar fonte levemente
- Renderizar com `--viewport-size=1080,1920`
- Salvar em `conteudo/carrosseis/[periodo]/[dia]/tiktok/`

---

## Output final

```
conteudo/carrosseis/[periodo]/[dia]/
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
- Nunca prometer prazos ou preços nos slides (verificar restrições de compliance em `_contexto/preferencias.md`)
- Não usar referências a obras com EPI incorreto
- Tamanhos de fonte nunca abaixo dos valores de `typography` no DESIGN.md — o conteúdo é visto no feed mobile
- Quando texto em excesso: cortar parágrafo final, nunca reduzir fonte para encaixar
