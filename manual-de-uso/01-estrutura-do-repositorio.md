# Estrutura do Repositório — Cada Arquivo Explicado

## Mapa completo de pastas

```
Design-template/
│
├── CLAUDE.md                        ← Regras do sistema (lido automaticamente)
├── MAPA-TECNICO.md                  ← Documentação técnica do projeto
├── PROJETO.md                       ← Visão geral do projeto (status de implementação)
├── README.md                        ← Introdução ao repositório
├── skills-lock.json                 ← Versões das skills instaladas
│
├── _contexto/                       ← Memória da empresa (não apagar)
│   ├── empresa.md
│   ├── preferencias.md
│   ├── estrategia.md
│   └── referencias.md
│
├── marca/
│   └── DESIGN.md                    ← Identidade visual completa
│
├── credentials/                     ← API keys (nunca commitadas)
│   ├── openai_key.txt
│   ├── gemini.txt
│   ├── meta.txt
│   └── .gitkeep
│
├── conteudo/                        ← Output do sistema (criado automaticamente)
│   └── carrosseis/
│       └── [tema-do-conteudo]/
│           └── carousel-text.md
│
├── dados/                           ← Arquivos para análise (CSV, PDF, prints)
│
├── .env.example                     ← Template das variáveis de ambiente
│
├── .claude/
│   ├── settings.json                ← Configurações do Claude Code
│   ├── settings.local.json          ← Configurações locais (não commitadas)
│   ├── commands/                    ← Comandos do sistema (setup, syncar, mapear)
│   │   ├── setup.md
│   │   ├── syncar.md
│   │   └── mapear.md
│   └── skills/                      ← 19 skills locais do projeto
│       ├── gerador-de-angulos-para-um-tema/
│       │   └── SKILL.md
│       ├── gerador-de-angulos-de-conteudo/
│       │   └── SKILL.md
│       ├── banco-de-objecoes-do-avatar/
│       │   └── SKILL.md
│       ├── calendario-comercial/
│       │   ├── SKILL.md
│       │   └── Agent_Template.md
│       ├── briefing-unity/
│       │   └── briefing-unity.md
│       ├── hooks-para-carrossel/
│       │   └── SKILL.md
│       ├── hooks-para-instagram-reels/
│       │   └── SKILL.md
│       ├── carrossel-unity/
│       │   └── SKILL.md
│       ├── carrossel-de-quebra-de-objecao/
│       │   └── SKILL.md
│       ├── estatico-unity/
│       │   └── SKILL.md
│       ├── roteiro-unity/
│       │   └── SKILL.md
│       ├── legenda-para-carrossel/
│       │   └── SKILL.md
│       ├── legenda-para-reel/
│       │   └── SKILL.md
│       ├── legenda-para-post-estatico/
│       │   └── SKILL.md
│       ├── gerador-de-prompts-de-imagem/
│       │   └── SKILL.md
│       ├── gerador-de-prompts-para-imagens-de-produto/
│       │   └── SKILL.md
│       ├── 1-conteudo-em-7-formatos/
│       │   └── SKILL.md
│       ├── gpt-image2-unity/           ← motor
│       │   ├── SKILL.md
│       │   └── gerar-imagem.py         ← Script Python da geração de imagem
│       ├── ogilvy-copy/                ← motor
│       │   └── SKILL.md
│       └── schwartz-copy/              ← motor
│           └── SKILL.md
│
└── templates/                       ← Templates para criar novas skills
    ├── ferramentas/
    │   └── catalogo.md              ← APIs e ferramentas disponíveis
    ├── marca/
    │   └── exemplos/                ← Exemplos de design guides
    ├── perfis/                      ← Templates de CLAUDE.md por tipo de negócio
    └── skills/                      ← Templates de skills para personalizar
```

---

## Arquivos raiz

### `CLAUDE.md`
O arquivo mais importante do repositório. É lido pelo Claude em toda conversa e define:
- O que este workspace é e como se comportar
- Quais arquivos de contexto ler no início de cada conversa
- Quais skills estão disponíveis e para que servem
- O fluxo principal de conteúdo
- Regras de comportamento (o que nunca fazer, como aprender com correções)

**Nunca apague este arquivo.** Sem ele, o Claude não sabe que está num workspace de conteúdo configurado para a empresa.

### `skills-lock.json`
Registra as versões das skills instaladas. Funciona como um `package-lock.json`: garante que você saiba exatamente qual versão de cada skill está rodando. Não edite manualmente.

---

## Pasta `_contexto/` — A memória da empresa

Esta pasta é o cérebro do sistema. O Claude lê esses arquivos no início de cada conversa para saber quem é a empresa e como se comportar.

### `_contexto/empresa.md`
**O que contém:** Descrição completa da empresa — o que faz, quem é o público-alvo, modelo de negócio, posicionamento, objeções frequentes, canais ativos.

**Por que importa:** Sem este arquivo, o Claude não sabe para qual empresa está trabalhando nem quais são os produtos e posicionamento. Com ele, qualquer copy gerada menciona os termos certos, o posicionamento correto e os argumentos de venda adequados.

**Quando atualizar:** Sempre que algo mudar na empresa — novos produtos, novo público, mudança de posicionamento, novo canal de vendas.

### `_contexto/preferencias.md`
**O que contém:** Tom de voz da marca, palavras recomendadas e proibidas, exemplos de copy no estilo certo e fora de estilo, restrições legais e de compliance.

**Por que importa:** É o filtro de qualidade do texto. Define a diferença entre a linguagem correta da marca e a linguagem inadequada. Também garante que o sistema nunca faça promessas técnicas sem laudo.

**Quando atualizar:** Quando a marca evoluir, quando novas restrições de compliance aparecerem, ou quando um tipo de copy for aprovado/reprovado consistentemente.

### `_contexto/estrategia.md`
**O que contém:** Foco atual do negócio, gaps prioritários a resolver com conteúdo, jornada de conteúdo por etapa do funil, campanhas prioritárias, KPIs.

**Por que importa:** Garante que o calendário e os briefings estejam alinhados com o que a empresa está priorizando agora — não com o que era prioridade há 6 meses.

**Quando atualizar:** A cada trimestre, ou quando a estratégia mudar.

### `_contexto/referencias.md`
**O que contém:** Links e IDs das pastas do Google Drive com material de referência — logos, fotos de produtos, catálogos técnicos, referências de estilo visual.

**Por que importa:** Antes de criar qualquer conteúdo visual, o Claude pode consultar as fotos reais da empresa no Drive para usar como referência de estilo e produto. Isso evita que as imagens geradas por IA fiquem genéricas.

**Exemplo de pastas a configurar:**
- Identidade Visual (logos, assets da marca)
- Fotos do Produto (fotos reais de obras e instalações)
- Catálogo Técnico (documentação dos produtos)
- Referências Visuais (benchmark de marcas do setor)

---

## Arquivo `marca/DESIGN.md` — A identidade visual

Este é o manual de marca em formato estruturado que o sistema consegue ler e aplicar diretamente no código HTML dos posts.

**O que contém:**
- `colors` — paleta completa com HEX de cada cor (primária, secundária, canvas, etc.)
- `typography` — fontes, tamanhos e pesos para cada nível (display, heading, body, label, caption)
- `spacing` — espaçamentos padronizados
- `rounded` — arredondamentos de borda
- Regras do logo
- `components` — especificações de botões, cards, tags
- `image_style` — como devem ser as fotos, os backgrounds, os elementos gráficos
- `layout_templates` — os 7 templates de layout mapeados no benchmark visual da marca

**Variável crítica:** `status: configured`. Quando este campo não está como `configured`, todas as skills de produção visual param e avisam que o DESIGN.md precisa ser configurado. Isso evita que posts sejam gerados com cores improvisadas.

**Cores a configurar (preencher conforme identidade visual da empresa):**
- Cor primária: `[#XXXXXX]`
- Cor secundária: `[#XXXXXX]`
- Canvas (fundo): `[#XXXXXX]`
- Texto: `[#XXXXXX]`

---

## Pasta `credentials/` — As chaves de API

Contém as credenciais necessárias para as integrações com serviços externos. **Esta pasta está no `.gitignore` — nunca é commitada para o GitHub.**

### `credentials/openai_key.txt`
Chave da OpenAI. Necessária para geração de imagens via `gpt-image-1`. Uma linha, só a chave.

### `credentials/gemini.txt`
Chave da API do Google Gemini. Usada pelo motor `nanobanana-unity` como fallback gratuito de geração de imagem.

### `credentials/meta.txt`
Token de acesso à Meta Graph API. Usado pela skill `/publicar-social-unity` para publicar no Instagram e Facebook. **Expira a cada 60 dias** — precisa ser renovado.

---

## Pasta `.claude/skills/` — Os programas do sistema

Cada skill é uma pasta com um arquivo `SKILL.md` que contém as instruções detalhadas de como o Claude deve executar aquela tarefa. São 19 skills no total.

**Ideação e pesquisa**

### `gerador-de-angulos-para-um-tema/`
Pega um tema e gera 10 lentes criativas para abordá-lo. Use antes do briefing quando você tem o assunto mas não sabe o ângulo de entrada.

### `gerador-de-angulos-de-conteudo/`
Versão mais analítica: usa uma matriz perspectivas × audiência × formatos narrativos. Use quando quer segmentar por avatar (arquiteto vs construtor vs proprietário).

### `banco-de-objecoes-do-avatar/`
Mapeia as objeções do ICP em 6 tipos (valor, percepção, confiança técnica, confiança em si mesmo, relevância, urgência) com resposta em formato de conteúdo para cada uma. Alimenta o `/carrossel-de-quebra-de-objecao`.

**Planejamento**

### `calendario-comercial/`
Cria o mapa estratégico de conteúdo do mês. Pesquisa eventos culturais, esportivos e de entretenimento do período para identificar janelas quentes (🟢), mornas (🟡) e frias (🔴). Usa o framework MOMENTO para cruzar produto × momento cultural.

### `briefing-unity/`
Gera o briefing completo de um conteúdo. Lê o output do calendário comercial e produz: gancho, copy base, formato recomendado, orientações visuais, hashtags e metadados. Salva o briefing aprovado em `conteudo/[tipo]/[periodo]/[dia-tema]/`.

**Hooks e capas**

### `hooks-para-carrossel/`
Gera 5 opções de capa para o carrossel, cada uma com headline, direção visual e tipo de gancho diferente. Use após o briefing e antes do `/carrossel-unity`.

### `hooks-para-instagram-reels/`
Gera 7 opções de hook para Reel combinando primeiro frame (visual) com frase de abertura (narração). Use antes do `/roteiro-unity`.

**Produção de conteúdo**

### `carrossel-unity/`
Produz um carrossel completo em 3 fases:
1. Texto dos slides (8-10 slides com texto revisado)
2. Geração de imagens (capa obrigatória + até 2 slides de impacto)
3. HTML por slide → PNG via Playwright

### `carrossel-de-quebra-de-objecao/`
Cria a estrutura de um carrossel de conversão que desmonta uma objeção em 3 movimentos: nomeação → reframe → prova (9 slides). Use para conteúdo de fundo de funil. Entrega a estrutura para o `/carrossel-unity` produzir o visual.

### `estatico-unity/`
Produz um post estático (card único) em 3 fases:
1. Copy + prompt da foto de fundo
2. Geração da foto (GPT Image 2)
3. HTML montado com copy + identidade visual → PNG via Playwright

### `roteiro-unity/`
Produz roteiros de vídeo para Reels e TikTok. Usa Ogilvy para vídeos orgânicos (autoridade, educação) e Schwartz para criativos de tráfego pago (conversão).

**Legendas**

### `legenda-para-carrossel/`
Escreve a legenda do carrossel orientada a saves, com hook de abertura, corpo que complementa os slides (sem repetir) e CTA com razão específica para salvar.

### `legenda-para-reel/`
Escreve a legenda do Reel. Nunca repete o roteiro — complementa, adiciona contexto ou aprofunda um ponto. Inclui primeira linha visível antes do play e CTA.

### `legenda-para-post-estatico/`
Escreve a legenda para post estático em 4 tipos: narrativa, reflexão, lançamento ou conexão.

**Imagem**

### `gerador-de-prompts-de-imagem/`
Constrói um prompt estruturado e otimizado para o `gpt-image-1`. Entrega 3 versões (principal, minimalista, impactante) + comando PowerShell pronto para executar.

### `gerador-de-prompts-para-imagens-de-produto/`
Versão especializada focada nos estilos fotográficos configurados em `marca/DESIGN.md`: `architectural_installation`, `dark_lifestyle` e `product_closeup`. Use quando a imagem precisa mostrar o produto da empresa.

**Distribuição**

### `1-conteudo-em-7-formatos/`
Pega um conteúdo aprovado e adapta para 7 canais (Reel, Carrossel, Post estático, Stories, Thread X, LinkedIn e E-mail), adaptando a gramática de cada plataforma.

**Motores internos**

### `gpt-image2-unity/`
Motor de geração de imagem. Contém a SKILL.md com as instruções e o script Python `gerar-imagem.py` que faz a chamada à API da OpenAI.

**O script `gerar-imagem.py`:**
- Recebe: prompt em inglês, caminho de saída, aspect ratio
- Lê a API key de `credentials/openai_key.txt` (ou da variável de ambiente)
- Chama o modelo `gpt-image-1` com qualidade `high`
- Salva o PNG no caminho informado
- Exit codes: 0 (sucesso), 2 (API key não encontrada), 4 (erro de API)

### `ogilvy-copy/`
Motor de copy baseado na metodologia de David Ogilvy. Usado para conteúdo orgânico, autoridade e construção de marca. Foco em big idea, headlines informativas e copy que constrói reputação a longo prazo.

### `schwartz-copy/`
Motor de copy baseado na metodologia de Eugene Schwartz. Usado para conteúdo de resposta direta e tráfego pago. Foco em consciência do cliente, mecanismo único e conversão.

---

## Pasta `templates/` — Modelos para expansão

Contém templates para quando você quiser criar novas skills ou adaptar o sistema para outro negócio.

### `templates/skills/`
Templates prontos de skills para processos comuns: carrossel, roteiro, proposta comercial, análise de dados, email profissional, etc. Use com `/mapear` para criar skills personalizadas.

### `templates/ferramentas/catalogo.md`
Lista todas as APIs e ferramentas disponíveis no sistema, com descrição de uso e quando acionar cada uma.

### `templates/perfis/`
Templates de `CLAUDE.md` para diferentes tipos de negócio: agência, empresa, freelancer, solopreneur. Útil para replicar o sistema para outros clientes.

---

## Pasta `conteudo/` — O output do sistema

Criada automaticamente quando os primeiros conteúdos são gerados. Cada skill salva seu output numa subpasta organizada por tipo e tema.

```
conteudo/                                    ← convenção: conteudo/[tipo]/[periodo]/[dia-tema]/
  calendarios/
    junho-2026/
      calendario-detalhado.md ← calendário post a post
      _aprovado.md            ← registro da aprovação
      dashboard.html          ← grid visual do mês
  carrosseis/
    junho/
      dia-02-5-criterios-especificacao/
        _briefing.md          ← briefing do conteúdo
        _legenda.md           ← legenda aprovada (lida pelo /publicar-social-unity)
        _prompts-imagens.md   ← prompts das imagens
        _aprovado.md          ← registro do que foi aprovado
        instagram/
          img-slide01.jpg     ← foto de fundo (IA ou foto real do Drive)
          slide-01.html
          slide-01.png        ← slide renderizado (arquivo final)
          slide-02.html
          slide-02.png
          ...
  post-estatico/
    junho/
      dia-06-vedacao-perimetral/
        _briefing.md
        _legenda.md           ← legenda aprovada
        _prompt.md            ← prompt da foto
        img-post.png          ← foto de fundo
        post-01.html          ← layout montado
        post-01.png           ← post final (arquivo para publicar)
        _aprovado.md
  roteiros/
    [periodo]/
      [dia-tema]/
        _briefing.md
        roteiro-[plataforma].md
        _legenda.md
        _aprovado.md
```

**Os arquivos `.png` no nível mais profundo de cada pasta são os arquivos finais** — prontos para publicar.

Os arquivos `_aprovado.md` são o histórico de qualidade: registram o que funcionou bem, o que foi ajustado e o que evitar nas próximas execuções do mesmo tema.
