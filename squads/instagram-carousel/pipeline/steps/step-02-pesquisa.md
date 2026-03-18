---
execution: subagent
agent: squads/instagram-carousel/agents/pesquisador
inputFile: squads/instagram-carousel/output/research-focus.md
outputFile: squads/instagram-carousel/output/research-brief.md
model_tier: powerful
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/research-focus.md` — User's chosen topic and time range
- `squads/instagram-carousel/pipeline/data/research-brief.md` — Domain research template for reference
- `_opensquad/_memory/company.md` — Company context (CEDOA, Dr. Thiago Russo)

## Instructions

### Process

1. **Parse the user's research focus** from `research-focus.md`. Extract the topic and the time range selection.
2. **Conduct web research** using `web_search` on the specified topic within the chosen time range.
   - Search in both Portuguese and English for broader coverage.
   - Use queries like: "[topic] ophthalmology research 2026", "[topic] oftalmologia estudo recente", "[topic] patient education".
3. **Find 5-10 relevant sources.** Prioritize:
   - Peer-reviewed studies and medical journals (AAO, CBO, Lancet Ophthalmology)
   - Reputable health news outlets
   - Guidelines from ophthalmology societies (CBO, AAO, WHO)
   - Patient-facing educational content from established clinics
4. **Cross-reference claims** — no single-source facts. Every key finding must appear in at least 2 sources.
5. **Identify trending angles** — what is new, surprising, or underreported about this topic?
6. **Note gaps** — what important aspects lack sufficient sourcing?
7. **Produce the structured research brief** following the output format below.

## Output Format

```markdown
# Research Brief: [Topic]

**Data da pesquisa:** [date]
**Periodo:** [time range selected]
**Total de fontes:** [N]

## KEY FINDINGS

1. [Finding with citation]
2. [Finding with citation]
...

## TRENDING ANGLES

1. [Angle + why it's trending]
2. [Angle + why it's trending]
3. [Angle + why it's trending]

## SOURCES

| # | Title | Source | Type | Date | Relevance |
|---|-------|--------|------|------|-----------|
| 1 | ...   | ...    | ...  | ...  | ...       |

## RECOMMENDATIONS

- Best angle for Instagram carousel: [recommendation]
- Audience resonance: [why this matters to patients]
- Content gap opportunity: [what competitors aren't covering]

## GAPS

- [Topic area with insufficient evidence]
- [Claims that could not be cross-referenced]
```

## Output Example

```markdown
# Research Brief: Glaucoma e Prevencao

**Data da pesquisa:** 2026-03-18
**Periodo:** Ultimo mes
**Total de fontes:** 8

## KEY FINDINGS

1. Glaucoma afeta 3.4% dos brasileiros acima de 40 anos, mas 50% dos casos nao sao diagnosticados (CBO 2025; WHO Global Eye Health Report 2026).
2. A pressao intraocular elevada e o principal fator de risco modificavel, mas glaucoma de pressao normal representa 30% dos casos no Brasil (Estudo EPIC-Brazil 2025; AAO Guidelines 2026).
3. Exame oftalmologico anual a partir dos 40 anos reduz o risco de perda visual irreversivel em 60% (Lancet Ophthalmology Meta-analysis 2025; CBO Diretrizes 2026).
4. Novos colirios com conservantes reduzidos mostram adesao 40% maior ao tratamento (JAMA Ophthalmology 2026; British Journal of Ophthalmology 2025).
5. Historico familiar aumenta o risco em 4-9x, mas apenas 15% dos brasileiros com historico fazem rastreamento regular (IBGE Saude 2025; CBO 2026).

## TRENDING ANGLES

1. "Glaucoma silencioso" — campanha da CBO 2026 reforca que a doenca nao doi e nao avisa, gerando engajamento em redes sociais.
2. Tecnologia OCT e diagnostico precoce — novos equipamentos detectam danos 5 anos antes dos exames tradicionais.
3. Miopia como fator de risco — estudos recentes ligam alta miopia a maior risco de glaucoma, relevante para publico jovem.

## SOURCES

| # | Title | Source | Type | Date | Relevance |
|---|-------|--------|------|------|-----------|
| 1 | Global Eye Health Report 2026 | WHO | Relatorio | 2026-01 | Alta |
| 2 | Diretrizes de Glaucoma 2026 | CBO | Diretriz | 2026-02 | Alta |
| 3 | Primary Open-Angle Glaucoma Guidelines | AAO | Diretriz | 2026-01 | Alta |
| 4 | Glaucoma prevalence in Brazil: EPIC study | Lancet Ophthalmology | Estudo | 2025-11 | Alta |
| 5 | Preservative-free drops and adherence | JAMA Ophthalmology | Estudo | 2026-01 | Media |
| 6 | Family history and screening gaps | CBO Congresso | Apresentacao | 2026-02 | Alta |
| 7 | OCT advances in glaucoma detection | British J Ophthalmology | Estudo | 2025-09 | Media |
| 8 | Pesquisa Nacional de Saude Ocular | IBGE | Pesquisa | 2025-12 | Media |

## RECOMMENDATIONS

- Best angle for Instagram carousel: "Glaucoma silencioso" — alto impacto emocional, dados fortes, campanha CBO ativa
- Audience resonance: Pacientes 40+ temem perder a visao; mensagem preventiva gera compartilhamentos
- Content gap opportunity: Poucos perfis medicos abordam glaucoma de pressao normal — oportunidade de diferenciacao

## GAPS

- Dados especificos sobre prevalencia na regiao Norte/Amazonia sao escassos
- Eficacia comparativa entre colirios genericos vs. marca nao tem consenso recente
```

## Veto Conditions

- **REJECT** if any finding is presented without at least one source citation
- **REJECT** if opinions or speculation are presented as established facts
- **REJECT** if fewer than 5 distinct sources are cited
- **REJECT** if sources are outdated (>3 years) without justification
- **REJECT** if the brief lacks the GAPS section (intellectual honesty is required)

## Quality Criteria

- All findings are cross-referenced across at least 2 sources
- Sources include a mix of types (studies, guidelines, reports)
- Trending angles are genuinely current and relevant to Instagram audience
- Recommendations are specific and actionable for carousel creation
- Brief is written in Portuguese where appropriate (topic terms, audience notes)
- Research covers both clinical accuracy and patient-facing communication angles
