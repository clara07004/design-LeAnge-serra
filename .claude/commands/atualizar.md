---
name: atualizar
description: >
  Traz as mudanças mais recentes do GitHub pro computador local (git pull).
  É o inverso do /syncar: o /syncar sobe o trabalho pro GitHub, o /atualizar baixa.
  Use quando o usuário disser "atualiza", "atualizar", "baixa do github",
  "pega as mudanças", "puxa do github", "tá desatualizado", "git pull",
  ou no começo de uma sessão pra garantir que está na versão mais nova.
---

# /atualizar — Baixar do GitHub

Traz pro computador local o que foi alterado no GitHub. Use no começo do trabalho
ou quando alguém (a Ecoframe ou outro colaborador) tiver feito mudanças no repositório.

## Verificação inicial

Rode pra entender o estado atual:

```bash
git remote get-url origin 2>/dev/null
git status --short
```

---

## Fluxo A: sem remote configurado

Se `git remote get-url origin` não retornar nada, o workspace não está conectado ao GitHub.

> "Esse workspace ainda não está conectado a um repositório no GitHub, então não tem
> de onde baixar. Se quiser conectar, é só me chamar com /syncar que eu configuro."

---

## Fluxo B: tem mudanças locais não salvas

Se `git status --short` mostrar arquivos modificados, **pare antes de puxar** — baixar por
cima de trabalho não salvo pode dar conflito. Avise:

> "Você tem alterações no computador que ainda não foram salvas no GitHub:
> [listar arquivos]
>
> Antes de baixar as novidades, o ideal é salvar o que você fez. Quer que eu:
> 1. **Salve seu trabalho primeiro** (faço /syncar e depois atualizo) — recomendado
> 2. **Descarte o que você mexeu** e pegue exatamente o que está no GitHub (não dá pra desfazer)"

Só siga pro Fluxo C depois da escolha. Se escolher salvar, faça commit + push antes do pull.

---

## Fluxo C: tudo limpo, pode baixar

Se não houver mudanças locais pendentes, baixe:

```bash
git pull
```

Depois confirme em linguagem simples:

- **Se baixou novidades:** "Pronto, atualizei. Vieram mudanças novas: [resumir em 1 linha o que mudou — ex: 2 arquivos atualizados]. Já está tudo na versão mais recente."
- **Se já estava em dia:** "Tudo certo, você já estava com a versão mais recente. Nada novo pra baixar."

---

## Fluxo D: deu conflito

Se o `git pull` acusar conflito (mesmo arquivo mexido nos dois lados), **não tente resolver
sozinho no escuro**. Explique de forma simples:

> "Deu um conflito: o arquivo [nome] foi alterado tanto no seu computador quanto no GitHub,
> e o Git não sabe qual versão manter.
>
> Não se preocupe, nada foi perdido. Me diz qual versão você quer manter nesse arquivo
> (a sua ou a do GitHub) que eu resolvo pra você."

Resolva conforme a escolha do usuário, sem expor comandos técnicos a menos que ele peça.

---

## Fluxo E: erro no pull

Se falhar por outro motivo (conexão, autenticação):

> "Não consegui baixar do GitHub. O erro foi: [mensagem]
>
> Causas mais comuns:
> - Sem conexão com internet
> - Precisa configurar autenticação no GitHub
>
> Se quiser resolver agora, me diz e eu te ajudo passo a passo."

---

## Regras

- Tom direto e simples — quem usa não tem conhecimento técnico. Nada de jargão de git
  a menos que o usuário pergunte.
- **Nunca** descartar mudanças locais sem confirmação explícita do usuário.
- Sempre resumir em linguagem natural o que foi baixado — não despejar o output cru do git.
- Se der erro ou conflito, sempre dizer o próximo passo — nunca só mostrar o erro.
