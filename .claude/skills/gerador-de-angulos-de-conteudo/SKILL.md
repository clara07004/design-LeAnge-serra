---
name: gerador-de-angulos-de-conteudo
description: Recebe tema, nicho e público — entrega 10 ângulos únicos com perspectiva diferente, nível de audiência diferente e formato diferente. Ideal para preencher calendário editorial ou quando a marca está sempre abordando os mesmos assuntos do mesmo jeito. Complementar ao /gerador-de-angulos-para-um-tema — este usa matriz de variação (perspectivas × níveis × formatos narrativos), aquele usa 10 lentes criativas. Use ANTES do /briefing-leange. Dispara quando: "preciso de ideias para o tema X", "me dá ângulos sobre Y", "quero variar o conteúdo sobre Z".
---

# Gerador de Ângulos de Conteúdo

## Contexto da empresa

Antes de gerar, ler:
- `_contexto/empresa.md` — ICP, pousada/serviços e posicionamento
- `_contexto/preferencias.md` — tom de voz, palavras proibidas, restrições de compliance
- `_contexto/estrategia.md` — gaps prioritários a resolver com conteúdo

O "criador" é a marca, o "seguidor" é o ICP definido em empresa.md.

---

## O que essa skill faz

Transforma um tema em 10 ângulos distintos — cada um com uma perspectiva única, um nível de audiência claro e um gancho pronto para usar.

O maior erro é tratar o tema como o ângulo. "Pousada pet friendly" não é um ângulo — é um tema com dezenas de entradas possíveis.

---

## Coleta de Informações

**Obrigatório:**
- `[TEMA]` — o assunto central (ex: viajar com pets, all inclusive pet friendly, inverno na Serra com cães)
- `[NICHO]` — segmento de mercado da empresa (conforme `_contexto/empresa.md`)
- `[PÚBLICO]` — quem é a audiência em uma frase (conforme seção ICP em `_contexto/empresa.md`)

Se algum estiver ausente, perguntar antes de gerar.

---

## Regra fundamental

**Nenhum dos 10 ângulos pode abordar o tema pelo mesmo lado.**

Antes de entregar: ler os 10 ganchos em sequência. Se dois poderiam pertencer ao mesmo post, substituir um.

---

## Matriz de variação

### Perspectivas disponíveis

| Perspectiva | O que faz |
|---|---|
| Educacional | Ensina um conceito, processo ou dado concreto do zero |
| Opinião | Toma uma posição sobre algo polêmico ou contraintuitivo no setor |
| Bastidor | Mostra como a empresa ou o profissional faz na prática |
| Erro comum | Expõe uma crença falsa ou armadilha que o avatar cai sem perceber |
| Comparativo | Contrasta duas abordagens ou experiências (pet friendly vs pet lover, etc.) |
| Resultado real | Mostra transformação com dados, antes/depois ou caso real |

### Níveis de audiência

| Nível | Quem é |
|---|---|
| Iniciante | Ainda descobrindo o básico, quer validação antes de reservar |
| Intermediário | Já conhece a pousada, quer aprofundar além do básico |
| Avançado | Já conhece/frequenta a pousada, quer detalhes que confirmem a escolha |

### Formatos narrativos

| Formato | Como funciona |
|---|---|
| Lista | X erros, X razões, X passos — clareza e salvamento |
| Narrativa | História com início, tensão e virada — cria identificação |
| Provocação | Afirmação contraintuitiva que força pausa — gera debate |
| Tutorial | Passo a passo com instruções acionáveis — gera salvamento |

---

## Output

```
TEMA: [tema]
NICHO: [nicho]
PÚBLICO: [público]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ÂNGULOS GERADOS:

1. [Nome do Ângulo]
   Perspectiva: [tipo] | Nível: [iniciante/intermediário/avançado] | Formato: [tipo]
   Gancho: [gancho de até 8 palavras]
   O que entregaria: [Frase 1 — problema ou tensão. Frase 2 — o insight ou mudança de perspectiva.]

[Repetir para 10 ângulos]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PARA COMEÇAR: mix recomendado para a próxima semana:
- 1 ângulo de resultado real ou erro comum → tende a ser compartilhado, amplia alcance
- 1 ângulo educacional → tende a ser salvo, constrói autoridade
- 1 ângulo de opinião → gera comentários e debate, aumenta engajamento
- 1 ângulo de bastidor → cria proximidade com quem já conhece a marca
```
