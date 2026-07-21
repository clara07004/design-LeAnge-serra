---
name: briefing-leange
description: >
  Gera o briefing completo de um conteúdo para redes sociais — gancho, copy por plataforma,
  formato recomendado, orientações visuais, hashtags e qual skill acionar na sequência.
  Use antes de qualquer produção de asset (carrossel, post estático ou vídeo).
  Dispara quando: "faz o briefing", "briefing de conteúdo", "o que postar sobre X",
  "define o conteúdo", "quero um briefing", ou após aprovar o calendário comercial.
---

# briefing-leange

Gera o briefing completo de um conteúdo para redes sociais da empresa ativa, a partir do output do `calendario-comercial` e do contexto de marca em `_contexto/`.

---

## Quando usar

Invoke após o calendário comercial do mês ser aprovado. Para cada janela de conteúdo aprovada, rode `/briefing-leange` para gerar o briefing antes de acionar qualquer skill de geração de asset.

---

## Histórico de execuções

Antes de iniciar, verificar se já existe um `_aprovado.md` na pasta do conteúdo
(`conteudo/[tipo]/[periodo]/[dia-tema]/_aprovado.md`). Se existir, ler e usar como referência de
qualidade mínima: reaproveitar o gancho e ângulo aprovados como ponto de partida, evitar o que
estiver marcado em "O que evitar".

---

## Input esperado

O usuário deve fornecer (ou o CCOS deve ter em contexto):

- **Janela de conteúdo** — output do `calendario-comercial`: tema narrativo, produto a promover, timing, gancho sugerido
- **Contexto da marca** — empresa, tom de voz, público-alvo, restrições editoriais
- **Plataforma(s) alvo** — Instagram, TikTok, LinkedIn, YouTube (afeta formato e copy)
- **Formato pretendido** — carrossel, imagem avulsa, Reels/TikTok, YouTube (se já definido)

Se algum desses itens estiver ausente, pergunte antes de gerar.

---

## O que este briefing entrega

```
1. GANCHO
   - Linha de abertura (primeira frase do post / primeiro frame do vídeo)
   - Por que vai funcionar para este público neste momento

2. COPY BASE
   - Corpo do texto adaptado para cada plataforma solicitada
   - Tom: adequado à marca (use ogilvy-copy para construção de identidade; schwartz-copy para conversão)
   - CTA claro no encerramento

3. FORMATO RECOMENDADO
   - Carrossel (quantos cards, estrutura narrativa por card)
   - Imagem avulsa (enquadramento, foco visual)
   - Reels/TikTok (duração estimada, ritmo de corte, gancho nos primeiros 3s)
   - YouTube (duração, estrutura de vídeo)

4. ORIENTAÇÕES VISUAIS
   - Paleta de cor dominante (alinhada à identidade da marca)
   - Estilo de imagem (foto real, ilustração, tipografia dominante)
   - Elementos obrigatórios (logo, produto, pessoa?)
   - Referência de estilo se aplicável

5. HASHTAGS POR PLATAFORMA
   - Instagram: 5-10 hashtags relevantes (mix nicho + descoberta)
   - TikTok: 3-5 tags
   - LinkedIn: 3 tags profissionais

6. METADADOS DO BRIEFING
   - Empresa: [nome]
   - Data de publicação ideal: [data]
   - Plataformas: [lista]
   - Formato: [formato]
   - Skill de geração indicada: [carrossel-leange | gpt-image2-leange | roteiro-leange]
```

---

## Gates de aprovação

Este fluxo **para e aguarda confirmação humana** antes de avançar para geração de assets.

Após entregar o briefing, exiba:

```
---
BRIEFING GERADO. Revise antes de continuar.

[A] Aprovar e gerar asset → informa qual skill acionar
[E] Editar → especifique o que ajustar
[C] Cancelar → encerra o fluxo para este conteúdo
---
```

- **[A]**: criar a pasta de produção `conteudo/[tipo]/[periodo]/[dia-tema]/` conforme o formato
  (carrossel → `carrosseis`; imagem avulsa/post → `post-estatico`; Reels/vídeo → `roteiros`),
  salvar o briefing como `_briefing.md` e a memória de aprovação como `_aprovado.md` (gancho
  aprovado, ângulo e ajustes feitos) **na mesma pasta**; depois acionar a skill indicada nos
  metadados (`/carrossel-leange`, `/gpt-image2-leange`/`/estatico-leange` ou `/roteiro-leange`)
- **[E]**: reescreva apenas a seção indicada e apresente novamente o gate
- **[C]**: registre o cancelamento e encerre

---

## Skill de geração a acionar (por formato)

| Formato | Skill padrão | Observação |
|---|---|---|
| Carrossel | `carrossel-leange` | HTML → PNG via Playwright |
| Imagem avulsa | `gpt-image2-leange` | GPT Image 2 via OAuth ChatGPT (sem custo extra) |
| Imagem avulsa (fallback) | `nanobanana-leange` | Gemini grátis — usar quando quota do ChatGPT esgotada |
| Imagem avulsa (contingência) | `image-gen-leange` | FAL API, pago (~$0,06–$0,22/img) — último recurso |
| Reels/TikTok/YouTube | `roteiro-leange` | Disponível na V1 |

---

## Integração com a Biblioteca de Conteúdo (V1+)

Quando a Fase 7 da biblioteca estiver concluída:

1. Extraia o gancho aprovado como query em texto
2. Envie para a REST API da biblioteca (Supabase pgvector)
3. Incorpore os campos retornados (`Titulo`, `Fonte`, `Resumo_IA`, `Tags`, `Politica_Ref`) nas orientações do briefing

**No MVP:** opere sem a biblioteca. As informações da pousada virão do contexto fornecido no input.

---

## Contexto de marca

Ler obrigatoriamente antes de gerar qualquer briefing:
- `_contexto/empresa.md` — quem é a empresa, ICP, posicionamento, restrições
- `_contexto/preferencias.md` — tom de voz, palavras proibidas, estilo
- `_contexto/estrategia.md` — foco atual e prioridades

Não usar contexto genérico. Todos os dados de empresa vêm desses arquivos.

---

## Exemplo de invocação

```
/briefing-leange

Janela: semana de 20/07 — Dia do Amigo
Tema: o pet como parte da família — férias na Serra sem deixar ninguém para trás
Plataforma: Instagram + TikTok
Formato: Carrossel (Instagram) + Reels (TikTok)
Contexto: tutor que trata o pet como família e busca destino sem restrição de pet
```

---

*Skill: briefing-leange*
