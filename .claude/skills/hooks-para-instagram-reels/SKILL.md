---
name: hooks-para-instagram-reels
description: Gera hooks específicos para Instagram Reels — combinando o primeiro frame visual com a primeira frase falada ou texto na tela. Usado DENTRO do /roteiro-leange antes de escrever o roteiro completo. Considera a lógica de salvamentos e compartilhamentos do Instagram. Dispara quando: "hook para Reel", "como começar meu Reel", "abertura de Reel Instagram", "como parar o scroll no Instagram", "primeiros segundos do Reel".
---

# Hooks para Instagram Reels

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — ICP e posicionamento
- `_contexto/preferencias.md` — tom de voz e restrições de compliance

O "nicho" e o "avatar" são definidos em `_contexto/empresa.md`.

---

## O que essa skill faz

Cria hooks para Reels — a combinação entre o primeiro frame visual e a primeira frase que determinam se o espectador vai assistir ou deslizar.

No Instagram, o Reel compete com fotos, carrosseis, stories e outros Reels no mesmo feed. O hook precisa se destacar nesse contexto específico.

---

## Coleta de Informações

**Obrigatório:**
- `[TEMA]` — sobre o que é o Reel
- `[AVATAR]` — persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)
- `[OBJETIVO DO REEL]` — salvar, compartilhar, comentar, converter

**Opcional:**
- `[TOM]` — educativo, informativo, provocativo, revelador
- `[FORMATO]` — talking head, B-roll com narração, texto na tela

---

## A Diferença do Hook para Reels

No Instagram, o usuário não está necessariamente em modo de scroll de vídeos. O hook visual (primeiro frame) precisa ser ainda mais forte para parar alguém que não estava esperando um vídeo.

**O que o algoritmo do Instagram recompensa:**
- Salvamentos → hook que promete valor prático durável
- Compartilhamentos → hook de identificação ("isso é exatamente o que eu vivo")
- Completion rate → hook que cria curiosidade que só se resolve no final

---

## Os 7 Tipos de Hook para Reels

1. **O salvável**: "Salva esse porque você vai precisar quando for planejar a próxima viagem com pet"
2. **O compartilhável**: "Manda para o amigo tutor de pet que vai te agradecer"
3. **A promessa de valor prático**: "[N] coisas sobre [tema] que mudam como você escolhe a pousada"
4. **O contraste**: "Antes eu deixava o pet em casa por padrão. Hoje penso diferente."
5. **A pergunta de identificação**: "Você também já cancelou uma viagem porque a pousada não aceitava seu pet?"
6. **O micro-tutorial**: "Como avaliar se uma pousada é realmente pet friendly em 3 passos"
7. **A afirmação polarizadora**: "Pousada que só 'aceita pet' não é pousada pet lover. É outra experiência."

---

## Output

```
TEMA: [tema]
AVATAR: [persona LeAnge (tutora de alta renda 26–55, pet como filho de 4 patas; ver `_contexto/persona.md`)]
OBJETIVO: [salvar / compartilhar / comentar / converter]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOOKS GERADOS:

[Tipo 1 — O salvável]
Primeiro frame: [o que mostrar — expressão, texto sobreposto, cena da pousada]
Frase de abertura: "[hook]"
Por que funciona: [conexão com comportamento de salvamento]

[Tipo 2 — O compartilhável]
Primeiro frame: [...]
Frase de abertura: "[hook]"
Por que funciona: [...]

[repetir para os 7 tipos]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HOOK MAIS ALINHADO COM O OBJETIVO ([objetivo]):
[Hook recomendado + como abrir o Reel visualmente para reforçá-lo]
```
