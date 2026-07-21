# Resolução de Problemas

## Erros de geração de imagem

### "ERRO: OPENAI_API_KEY não encontrada" (exit code 2)

**Causa:** o arquivo `credentials/openai_key.txt` não existe ou está vazio.

**Solução:**
1. Acesse [platform.openai.com](https://platform.openai.com) → API Keys → Create new secret key
2. Copie a chave (começa com `sk-...`)
3. Abra o arquivo `credentials/openai_key.txt` e cole apenas a chave, sem espaço nem quebra de linha
4. Tente novamente

---

### "ERRO: ..." com exit code 4

**Causa:** problema na chamada à API da OpenAI. Pode ser:
- Saldo insuficiente na conta OpenAI
- Prompt contendo conteúdo bloqueado pela política da OpenAI
- Instabilidade temporária da API

**Solução — saldo:**
1. Acesse [platform.openai.com/account/billing](https://platform.openai.com/account/billing)
2. Verifique o saldo disponível
3. Se necessário, adicione créditos (mínimo $5)

**Solução — prompt bloqueado:**
Ajuste o prompt removendo termos que possam ser interpretados como problemáticos. Prompts de pousada raramente são bloqueados — se acontecer, simplifique a descrição da cena.

**Solução — API instável:**
Aguarde alguns minutos e tente novamente. Ou acione o fallback:

```
Claude: A geração via OpenAI falhou. Quer tentar via Gemini (gratuito)?
Você: Sim
```

---

### A imagem gerou mas não está no caminho esperado

**Causa:** o diretório de destino não foi criado. O script cria a pasta automaticamente via `mkdir(parents=True)`, mas pode falhar se o caminho tiver caracteres especiais.

**Solução:** verifique se o caminho de saída usa apenas letras, números e hífens. Evite acentos e espaços nos nomes de tema.

---

### A imagem não tem nada a ver com o prompt

**Causa comum:** prompt muito genérico ou muito longo sem hierarquia clara.

**Como melhorar o prompt:**
- Descrever a cena principal nos primeiros 15 palavras
- Incluir estilo fotográfico explícito: `professional lifestyle photography`
- Especificar iluminação: `natural daylight`, `soft ambient light`
- Especificar enquadramento: `wide shot`, `close-up detail`, `mid shot`
- Incluir contexto de produto: descrição do produto, tipo de ambiente, contexto de uso

**Exemplo de prompt ruim:**
```
a pousada room that shows the quality and the premium feeling of the brand
```

**Exemplo de prompt bom:**
```
cozy pousada suite interior, [produto] in the scene, natural daylight flooding in, contemporary minimal decor, warm wood tones, professional lifestyle photography, wide shot, no text overlay, no watermarks
```

---

## Erros de renderização (Playwright)

### "npx não é reconhecido como um comando"

**Causa:** Node.js não está no PATH do PowerShell.

**Solução:** use o comando com o PATH forçado:
```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright screenshot ...
```

O `npx.cmd` (com `.cmd`) é necessário no PowerShell do Windows — `npx` sem extensão não funciona.

---

### "Error: browserType.launch: Executable doesn't exist"

**Causa:** o Chromium do Playwright não foi instalado.

**Solução:**
```powershell
npx.cmd playwright install chromium
```

---

### O PNG gerado está em branco ou incompleto

**Causa:** o HTML referencia um arquivo de imagem com caminho relativo que o Playwright não consegue encontrar.

**Como o caminho deve estar no HTML:**
```html
<img src="./img-slide01.png">
```

**Como o comando deve ser executado:** o arquivo HTML e o arquivo de imagem devem estar na mesma pasta. O caminho no `file:///` deve usar barras normais (`/`), não barras invertidas (`\`).

**Exemplo correto:**
```powershell
npx.cmd playwright screenshot --viewport-size=1080,1350 --full-page "file:///C:/Users/[usuario]/Documents/Design-LeAnge-Serra/conteudo/carrosseis/tema/instagram/slide-01.html" "C:/Users/[usuario]/Documents/Design-LeAnge-Serra/conteudo/carrosseis/tema/instagram/slide-01.png"
```

---

### O texto está cortado ou fora do slide

**Causa:** o texto é longo demais para o tamanho de fonte definido no DESIGN.md.

**Regra do sistema:** nunca reduzir a fonte para encaixar o texto. O que fazer:
- Cortar o parágrafo final do slide
- Mover parte do conteúdo para o slide seguinte
- Pedir ao Claude: "O texto do slide 3 está cortado — adapte para caber sem reduzir a fonte"

---

## Erros de configuração

### "⚠️ O DESIGN.md ainda não foi configurado"

**Causa:** `marca/DESIGN.md` tem `status: not-configured` ou um campo obrigatório está em branco.

**Solução:**
1. Abra `marca/DESIGN.md`
2. Verifique se `status: configured` (não `not-configured`)
3. Verifique se os campos `colors.primary`, `colors.canvas`, `typography.heading.fontFamily` estão preenchidos
4. Se qualquer campo obrigatório estiver `""`, preencha com o valor correto da identidade visual

---

### O Claude não sabe para qual empresa está trabalhando

**Causa:** `CLAUDE.md` ou os arquivos de `_contexto/` estão faltando ou vazios.

**Solução:**
1. Confirme que `CLAUDE.md` existe na raiz do repositório
2. Confirme que `_contexto/empresa.md` está preenchido
3. Inicie uma nova conversa (o Claude lê os arquivos no início de cada conversa)

---

### O Claude não encontra a skill

**Causa:** o arquivo `SKILL.md` está em lugar errado ou com nome diferente.

**Estrutura correta:**
```
.claude/skills/nome-da-skill/SKILL.md
```

O nome da pasta deve ser exatamente igual ao nome do comando (sem a barra). Por exemplo, `/carrossel-leange` → `.claude/skills/carrossel-leange/SKILL.md`.

---

## Problemas com o token da Meta (publicação no Instagram)

### "Token expirado" ou erro de autenticação

**Causa:** o META_ACCESS_TOKEN expira a cada 60 dias.

**Solução:**
1. Acesse [developers.facebook.com/tools/explorer](https://developers.facebook.com/tools/explorer)
2. Selecione seu app
3. Gere um novo token com as permissões `instagram_basic`, `instagram_content_publish`
4. Use a opção "Extend token" para gerar um token de longa duração (60 dias)
5. Atualize `credentials/meta.txt` com o novo token

---

## O conteúdo gerado não está no estilo da marca

### O texto soa muito genérico

**Causa:** `_contexto/empresa.md` ou `_contexto/preferencias.md` estão incompletos.

**Solução:**
1. Abra `_contexto/preferencias.md`
2. Adicione mais exemplos de copy no estilo certo
3. Adicione mais expressões proibidas
4. Na próxima conversa, o Claude aplicará as novas regras

---

### A imagem não condiz com o nível premium da marca

**Causa:** o prompt não especificou o contexto correto da cena.

**Elementos que elevam a qualidade da imagem:**
- `cozy pousada interior` — contexto da cena
- `high-end pet-friendly retreat` — nível de acabamento
- `natural light, diffuse` — iluminação premium
- `clean minimal interior` — estética da marca
- `professional lifestyle photography` — estilo fotográfico

**Elementos que rebaixam:**
- `house`, `home` (muito genérico — use `cozy pousada suite` ou `pet-friendly retreat`)
- `pousada` sem qualificação (use `cozy boutique pousada, high-end finishes, warm inviting spaces`)

---

## Dúvidas frequentes

### Posso usar o sistema sem a API da OpenAI?

Sim, com limitações. Para geração de imagem, você pode usar o fallback Gemini (gratuito). O sistema vai tentar OpenAI primeiro, avisar que falhou e perguntar se quer tentar Gemini. Para carrosséis com fundo sólido (sem imagem), o Playwright funciona normalmente sem nenhuma API.

### Quanto custa gerar um carrossel completo?

Um carrossel de 10 slides com 3 imagens (capa + 2 slides de impacto) custa aproximadamente $0,06–$0,30 na OpenAI. O custo maior é de tempo de renderização — cerca de 10-20 minutos de trabalho do Claude para o processo completo.

### O Claude pode publicar automaticamente no Instagram?

Sim, com `/publicar-social-leange` e o token da Meta configurado. O processo ainda requer aprovação humana do conteúdo antes de publicar — o sistema não publica nada sem confirmação explícita.

### Posso recriar um post com variações?

Sim. Cada execução aprovada salva um arquivo `_aprovado.md` com o prompt exato usado. Na próxima execução do mesmo tema, o Claude lê esse histórico e parte do mesmo prompt como base, facilitando variações. Você pode pedir: "Cria uma variação do post sobre viajar com pet com outra cena de ambiente."

### O que acontece se eu fechar a conversa no meio do processo?

Os arquivos gerados até aquele ponto ficam salvos em `conteudo/`. Você pode retomar na próxima conversa apontando para os arquivos existentes. "Tenho o texto aprovado em `conteudo/carrosseis/tema/carousel-text.md` — pode continuar para a fase de imagens?"

### Como crio uma skill nova para um processo que faço sempre?

Use `/mapear`. O Claude vai entrevistar você sobre o processo, identificar os passos repetíveis e criar um arquivo `SKILL.md` personalizado. Você escolhe se a skill fica local (só neste projeto) ou global (disponível em qualquer projeto).
