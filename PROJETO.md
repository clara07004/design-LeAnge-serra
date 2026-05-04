# Projeto — Unity Content (Status de Implementação)

## Status atual

**Fase:** MVP — conectar as peças que já existem

**Skills instaladas:**
- `calendario-comercial` ✅
- `briefing-unity` ✅ (gates de aprovação conversacionais incluídos)
- `schwartz-copy` ✅
- `ogilvy-copy` ✅
- `carrossel-unity` ✅ (integra gpt-image2-unity para imagens fotográficas nos slides)
- `gpt-image2-unity` ✅ (gpt-image-1 via OpenAI API; key em `credentials/openai_key.txt`)

**Infraestrutura:**
- Node.js 24.15.0 instalado
- Playwright + Chromium instalados e testados (renderização HTML → PNG OK)
- Python 3.14 + openai SDK 2.33.0 instalados (geração de imagem)

## Próximo passo

1. Adicionar API key OpenAI em `credentials/openai_key.txt`
2. Preencher `marca/design-guide.md` com identidade visual da empresa piloto
3. Fazer a 1ª run real do fluxo completo: `/calendario` → `/briefing-unity` → `/carrossel-unity`
4. Validar com 10 conteúdos produzidos pelo fluxo

## Skills pendentes (instalar conforme fluxo avança)

| Skill | Status |
|---|---|
| `nanobanana-unity` | 🔜 Fallback de imagem (quando GPT falhar) |
| `image-gen-unity` | 🔜 Contingência |
| `publicar-social-unity` | 🔜 Quando chegar na publicação |
| `triagem-youtube-unity` | 🔜 V1 |
| `roteiro-unity` | 🔜 V1 (a construir) |

---

<!-- Atualizar conforme o projeto avança. Para arquitetura completa, ver MAPA-TECNICO.md -->
