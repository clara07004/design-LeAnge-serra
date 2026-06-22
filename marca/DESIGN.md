---
version: "1.0"
name: "[Nome da empresa]"
description: "[Descrição da empresa] — Manual de Marca v1.0"
status: configured
---

colors:
  primary: "[#XXXXXX]"           # Cor primária — ícone, estrutura, elementos principais
  primary-active: "[#XXXXXX]"    # Cor primária escurecida para hover/ativo
  primary-disabled: "[#XXXXXX]"  # Cor primária desbotada para estados desabilitados
  on-primary: "#FFFFFF"          # Texto branco sobre fundo primário (ou ajustar)
  secondary: "[#XXXXXX]"         # Cor secundária — [uso: tagline, acento, eco, etc.]
  on-secondary: "#FFFFFF"
  canvas: "[#XXXXXX]"            # Off-white ou fundo principal, backgrounds
  surface-card: "#FFFFFF"        # Branco puro — cards e superfícies
  ink: "[#XXXXXX]"               # Cor do texto principal
  body: "[#XXXXXX]"
  accent: "[#XXXXXX]"            # Cor de acento
  muted: "[#XXXXXX]"             # Cinza — textos secundários, legendas

  # Paleta de suporte
  white: "#FFFFFF"
  black: "[#XXXXXX]"
  off-white: "[#XXXXXX]"
  gray: "[#XXXXXX]"

  # DESCONTINUADA — preencher se houver cor descontinuada a evitar
  # [cor-descontinuada]: "[#XXXXXX]" — [motivo da descontinuação]

typography:
  display:
    fontFamily: "[Fonte de display — ex.: Poppins]"
    fontSize: "100px"
    fontWeight: "700"          # Bold
    lineHeight: "1.1"
    letterSpacing: "-0.02em"
  heading:
    fontFamily: "[Fonte heading]"
    fontSize: "70px"
    fontWeight: "700"
    lineHeight: "1.2"
  subheading:
    fontFamily: "[Fonte subheading]"
    fontSize: "48px"
    fontWeight: "600"
    lineHeight: "1.3"
  body:
    fontFamily: "[Fonte body — ex.: Montserrat, Lato, Inter]"
    fontSize: "28px"
    fontWeight: "400"
    lineHeight: "1.5"
  label:
    fontFamily: "[Fonte label]"
    fontSize: "22px"
    fontWeight: "700"
    lineHeight: "1.3"
  caption:
    fontFamily: "[Fonte caption]"
    fontSize: "20px"
    fontWeight: "400"
    lineHeight: "1.4"

  # Regras de uso
  # - [Fonte 1]: títulos, identidade da marca, headlines
  # - [Fonte 2]: corpo, labels, notas técnicas, legendas
  # - Mínimo 12px digital / 9pt impresso
  # - Não misturar mais de 2 famílias tipográficas
  # - [Regra adicional da marca, se houver]

spacing:
  xs: "16px"
  sm: "24px"
  md: "40px"
  lg: "64px"
  xl: "96px"
  section: "160px"

rounded:
  sm: "4px"
  md: "8px"
  lg: "16px"
  pill: "9999px"

# Logo
# - Nome: "[nome exato do logo — ex.: 'nomemarca' em minúsculo]"
# - [Descrever composição tipográfica, se houver: ex. 'nome' em Light + 'marca' em Bold]
# - Versão principal: [descrever — ex.: Vertical cor principal]
# - Versões aprovadas: [listar versões disponíveis]
# - Tamanho mínimo: 80px digital / 20mm impresso
# - Não alterar cores fora da paleta oficial
# - Não aplicar sombras, contornos ou efeitos
# - Não distorcer ou esticar
# - Não recriar com fontes diferentes
# - [Restrição adicional, se houver]

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: "16px 32px"
    height: "52px"
    fontFamily: "[Fonte dos botões]"
    fontWeight: "700"
    fontSize: "16px"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "16px 32px"

  card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "40px"
    border: "1px solid [#XXXXXX — cor da borda do card]"

  tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    fontFamily: "[Fonte das tags]"
    fontWeight: "700"
    fontSize: "12px"

# Regras de uso das cores
# PODE:
# - [Cor primária] com fundo branco — combinação principal
# - [Cor secundária] em [uso específico] sobre fundo claro
# - Logo branco sobre fundo [cor primária] — versão negativo
# - Texto escuro sobre off-white para leitura longa
#
# NÃO PODE:
# - [Cor primária] + [Cor secundária] sobrepostos sem elemento neutro
# - [Cor descontinuada] — paleta descontinuada
# - Alterar os valores HEX das cores primárias
# - [Restrição adicional]

# =============================================================================
# ESTILO DE IMAGEM — Referência visual da marca
# Para uso pelos motores de geração de imagem (gpt-image-1, etc.)
# Fonte: análise visual da referência em [data]
# =============================================================================

image_style:

  # ---------------------------------------------------------------------------
  # FILOSOFIA VISUAL — princípios que regem todos os posts
  # ---------------------------------------------------------------------------
  visual_philosophy:

    feel: "[Descreva a sensação visual da marca — ex.: Fluido, divertido e acolhedor / Técnico e elegante / Clean e premium]"

    forbidden_aesthetic: "[Descreva o que é proibido visualmente — ex.: layouts muito simétricos, estética de template pronto, fundo chapado com cor sólida + texto]"

    background_rule: |
      OBRIGATÓRIO: [Regra sobre o fundo de cada imagem/slide — ex.: toda imagem precisa ter um fundo
      com elementos visuais: texturas, gradientes, formas, fotografias. Fundo chapado + texto é inaceitável.]

    avoid:
      - "[O que evitar visualmente — ex.: layouts retos e muito centrados]"
      - "[Outro elemento proibido]"
      - "[Outro]"
      - "[Outro]"

    pursue:
      - "[O que buscar — ex.: composições com camadas: fundo + elementos decorativos + texto]"
      - "[Outro elemento desejado]"
      - "[Outro]"
      - "[Outro]"

  # ---------------------------------------------------------------------------
  # FOTOGRAFIA — como devem ser as fotos
  # ---------------------------------------------------------------------------
  photography:

    [estilo_foto_1]:
      description: "[Nome e descrição do estilo — ex.: Pessoas em ação no ambiente de uso do produto]"
      mood: "[Tom geral — ex.: Moody, atmosférico, slightly desaturated]"
      lighting: "[Iluminação — ex.: Ambient natural, soft side light]"
      color_grade: "[Tratamento de cor — ex.: Cool-neutral to warm shadows]"
      subjects: "[O que aparece na foto — ex.: Pessoas, ambientes, produto em contexto]"
      framing: "[Enquadramento — ex.: Often cropped tight, subject off-center]"
      brand_subjects: "[Sujeitos específicos desta marca — ex.: Profissional X revisando Y, cliente Z apreciando W]"

    [estilo_foto_2]:
      description: "[Nome e descrição]"
      mood: "[Tom]"
      lighting: "[Iluminação]"
      color_grade: "[Tratamento de cor]"
      framing: "[Enquadramento]"
      brand_subjects: "[Sujeitos específicos]"

    [estilo_foto_3]:
      description: "[Nome e descrição — ex.: Macro/detalhe da superfície e estrutura do produto]"
      mood: "[Tom — ex.: Técnico e elegante simultaneamente]"
      framing: "[Enquadramento — ex.: Close-up extremo — textura de superfície]"
      color_grade: "[Neutro, fiel às cores reais do produto]"
      brand_subjects: "[Ex.: Detalhe de material, acabamento, corte transversal]"

  # ---------------------------------------------------------------------------
  # BACKGROUNDS — tipos de fundo por slide
  # ---------------------------------------------------------------------------
  backgrounds:

    off_white_textured:
      use: "[Quando usar — ex.: Slides educativos, infográficos, textos principais]"
      color: "[Cor aproximada — ex.: #F5F5F0 cream/warm off-white]"
      texture: "[Textura — ex.: Paper ou linen texture sutil]"
      feel: "[Sensação — ex.: Leve, limpo, premium]"

    solid_accent:
      use: "[Quando usar — ex.: Slides de CTA final, fechamento, produto destaque]"
      color: "[Cor primária da marca — fundo sólido completo]"
      texture: "[Opcional: textura sutil]"
      feel: "[Sensação — ex.: Impacto, energia, marca]"

    full_bleed_dark:
      use: "[Quando usar — ex.: Cover, slides de problema, slides de transição]"
      description: "[Foto ocupa 100% do slide, tom escuro predominante]"
      overlay: "[Tipo de overlay — ou 'Nenhum overlay opaco']"
      text_color: "[Cor do texto sobre essa foto — ex.: Branco puro]"

    full_bleed_bright:
      use: "[Quando usar — ex.: Slides de solução com produto instalado]"
      description: "[Foto ocupando 100%, tom claro/natural, produto visível]"
      text: "[Cor do texto — ex.: Cor primária ou branco dependendo da foto]"

    split_dynamic:
      use: "[Quando usar — ex.: Slides de contexto/problema]"
      layout: "[Descrição do layout — ex.: 60% foto escura + 40% painel cor, borda curva na divisão]"
      text: "[Cor e posição do texto]"

  # ---------------------------------------------------------------------------
  # ELEMENTOS GRÁFICOS — os 'assets' de design recorrentes
  # ---------------------------------------------------------------------------
  graphic_elements:

    text_highlight_box:
      description: "Retângulo sólido atrás de palavras-chave dentro do corpo de texto"
      color: "[Cor primária da marca] (sobre fundo claro) ou Branco (sobre fundo escuro)"
      text_color: "[Branco se box escura, cor primária se box branca]"
      usage: "[Quando usar — ex.: destacar nome do produto, specs técnicos, frases de prova]"
      style: "Padding pequeno (4-8px), sem border-radius exagerado"

    hand_drawn_loop:
      description: "Oval ou loop desenhado à mão em traço fino, circunda o sujeito ou produto"
      color: "[Cor primária da marca]"
      style: "Brush stroke thin, slightly imperfect — NOT geometric — organic hand annotation feel"
      usage: "[Quando usar — ex.: Cover slides sobre pessoa, slides de produto]"

    white_bracket_frame:
      description: "Forma geométrica angular em branco — tipo colchete estilizado circulando o headline"
      color: "Branco puro"
      usage: "[Quando usar — ex.: Cover escuro — cria moldura de destaque ao redor do título]"
      style: "Open bracket shape — não é retângulo fechado, apenas arestas decorativas"

    floating_card:
      description: "Retângulo branco arredondado flutuando sobre a foto, com soft glow/sombra suave"
      radius: "16-24px"
      shadow: "Soft ambient shadow, não hard drop shadow"
      usage: "[Quando usar — ex.: Container de informação técnica em slides full-bleed]"

    icon_circle:
      description: "Círculo sólido preenchido com ícone de linha branco dentro"
      fill: "[Cor primária da marca]"
      icon: "Branco, estilo outline/line icon"
      usage: "[Quando usar — ex.: Infográficos de comparação SEM vs COM]"
      icon_subjects: "[Ícones relevantes ao produto/serviço — ex.: janela, gota, folha, ferramenta]"

    accent_blob:
      description: "Forma orgânica grande em cor primária aparecendo parcialmente por um dos cantos"
      usage: "[Quando usar — ex.: Canto dos slides de solução, transição para CTA]"
      style: "Quarto de círculo ou forma orgânica — só a borda aparece, resto cortado pela margem"

    pill_cta:
      description: "Botão de contorno pill/cápsula com texto pequeno"
      style: "Outline (border only, sem preenchimento) — Branco sobre fundos escuros, cor primária sobre fundos claros"
      radius: "9999px (pill completo)"
      usage: "[Quando usar — ex.: CTA do cover, CTA final]"

    spec_bar:
      description: "Barra horizontal na base do slide com especificações técnicas"
      style: "Fundo escuro, texto branco, labels pequenos"
      usage: "[Quando usar — ex.: Slides de produto específico]"
      brand_specs: "[Specs reais do produto — ex.: Spec1: valor | Spec2: valor | Linha: nome]"

  # ---------------------------------------------------------------------------
  # TEMPLATES DE LAYOUT — os 7 modelos de composição
  # ---------------------------------------------------------------------------
  layout_templates:

    T1_cover_atmosferico:
      name: "Cover Atmosférico"
      background: "Full-bleed dark photo"
      elements:
        - "White bracket frame centered (middle third)"
        - "Mixed-weight white headline: small sans label + large display + bold statement"
        - "Pill CTA at bottom (question form)"
      palette: "Dark image + pure white elements + optional accent loop"
      prompt_style: "Cinematic, moody, wide angle environmental photo with people, f/2.8 style, dark and atmospheric"

    T2_problema_highlight:
      name: "Problema com Highlight"
      background: "Off-white textured"
      elements:
        - "Dark charcoal headline, large scale, left-aligned or centered"
        - "Body text in gray, regular weight"
        - "Inline text highlight boxes (solid accent color behind key phrases)"
      palette: "Off-white + charcoal + cor primária highlight"
      no_photo: true

    T3_regra_simples:
      name: "Regra Simples"
      background: "Off-white textured"
      elements:
        - "Title 'Regra simples' — gray, medium weight, top"
        - "2 rows: [icon circle] + [highlight label] + [gray body]"
        - "Very high whitespace, no photos"
      palette: "Off-white + gray text + círculos cor primária + highlight boxes"
      no_photo: true

    T4_split_dinamico:
      name: "Split Dinâmico"
      background: "Left dark photo (60%) + right solid cor primária panel (40%), curved arc boundary"
      elements:
        - "Text on color panel only, white"
        - "Bold headline + regular body"
      palette: "Dark photo + cor primária + white text"

    T5_photo_floating_card:
      name: "Full Photo com Floating Card"
      background: "Full-bleed lifestyle/architectural photo"
      elements:
        - "Floating white rounded card with text"
        - "Accent lines flanking the card"
        - "Accent highlight within card text"
      palette: "Atmospheric photo + white card + cor primária highlight"

    T6_solucao_produto:
      name: "Solução Produto"
      background: "Off-white textured"
      elements:
        - "Left: headline with accent-color box behind product name"
        - "Right: rounded-arch photo container (product/installation photo)"
        - "Bottom: product detail/close-up"
        - "Thin hand-drawn loop around the main composition"
      palette: "Off-white + cor primária highlights + real product photos"

    T7_cta_acento:
      name: "CTA Acento"
      background: "Solid cor primária (full slide)"
      elements:
        - "Logo branco, centered"
        - "Short punchy headline in white"
        - "Pill CTA button outline in white"
        - "Previous slide photo peeking from one edge (continuity)"
        - "Optional: subtle texture on colored background"
      palette: "Cor primária + white elements"

  # ---------------------------------------------------------------------------
  # HIERARQUIA TIPOGRÁFICA NAS IMAGENS
  # ---------------------------------------------------------------------------
  image_typography:
    cover_label: "[Fonte body] 400, small (14-16px equiv), uppercase or sentence case"
    cover_headline: "[Fonte display] 700, very large (60-80px equiv), white on dark"
    slide_headline: "[Fonte display] 700, large (40-56px equiv), dark charcoal on light bg"
    body_text: "[Fonte body] 400, medium (20-24px equiv)"
    highlight_text: "Same font/weight as surrounding — only background changes"
    cta_text: "[Fonte body] 700, small (14-16px equiv)"

  # ---------------------------------------------------------------------------
  # ADAPTAÇÃO — o que muda da referência para esta marca
  # ---------------------------------------------------------------------------
  brand_adaptation:
    accent_color: "[Cor da referência] → [Cor primária desta marca]"
    cta_slide: "[Cor do fundo CTA da referência] → [Cor primária desta marca]"
    split_panel: "[Cor do painel da referência] → [Cor primária desta marca]"
    highlight_box: "[Box da referência] → [Box cor primária (texto branco dentro)]"
    icon_circles: "[Círculos da referência] → [Círculos cor primária desta marca]"
    product_photos: "[Produto da referência] → [Produto desta marca]"
    lifestyle_context: "[Contexto da referência] → [Contexto desta marca]"
    spec_bar_values: "[Specs da referência] → [Specs do produto desta marca]"
    infographic_contrast: "[Comparação da referência] → [Comparação desta marca]"
