# [Nome do Projeto/Cliente] — Inventário de Fotos

Subpasta do Drive de fotos de obras para a empresa. Preencher com o inventário das fotos disponíveis para o projeto.

**ID da pasta no Drive:** `[ID_DA_PASTA_NO_DRIVE]`
**Link direto:** `[URL_DA_PASTA_NO_DRIVE]`

## Atenção ao formato das fotos

[Descrever o formato das fotos — ex: JPEG, PNG, HEIC]

Se as fotos estiverem em formato **HEIC** (padrão Apple):

- **Windows não exibe nativamente** (precisa de extensão ou conversão)
- **Pesadas** (1,5–4MB cada) — não cabem facilmente em contexto de conversa
- **API de download retorna base64 muito grande**

### Como usar essas fotos

**Opção 1 — Conversão em lote (recomendado):**

1. Baixar a pasta inteira do Drive em zip
2. Converter com ImageMagick: `magick mogrify -format jpg -resize 1920x1920\> *.heic`
3. Salvar versões JPEG em `produtos/fotos-obras/[projeto]/` localmente

**Opção 2 — Conversão individual sob demanda:**

1. Identificar a foto desejada pelo ID na lista abaixo
2. Baixar via `mcp__claude_ai_Google_Drive__download_file_content`
3. Salvar como `.heic` localmente
4. Converter com ferramenta online (cloudconvert.com) ou ImageMagick

**Opção 3 — Visualizar direto no Drive:**

- Abrir o link de view de cada foto no navegador (Google Drive converte HEIC automaticamente)
- Capturar screenshot caso precise usar a imagem em conteúdo

---

## Lista de fotos

Organizar por série/sessão conforme disponível.

| Arquivo | ID Drive | Tamanho |
|---|---|---|
| [preencher] | `[ID_DRIVE]` | [tamanho] |

---

## Notas do inventário

[Observações sobre as fotos: perspectiva de cada série, variações de ambiente, formatos especiais, data das capturas, etc.]

---

## Próximo passo recomendado

Para incorporar este acervo ao fluxo de conteúdo:

1. Baixar a pasta inteira do Drive (botão "Baixar" no Google Drive faz zip automático)
2. Converter HEIC → JPEG em lote (se necessário)
3. Salvar versões otimizadas (1920×1920, ~300KB) em `produtos/fotos-obras/[projeto]/`
4. Criar mini-galeria com classificação manual (fachada / interior / detalhe / produto)
