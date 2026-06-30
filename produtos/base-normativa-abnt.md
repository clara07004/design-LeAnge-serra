# Base Normativa ABNT — Steel Frame e Drywall (setor de construção a seco)

> Conhecimento técnico lido **direto das normas ABNT** (10 documentos), aplicável a qualquer empresa do setor de **construção a seco / Steel Frame / Drywall**. É a base normativa obrigatória para afirmações de conteúdo sobre estrutura, fechamento, perfis e galvanização.
> **Nunca inventar valor, ensaio ou redação de norma.** Disclaimer obrigatório ao comunicar cálculo: "Cálculos estruturais devem ser realizados por profissional habilitado."
> **Template:** este arquivo vem preenchido como conhecimento do setor. Empresa que não atue em Steel Frame/Drywall pode remover; empresa do setor herda como está.

---

## ⭐ Conceito central — quem é responsável pela integridade estrutural

**No Steel Frame brasileiro, a integridade e a estabilidade estrutural são responsabilidade EXCLUSIVA da estrutura de aço (perfis formados a frio). O fechamento/revestimento — placa de gesso (drywall), OSB, placa cimentícia — é VEDAÇÃO NÃO ESTRUTURAL: fecha, protege e dá acabamento, sem colaborar na estruturação.**

Isso está escrito de forma literal nas normas:

- **NBR 16970-2 (Projeto estrutural), §4.1 — Princípios de projeto:** os perfis de aço formam "painéis que têm comportamento estrutural", submetidos "às ações gravitacionais, à ação do vento e à ação de sismos". E: *"Elementos não estruturais não podem comprometer a continuidade da estrutura, para poder assegurar a estabilidade e a vida útil do sistema."*
- **NBR 16970-1 (Desempenho), §3.14:** os componentes de fechamento/acabamento *"não colaboram na estruturação das paredes, tendo função estética e papel relevante na durabilidade."*
- **NBR 16970-1** separa formalmente **§5.2 "Componentes ou elementos estruturais"** (perfis, fitas metálicas, chapas gusset) de **§5.3 "Componentes de fechamento e revestimento da vedação vertical"** (fibrocimento, OSB, gesso). As exigências das chapas de fechamento são de resistência a impacto/água/durabilidade — **nunca capacidade portante**.
- **NBR 15253 (perfis estruturais), §3.1 — painel reticulado:** "sistema estrutural plano constituído por perfis ligados entre si, **podendo ou não estar associado a placas de vedação**" — a placa de vedação é associação **opcional**.
- **NBR 14762 (dimensionamento):** dimensiona **a estrutura de aço** pelos estados-limite (Sd ≤ Rd) para resistir a todas as ações (peso próprio, vento, sobrecarga, sismo). O fechamento entra **apenas como carga**, nunca como elemento resistente.

### Diferença para o modelo americano (importante)

Nos EUA, o OSB é frequentemente computado como **diafragma estrutural** (shear wall). **A norma brasileira NÃO faz isso:**

- O OSB aparece na NBR 16970-1 **somente como componente de vedação** (§5.3.4) — **sem cláusula que o compute como diafragma resistente**.
- A **estabilização lateral (contraventamento)** é feita por **elementos de aço**: fitas metálicas em X (strap bracing) e treliças/perfis — dimensionados pela NBR 14762 (NBR 16970-2, §7). Não pela placa de fechamento.

**Consequência prática:** como nenhum fechamento é estrutural no Brasil, a placa de drywall vai **diretamente fixada na estrutura de aço**. Por isso, na comunicação, trocar "OSB" por "Placa Performa" (regra em [../_contexto/preferencias.md](../_contexto/preferencias.md)) **não perde nenhuma função estrutural** — o fechamento nunca foi estrutural aqui.

**O que o conteúdo PODE afirmar:** "quem sustenta é o aço normatizado; a placa veda." **O que o conteúdo NÃO PODE afirmar:** que o fechamento (OSB, gesso ou cimentícia) "dá rigidez", "contribui para a estrutura" ou "dissipa a energia do vento" — isso é a lógica americana e contraria a NBR.

> ⚠️ Nota de fidelidade: a NBR 16970 **ainda lista o OSB** como opção válida de vedação (não estrutural). A norma não proíbe OSB. Não usar/mencionar OSB e aplicar a placa de gesso direto na estrutura é **prática comercial/construtiva** — não exigência normativa.

---

## As 10 normas (o que cada uma regula)

| Norma | Título resumido | Papel |
|---|---|---|
| **NBR 16970-1:2022** | LSF — Desempenho | Componentes e desempenho do sistema (estrutural, vedação, térmico, acústico, fogo). Até 2 pavimentos. |
| **NBR 16970-2:2022** | LSF — Projeto estrutural | Projeto/dimensionamento da estrutura de aço pelos estados-limite (base: NBR 14762). |
| **NBR 16970-3:2022** | LSF — Interfaces | Detalhes construtivos de interfaces (parede×piso, esquadria, instalações). |
| **NBR 15253:2014** | Perfis para painéis estruturais (LSF) | Perfil **estrutural** do Steel Frame: requisitos, dimensões, galvanização, fy. |
| **NBR 6355:2012** | Perfis formados a frio — Padronização | Padroniza geometria/designação/tolerâncias dos perfis estruturais. |
| **NBR 14762:2010** | Dimensionamento de perfis formados a frio | Como dimensionar a estrutura de aço (estados-limite, flambagem). |
| **NBR 15217:2025** | Perfilados para drywall | Perfil de drywall (**não estrutural**): requisitos e ensaios. |
| **NBR 7008-1:2021** | Chapas/bobinas revestidas de zinco — Requisitos | Classes de revestimento (Z e ZF) e gramaturas. |
| **NBR 7008-2:2021** | Idem — Aços comercial/estampagem | Graus ZC, ZE/ZEE (conformáveis). |
| **NBR 7008-3:2021** | Idem — Aços estruturais | Graus **ZAR** (resistência) — referenciado pelos perfis. |

> Correlatas: **NBR 15575** (desempenho de edificações), **NBR 6123** (forças devidas ao vento), **NBR 8800** (estruturas de aço/concreto).

---

## Dados técnicos por norma (lastro para conteúdo)

### NBR 15253 — perfil ESTRUTURAL do Steel Frame
- **Aço com qualificação estrutural**, escoamento mínimo **fy ≥ 230 MPa** (§5.2).
- **Galvanização:** **Z275** (275 g/m²) ou **AZ150** (150 g/m², alumínio-zinco) — massa mínima total das duas faces (§5.1).
- **Espessura mínima** da chapa (sem revestimento): **0,80 mm** (§6.2.1).
- **Componentes:** montante (vertical), guia (horizontal), viga/verga (aberturas), terça, ripa, bloqueador, enrijecedor.
- **Dimensões (Tabela 4, mm):** Montante M90 (alma 90 / mesa 39 / enrij. 12), M140, M200; Guia U90 (92×39), U140, U200.

### NBR 6355 — padronização dos perfis estruturais
- **Notação:** `alma × mesa × (enrijecedor) × espessura` (mm).
- **Designações:** **L** cantoneira; **U** (U simples); **Ue** (U enrijecido); **Z90 / Z45**; **Cr** (cartola).
- **Série de espessuras:** 0,80 / 0,95 / 1,10 / 1,25 / 1,50 / 1,80 / 2,00 / 2,25 / 2,65 / 3,00 / 3,35 / 3,75 / 4,25 / 4,75 mm.

### NBR 15217 — perfil de DRYWALL (não estrutural)
- **Uso:** paredes, forros e revestimentos **internos não estruturais**.
- **Aço:** **ZAR-230** (NBR 7008-3); escoamento **≥ 230 MPa**.
- **Galvanização:** **Z275** nas guias/cantoneiras; **Z120** nos montantes/canaletas.
- **Espessura mínima:** **0,50 mm** (guias/cantoneiras), **0,48 mm** (montantes/canaletas).
- **Larguras (mm):** Guia/Montante **48 / 70 / 90**.

### NBR 7008 — chapas/bobinas galvanizadas
- **Z = zinco puro** (proteção anticorrosiva por barreira); **ZF = liga zinco-ferro (galvannealed)** (melhor pintura/solda).
- **Gramaturas (g/m², total das 2 faces):** Z85, Z100, Z120, Z140, Z180, Z225, **Z275**, **Z350**, Z450, Z600.
- **Aços estruturais (Parte 3 — ZAR):** o número = escoamento mínimo em MPa. **ZAR-230** (LE 230/LR 310/along. 22%), 250, 280, 320, 345, 400, 550.

### NBR 14762 — dimensionamento da estrutura de aço
- **Método dos estados-limite:** segurança **Sd ≤ Rd**. Verifica **flambagem global, local e distorcional**.
- **Ações** (§6): permanentes, variáveis (sobrecarga, vento), excepcionais — todas resistidas **pela estrutura de aço**.

---

## Como usar em conteúdo

- **Afirmações de estrutura** → sempre atribuir ao **aço normatizado**, nunca ao fechamento. Citar NBR 15253 / 6355 / 14762 / 16970.
- **Vento/sismo** → resistência é da **estrutura + contraventamento metálico** (NBR 14762/16970/6123), não do fechamento.
- **OSB** → ver regra de substituição (OSB → Placa Performa) em [../_contexto/preferencias.md](../_contexto/preferencias.md); nunca atribuir função estrutural a placa de fechamento.
- **Disclaimers** → cálculo estrutural por profissional habilitado; imagens ilustrativas.

> Fonte: leitura direta das normas ABNT NBR 16970-1/2/3:2022, 15253:2014, 6355:2012, 14762:2010, 15217:2025 e 7008-1/2/3:2021.
