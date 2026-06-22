---
name: legenda-para-post-estatico
description: Escreve a legenda de um post estático do Instagram — imagem única com copy sobreposta. Chamado no final do /estatico-unity antes de entregar o PNG. No post estático, a legenda carrega mais peso porque a imagem não se move — é ela que faz a pessoa engajar. Dispara quando: "escreve a legenda desse post", "caption para post de imagem", "legenda para post estático".
---

# Legenda para Post Estático

## Contexto da empresa

Antes de escrever, confirmar que tem em contexto:
- O que a imagem mostra e o que o post comunica
- O avatar (conforme seção ICP em `_contexto/empresa.md`)
- `_contexto/preferencias.md` — tom de voz e restrições de compliance

**Contexto algorítmico:** posts estáticos têm menor alcance orgânico no Instagram do que Reels e carrosseis. A legenda precisa puxar ainda mais peso em comentários e compartilhamentos — os sinais que o algoritmo usa para redistribuir posts estáticos.

---

## Coleta de Informações

**Obrigatório:**
- `[O QUE A IMAGEM MOSTRA]` — cena arquitetônica, produto instalado, close de detalhe
- `[O QUE A LEGENDA PRECISA ENTREGAR]` — história técnica, reflexão, argumento, lançamento
- `[AVATAR]` — arquiteto / construtor / proprietário

**Opcional:**
- `[TOM]` — técnico / reflexivo / consultivo / provocador
- `[CTA]` — comentar, compartilhar, salvar, link na bio
- `[CONTEXTO]` — obra real, detalhe técnico, bastidor, conteúdo recorrente

---

## Os 4 Tipos de Legenda para Post Estático

**1. Legenda narrativa**
Conta uma história — a imagem é o ponto de entrada, a legenda é a história completa.
Funciona melhor com: fotos de obra, instalação concluída, projeto real.

**2. Legenda de reflexão técnica**
Uma perspectiva ou insight desenvolvido com profundidade. Precisa ter argumento.
Funciona melhor com: imagens de produto, detalhe técnico, seção transversal.

**3. Legenda de lançamento com contexto**
Comunica algo novo com a história por trás — não só o fato.
Funciona melhor com: novo produto, nova linha, parceria técnica.

**4. Legenda de conexão**
Nomeia a situação do avatar, valida o que ele sente, cria identificação.
Funciona melhor com: imagens que representam uma dor ou aspiração do ICP.

---

## Anatomia da Legenda de Post Estático

### Primeira linha — o hook
Aparece antes do "ver mais". Precisa funcionar sozinha.

### Corpo — onde o valor está
Parágrafos curtos (máximo 3-4 linhas) com quebra de linha entre eles.
O post estático suporta legendas mais longas — use isso.
A virada ou o insight principal fica no penúltimo parágrafo — não no primeiro.

### CTA orientado a comentários ou compartilhamentos
- "Me conta nos comentários: como você especifica esquadrias hoje?"
- "Manda esse post para o arquiteto ou construtor que precisa ver isso"
- "Salva para mostrar no próximo briefing de projeto"

---

## Output

```
IMAGEM: [o que a imagem mostra]
TIPO DE LEGENDA: [narrativa / reflexão / lançamento / conexão]
AVATAR: [arquiteto / construtor / proprietário]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGENDA:

[PRIMEIRA LINHA — hook antes do "ver mais"]

[Parágrafo 1]

[Parágrafo 2]

[Parágrafo 3]

[Parágrafo 4 — a virada ou o insight principal]

[CTA — comentar, compartilhar ou salvar com razão específica]

[Hashtags — ao final, se aplicável]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VARIAÇÃO DE PRIMEIRA LINHA:
[Opção 2 — tom ou ângulo diferente]
```

---

## Limites técnicos obrigatórios

- **Máximo absoluto:** 2.200 caracteres (limite do Instagram)
- **Alvo real:** 800–1.400 caracteres — post estático suporta legenda mais longa que carrossel, mas ainda deve ser enxuta
- **Máximo de hashtags:** 30 — usar entre 5 e 10, sempre no final
- Antes de entregar, verificar mentalmente o tamanho. Se passou de 1.500 caracteres, há redundância — cortar.

## O Que Não Fazer

- Começar com o nome da marca ou "ei"
- Legenda genérica que poderia ter sido escrita por qualquer empresa
- Descrever a imagem na legenda — a imagem já se descreve
- Mais de um CTA
- Promessas absolutas de desempenho sem base técnica (ver `_contexto/preferencias.md`)
- Ultrapassar 1.500 caracteres sem justificativa real de conteúdo

---

## Onde salvar

Após aprovação, salvar a legenda como **`_legenda.md`** (sempre com underscore) na pasta do
conteúdo: `conteudo/post-estatico/[periodo]/[dia-tema]/_legenda.md`, sob a seção "LEGENDA APROVADA".
É esse arquivo que o `/publicar-social-unity` lê na hora de publicar.
