---
name: publicar-social-leange
description: >
  Publica conteúdo aprovado no Instagram via Meta Graph API.
  Suporta post estático (imagem única) e carrossel (múltiplos slides).
  Requer aprovação humana explícita antes de publicar — nunca publica automaticamente.
  Use após /carrossel-leange ou /estatico-leange entregarem os PNGs finais.
---

# /publicar-social-leange — Publicação no Instagram

## Dependências

- **Python:** 3.x com `requests` instalado (`pip install requests`)
- **Script de publicação:** `.claude/skills/publicar-social-leange/publicar-instagram.py`
- **Script de descoberta de ID:** `.claude/skills/publicar-social-leange/descobrir-ig-user-id.py`
- **Credenciais (obrigatórias):**
  - `credentials/meta_access_token.txt` — token de acesso Meta (long-lived)
  - `credentials/meta_ig_user_id.txt` — Instagram Business/Creator User ID
  - `credentials/imgbb_api_key.txt` — chave da API imgbb para hospedar imagens

---

## Configuração inicial (primeira vez)

### 1. Token Meta (access token)

O arquivo `credentials/meta_access_token.txt` já deve estar preenchido com o token.

Para verificar se está válido:
```powershell
python ".claude/skills/publicar-social-leange/descobrir-ig-user-id.py"
```

Se retornar erro de token inválido, gere um novo em:
[developers.facebook.com → Graph API Explorer → Generate Access Token]

Permissões necessárias:
- `instagram_basic`
- `instagram_content_publish`
- `pages_read_engagement`
- `pages_show_list`

Depois de gerar, converta para **long-lived token** (válido 60 dias):
```
GET https://graph.facebook.com/v22.0/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id={META_APP_ID}
  &client_secret={META_APP_SECRET}
  &fb_exchange_token={token_curto}
```

Salve o resultado em `credentials/meta_access_token.txt`.

**Atenção:** o token expira em 60 dias. Renove antes do vencimento.

### 2. Instagram User ID

Execute o script de descoberta:
```powershell
python ".claude/skills/publicar-social-leange/descobrir-ig-user-id.py"
```

Se a conta Instagram estiver vinculada a uma Página do Facebook, o script descobre e salva automaticamente em `credentials/meta_ig_user_id.txt`.

Se não funcionar:
1. Acesse [business.facebook.com](https://business.facebook.com)
2. Vincule sua conta Instagram à Página do Facebook
3. Execute o script novamente

### 3. imgbb API key

O imgbb hospeda as imagens publicamente para que o Instagram possa buscá-las durante a publicação.

1. Acesse [imgbb.com](https://imgbb.com) → faça login → API
2. Gere uma chave gratuita
3. Salve em `credentials/imgbb_api_key.txt`

**Plano gratuito:** suficiente para uso normal. Imagens ficam hospedadas por 6 meses (deletáveis depois da publicação).

### Checklist de configuração

```
credentials/meta_access_token.txt   → token Meta preenchido e válido
credentials/meta_ig_user_id.txt     → ID do usuário Instagram preenchido
credentials/imgbb_api_key.txt       → chave imgbb preenchida
pip install requests                → biblioteca instalada
```

---

## Workflow

### Pré-condição

O conteúdo precisa estar aprovado e pronto em disco antes de chamar esta skill:
- **Carrossel:** `conteudo/carrosseis/[periodo]/[dia]/instagram/slide-01.png` ... `slide-0N.png`
- **Post estático:** `conteudo/post-estatico/[periodo]/[dia]/post-01.png`
- **Legenda:** `conteudo/[tipo]/[periodo]/[dia-tema]/_legenda.md` (seção "LEGENDA APROVADA")

---

### Fase 0 — Checklist de qualidade (obrigatório antes de qualquer publicação)

Antes de mostrar a confirmação ao usuário, verificar cada item. Se qualquer um falhar, **bloquear a publicação e informar o que está faltando**.

```
[ ] Briefing aprovado existe em _briefing.md na pasta do conteúdo
[ ] Legenda vem do _legenda.md aprovado — não foi improvisada agora
[ ] Legenda tem menos de 2.200 caracteres
[ ] Legenda tem no máximo 30 hashtags
[ ] PNGs existem em disco e estão na ordem correta (slide-01, slide-02...)
[ ] Todos os PNGs têm EXATAMENTE 1080×1350 — rodar validar-dimensao.py (comando abaixo); bloquear se algum estiver fora
[ ] Nenhum texto cortado/transbordando — rodar validar-overflow.js (comando abaixo); bloquear se algum slide falhar. NÃO confiar só na conferência visual: corte de poucos px no canto passa batido no olho
[ ] Conferência visual dos PNGs como reforço (sobreposição, legibilidade, alinhamento)
[ ] Para sábado/domingo: --agendar está definido (publicação imediata bloqueada)
[ ] Para terça a sexta: confirmar que não é fim de semana antes de publicar imediatamente
```

**As DUAS validações abaixo são gate de publicação — exit 1 em qualquer uma BLOQUEIA o post:**
```powershell
# 1) Dimensão exata do canvas (o Instagram redimensiona tamanho errado e desloca/corta o texto)
python ".claude/skills/publicar-social-leange/validar-dimensao.py" "conteudo/carrosseis/[periodo]/[dia-tema]/instagram" 1080 1350
python ".claude/skills/publicar-social-leange/validar-dimensao.py" "conteudo/post-estatico/[periodo]/[dia-tema]/post-01.png" 1080 1350

# 2) Overflow interno — texto que sangra para fora do canvas (info bar/rodapé cortado no canto).
#    A validação de dimensão NÃO pega isso: o canvas continua 1080×1350, mas o texto vaza.
node ".claude/skills/publicar-social-leange/validar-overflow.js" "conteudo/carrosseis/[periodo]/[dia-tema]/instagram"
node ".claude/skills/publicar-social-leange/validar-overflow.js" "conteudo/post-estatico/[periodo]/[dia-tema]"
```
Se qualquer script retornar erro (exit 1), **não publicar** — voltar à skill de produção, corrigir o
HTML, re-renderizar o slide afetado e rodar as duas de novo. O `validar-overflow.js` aponta o slide,
o trecho de texto e quantos px transbordam.

Dados citados na legenda (unidade, número de suítes, valores da experiência) devem ter correspondência nos slides aprovados — não verificar automaticamente, mas se houver dúvida flagrar para o operador confirmar.

---

### Fase 1 — Confirmar o que vai ser publicado

Antes de qualquer ação, mostrar ao usuário:

```
Pronto para publicar:
  Tipo: carrossel (6 slides)
  Pasta: conteudo/carrosseis/julho-2026/dia-01-serra-inverno/instagram/
  Slides: slide-01.png → slide-06.png
  Legenda: [primeiros 100 caracteres da legenda]...

Confirma publicação no Instagram? [S para confirmar / N para cancelar]
```

**NUNCA publicar sem confirmação explícita do usuário.**

---

### Fase 2 — Publicar

**Publicação imediata** (terça a sexta):
```powershell
# Carrossel
python ".claude/skills/publicar-social-leange/publicar-instagram.py" `
  --tipo carrossel `
  --pasta "conteudo/carrosseis/[periodo]/[dia]/instagram/" `
  --legenda "LEGENDA COMPLETA AQUI"

# Post estático
python ".claude/skills/publicar-social-leange/publicar-instagram.py" `
  --tipo imagem `
  --imagem "conteudo/post-estatico/[periodo]/[dia]/post-01.png" `
  --legenda "LEGENDA COMPLETA AQUI"
```

**Publicação agendada** (sábado e domingo — obrigatório):
```powershell
# Carrossel agendado
python ".claude/skills/publicar-social-leange/publicar-instagram.py" `
  --tipo carrossel `
  --pasta "conteudo/carrosseis/[periodo]/[dia]/instagram/" `
  --legenda "LEGENDA COMPLETA AQUI" `
  --agendar "05/07/2026 10:00"

# Post estático agendado
python ".claude/skills/publicar-social-leange/publicar-instagram.py" `
  --tipo imagem `
  --imagem "conteudo/post-estatico/[periodo]/[dia]/post-01.png" `
  --legenda "LEGENDA COMPLETA AQUI" `
  --agendar "06/07/2026 09:30"
```

**Formato de data:** `DD/MM/AAAA HH:MM` — horário local do sistema. Mínimo 20 minutos no futuro, máximo 75 dias.

**Verificar agendamentos:**
```powershell
python ".claude/skills/publicar-social-leange/publicar-instagram.py" --listar-agendados
```

A legenda deve ser extraída do arquivo `_legenda.md` — seção "LEGENDA APROVADA", sem o bloco de metadados.

---

### Fase 3 — Confirmar publicação

Após o script retornar `OK`, mostrar ao usuário:

```
Publicado com sucesso!
  Media ID: [id]
  URL: https://www.instagram.com/p/[id]/

Próximos passos:
  [ ] Atualizar status no calendário: "Publicado" (conteudo/calendarios/[periodo]/calendario-detalhado.md)
  [ ] /syncar para salvar o estado no GitHub
```

---

## Erros comuns e soluções

| Erro | Causa | Solução |
|---|---|---|
| `credencial não encontrada` | Arquivo ausente em credentials/ | Criar o arquivo com o valor correto |
| `Error validating access token` | Token expirado (>60 dias) | Gerar novo token no Graph API Explorer |
| `Instagram account not found` | IG não vinculado à Página | Vincular em business.facebook.com |
| `Media posted before cooldown` | Postou muito rápido | Aguardar alguns minutos e tentar de novo |
| `imgbb: 400` | Imagem muito grande ou formato inválido | Converter para JPG < 10MB |
| `CAROUSEL_CHILD_LIMIT` | Mais de 10 slides | O script limita automaticamente aos primeiros 10 |

---

## Pendências conhecidas

| # | Pendência | Impacto |
|---|---|---|
| P2 | **imgbb sem fallback** — serviço gratuito sem SLA. Se sair do ar, publicação para completamente. Implementar alternativa (Cloudflare R2, S3, servidor próprio). | Publicação para completamente |

---

## Limites da Meta Graph API (Instagram)

- Máximo 25 publicações por 24h (por conta)
- Máximo 10 slides por carrossel
- Imagem: JPEG ou PNG, mínimo 320px, máximo 1440px de largura
- Arquivo máximo: 8MB para imagens (o script avisa se passar)
- Legenda: máximo 2.200 caracteres, 30 hashtags
- Rate limit geral: 200 calls/hora por token

---

## Estrutura de arquivos

```
.claude/skills/publicar-social-leange/
  SKILL.md                      ← este arquivo
  publicar-instagram.py         ← script principal de publicação
  descobrir-ig-user-id.py       ← helper: descobre e salva o IG User ID

credentials/  (não committar — .gitignore)
  meta_access_token.txt         ← token Meta long-lived (renovar a cada 60 dias)
  meta_ig_user_id.txt           ← Instagram Business/Creator User ID
  imgbb_api_key.txt             ← chave imgbb para hospedar imagens
```

---

## Regras

- **Aprovação humana sempre** — nunca publicar sem confirmação explícita
- **Dias de postagem:** terça a domingo. Segunda-feira não é dia de post.
- **Sábado e domingo obrigatoriamente agendados** — usar `--agendar "DD/MM/AAAA HH:MM"`. Nunca publicar imediatamente em fins de semana.
- **Horário de agendamento** — editável a cada post. Não há horário fixo definido: perguntar ao usuário qual horário usar antes de agendar.
- **Ler a legenda do arquivo** — não usar legenda improvisada; sempre do `_legenda.md` aprovado
- **Ordem dos slides** — o script publica em ordem alfabética (`slide-01.png`, `slide-02.png`...). Confirmar que os nomes estão corretos antes de publicar
- **Atualizar o calendário** — após publicar ou agendar, atualizar o status no `calendario-detalhado.md`: "Publicado" (imediato) ou "🕐 Agendado DD/MM HH:MM" (agendado)
- **Token Meta** — avisar o usuário quando o token estiver próximo de expirar (verificar a data de geração)
