---
name: legenda-para-carrossel
description: Escreve a legenda de um carrossel do Instagram — a primeira linha que aparece no feed antes de deslizar, o corpo que aprofunda sem repetir os slides, e o CTA de salvamento. Chamado no final do /carrossel-unity antes de entregar o pacote completo. Dispara quando: "escreve a legenda do meu carrossel", "preciso de uma legenda para esse post", "caption para carrossel do Instagram".
---

# Legenda para Carrossel

## Contexto da empresa

Antes de escrever, confirmar que tem em contexto:
- O tema e o objetivo do carrossel
- O avatar (conforme seção ICP em `_contexto/empresa.md`)
- `_contexto/preferencias.md` — tom de voz e restrições de compliance

A legenda funciona como pré-frame: prepara o leitor para o que vem nos slides e aumenta a taxa de swipe-through.

**Sinal algorítmico principal do carrossel:** salvamentos. O CTA precisa ser orientado para salvar — com uma razão específica para salvar, não só "salva esse post".

---

## Coleta de Informações

**Obrigatório:**
- `[O QUE O CARROSSEL ENTREGA]` — o tema, o framework ou o conteúdo dos slides
- `[OBJETIVO DO CARROSSEL]` — autoridade / nutrição / conversão / quebra de objeção / educativo
- `[AVATAR]` — arquiteto / construtor / proprietário

**Opcional:**
- `[SLIDE DE COVER]` — o título do primeiro slide, para a legenda não repetir
- `[CTA]` — padrão é salvar, mas pode ser comentar, seguir ou link na bio
- `[TOM]` — direto / técnico / provocador / instrutivo

---

## Anatomia da Legenda de Carrossel

### Primeira linha — o hook
Aparece no feed antes de o espectador deslizar.
- Não repete o título do cover — complementa, instiga ou adiciona contexto
- Opções eficazes:
  - A promessa do que está dentro: "Aqui está o framework que uso para especificar [produto]"
  - Uma afirmação que só faz sentido depois de ver os slides
  - Um número: "7 critérios que separam esquadrias de alto desempenho das comuns"
  - Uma pergunta que os slides respondem

### Corpo — pré-frame ou aprofundamento

**Opção A — Pré-frame (recomendado para autoridade e conversão):**
Prepara o leitor para o que vem nos slides — dá contexto de por que esse conteúdo importa.

**Opção B — Complemento (recomendado para educativo e nutrição):**
Adiciona uma camada que os slides não cobriram.
"O slide 3 é o mais importante — e vai contra o que a maioria especifica por padrão."

### CTA de salvamento com razão específica
- Não: "salva esse post"
- Sim: "salva para consultar quando estiver especificando esquadrias no próximo projeto"
- Sim: "salva esse comparativo — você vai querer mostrar para seu cliente"

---

## Output

```
CARROSSEL: [o que os slides entregam]
OBJETIVO: [autoridade / nutrição / conversão / educativo]
AVATAR: [arquiteto / construtor / proprietário]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGENDA:

[PRIMEIRA LINHA — hook antes do "ver mais" / antes de deslizar]

[Parágrafo 1 — pré-frame ou contexto]

[Parágrafo 2 — por que esse conteúdo importa para o avatar]

[Parágrafo 3 — opcional: highlight de um slide específico]

[CTA — salvar com razão específica + ação secundária se houver]

[Hashtags — ao final, sem misturar com o corpo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VARIAÇÃO DE PRIMEIRA LINHA:
[Opção 2 — ângulo diferente para testar]
```

---

## Limites técnicos obrigatórios

- **Máximo absoluto:** 2.200 caracteres (limite do Instagram)
- **Alvo real:** 600–1.000 caracteres — legenda de carrossel compete com os slides; deve ser breve e direta
- **Máximo de hashtags:** 30 — usar entre 5 e 10, sempre no final, sem misturar com o corpo
- Antes de entregar, contar os caracteres mentalmente. Se passar de 1.200, cortar — a legenda não deve ser o conteúdo principal, os slides são.

## O Que Não Fazer

- Repetir o texto do cover ou dos slides — a legenda adiciona, não duplica
- CTA genérico ("salva esse post") sem razão específica para salvar
- Revelar tudo na legenda antes de o leitor deslizar
- Prometer desempenho técnico sem base (ex: "elimina 100% do ruído")
- Ultrapassar 1.200 caracteres — se precisou de mais do que isso, o texto está redundante

---

## Onde salvar

Após aprovação, salvar a legenda como **`_legenda.md`** (sempre com underscore) na pasta do
conteúdo: `conteudo/carrosseis/[periodo]/[dia-tema]/_legenda.md`, sob a seção "LEGENDA APROVADA".
É esse arquivo que o `/publicar-social-unity` lê na hora de publicar.
