# Guia de Skills — Como Usar, Quando Usar, Sequências e Resultados

> Este arquivo é o guia prático de todas as 19 skills do repositório.
> Para cada skill: o que faz, quando chamar, como invocar, o que entrega.
> No final: os fluxos sequenciais completos para cada tipo de conteúdo.

---

## Como invocar uma skill

**Opção 1 — Comando direto:**
```
/nome-da-skill
```

**Opção 2 — Linguagem natural:**
Descreva o que quer. O Claude identifica a skill certa automaticamente.
- "quero ideias de conteúdo sobre [tema]" → aciona `/gerador-de-angulos-para-um-tema`
- "faz um carrossel sobre desempenho térmico" → aciona `/carrossel-unity`
- "quais as objeções do [avatar] sobre [produto]?" → aciona `/banco-de-objecoes-do-avatar`

**Regra geral:** se existir uma skill para o que você quer, o Claude usa ela. Se não existir, executa normalmente e pergunta se quer criar uma skill para a próxima vez.

---

## As 19 skills — referência rápida

### Grupo 1 — Ideação e pesquisa

---

#### `/gerador-de-angulos-para-um-tema`
**O que faz:** Pega um tema e gera 10 lentes criativas para abordá-lo — cada uma com um ângulo diferente para o mesmo assunto.

**Quando usar:** Antes do briefing, quando você tem um tema mas não sabe qual ângulo explorar. Ex: "quero falar sobre [tema], mas não sei como entrar no assunto."

**Como invocar:**
```
/gerador-de-angulos-para-um-tema [tema]
```
Exemplo: `/gerador-de-angulos-para-um-tema [tema]`

**O que precisa fornecer:** o tema. Pode ser amplo ("[produto]") ou específico ("[aspecto específico do setor]").

**O que entrega:**
- 10 ângulos prontos para usar como ponto de partida do briefing
- Cada ângulo com: título do post sugerido, gancho, por que funciona para a empresa

**Resultado esperado:** você escolhe 1 dos 10 ângulos e leva para o `/briefing-unity`.

---

#### `/gerador-de-angulos-de-conteudo`
**O que faz:** Abordagem mais estruturada que o anterior — usa uma matriz de perspectivas × audiência × formatos narrativos para gerar ângulos mais sofisticados.

**Quando usar:** Quando quer ângulos com mais profundidade estratégica, ou quando o tema é mais complexo e precisa de recorte de audiência (arquiteto vs construtor vs proprietário).

**Como invocar:**
```
/gerador-de-angulos-de-conteudo [tema] [avatar opcional]
```

**O que entrega:**
- 10 ângulos únicos com combinações de perspectiva + audiência + formato narrativo
- Indicação de qual formato de post funciona melhor para cada ângulo

**Diferença do anterior:** este é mais analítico e segmentado por audiência. O `/gerador-de-angulos-para-um-tema` é mais criativo e rápido.

---

#### `/banco-de-objecoes-do-avatar`
**O que faz:** Mapeia todas as objeções que o ICP tem antes de especificar, comprar ou recomendar o produto — organizadas em 6 tipos, com resposta em formato de conteúdo para cada uma.

**Quando usar:** Quando quer criar conteúdo de meio/fundo de funil, ou quando percebe que os posts não estão convertendo e quer entender o que trava o cliente.

**Como invocar:**
```
/banco-de-objecoes-do-avatar [avatar: arquiteto / construtor / proprietário]
```

**O que entrega:**
- Banco completo com 6 tipos de objeção (valor, percepção, confiança técnica, confiança em si mesmo, relevância, urgência)
- Para cada objeção: como o avatar formula, raiz real, resposta em conteúdo, resposta em copy
- Lista das 3 objeções mais críticas
- Plano de conteúdo com sugestão de post para cada objeção

**Resultado esperado:** usar cada objeção como input para o `/carrossel-de-quebra-de-objecao`.

---

### Grupo 2 — Planejamento e briefing

---

#### `/calendario-comercial`
**O que faz:** Cria o mapa estratégico de conteúdo para o mês — cruzando eventos culturais, datas relevantes e objetivos da empresa para identificar quando e o que postar.

**Quando usar:** Uma vez por mês, antes de começar qualquer produção.

**Como invocar:**
```
/calendario-comercial [mês] [ano]
```
Exemplo: `/calendario-comercial junho 2025`

**O que entrega:**
- Radar cultural do período
- Mapa de oportunidades por semana (🟢 alta, 🟡 média, 🔴 baixa)
- Tema narrativo do mês
- Alertas de risco e datas sensíveis

---

#### `/briefing-unity`
**O que faz:** Gera o briefing completo de um post — mensagem central, gancho, copy, formato recomendado, orientações visuais, hashtags.

**Quando usar:** Para cada post que vai produzir. Pode vir depois do calendário ou de um ângulo aprovado.

**Como invocar:**
```
/briefing-unity [tema ou ângulo escolhido]
```

**O que entrega:**
- Mensagem central (a linha que não pode se perder)
- Gancho principal
- Copy por plataforma
- Formato recomendado com justificativa
- Orientações visuais
- Hashtags

**Checkpoint:** `[A] Aprovar / [E] Editar / [C] Cancelar` — o fluxo não avança sem aprovação.

---

### Grupo 3 — Hooks e capas

---

#### `/hooks-para-carrossel`
**O que faz:** Gera 5 opções de capa para o carrossel — cada uma com headline, direção visual e tipo de gancho diferente.

**Quando usar:** Antes de produzir o carrossel, quando o briefing foi aprovado e você quer escolher o melhor ângulo de entrada.

**Como invocar:**
```
/hooks-para-carrossel [tema ou briefing aprovado]
```

**O que entrega:**
- 5 opções de capa com: headline, subtítulo opcional, direção visual (o que colocar na imagem), tipo de gancho (promessa, dor, número, polêmica, identificação, antes/depois, dado)

**Resultado esperado:** você escolhe 1 capa e leva para o `/carrossel-unity`.

---

#### `/hooks-para-instagram-reels`
**O que faz:** Gera 7 opções de hook para Reel — cada uma combinando o que aparece no primeiro frame (visual) com a frase de abertura (narração).

**Quando usar:** Antes de produzir o roteiro do Reel.

**Como invocar:**
```
/hooks-para-instagram-reels [tema ou briefing aprovado]
```

**O que entrega:**
- 7 hooks com: primeiro frame (o que o espectador vê antes de dar play), frase de abertura, tipo de gancho (salvável, compartilhável, promessa, contraste, identificação, micro-tutorial, polarizador)

**Resultado esperado:** você escolhe 1 hook e leva para o `/roteiro-unity`.

---

### Grupo 4 — Produção de conteúdo

---

#### `/carrossel-unity`
**O que faz:** Produz o carrossel completo — do texto ao PNG renderizado, pronto para publicar.

**Quando usar:** Quando o briefing define formato "carrossel".

**Como invocar:**
```
/carrossel-unity
```
(Com o briefing e o hook já aprovados no contexto da conversa.)

**3 fases com checkpoint em cada:**
1. **Texto** — 8 a 10 slides com estrutura narrativa
2. **Imagens** — geração via GPT Image 2 para capa e slides de impacto
3. **HTML + PNG** — renderização via Playwright (1080×1350px)

**O que entrega:**
```
conteudo/carrosseis/[periodo]/[dia-tema]/instagram/
  slide-01.png  (capa)
  slide-02.png
  ...
  slide-10.png
```

---

#### `/carrossel-de-quebra-de-objecao`
**O que faz:** Cria a estrutura de um carrossel específico para desmontar uma objeção — slide a slide, em 3 movimentos: nomeação → reframe → prova.

**Quando usar:** Para conteúdo de fundo de funil, quando quer converter quem está com dúvida sobre o produto. Diferente do carrossel educativo: este foca em conversão.

**Como invocar:**
```
/carrossel-de-quebra-de-objecao [a objeção] [avatar]
```
Exemplo: `/carrossel-de-quebra-de-objecao "[objeção específica]" [avatar]`

**O que precisa fornecer:**
- A objeção exata (como o avatar formula)
- O avatar (arquiteto / construtor / proprietário)
- Opcional: caso real de cliente que tinha essa objeção

**O que entrega:**
- Estrutura slide a slide (9 slides)
  - Slides 1–3: nomeação + validação da objeção
  - Slides 4–7: reframe em camadas
  - Slides 8–9: prova com caso concreto
- Legenda completa para o post
- Handoff para o `/carrossel-unity` produzir o visual

---

#### `/estatico-unity`
**O que faz:** Produz um post estático (card único) — foto de fundo gerada por IA + copy + identidade visual.

**Quando usar:** Quando o briefing define formato "imagem" ou você quer alto impacto visual com texto mínimo.

**Como invocar:**
```
/estatico-unity
```
(Com o briefing aprovado no contexto.)

**3 fases:**
1. Copy + prompt da foto
2. Geração da foto via GPT Image 2
3. Montagem HTML + renderização PNG

**O que entrega:**
```
conteudo/post-estatico/[periodo]/[dia-tema]/
  img-post.png
  post-01.png   ← arquivo final para publicar
```

---

#### `/roteiro-unity`
**O que faz:** Produz roteiros de vídeo para Instagram Reels e TikTok.

**Quando usar:** Quando o briefing define formato "vídeo".

**Como invocar:**
```
/roteiro-unity [orgânico / tráfego pago]
```

**Dois modos:**
- **Orgânico** — autoridade, educação, marca → motor Ogilvy
- **Tráfego pago** — conversão, resposta direta → motor Schwartz

**O que entrega:** roteiro completo com duração por cena, narração, orientações de câmera e corte.

---

### Grupo 5 — Legendas

---

#### `/legenda-para-carrossel`
**O que faz:** Escreve a legenda do carrossel — orientada a saves, com CTA específico.

**Quando usar:** Após o carrossel estar pronto (textos aprovados).

**Como invocar:**
```
/legenda-para-carrossel
```
(Com o tema e a mensagem central do carrossel no contexto.)

**Estrutura da legenda entregue:**
- Linha de abertura (hook que filtra quem vai ler)
- Corpo complementar (aprofunda sem repetir os slides)
- CTA com razão específica para salvar

---

#### `/legenda-para-reel`
**O que faz:** Escreve a legenda do Reel — a primeira linha que aparece antes do play, o corpo que complementa sem repetir o roteiro, e o CTA.

**Quando usar:** Após o roteiro estar pronto.

**Como invocar:**
```
/legenda-para-reel
```

**Regra crítica:** a legenda nunca repete o que foi dito no vídeo. Ela complementa, adiciona contexto ou aprofunda um ponto.

---

#### `/legenda-para-post-estatico`
**O que faz:** Escreve a legenda para post estático — 4 tipos disponíveis: narrativa, reflexão, lançamento ou conexão.

**Quando usar:** Após o post estático estar pronto.

**Como invocar:**
```
/legenda-para-post-estatico [tipo: narrativa / reflexão / lançamento / conexão]
```

---

### Grupo 6 — Imagem

---

#### `/gerador-de-prompts-de-imagem`
**O que faz:** Constrói um prompt estruturado e otimizado para o `gpt-image-1` — para capas de carrossel, posts estáticos, stories.

**Quando usar:** Antes de gerar qualquer imagem via IA, quando quiser um prompt mais elaborado do que o padrão gerado pelas skills de produção.

**Como invocar:**
```
/gerador-de-prompts-de-imagem [uso da imagem] [o que deve aparecer] [estética] [proporção]
```

**O que entrega:**
- Prompt principal completo e otimizado
- Variação A (mais minimalista)
- Variação B (mais impactante)
- Comando PowerShell pronto para copiar e executar

---

#### `/gerador-de-prompts-para-imagens-de-produto`
**O que faz:** Versão especializada do gerador de prompts, focada nos estilos fotográficos configurados em `marca/DESIGN.md`.

**Quando usar:** Quando a imagem precisa mostrar o produto da empresa — produto instalado, detalhes técnicos, produto em contexto de uso.

**Como invocar:**
```
/gerador-de-prompts-para-imagens-de-produto [linha/variante] [estilo: architectural_installation / dark_lifestyle / product_closeup]
```

**Os 3 estilos:**
- `architectural_installation` — produto instalado em projeto acabado, luz natural, ambiente premium
- `dark_lifestyle` — pessoa em ação no ambiente (arquiteto em obra, proprietário apreciando)
- `product_closeup` — macro do produto com detalhes técnicos específicos

**O que entrega:** prompts para os 3 estilos + comando PowerShell pronto

---

### Grupo 7 — Distribuição

---

#### `/1-conteudo-em-7-formatos`
**O que faz:** Pega um conteúdo aprovado (post, roteiro, briefing) e adapta para 7 canais diferentes — sem copiar o mesmo texto, adaptando a gramática de cada plataforma.

**Quando usar:** Após aprovar um conteúdo que vale distribuir além do Instagram.

**Como invocar:**
```
/1-conteudo-em-7-formatos [cole o conteúdo original]
```

**Os 7 formatos entregues:**
1. **Reel / TikTok** — script de narração com marcações de pausa, legenda curta
2. **Carrossel Instagram** — estrutura de 7 slides
3. **Post estático** — conceito visual + legenda
4. **Sequência de Stories** — 4 a 5 cards com interação sugerida
5. **Thread Twitter/X** — 6 a 8 tweets numerados
6. **Post LinkedIn** — 200 a 400 palavras, tom técnico-profissional B2B
7. **E-mail / Newsletter** — 300 a 500 palavras com assunto + 2 alternativas para teste A/B

---

### Grupo 8 — Sistema

---

#### `/syncar`
Salva tudo no GitHub. Usar ao final de toda sessão produtiva.

#### `/setup`
Configura o repositório para um novo negócio. Usar apenas na primeira vez.

#### `/mapear`
Entrevista você sobre um processo repetitivo e cria uma skill nova.

---

## Fluxos sequenciais por objetivo

### Fluxo 1 — Carrossel educativo (mais comum)

```
Passo 1: /gerador-de-angulos-para-um-tema [tema]
         → escolhe 1 dos 10 ângulos

Passo 2: /briefing-unity [ângulo escolhido]
         → aprova o briefing [A]

Passo 3: /hooks-para-carrossel
         → escolhe 1 das 5 capas

Passo 4: /carrossel-unity
         → aprova textos → aprova imagens → aprova slides renderizados

Passo 5: /legenda-para-carrossel
         → legenda pronta para colar no Instagram

Passo 6 (opcional): /1-conteudo-em-7-formatos
         → distribui para LinkedIn, e-mail, stories etc.
```

**Resultado final:** pasta `conteudo/carrosseis/[periodo]/[dia-tema]/instagram/` com todos os PNGs + legenda pronta.

**Tempo estimado:** 30–60 min (dependendo das aprovações e do tempo de geração de imagem).

---

### Fluxo 2 — Carrossel de quebra de objeção (fundo de funil)

```
Passo 1: /banco-de-objecoes-do-avatar [avatar]
         → identifica as objeções prioritárias

Passo 2: /carrossel-de-quebra-de-objecao [objeção escolhida] [avatar]
         → estrutura do carrossel aprovada

Passo 3: /carrossel-unity
         → produz o visual com a estrutura do passo 2

Passo 4: /legenda-para-carrossel
         → legenda orientada a conversão
```

**Resultado final:** carrossel completo pronto para publicar, focado em converter leads com dúvidas sobre o produto.

---

### Fluxo 3 — Post estático

```
Passo 1: /briefing-unity [tema]
         → define mensagem central e orientação visual

Passo 2: /gerador-de-prompts-de-imagem  ou  /gerador-de-prompts-para-imagens-de-produto
         → prompt otimizado para a foto de fundo

Passo 3: /estatico-unity
         → gera foto → monta HTML → renderiza PNG

Passo 4: /legenda-para-post-estatico [tipo]
         → legenda pronta
```

**Resultado final:** `post-01.png` pronto para publicar + legenda.

---

### Fluxo 4 — Reel orgânico

```
Passo 1: /gerador-de-angulos-para-um-tema [tema]
         → escolhe ângulo com potencial para vídeo curto

Passo 2: /briefing-unity [ângulo]
         → aprovar formato "vídeo orgânico"

Passo 3: /hooks-para-instagram-reels
         → escolhe hook (primeiro frame + frase de abertura)

Passo 4: /roteiro-unity orgânico
         → roteiro completo com cenas, narração, orientações de edição

Passo 5: /legenda-para-reel
         → legenda que complementa o vídeo
```

**Resultado final:** roteiro pronto para gravar + legenda completa.

---

### Fluxo 5 — Planejamento mensal + produção

```
Passo 1: /calendario-comercial [mês] [ano]
         → aprova o calendário com janelas 🟢🟡🔴

Passo 2: Para cada janela verde do calendário:
         → /briefing-unity [tema da janela]
         → escolhe o formato (carrossel, estático ou reel)
         → segue o fluxo correspondente (1, 3 ou 4 acima)

Passo 3 (ao final de cada sessão): /syncar
         → tudo salvo no GitHub
```

---

### Fluxo 6 — Escalar um conteúdo para vários canais

```
Passo 1: Aprova um conteúdo (carrossel, reel ou post) por qualquer fluxo acima

Passo 2: /1-conteudo-em-7-formatos
         → cole o conteúdo aprovado
         → escolhe quais dos 7 formatos quer (pode ser todos ou seleção)

Resultado: 7 adaptações prontas — Reel, Carrossel, Stories, Thread, LinkedIn, E-mail, Post estático
```

**Quando usar este fluxo:** quando um conteúdo performa bem ou quando quer extrair o máximo de um único tema sem escrever do zero para cada canal.

---

## Tabela rápida — skill certa para cada situação

| Situação | Skill |
|---|---|
| Tenho um tema, não sei qual ângulo | `/gerador-de-angulos-para-um-tema` |
| Quero ângulos segmentados por audiência | `/gerador-de-angulos-de-conteudo` |
| Quero entender o que trava meu cliente | `/banco-de-objecoes-do-avatar` |
| Quero planejar o mês inteiro | `/calendario-comercial` |
| Quero definir a mensagem de um post | `/briefing-unity` |
| Quero 5 opções de capa para carrossel | `/hooks-para-carrossel` |
| Quero opções de abertura para Reel | `/hooks-para-instagram-reels` |
| Quero produzir um carrossel educativo | `/carrossel-unity` |
| Quero um carrossel que converte objeção | `/carrossel-de-quebra-de-objecao` → `/carrossel-unity` |
| Quero um post visual impactante | `/estatico-unity` |
| Quero um roteiro de Reel | `/roteiro-unity` |
| Quero a legenda do carrossel | `/legenda-para-carrossel` |
| Quero a legenda do Reel | `/legenda-para-reel` |
| Quero a legenda do post estático | `/legenda-para-post-estatico` |
| Quero um prompt melhor para imagem | `/gerador-de-prompts-de-imagem` |
| Quero foto do produto da empresa | `/gerador-de-prompts-para-imagens-de-produto` |
| Quero distribuir o conteúdo em outros canais | `/1-conteudo-em-7-formatos` |
| Quero salvar o trabalho no GitHub | `/syncar` |
| Quero criar uma skill para um processo meu | `/mapear` |

---

## O que nunca pular

1. **Nunca gerar imagem sem briefing aprovado** — a foto de fundo custa dinheiro, refazer custa mais.
2. **Nunca pular o hook** — o `/hooks-para-carrossel` e o `/hooks-para-instagram-reels` existem porque a capa decide se o post performa ou não.
3. **Nunca copiar o mesmo texto para todos os canais** — o `/1-conteudo-em-7-formatos` adapta a gramática de cada plataforma. Copiar e colar mata o alcance.
4. **Sempre usar `/syncar` ao final da sessão** — todo o conteúdo gerado fica em arquivo local. Sem o push, o backup não existe.
