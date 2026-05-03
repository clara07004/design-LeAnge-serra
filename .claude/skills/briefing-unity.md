# briefing-unity

Gera o briefing completo de um conteúdo para redes sociais do Grupo Unity a partir do output do `calendario-comercial` e do contexto de marca fornecido pelo CCOS.

---

## Quando usar

Invoke após o calendário comercial do mês ser aprovado. Para cada janela de conteúdo aprovada, rode `/briefing-unity` para gerar o briefing antes de acionar qualquer skill de geração de asset.

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
   - Skill de geração indicada: [carrossel-unity | gpt-image2-unity | roteiro-unity]
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

- **[A]**: acione a skill indicada nos metadados (`/carrossel-unity`, `/gpt-image2-unity` ou `/roteiro-unity`)
- **[E]**: reescreva apenas a seção indicada e apresente novamente o gate
- **[C]**: registre o cancelamento e encerre

---

## Skill de geração a acionar (por formato)

| Formato | Skill padrão | Observação |
|---|---|---|
| Carrossel | `carrossel-unity` | HTML → PNG via Playwright |
| Imagem avulsa | `gpt-image2-unity` | GPT Image 2 via OAuth ChatGPT (sem custo extra) |
| Imagem avulsa (fallback) | `nanobanana-unity` | Gemini grátis — usar quando quota do ChatGPT esgotada |
| Imagem avulsa (contingência) | `image-gen-unity` | FAL API, pago (~$0,06–$0,22/img) — último recurso |
| Reels/TikTok/YouTube | `roteiro-unity` | Disponível na V1 |

---

## Integração com a Biblioteca Técnica (V1+)

Quando a Fase 7 da biblioteca estiver concluída:

1. Extraia o gancho aprovado como query em texto
2. Envie para a REST API da biblioteca (Supabase pgvector)
3. Incorpore os campos retornados (`Titulo`, `Fabricante_Fonte`, `Resumo_IA`, `Tags`, `Norma_Ref`) nas orientações técnicas do briefing

**No MVP:** opere sem a biblioteca. O conteúdo técnico virá do contexto fornecido no input.

---

## Contexto de marca (empresa piloto)

**Empresa:** Construção a seco (drywall / steel frame)
**Público:** Construtores, engenheiros, arquitetos, clientes finais interessados em reforma/construção
**Tom:** Técnico mas acessível, autoridade sem arrogância, foco em praticidade e resultado
**Restrições:** Não prometer prazos ou preços; não usar imagens de obras com EPI incorreto

> Este bloco será substituído pelo contexto CCOS da empresa ativa quando o multi-empresa estiver em operação.

---

## Exemplo de invocação

```
/briefing-unity

Janela: semana de 12/05 — Dia das Mães
Produto: Drywall para reforma rápida de ambientes internos
Plataforma: Instagram + TikTok
Formato: Carrossel (Instagram) + Reels (TikTok)
Contexto: mãe que quer reformar sem obra longa, público feminino 35-50
```

---

*Skill: briefing-unity | Projeto: Unity Content | MVP*
