---
name: gerador-de-angulos-para-um-tema
description: Recebe um tema único e gera múltiplos ângulos diferentes para abordá-lo — cada ângulo com uma perspectiva, gancho e formato distintos. Resolve o problema de quem sabe sobre o que falar mas não sabe como tornar o mesmo assunto interessante de formas diferentes. Use ANTES do /briefing-unity para explorar ângulos antes de definir o formato. Dispara quando: "preciso de ângulos diferentes para um tema", "como falar sobre o mesmo assunto de formas novas", "variações de um tema", "me ajuda a explorar um tema".
---

# Gerador de Ângulos para um Tema

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — produtos/serviços, ICP e posicionamento
- `_contexto/preferencias.md` — tom de voz, palavras proibidas, restrições de compliance
- `_contexto/estrategia.md` — foco atual e gaps prioritários

O "criador" é a marca, o "avatar" é o ICP definido em empresa.md.

---

## O que essa skill faz

Recebe um tema e gera o máximo de ângulos distintos possíveis — cada um com uma perspectiva diferente, gancho diferente e potencial de alcançar um momento diferente do avatar.

Um tema não é um conteúdo. É uma matéria-prima que pode virar dezenas de peças. O trabalho é multiplicar as entradas para o mesmo tema sem que nenhuma pareça repetição das outras.

---

## Coleta de Informações

**Obrigatório:**
- `[TEMA]` — o assunto central (ex: isolamento acústico, PVC vs alumínio, instalação em Steel Frame)
- `[NICHO]` — segmento de mercado da empresa (conforme `_contexto/empresa.md`)
- `[AVATAR]` — perfil do cliente-alvo (conforme seção ICP em `_contexto/empresa.md`)

**Opcional:**
- `[PLATAFORMA]` — afeta quais formatos sugerir para cada ângulo
- `[QUANTIDADE]` — quantos ângulos gerar (padrão: 10-15)
- `[JÁ CRIOU]` — ângulos que já explorou (para não repetir)

---

## As 10 Lentes para Gerar Ângulos

Para qualquer tema, estas lentes geram ângulos distintos:

1. **Erro comum** — o que a maioria faz de errado sobre esse tema
2. **Contra-intuitivo** — o que parece verdade mas não é; o oposto do óbvio
3. **Antes/depois** — como era sem esse conhecimento vs. como é com ele
4. **Passo a passo** — como fazer na prática, passo a passo
5. **Por que não funciona** — as razões pelas quais tentativas comuns falham
6. **Iniciante vs. avançado** — o que muda na abordagem conforme o nível
7. **Mito vs. realidade** — desmontando uma crença popular sobre o tema
8. **Custo do problema** — o que acontece se o avatar não resolver isso
9. **Comparação** — esse método vs. outro método (ou essa crença vs. outra)
10. **História real** — como o produto ou empresa viveu esse tema na prática

---

## Output

```
TEMA: [tema]
NICHO: [nicho]
AVATAR: [avatar]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÂNGULOS GERADOS:

1. [Nome do ângulo — lente usada]
   Gancho: [primeira frase ou título]
   Perspectiva: [o que esse conteúdo defende ou revela]
   Formato recomendado: [Reel / carrossel / post estático / stories]

2. [Nome do ângulo]
   Gancho: [...]
   Perspectiva: [...]
   Formato: [...]

[Repetir para todos os ângulos]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÂNGULOS COM MAIOR POTENCIAL DE VIRALIZAÇÃO:
[2-3 ângulos com mais chance de alcance amplo — e por quê]

ÂNGULOS COM MAIOR POTENCIAL DE CONVERSÃO:
[2-3 ângulos que movem o avatar para mais perto do orçamento — e por quê]

SEQUÊNCIA SUGERIDA:
Se for criar uma série sobre [tema], publicar na ordem:
1. [ângulo X] — por quê começar aqui
2. [ângulo Y]
3. [ângulo Z]
```
