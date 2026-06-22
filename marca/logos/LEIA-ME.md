# Logos da marca

Adicionar os arquivos de logo aqui após rodar `/setup`.

## Arquivos esperados

| Arquivo | Uso |
|---|---|
| `logo-cor.png` | Logo colorida — slides com fundo claro |
| `logo-branco.png` | Logo branca — slides com fundo escuro (padrão dos carrosséis) |

## Como adicionar

1. Baixar as logos do Google Drive (pasta "Identidade Visual" configurada em `_contexto/referencias.md`)
2. Renomear para `logo-cor.png` e `logo-branco.png`
3. Salvar nesta pasta

As logos são referenciadas nos HTMLs de carrossel como:
```html
<!-- Slide escuro (padrão) -->
<img src="../../../../../marca/logos/logo-branco.png" style="height:48px;object-fit:contain;">

<!-- Fundo claro -->
<img src="../../../../../marca/logos/logo-cor.png" style="height:48px;object-fit:contain;">
```
