# Projeto — CCOS (Status de Implementação)

## Status atual

**Fase:** MVP validado — fluxo completo rodando. Template base pronto para replicação por empresa.

**Skills de produção instaladas:**
- `calendario-comercial` ✅ (atualizado: lê contexto, coleta frequência de postagem, output proporcional)
- `briefing-unity` ✅
- `carrossel-unity` ✅
- `estatico-unity` ✅ (novo: post card único — foto GPT + HTML + Playwright → PNG pronto)
- `roteiro-unity` ✅ (novo: script de vídeo — motor Ogilvy para orgânico, Schwartz para tráfego)

**Motores (usados internamente pelas skills de produção):**
- `gpt-image2-unity` ✅ (motor de imagem do carrossel e estatico-unity)
- `nanobanana-unity` ✅ (fallback gratuito)
- `ogilvy-copy` ✅ (motor de copy orgânica — roteiro-unity + conteúdo de marca)
- `schwartz-copy` ✅ (motor de copy de tráfego — roteiro-unity + criativos pagos)

**Infraestrutura:**
- Node.js 24.15.0 instalado
- Playwright + Chromium instalados e testados (renderização HTML → PNG OK)
- Python 3.14 + openai SDK 2.33.0 instalados

**Setup:**
- `/setup` reescrito: confirmação obrigatória antes de salvar, pergunta de manual da marca, coleta de frequência de postagem por plataforma, regra verbal > documento
- `/iniciar` removido (redundante — CLAUDE.md já carrega contexto automaticamente)

## Próximo passo

1. Replicar o template para cada empresa-alvo (rodar `/setup` em cada repositório)
2. Medir por empresa: tempo total vs. processo anterior, taxa de aprovação sem ajuste, qualidade percebida
3. Instalar `publicar-social-unity` quando chegar na etapa de publicação

## Skills pendentes

| Skill | Status |
|---|---|
| `image-gen-unity` | 🔜 Contingência (FAL API, pago) |
| `publicar-social-unity` | 🔜 Quando chegar na publicação |
| `triagem-youtube-unity` | 🔜 V1 |

---

<!-- Atualizar conforme o projeto avança. Para arquitetura completa, ver MAPA-TECNICO.md -->
