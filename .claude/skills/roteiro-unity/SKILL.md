---
name: roteiro-unity
description: >
  Cria roteiros de vídeo completos para Instagram Reels e TikTok.
  Usa Ogilvy para vídeos de conteúdo orgânico (autoridade, marca, educação)
  e Schwartz para criativos de tráfego pago (conversão, resposta direta).
  Use quando o briefing definir formato "vídeo", "reel" ou "roteiro",
  ou quando o usuário pedir "cria o roteiro", "escreve o vídeo", "faz o script".
---

# /roteiro-unity — Roteiro de Vídeo

## Dependências

- **Contexto do negócio:** `_contexto/empresa.md`
- **Tom de voz:** `_contexto/preferencias.md`
- **Identidade visual:** `marca/design-guide.md` (para orientações visuais de cena)
- **Motor de copy:** Ogilvy (orgânico) ou Schwartz (tráfego pago) — definido pelo objetivo do briefing

---

## Input

- Briefing aprovado em `conteudo/[semana]/[post].md` (vindo do /briefing-unity)
- Ou: tema + objetivo + plataforma fornecidos diretamente pelo usuário

---

## Workflow

### Fase 1 — Leitura e diagnóstico

1. Ler `_contexto/empresa.md`, `_contexto/preferencias.md`
2. Localizar o briefing aprovado — perguntar o caminho se não for informado
3. Do briefing, extrair:
   - **Objetivo:** o que esse vídeo precisa fazer (educar, gerar autoridade, vender, captar lead)
   - **Plataforma:** Instagram Reels, TikTok, ou ambos
   - **Duração alvo:** curto (15-30s), médio (30-60s) ou longo (60-90s)
   - **Público:** quem vai assistir e em que momento da jornada está

4. Definir o motor de copy com base no objetivo:

   **Ogilvy** — usar quando o objetivo for:
   - Conteúdo educacional ou de autoridade
   - Construção de marca e posicionamento
   - Storytelling institucional
   - Engajamento orgânico e retenção de audiência

   **Schwartz** — usar quando o objetivo for:
   - Criativo de tráfego pago (Meta Ads, TikTok Ads)
   - Conversão direta (venda, cadastro, ligação)
   - Resposta direta com CTA forte
   - Campanha com oferta específica

5. **CHECKPOINT:** apresentar o diagnóstico antes de escrever:
   > "Briefing lido. Objetivo: [objetivo]. Plataforma: [plataforma]. Duração: [X]s. Vou usar [Ogilvy/Schwartz] porque [razão]. Posso continuar?"

---

### Fase 2 — Escrita do roteiro

Escrever o roteiro seguindo a estrutura abaixo, com o tom do motor escolhido.

#### Estrutura padrão (adaptar à duração alvo)

**GANCHO (0-3s)**
- A frase de abertura mais forte do vídeo
- Precisa parar o scroll imediatamente
- Pode ser uma pergunta, afirmação provocativa, dado surpreendente ou promessa direta
- Para Ogilvy: gancho narrativo ou de curiosidade
- Para Schwartz: gancho de problema ou promessa de resultado

**DESENVOLVIMENTO (4s até -10s do fim)**
- Conteúdo principal: argumento, história, demonstração, prova
- Para Ogilvy: narrativa fluida, detalhes concretos, construção de autoridade
- Para Schwartz: apresentação do problema → solução → prova → oferta
- Cada bloco de 10-15s deve ter uma micro-retenção (virada, revelação, próximo passo)

**CTA (últimos 5-10s)**
- Instrução clara do que fazer depois de assistir
- Para Ogilvy: CTA suave (salva, comenta, segue, compartilha)
- Para Schwartz: CTA direto (clica no link, manda mensagem, acessa agora)

#### Formato do roteiro

```markdown
# Roteiro — [Nome do Post] | [Plataforma] | [Duração]s

**Motor:** [Ogilvy / Schwartz]
**Objetivo:** [objetivo]

---

## GANCHO (0-3s)
[Fala exata do apresentador]
*[Nota de direção: tom, expressão, enquadramento]*

## DESENVOLVIMENTO

### Bloco 1 (4-15s)
[Fala]
*[Nota de direção]*

### Bloco 2 (16-30s)
[Fala]
*[Nota de direção]*

### Bloco 3 (31-50s) — se duração permitir
[Fala]
*[Nota de direção]*

## CTA (últimos 5-10s)
[Fala exata]
*[Nota de direção: tom, gesto, olhar para câmera]*

---

## ORIENTAÇÕES DE GRAVAÇÃO

**Enquadramento:** [busto / rosto / corpo inteiro / produto em destaque]
**Cenário sugerido:** [onde gravar — escritório, obra, showroom, externo]
**Elementos visuais:** [o que mostrar na tela além do apresentador — produto, texto na tela, B-roll]
**Texto na tela (captions):** [palavras-chave para destacar em overlay]
**Música:** [instrumental / sem música / vibe sugerida]
**Legenda (caption do post):** [sugestão de legenda completa para acompanhar o vídeo]
```

**CHECKPOINT:** apresentar o roteiro completo. Aguardar aprovação ou ajustes antes de salvar.

---

### Fase 3 — Entrega

1. Salvar roteiro aprovado em:
```
conteudo/roteiros/[tema]/roteiro-[plataforma].md
```

2. Se for para Instagram e TikTok, verificar se precisa de adaptação:
   - Duração diferente entre plataformas → ajustar cortes
   - CTA diferente (ex: link na bio no Instagram vs link direto no TikTok) → adaptar

3. Confirmar entrega:
   > "Roteiro salvo em `conteudo/roteiros/[tema]/`. Próximo passo: gravar e passar pelo /publicar-social-unity."

---

## Output final

```
conteudo/roteiros/[tema]/
  roteiro-instagram.md    ← roteiro para Reels
  roteiro-tiktok.md       ← roteiro adaptado para TikTok (se solicitado)
```

---

## Regras

- O roteiro é escrito para ser falado, não lido — frases naturais, sem jargão corporativo
- Cada segundo conta: sem introduções longas, sem "olá, tudo bem?"
- Gancho nos primeiros 3 segundos é inegociável
- Notas de direção entre *itálicos* — orientam a gravação sem fazer parte da fala
- Nunca prometer preços, prazos ou resultados garantidos
- Sem EPI incorreto em cenas sugeridas de obra
- Se o usuário não souber o objetivo (orgânico ou tráfego), perguntar antes de escolher o motor
