---
name: legenda-para-reel
description: Escreve a legenda de um Reel do Instagram — a primeira linha que aparece antes do play, o corpo que complementa o vídeo sem repetir, e o CTA final. Chamado no final do /roteiro-leange antes de entregar o pacote completo. Dispara quando: "escreve a legenda do meu Reel", "caption para Reel", "legenda para vídeo do Instagram".
---

# Legenda para Reel

## Contexto da empresa

Antes de escrever, confirmar que tem em contexto:
- O assunto e argumento central do Reel
- O avatar (persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`))
- `_contexto/preferencias.md` — tom acolhedor e acessível, sem promessas absolutas

A legenda do Reel tem dois momentos de leitura:
1. **Antes de assistir** — a primeira linha decide se a pessoa dá play
2. **Depois de assistir** — quem assistiu lê a legenda completa para engajar

---

## Coleta de Informações

**Obrigatório:**
- `[O QUE O REEL ENTREGA]` — o assunto, o argumento central ou o insight do vídeo
- `[AVATAR]` — persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)
- `[CTA]` — o que quer que a pessoa faça após assistir

**Opcional:**
- `[ROTEIRO OU RESUMO DO VÍDEO]` — para a legenda complementar sem repetir
- `[TOM]` — direto / informativo / provocador / revelador
- `[HASHTAGS]` — se quiser incluir

---

## Anatomia da Legenda de Reel

### Primeira linha — o hook
Aparece antes do "ver mais". Precisa funcionar sozinha como motivo para assistir.
- Não começa com "Ei!" nem com o nome da marca
- Não repete o título do Reel — complementa ou instiga
- Opções eficazes:
  - A afirmação central do vídeo em uma frase
  - Uma pergunta que o vídeo responde
  - Um dado concreto da pousada que ancora o conteúdo
  - Uma afirmação que só faz sentido depois de assistir

### Corpo — o complemento
2-5 parágrafos curtos. Não resume o vídeo — adiciona contexto, exemplo ou detalhe da experiência que o vídeo não teve espaço para entregar.

### CTA — único e específico
Um único CTA no final — congruente com o objetivo do Reel.
- Educativo → salvar, comentar com sua opinião, enviar para um amigo tutor
- Autoridade → seguir para mais conteúdo da pousada
- Conversão → link na bio + instrução exata ("acesse o link na bio para consultar disponibilidade")

---

## Output

```
REEL: [resumo do que o vídeo entrega]
AVATAR: [persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)]
CTA: [ação desejada]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEGENDA:

[PRIMEIRA LINHA — hook antes do "ver mais"]

[Parágrafo 1 — complemento ou contexto adicional]

[Parágrafo 2 — dado adicional ou exemplo real]

[Parágrafo 3 — se necessário]

[CTA — único, específico, congruente com o objetivo do Reel]

[Hashtags — se aplicável: no final, sem misturar com o corpo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

VARIAÇÃO DE PRIMEIRA LINHA:
[Opção 2 — tom diferente para testar]
[Opção 3 — ângulo diferente]
```

---

## Limites técnicos obrigatórios

- **Máximo absoluto:** 2.200 caracteres (limite do Instagram)
- **Alvo real:** 400–800 caracteres — Reel já tem o vídeo fazendo o trabalho pesado; legenda complementa, não compete
- **Máximo de hashtags:** 30 — usar entre 5 e 10, sempre no final
- Antes de entregar, verificar o tamanho. Reel com legenda longa perde leitura — quem assistiu o vídeo não quer ler um ensaio.

## O Que Não Fazer

- Repetir o roteiro do vídeo — a legenda complementa, não duplica
- Mais de um CTA
- "Link na bio" sem instrução do que fazer lá
- Promessas absolutas sem base real (ver `_contexto/preferencias.md`)
- Ultrapassar 900 caracteres sem necessidade real

---

## Onde salvar

Após aprovação, salvar a legenda como **`_legenda.md`** (sempre com underscore) na pasta do
conteúdo: `conteudo/roteiros/[periodo]/[dia-tema]/_legenda.md`, sob a seção "LEGENDA APROVADA".
É esse arquivo que o `/publicar-social-leange` lê na hora de publicar.
