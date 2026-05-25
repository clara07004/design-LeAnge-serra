# Referência de Skills — O Que Cada Uma Faz

## Como invocar uma skill

Skills são chamadas com `/nome-da-skill` no início da mensagem. O Claude lê o arquivo `SKILL.md` correspondente em `.claude/skills/[nome]/` e segue as instruções.

Você também pode descrever o que quer em linguagem natural — o Claude identifica a skill relevante automaticamente. Por exemplo, "faz um carrossel sobre isolamento acústico" aciona `/carrossel-unity` sem você precisar digitar o comando.

---

## Skills de produção de conteúdo

### `/calendario-comercial`
**Arquivo:** `.claude/skills/calendario-comercial/SKILL.md`

**Para que serve:** Cria o mapa estratégico de oportunidades do mês. Cruza eventos culturais, esportivos e de entretenimento com os produtos e objetivos da empresa para identificar quando postar e com qual ângulo.

**Quando usar:** Uma vez por mês, antes de começar a produção de conteúdo.

**O que precisa ter:**
- `_contexto/empresa.md` configurado
- `_contexto/estrategia.md` configurado
- Acesso à internet (para pesquisar eventos do período)

**O que entrega:**
- Radar cultural do período
- Mapa de oportunidades por semana (🟢🟡🔴)
- Tema narrativo do mês
- Alertas e riscos
- Arquivo salvo em `conteudo/calendarios/[periodo]/`

**Metodologia:** Framework MOMENTO (Mídia, Oportunidades, Metas, Eventos, Narrativa, Timing, Objeções)

---

### `/briefing-unity`
**Arquivo:** `.claude/skills/briefing-unity/briefing-unity.md`

**Para que serve:** Gera o briefing completo de um post específico — gancho, copy, formato, orientações visuais, hashtags. É a ponte entre o calendário estratégico e a produção do asset.

**Quando usar:** Para cada post que vai produzir, após o calendário aprovado. Pode ser usado sem calendário se você já souber o tema.

**O que precisa ter:**
- Tema ou janela do calendário
- Plataforma destino
- Formato pretendido (opcional — o Claude pode recomendar)

**O que entrega:**
1. Gancho (linha de abertura do post)
2. Copy por plataforma
3. Formato recomendado com justificativa
4. Orientações visuais
5. Hashtags por plataforma
6. Metadados (skill a acionar, data ideal)

**Checkpoint de saída:** `[A] Aprovar / [E] Editar / [C] Cancelar`

---

### `/carrossel-unity`
**Arquivo:** `.claude/skills/carrossel-unity/SKILL.md`

**Para que serve:** Produz um carrossel completo — do texto ao PNG renderizado, pronto para publicar.

**Quando usar:** Quando o briefing define formato "carrossel" ou você quer um post de múltiplos slides.

**Dois modos de uso:**

**Fluxo rápido** — tudo em um:
`/carrossel-unity` cuida de texto + prompt + imagem IA + HTML + PNG internamente. Use quando não precisa de controle manual sobre as imagens.

**Fluxo enriquecido** — imagem aprovada antes:
Use `/gerador-de-prompts-para-imagens-de-produto` ou `/gerador-de-prompts-de-imagem` → gere e aprove a imagem via `/gpt-image2-unity` → só então chame `/carrossel-unity`, que monta o HTML usando a imagem já gerada.

> Quando houver fotos reais disponíveis no Google Drive (`_contexto/referencias.md` → pasta "Fotos do Produto"), usá-las tem prioridade sobre geração IA — resultado superior e sem custo de API.

**Fases:**
1. **Texto** (8–10 slides) + 3 opções de capa
2. **Imagens** (Drive, fluxo enriquecido, ou geração automática interna)
3. **HTML + PNG** via Playwright — um arquivo por slide

**Checkpoints:** após texto, após imagens, após slide 1 renderizado, após todos os slides

**Dimensões:** Instagram 1080×1350px | TikTok 1080×1920px (opcional)

**Output:**
```
conteudo/carrosseis/[tema]/instagram/
  img-slide01.png (ou .jpg se veio do Drive)
  slide-01.html → slide-01.png
  slide-02.html → slide-02.png
  ...
```

**Regras importantes:**
- Todo slide tem foto real ou gerada como fundo — nunca fundo sólido com texto
- Cada slide tem layout visual diferente (nunca repete template)
- Fonte nunca abaixo dos valores mínimos do DESIGN.md
- Texto em excesso: cortar parágrafo, nunca reduzir fonte
- Sem labels de seção, eyebrows ou badges de série nos slides

---

### `/estatico-unity`
**Arquivo:** `.claude/skills/estatico-unity/SKILL.md`

**Para que serve:** Produz um post estático (card único) — foto de fundo gerada por IA + copy + identidade visual, tudo montado em HTML e renderizado em PNG.

**Quando usar:** Quando o briefing define formato "imagem" ou você quer um post de alto impacto visual com texto mínimo.

**Fases:**
1. **Copy + prompt da foto** — extraídos do briefing ou fornecidos diretamente
2. **Foto de fundo** via GPT Image 2 (portrait 1024×1536)
3. **HTML** (1080×1350px) com foto + overlay + copy + logo → **PNG**

**Checkpoints:** após copy e prompt, após foto gerada, após post renderizado

**Regra crítica:** fundo de cor sólida é proibido. O post estático SEMPRE tem foto de fundo gerada por IA. Se a OpenAI falhar, tenta Gemini, depois FAL API. Só para se todos os três falharem.

**Output:**
```
conteudo/imagens/[tema]/
  foto-fundo.png
  prompt.txt
  post-01.html
  post-01.png          ← arquivo final para publicar
```

---

### `/roteiro-unity`
**Arquivo:** `.claude/skills/roteiro-unity/SKILL.md`

**Para que serve:** Produz roteiros de vídeo para Instagram Reels e TikTok.

**Quando usar:** Quando o briefing define formato "vídeo" ou você quer produzir conteúdo para Reels.

**Dois modos:**
- **Orgânico** (conteúdo de autoridade, educação, marca) → usa metodologia Ogilvy
- **Tráfego pago** (conversão, resposta direta) → usa metodologia Schwartz

**Output:** roteiro com duração por cena, narração, orientações de câmera e edição.

---

## Skills de pesquisa e ideação

### `/gerador-de-angulos-para-um-tema`
**Arquivo:** `.claude/skills/gerador-de-angulos-para-um-tema/SKILL.md`

**Para que serve:** Pega um tema e gera 10 lentes criativas para abordá-lo — cada uma com ângulo diferente.

**Quando usar:** Antes do briefing, quando você tem o assunto mas não sabe como entrar. Ex: "quero falar sobre PVC, mas não sei qual ângulo".

**Input:** o tema. Pode ser amplo ("PVC") ou específico ("durabilidade das esquadrias no litoral").

**Output:**
- 10 ângulos com: título sugerido, gancho, por que funciona para a Ecoframe
- Pronto para levar ao `/briefing-unity`

---

### `/gerador-de-angulos-de-conteudo`
**Arquivo:** `.claude/skills/gerador-de-angulos-de-conteudo/SKILL.md`

**Para que serve:** Versão mais estruturada — usa uma matriz perspectivas × audiência × formatos narrativos para gerar ângulos com recorte de público.

**Quando usar:** Quando quer segmentar por avatar (arquiteto vs construtor vs proprietário) ou quando o tema é mais complexo.

**Input:** tema + avatar (opcional)

**Output:**
- 10 ângulos com: perspectiva, audiência alvo, formato narrativo, formato de post sugerido

**Diferença do anterior:** mais analítico e estratégico. O `/gerador-de-angulos-para-um-tema` é mais criativo e rápido.

---

### `/banco-de-objecoes-do-avatar`
**Arquivo:** `.claude/skills/banco-de-objecoes-do-avatar/SKILL.md`

**Para que serve:** Mapeia todas as objeções do ICP antes de especificar, comprar ou recomendar a Ecoframe — organizadas em 6 tipos, com resposta em formato de conteúdo para cada uma.

**Quando usar:** Para criar conteúdo de meio/fundo de funil. Também quando posts não estão convertendo.

**Input:** avatar — `arquiteto`, `construtor` ou `proprietário`

**Output:**
- 6 tipos de objeção (valor, percepção, confiança técnica, confiança em si mesmo, relevância, urgência)
- Para cada objeção: como o avatar formula, raiz real, resposta em conteúdo, resposta em copy
- Top 3 objeções mais críticas
- Plano de conteúdo com 1 post sugerido por objeção

**Resultado esperado:** cada objeção vira input para o `/carrossel-de-quebra-de-objecao`

---

## Skills de hooks e capas

### `/hooks-para-carrossel`
**Arquivo:** `.claude/skills/hooks-para-carrossel/SKILL.md`

**Para que serve:** Gera 5 opções de capa para o carrossel — headline, subtítulo, direção visual e tipo de gancho para cada uma.

**Quando usar:** Após o briefing aprovado, antes do `/carrossel-unity`.

**Input:** tema ou briefing aprovado (no contexto da conversa)

**Output:**
- 5 opções de capa com: headline, subtítulo opcional, direção visual, tipo de gancho (promessa, dor, número, polêmica, identificação, antes/depois, dado)

**Resultado esperado:** você escolhe 1 capa e leva para o `/carrossel-unity`

---

### `/hooks-para-instagram-reels`
**Arquivo:** `.claude/skills/hooks-para-instagram-reels/SKILL.md`

**Para que serve:** Gera 7 opções de hook para Reel — combinando o que aparece no primeiro frame com a frase de abertura.

**Quando usar:** Após o briefing aprovado, antes do `/roteiro-unity`.

**Input:** tema ou briefing aprovado

**Output:**
- 7 hooks com: primeiro frame (visual), frase de abertura (narração), tipo de gancho (salvável, compartilhável, promessa, contraste, identificação, micro-tutorial, polarizador)

**Resultado esperado:** você escolhe 1 hook e leva para o `/roteiro-unity`

---

## Skills de fundo de funil

### `/carrossel-de-quebra-de-objecao`
**Arquivo:** `.claude/skills/carrossel-de-quebra-de-objecao/SKILL.md`

**Para que serve:** Cria a estrutura de um carrossel que desmonta uma objeção específica do ICP em 3 movimentos: nomeação → reframe → prova. Focado em conversão — diferente do carrossel educativo.

**Quando usar:** Para conteúdo de fundo de funil. Use após o `/banco-de-objecoes-do-avatar` para transformar cada objeção em um carrossel.

**Input:**
- A objeção exata (como o avatar formula)
- Avatar (`arquiteto`, `construtor` ou `proprietário`)
- Caso real de cliente (opcional, mas aumenta a prova)

**Output:**
- Estrutura de 9 slides:
  - Slides 1–3: nomeação + validação da objeção
  - Slides 4–7: reframe em camadas
  - Slides 8–9: prova com caso concreto
- Legenda completa do post
- Handoff direto para o `/carrossel-unity` produzir o visual

---

## Skills de legendas

### `/legenda-para-carrossel`
**Arquivo:** `.claude/skills/legenda-para-carrossel/SKILL.md`

**Para que serve:** Escreve a legenda do carrossel — orientada a saves, com CTA específico.

**Quando usar:** Após o carrossel estar produzido (textos aprovados).

**Input:** tema e mensagem central do carrossel (no contexto da conversa)

**Output:**
- Linha de abertura (hook que filtra quem vai ler)
- Corpo complementar (aprofunda sem repetir os slides)
- CTA com razão específica para salvar

---

### `/legenda-para-reel`
**Arquivo:** `.claude/skills/legenda-para-reel/SKILL.md`

**Para que serve:** Escreve a legenda do Reel. Nunca repete o roteiro — complementa, adiciona contexto ou aprofunda um ponto.

**Quando usar:** Após o roteiro estar pronto.

**Input:** tema e mensagem central do reel (no contexto)

**Regra crítica:** a legenda não repete o que foi dito no vídeo. Ela complementa.

**Output:** primeira linha (visível antes do play) + corpo + CTA

---

### `/legenda-para-post-estatico`
**Arquivo:** `.claude/skills/legenda-para-post-estatico/SKILL.md`

**Para que serve:** Escreve a legenda para post estático em 4 tipos disponíveis.

**Quando usar:** Após o post estático estar produzido.

**Input:** tipo desejado + tema (`narrativa`, `reflexão`, `lançamento` ou `conexão`)

**Output:** legenda no tipo escolhido, com abertura, corpo e CTA adequados ao formato

---

## Skills de imagem

Existem três caminhos para obter imagens para os posts. Use o melhor para cada situação:

| Caminho | Quando usar | Resultado |
|---|---|---|
| **Fotos reais do Drive** | Quando há foto de instalação ou produto disponível | Melhor — fotos reais de obra |
| `/gerador-de-prompts-para-imagens-de-produto` → `/gpt-image2-unity` | Imagem de produto em estética específica, ou quando Drive não tem o que precisa | Muito bom — prompt calibrado para Ecoframe |
| `/gerador-de-prompts-de-imagem` → `/gpt-image2-unity` | Imagem de contexto ou cena genérica | Bom — prompt estruturado mas menos específico |

---

### `/gerador-de-prompts-para-imagens-de-produto`
**Arquivo:** `.claude/skills/gerador-de-prompts-para-imagens-de-produto/SKILL.md`

**Para que serve:** Constrói prompts otimizados para as 3 estéticas fotográficas da Ecoframe. Mais preciso que o genérico porque conhece as linhas de produto e os estilos da marca.

**Quando usar:** Quando a imagem precisa mostrar o produto Ecoframe — esquadrias instaladas, detalhes técnicos, produto em contexto arquitetônico. Use este antes do genérico sempre que o produto for o foco.

**Input:** linha (`iTEC`, `euroTEC`, `TECplus100` ou `MAXXI`) + estilo desejado

**Os 3 estilos:**
- `architectural_installation` — produto instalado em projeto acabado, luz natural, ambiente premium
- `dark_lifestyle` — pessoa em ação no ambiente (arquiteto em obra, proprietário apreciando)
- `product_closeup` — macro do perfil PVC, câmaras internas, detalhes de vedação

**Output:** prompt principal + variação + comando PowerShell para `/gpt-image2-unity`

---

### `/gerador-de-prompts-de-imagem`
**Arquivo:** `.claude/skills/gerador-de-prompts-de-imagem/SKILL.md`

**Para que serve:** Constrói um prompt estruturado e otimizado para `gpt-image-1` para qualquer tipo de cena — não específico de produto.

**Quando usar:** Quando a imagem é de contexto (cena arquitetônica, ambiente, atmosfera) e não precisa mostrar o produto diretamente. Segunda opção quando o `/gerador-de-prompts-para-imagens-de-produto` não se aplica.

**Input:** uso da imagem + o que deve aparecer + estética + proporção

**Output:**
- Prompt principal completo e otimizado
- Variação A (mais minimalista)
- Variação B (mais impactante)
- Comando PowerShell pronto para `/gpt-image2-unity`

---

## Skills de distribuição

### `/1-conteudo-em-7-formatos`
**Arquivo:** `.claude/skills/1-conteudo-em-7-formatos/SKILL.md`

**Para que serve:** Pega um conteúdo aprovado e adapta para 7 canais — adaptando a gramática de cada plataforma, sem copiar o mesmo texto.

**Quando usar:** Após aprovar um conteúdo que vale distribuir além do Instagram.

**Input:** conteúdo original (post, roteiro ou briefing aprovado)

**Os 7 formatos entregues:**
1. **Reel / TikTok** — script de narração com marcações de pausa, legenda curta
2. **Carrossel Instagram** — estrutura de 7 slides
3. **Post estático** — conceito visual + legenda
4. **Sequência de Stories** — 4 a 5 cards com interação sugerida
5. **Thread Twitter/X** — 6 a 8 tweets numerados
6. **Post LinkedIn** — 200 a 400 palavras, tom técnico-profissional B2B
7. **E-mail / Newsletter** — 300 a 500 palavras com assunto + 2 alternativas para teste A/B

---

## Motores (usados internamente pelas skills)

### `/gpt-image2-unity`
**Arquivo:** `.claude/skills/gpt-image2-unity/SKILL.md`
**Script:** `.claude/skills/gpt-image2-unity/gerar-imagem.py`

**Para que serve:** Gera imagens usando o modelo `gpt-image-1` da OpenAI.

**Quando chamar diretamente:** quando precisar de uma imagem avulsa, fora do fluxo de carrossel ou post estático.

**Parâmetros do script:**
```powershell
python "gerar-imagem.py" "PROMPT_EM_INGLÊS" "CAMINHO_DE_SAÍDA.png" "ASPECT_RATIO"
```

**Aspect ratios:**
- `square` → 1024×1024 (Instagram feed quadrado)
- `portrait` → 1024×1536 (Instagram/TikTok vertical)
- `landscape` → 1536×1024 (LinkedIn banner)

**Leitura da API key:** o script procura em `credentials/openai_key.txt`. Se não encontrar, busca na variável de ambiente `OPENAI_API_KEY`.

**Exit codes:**
- `0` — sucesso
- `2` — API key não encontrada
- `4` — erro de API (quota, prompt inválido, etc.)

**Cadeia de fallback:**
```
GPT Image 2 (OpenAI) → nanobanana-unity (Gemini, grátis) → image-gen-unity (FAL API, pago)
```

**Custo aproximado:** $0,02–$0,10 por imagem (quality: high)

**Regras de prompt:**
- Sempre em inglês
- Incluir estilo fotográfico: `professional photography`, `architectural photography`
- Incluir: `no text overlay`, `no watermarks`, `no people` (a menos que o briefing peça)
- Nunca: obras com EPI incorreto, texto embutido na imagem, ilustrações genéricas

---

### `/ogilvy-copy`
**Arquivo:** `.claude/skills/ogilvy-copy/SKILL.md`

**Para que serve:** Motor de escrita baseado na metodologia de David Ogilvy. Usado para copy de marca, conteúdo orgânico, construção de autoridade.

**Princípios aplicados:**
- Pesquisa profunda antes de escrever
- Big idea que conecta produto e desejo humano
- Headlines informativas (não enigmáticas)
- Copy que vende sem parecer que está vendendo
- Foco no benefício real, não no produto em si

**Usado por:** `/roteiro-unity` (modo orgânico), `/briefing-unity`

---

### `/schwartz-copy`
**Arquivo:** `.claude/skills/schwartz-copy/SKILL.md`

**Para que serve:** Motor de escrita baseado na metodologia de Eugene Schwartz. Usado para copy de resposta direta, tráfego pago, conversão.

**Princípios aplicados:**
- Identificar o nível de consciência do cliente
- Mecanismo único que explica como o produto funciona
- Headlines que capturam a atenção no estado certo
- Copy que move o leitor pelo funil de decisão

**Usado por:** `/roteiro-unity` (modo tráfego pago), `/briefing-unity` (para conversão)

---

## Comandos do sistema

### `/syncar`
**Arquivo:** `.claude/commands/syncar.md`

**Para que serve:** Salva o estado atual do repositório no GitHub (git add + commit + push).

**Quando usar:**
- Ao final de uma sessão produtiva
- Antes de uma pausa longa
- Sempre que quiser garantir backup do conteúdo gerado

**O que faz:**
1. Verifica se o git está configurado
2. Identifica arquivos novos e modificados
3. Faz commit com mensagem descritiva
4. Faz push para o repositório remoto

---

### `/setup`
**Arquivo:** `.claude/commands/setup.md`

**Para que serve:** Configura o sistema para um novo negócio. Guia o preenchimento dos arquivos de contexto e do DESIGN.md através de uma entrevista estruturada.

**Quando usar:** na primeira vez que usar o repositório para um novo cliente, ou quando quiser reconfigurar completamente.

---

### `/mapear`
**Arquivo:** `.claude/commands/mapear.md`

**Para que serve:** Entrevista você sobre processos repetitivos e cria skills personalizadas.

**Quando usar:** quando identificar uma tarefa que faz frequentemente e quer automatizar com uma skill específica.

**Perguntas durante o /mapear:**
- Qual é a tarefa?
- Quantas vezes por semana/mês você faz isso?
- Quais são os passos?
- Qual é o output esperado?
- É específica desta empresa ou útil em qualquer projeto?

---

## Tabela resumo — skills por formato de conteúdo

| Formato | Skill principal | Imagem (em ordem de preferência) | Motor de copy |
|---|---|---|---|
| Carrossel (rápido) | `/carrossel-unity` | Drive → geração interna automática | Direto na skill |
| Carrossel (enriquecido) | `/gerador-de-prompts-para-imagens-de-produto` → `/gpt-image2-unity` → `/carrossel-unity` | Drive → prompt enriquecido → GPT | Direto na skill |
| Carrossel de objeção | `/carrossel-de-quebra-de-objecao` → `/carrossel-unity` | Drive → GPT automático | Direto na skill |
| Post estático | `/gerador-de-prompts-para-imagens-de-produto` → `/gpt-image2-unity` → `/estatico-unity` | Prompt enriquecido → GPT | Direto na skill |
| Reel/TikTok orgânico | `/roteiro-unity` | — | `ogilvy-copy` |
| Reel/TikTok pago | `/roteiro-unity` | — | `schwartz-copy` |
| Imagem avulsa | `/gpt-image2-unity` | GPT direto | — |
| Calendário | `/calendario-comercial` | — | — |
| Briefing | `/briefing-unity` | — | `ogilvy-copy` ou `schwartz-copy` |

---

## Tabela resumo — skills por objetivo

| Objetivo | Skill |
|---|---|
| Tenho um tema, não sei qual ângulo | `/gerador-de-angulos-para-um-tema` |
| Quero ângulos segmentados por audiência | `/gerador-de-angulos-de-conteudo` |
| Quero entender o que trava meu cliente | `/banco-de-objecoes-do-avatar` |
| Mapear o mês estrategicamente | `/calendario-comercial` |
| Definir o que um post vai comunicar | `/briefing-unity` |
| Escolher a melhor capa para o carrossel | `/hooks-para-carrossel` |
| Escolher o melhor hook para o Reel | `/hooks-para-instagram-reels` |
| Produzir um carrossel educativo | `/carrossel-unity` |
| Produzir um carrossel que converte objeção | `/carrossel-de-quebra-de-objecao` → `/carrossel-unity` |
| Impacto visual rápido no feed | `/estatico-unity` |
| Conteúdo em vídeo (orgânico) | `/roteiro-unity` |
| Anúncio em vídeo (tráfego pago) | `/roteiro-unity` |
| Escrever a legenda do carrossel | `/legenda-para-carrossel` |
| Escrever a legenda do Reel | `/legenda-para-reel` |
| Escrever a legenda do post estático | `/legenda-para-post-estatico` |
| Criar um prompt melhor para imagem | `/gerador-de-prompts-de-imagem` |
| Criar foto do produto Ecoframe | `/gerador-de-prompts-para-imagens-de-produto` |
| Distribuir um conteúdo para outros canais | `/1-conteudo-em-7-formatos` |
| Gerar uma foto avulsa | `/gpt-image2-unity` |
| Salvar o trabalho no GitHub | `/syncar` |
| Criar uma nova skill personalizada | `/mapear` |
