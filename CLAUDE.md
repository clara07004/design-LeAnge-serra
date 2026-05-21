# Unity Content — Claude Code OS

## O que é esse workspace

> **Este projeto é uma base/template.** Não é executado diretamente aqui — projetos reais são replicados a partir deste. Credenciais, contexto (`_contexto/`) e outputs (`conteudo/`) ficam no projeto replicado, não aqui. Nunca tentar testar, executar scripts ou verificar configurações neste workspace.

Sistema de automação do processo de criação de conteúdo para redes sociais do Grupo Unity. Orquestra skills de IA para ir da definição estratégica até a entrega do pacote de conteúdo pronto para publicação.

**Empresa:** Ecoframe — Esquadrias em PVC de alta performance (Steel Frame, Drywall, arquitetura contemporânea).

**Estrutura de pastas:**
- `_contexto/` — memória do sistema (não apagar)
- `marca/` — DESIGN.md e identidade visual
- `dados/` — arquivos para análise (CSV, PDF, prints, referências)
- `templates/skills/` — templates de skills prontos pra personalizar com /mapear
- `templates/ferramentas/catalogo.md` — APIs e ferramentas disponíveis pra usar em skills
- `credentials/` — credenciais e tokens (não committar)

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar
4. `_contexto/referencias.md` — pastas do Google Drive com material de referência visual

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/DESIGN.md` como referência de estilo.

**Referências visuais do Drive:** quando `_contexto/referencias.md` tiver pastas configuradas, consultá-las antes de criar qualquer conteúdo visual. Usar o MCP do Google Drive para listar os arquivos da pasta relevante (`search_files` com `parentId = 'ID_DA_PASTA'`) e baixar as imagens com `download_file_content`. Priorizar imagens menores que 300KB para caber no contexto. Usar o material encontrado como referência de estilo, produto e padrão visual — não como template a copiar literalmente.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Skills disponíveis

**Skills do sistema CCOS (genéricas):**
- `/setup` — configura o sistema pro seu negócio (rodar na primeira vez)
- `/syncar` — salva o trabalho no GitHub (commit + push)
- `/mapear` — entrevista processos repetitivos e cria skills personalizadas

**Skills de conteúdo Unity:**
- `/calendario-comercial` — mapa de oportunidades do período (quando e o quê postar)
- `/briefing-unity` — briefing completo de um tema: objetivo, mensagem, formato, referências
- `/carrossel-unity` — produção de carrossel: texto + HTML + PNG via Playwright
- `/estatico-unity` — produção de post card único: foto IA + HTML + PNG via Playwright
- `/roteiro-unity` — roteiro de vídeo para Reels/TikTok (orgânico via Ogilvy, tráfego via Schwartz)
- `/publicar-social-unity` — publica conteúdo aprovado no Instagram, TikTok, LinkedIn
- `/triagem-youtube-unity` — análise editorial para YouTube

**Skills de pesquisa e ideação:**
- `/gerador-de-angulos-para-um-tema` — 10 lentes criativas para explorar um tema antes do briefing
- `/gerador-de-angulos-de-conteudo` — matrix perspectivas × audiência × formatos narrativos, 10 ângulos únicos
- `/banco-de-objecoes-do-avatar` — mapeia 6 tipos de objeção por ICP com resposta em conteúdo

**Skills de copy e distribuição:**
- `/hooks-para-carrossel` — 5 opções de capa para carrossel com direção visual (usar antes do /carrossel-unity)
- `/hooks-para-instagram-reels` — 7 tipos de hook combinados (primeiro frame + frase de abertura)
- `/legenda-para-carrossel` — legenda orientada a save com CTA específico
- `/legenda-para-reel` — legenda que complementa o vídeo sem repetir o script
- `/legenda-para-post-estatico` — 4 tipos de legenda para post estático
- `/carrossel-de-quebra-de-objecao` — carrossel de fundo de funil em 3 movimentos (nomeação → reframe → prova)
- `/1-conteudo-em-7-formatos` — repurposing: transforma 1 conteúdo em Reel, Carrossel, Story, Thread, LinkedIn, E-mail e Post estático

**Skills de imagem:**
- `/gerador-de-prompts-de-imagem` — prompt estruturado para gpt-image-1 (usar antes de gerar imagem)
- `/gerador-de-prompts-para-imagens-de-produto` — prompts para as 3 estéticas de produto da Ecoframe (dark_lifestyle, architectural_installation, product_closeup)

**Motores (usados internamente pelas skills de produção):**
- `/gpt-image2-unity` — gera foto de fundo via GPT Image 2 (motor de imagem do carrossel e post estático)
- `/nanobanana-unity` — fallback de imagem via Gemini (grátis)
- `/image-gen-unity` — contingência de imagem via FAL API (pago)
- `/ogilvy-copy` — copy de marca e conteúdo orgânico (motor do roteiro orgânico)
- `/schwartz-copy` — copy de resposta direta (motor do roteiro de tráfego pago)

---

## Fluxo principal de conteúdo

```
/gerador-de-angulos-para-um-tema  ou  /gerador-de-angulos-de-conteudo   ← ideação
    ↓ [escolhe ângulo]
/calendario-comercial
    ↓ [aprova calendário]
/briefing-unity  →  define o formato do conteúdo
    ↓ [aprova briefing]
    ├── formato carrossel  →  /hooks-para-carrossel
    │                              ↓
    │                         /carrossel-unity  (motor: gpt-image2-unity)
    │                              ↓
    │                         /legenda-para-carrossel
    │
    ├── formato imagem     →  /gerador-de-prompts-de-imagem  ou  /gerador-de-prompts-para-imagens-de-produto
    │                              ↓
    │                         /estatico-unity  (motor: gpt-image2-unity)
    │                              ↓
    │                         /legenda-para-post-estatico
    │
    └── formato vídeo      →  /hooks-para-instagram-reels
                                   ↓
                              /roteiro-unity  (motor: ogilvy ou schwartz)
                                   ↓
                              /legenda-para-reel
    ↓ [aprova conteúdo]
/1-conteudo-em-7-formatos   ← opcional: distribui para outros canais
    ↓
/publicar-social-unity
```

**Fluxo alternativo — conteúdo de fundo de funil:**
```
/banco-de-objecoes-do-avatar
    ↓ [escolhe objeção]
/carrossel-de-quebra-de-objecao
    ↓
/carrossel-unity  +  /legenda-para-carrossel
```

**Aprovação humana obrigatória** em cada etapa — o fluxo para e aguarda antes de avançar.

---

## Regras do sistema

- Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/`
- Se encontrar, seguir as instruções da skill
- Conteúdo da empresa: sempre manter o contexto da Ecoframe — esquadrias em PVC, premium técnico, Steel Frame e Drywall
- Arquivos de credenciais: nunca commitar (estão no .gitignore)

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo ou dar instrução permanente ("na verdade é assim", "não faça mais isso", "sempre que...", "evita..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde salvar:

- **Sobre o negócio** → `_contexto/empresa.md`
- **Sobre preferências e estilo** → `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** → `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** → `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro.

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo ao contexto
4. Se a skill precisar de arquivos de apoio, criar dentro da pasta da skill
