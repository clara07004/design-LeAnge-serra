---
version: "1.0"
name: "LeAnge"
description: "Pousada Pet Lover — LeAnge Serra — Identidade Visual"
status: configured
---

# =============================================================================
# FONTE: preenchido fielmente a partir do documento oficial `identidade-visual.md`
# (ver ingestão completa em marca/identidade-visual.md).
# REGRA: valores marcados "DOCUMENTADO" vêm do documento. Valores "" com comentário
# "NÃO DOCUMENTADO" NÃO existem no documento — não inferir; preencher só quando houver
# documento específico. Valores "OPERACIONAL" são defaults técnicos do sistema (contraste,
# escala), não afirmações de marca.
# Grafia obrigatória: sempre "LeAnge" (L e A maiúsculos, sem espaço, sem hífen).
# NUNCA: "Le Ange", "LE ANGE", "leange", "LEANGE", "Le-Ange".
# =============================================================================

# ----------------------------------------------------------------------------
# PALETA OFICIAL — 8 cores (DOCUMENTADO, com o "uso" exato do documento)
# (repositório exclusivo da LeAnge Serra — cores fora do escopo da Serra não constam nesta paleta)
# ----------------------------------------------------------------------------
paleta_oficial:
  verde_escuro:  { hex: "#475323", uso: "Cor principal da marca, fundos institucionais" }
  verde_oliva:   { hex: "#8A8C4A", uso: "Suporte, detalhes" }
  verde_limao:   { hex: "#CBD967", uso: "Destaque, energia, CTAs" }
  laranja:       { hex: "#CB722C", uso: "Calor, Serra, outono/inverno" }
  dourado:       { hex: "#BFA656", uso: "Luxo, sofisticação, versão colorida do logo" }
  oliva_claro:   { hex: "#A59C13", uso: "Suporte" }
  cinza:         { hex: "#4D4D4D", uso: "Texto" }
  preto:         { hex: "#000000", uso: "Versão P&B do logo" }

# ----------------------------------------------------------------------------
# Mapeamento para os tokens que as skills consomem
# (só preenchido onde o documento sustenta; o resto fica vazio até haver documento)
# ----------------------------------------------------------------------------
colors:
  primary: "#475323"             # DOCUMENTADO — Verde Escuro, "cor principal da marca"
  accent: "#CBD967"              # DOCUMENTADO — Verde Limão, "destaque, energia, CTAs"
  secondary: "#BFA656"           # DOCUMENTADO — Dourado, "versão colorida do logo, luxo"
  ink: "#4D4D4D"                 # DOCUMENTADO — Cinza, "Texto"
  black: "#000000"               # DOCUMENTADO — Preto, "versão P&B do logo"
  serra: "#CB722C"               # DOCUMENTADO — Laranja, "Serra, outono/inverno"
  oliva: "#8A8C4A"               # DOCUMENTADO — Verde Oliva, "suporte, detalhes"
  oliva-claro: "#A59C13"         # DOCUMENTADO — Oliva Claro, "suporte"
  # Slots operacionais / não documentados:
  on-primary: "#FFFFFF"          # OPERACIONAL — contraste de texto; não consta no documento
  surface-card: "#FFFFFF"        # OPERACIONAL — superfície; não consta no documento
  canvas: ""                     # NÃO DOCUMENTADO — o documento não define off-white/fundo de canvas
  primary-active: ""             # NÃO DOCUMENTADO — o documento não define tom de hover
  primary-disabled: ""           # NÃO DOCUMENTADO
  muted: ""                      # NÃO DOCUMENTADO — o documento não define cor de texto secundário

# ----------------------------------------------------------------------------
# TIPOGRAFIA (DOCUMENTADO)
# ----------------------------------------------------------------------------
typography:
  principal:
    fontFamily: "Comfortaa"                 # DOCUMENTADO — "logotipo, títulos, headlines"
  secundaria:
    fontFamily: "AvenirNext LT Pro Cn"      # DOCUMENTADO — "textos de apoio, legendas, corpo"
  dica_digital: "Em layouts digitais, usar espaçamento entre letras (tracking 50–150) na AvenirNext para transmitir leveza e modernidade."  # DOCUMENTADO
  # Chaves que as skills leem (mapeadas às 2 fontes documentadas):
  display:  { fontFamily: "Comfortaa" }            # DOCUMENTADO (fonte); tamanho NÃO DOCUMENTADO
  heading:  { fontFamily: "Comfortaa" }            # DOCUMENTADO (fonte); tamanho NÃO DOCUMENTADO
  body:     { fontFamily: "AvenirNext LT Pro Cn" } # DOCUMENTADO (fonte); tamanho NÃO DOCUMENTADO
  label:    { fontFamily: "AvenirNext LT Pro Cn" } # DOCUMENTADO (fonte); tamanho NÃO DOCUMENTADO
  caption:  { fontFamily: "AvenirNext LT Pro Cn" } # DOCUMENTADO (fonte); tamanho NÃO DOCUMENTADO
  # NÃO DOCUMENTADO: o documento não especifica tamanhos, pesos, line-height ou letter-spacing.

# ----------------------------------------------------------------------------
# LOGOS (DOCUMENTADO — 3 versões oficiais + símbolo)
# ----------------------------------------------------------------------------
logos:
  assinatura: "LeAnge + POUSADA PET FRIENDLY"
  versao_1_vertical_pb:
    composicao: "Símbolo do cão com auréola (line art) + 'LeAnge' + 'POUSADA PET FRIENDLY'"
    fundo: "branco"
    uso: "documentos, papelaria, fundos claros"
  versao_2_vertical_colorida:
    composicao: "Mesma composição em dourado (#BFA656) sobre fundo verde escuro (#475323)"
    uso: "peças institucionais, posts, apresentações"
  versao_3_horizontal_pb:
    composicao: "Símbolo à esquerda + 'LeAnge' à direita"
    fundo: "preto"
    uso: "aplicações horizontais, capas, banners"
  simbolo:
    descricao: "Cão sentado de perfil, linha contínua, com auréola"
    estilo: "flat, linear, sem preenchimento; sem perspectiva, realismo ou profundidade"
    uso: "pode ser usado só símbolo, só logotipo, ou completo — depende do espaço disponível"

# ----------------------------------------------------------------------------
# BOXES E LAYOUTS (DOCUMENTADO)
# ----------------------------------------------------------------------------
boxes:
  cantos: "menos arredondados (não o arredondado original do manual antigo)"
  transparencia: "70–85%"
  cor_do_box: "harmonizada com a foto de fundo — usar a cor da paleta mais próxima à foto; se a paleta ficaria grotesca, usar cor da própria imagem"
  sombra: "drop shadow sutil permitida para leveza"

# ----------------------------------------------------------------------------
# CANAIS / LOCALIZAÇÃO (DOCUMENTADO)
# ----------------------------------------------------------------------------
instagram: "@pousadaleange"
localizacao_geral: "Vale das Videiras, RJ"

# ----------------------------------------------------------------------------
# TOKENS ESTRUTURAIS OPERACIONAIS (NÃO DOCUMENTADO — defaults técnicos do sistema)
# O documento de identidade não define espaçamento, raios, botões nem escala.
# Mantidos como defaults neutros para as skills funcionarem; não são regras de marca.
# ----------------------------------------------------------------------------
spacing: { xs: "16px", sm: "24px", md: "40px", lg: "64px", xl: "96px", section: "160px" }  # OPERACIONAL
rounded: { sm: "4px", md: "8px", lg: "16px", pill: "9999px" }                               # OPERACIONAL

# ----------------------------------------------------------------------------
# ESTILO DE IMAGEM — NÃO DOCUMENTADO
# Nenhum documento de direção visual / fotografia foi ingerido.
# O documento de identidade traz apenas grafia, cores, tipografia, logos e boxes.
# NÃO INFERIR estilos de foto, mood, backgrounds ou templates de layout.
# Preencher fielmente somente quando houver um documento específico de direção de imagem.
# ----------------------------------------------------------------------------
image_style:
  status: nao-documentado
