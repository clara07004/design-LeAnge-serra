# Configuração Inicial — Do Zero ao Sistema Funcionando

## Pré-requisitos de software

Antes de qualquer coisa, confirme que seu computador tem:

**Python 3.x**
```powershell
python --version
# Deve retornar: Python 3.x.x
```

**Node.js**
```powershell
node --version
# Deve retornar: v18.x.x ou superior
```

**SDK da OpenAI para Python** (inclui `httpx` — usado também nos scripts de publicação)
```powershell
python -m pip install openai
```

**Playwright (para renderizar HTML em PNG)**
```powershell
npx.cmd playwright install chromium
```

Se algum desses não estiver instalado, o sistema vai travar na hora de gerar imagens ou renderizar posts.

---

## Passo 1 — Configurar as credenciais de API

As credenciais ficam em `credentials/`. Esta pasta está no `.gitignore` e nunca vai para o GitHub.

### OpenAI (obrigatório para geração de imagem)

1. Acesse [platform.openai.com](https://platform.openai.com)
2. Vá em **API Keys** → **Create new secret key**
3. Copie a chave (começa com `sk-...`)
4. Cole no arquivo `credentials/openai_key.txt` — só a chave, sem espaços ou quebras de linha

```
sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Custo estimado:** ~$0,02–$0,10 por imagem (qualidade high). $5 de crédito cobrem dezenas de imagens.

### Gemini (opcional — fallback gratuito)

Usado pelo motor `nanobanana-leange` quando a OpenAI falha.

1. Acesse [aistudio.google.com](https://aistudio.google.com)
2. Clique em **Get API Key** → **Create API key**
3. Cole a chave em `credentials/gemini.txt`

### Meta Graph API (opcional — para publicação automática)

Usado pela skill `/publicar-social-leange` para publicar no Instagram.

**3 arquivos necessários em `credentials/`:**

#### `credentials/meta_access_token.txt` — token Meta long-lived

1. Acesse [developers.facebook.com](https://developers.facebook.com) → seu app → Graph API Explorer
2. Selecione seu app e gere um token com as permissões:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_read_engagement`
   - `pages_show_list`
3. Converta para long-lived token (válido 60 dias):
   ```
   GET https://graph.facebook.com/v22.0/oauth/access_token
     ?grant_type=fb_exchange_token
     &client_id={SEU_APP_ID}
     &client_secret={SEU_APP_SECRET}
     &fb_exchange_token={TOKEN_CURTO}
   ```
4. Salve só o token em `credentials/meta_access_token.txt` (sem espaços)

**Atenção:** expira em 60 dias — renove antes do vencimento.

#### `credentials/meta_ig_user_id.txt` — ID do usuário Instagram

Execute o script de descoberta automática:
```powershell
python ".claude/skills/publicar-social-leange/descobrir-ig-user-id.py"
```

O script lê o token e salva o IG User ID automaticamente. Requer que a conta Instagram Business/Creator esteja vinculada a uma Página do Facebook em [business.facebook.com](https://business.facebook.com).

#### `credentials/imgbb_api_key.txt` — chave imgbb para hospedar imagens

1. Acesse [imgbb.com](https://imgbb.com) → faça login → clique no avatar → API
2. Gere uma chave (gratuito)
3. Salve em `credentials/imgbb_api_key.txt`

O imgbb hospeda as imagens publicamente para que o Instagram possa buscá-las durante a publicação. O plano gratuito é suficiente para uso normal.

---

## Passo 2 — Configurar o contexto da empresa

Os arquivos em `_contexto/` são templates — preencha cada um com o contexto da empresa antes de usar o sistema.

### `_contexto/empresa.md`

Descreve o negócio. Preencha com:
- O que a empresa faz e o que vende
- Público-alvo (quem compra, quais são os objetivos e medos deles)
- Modelo de negócio (como as vendas acontecem)
- Posicionamento (como a empresa quer ser percebida)
- Objeções frequentes e como contra-argumentar
- Canais ativos (Instagram, WhatsApp, site, etc.)
- Quais APIs estão disponíveis

### `_contexto/preferencias.md`

Define como a marca fala. Preencha com:
- Idioma e tom de voz (formal, técnico, descontraído, etc.)
- Palavras e expressões recomendadas
- Palavras e expressões proibidas
- Exemplos de copy no estilo certo (para o Claude aprender por exemplo)
- Exemplos de copy fora de estilo
- Restrições legais e de compliance

### `_contexto/estrategia.md`

Define as prioridades atuais. Preencha com:
- Foco principal do momento
- Gaps que o conteúdo deve resolver
- Jornada de conteúdo por etapa do funil
- Campanhas em andamento
- KPIs que estão sendo acompanhados

**Dica:** Este arquivo envelhece rápido. Revise a cada trimestre ou quando a estratégia mudar.

### `_contexto/referencias.md`

Links para as pastas do Google Drive com material de referência visual. O formato é:

```markdown
## Nome da pasta
**Descrição:** O que tem nessa pasta
**ID da pasta:** `ID_DO_GOOGLE_DRIVE`
```

Para encontrar o ID de uma pasta no Drive: abra a pasta, olhe a URL. O ID é o código alfanumérico no final:
`https://drive.google.com/drive/folders/AQUI_ESTÁ_O_ID`

---

## Passo 3 — Verificar o DESIGN.md

Abra `marca/DESIGN.md` e confirme que:

1. `status: configured` — se estiver `not-configured`, as skills de produção visual vão parar
2. As cores estão corretas para a empresa
3. A tipografia está definida
4. Os `layout_templates` estão preenchidos (ou pelo menos o básico)

Para uma nova empresa, preencher todos os campos com a identidade visual real. Alterar `status` para `configured` somente quando todos os campos obrigatórios estiverem preenchidos.

---

## Passo 4 — Testar o sistema

Para verificar que tudo está funcionando, faça um teste simples:

**Teste de geração de imagem:**
```powershell
python ".claude/skills/gpt-image2-leange/gerar-imagem.py" "cozy pousada suite, natural light, lifestyle photography, no text" "conteudo/_teste/foto-teste.png" "square"
```

Resultado esperado:
```
Gerando imagem (1024x1024) — pode demorar 60-180s...
OK: conteudo/_teste/foto-teste.png
```

Se retornar:
- `ERRO: OPENAI_API_KEY não encontrada` → verifique `credentials/openai_key.txt`
- `ERRO: ...` com exit code 4 → problema no prompt ou na conta OpenAI

**Teste do Playwright:**
```powershell
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
npx.cmd playwright --version
```

Deve retornar a versão do Playwright.

---

## Passo 5 — Primeira conversa

Abra o Claude Code neste diretório. O sistema vai ler automaticamente todos os arquivos de contexto.

Para confirmar que está tudo certo, você pode perguntar:
> "O que é [nome da empresa]?"

O Claude deve responder com informações precisas sobre o negócio, produtos e posicionamento — sem você ter precisado explicar nada.

Se a resposta for genérica ou errada, verifique se o arquivo `_contexto/empresa.md` está preenchido corretamente.

---

## Checklist de configuração

Antes de usar o sistema pela primeira vez, marque cada item:

- [ ] Python 3.x instalado e acessível via terminal
- [ ] Node.js instalado e acessível via terminal
- [ ] `python -m pip install openai` executado
- [ ] `npx.cmd playwright install chromium` executado
- [ ] `credentials/openai_key.txt` preenchido com a chave da OpenAI
- [ ] (quando for usar publicação) `credentials/meta_access_token.txt` preenchido
- [ ] (quando for usar publicação) `credentials/meta_ig_user_id.txt` preenchido via `descobrir-ig-user-id.py`
- [ ] (quando for usar publicação) `credentials/imgbb_api_key.txt` preenchido
- [ ] `_contexto/empresa.md` preenchido e revisado
- [ ] `_contexto/preferencias.md` preenchido e revisado
- [ ] `_contexto/estrategia.md` preenchido e revisado
- [ ] `marca/DESIGN.md` com `status: configured`
- [ ] Teste de geração de imagem executado com sucesso
- [ ] Teste do Playwright executado com sucesso

---

## Adaptando para outro cliente

Este repositório é um template reutilizável para qualquer negócio. Para adaptar:

1. Edite `_contexto/empresa.md` com o contexto do novo negócio
2. Edite `_contexto/preferencias.md` com o tom de voz da nova marca
3. Edite `_contexto/estrategia.md` com as prioridades atuais
4. Edite `marca/DESIGN.md` com a identidade visual da nova marca
5. Atualize `CLAUDE.md` se o nome da empresa aparecer no texto
6. Substitua as credenciais em `credentials/`

Revise o `CLAUDE.md` se precisar ajustar o nome da empresa ou contexto do negócio na seção de "Contexto do negócio".
