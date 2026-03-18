---
execution: subagent
agent: squads/instagram-carousel/agents/pesquisador
inputFile: squads/instagram-carousel/output/research-focus.md
outputFile: squads/instagram-carousel/output/research-brief.md
model_tier: powerful
---

## Context Loading

Load the following files before starting:

- `squads/instagram-carousel/output/research-focus.md` — User's selected topic and time range
- `squads/instagram-carousel/pipeline/data/research-brief.md` — Domain research template for reference
- `_opensquad/_memory/company.md` — Company context (CEDOA, Dr. Thiago Russo)

## Instructions

### Process

1. **Parse user input**: Extract the research topic and time range from `research-focus.md`.
2. **Execute web search**: Use `web_search` to find 5-10 relevant sources about the topic. Search in both Portuguese and English for broader coverage. Prioritize:
   - Peer-reviewed studies (PubMed, SciELO, Cochrane)
   - Medical society guidelines (CBO, AAO, WHO)
   - Recent news articles from reputable health outlets
   - Brazilian ophthalmology sources when available
3. **Cross-reference claims**: Verify key claims appear in at least 2 independent sources. Flag any claim with a single source as "needs verification."
4. **Identify trending angles**: Look for what makes this topic timely or relevant — new studies, seasonal relevance, common misconceptions, patient concerns.
5. **Compile the research brief**: Organize all findings into the structured output format below.
6. **Assess gaps**: Note areas where information is scarce or conflicting, suggesting additional research if needed.

## Output Format

```markdown
# Research Brief: [Topic]

## Metadata
- **Tema**: [topic]
- **Período**: [time range]
- **Data da pesquisa**: [date]
- **Total de fontes**: [count]

## Key Findings
1. [Finding with source reference]
2. [Finding with source reference]
...

## Trending Angles
1. [Angle — why it's relevant now]
2. [Angle — why it's relevant now]
...

## Sources Table
| # | Title | Source | Type | Date | Relevance |
|---|-------|--------|------|------|-----------|
| 1 | ...   | ...    | ...  | ...  | ...       |

## Recommendations
- [Which angles are strongest for Instagram carousel format]
- [Which findings have the most patient relevance]
- [Suggested narrative direction]

## Gaps
- [Areas needing more research]
- [Conflicting information found]
```

## Output Example

```markdown
# Research Brief: Glaucoma Prevenção

## Metadata
- **Tema**: glaucoma prevenção e diagnóstico precoce
- **Período**: Sem restrição (evergreen)
- **Data da pesquisa**: 2026-03-18
- **Total de fontes**: 8

## Key Findings
1. Glaucoma é a principal causa de cegueira irreversível no mundo, afetando ~80 milhões de pessoas (WHO, 2023).
2. Até 50% dos pacientes com glaucoma não sabem que têm a doença — diagnóstico frequentemente ocorre em estágios avançados (CBO, 2024).
3. Exame de tonometria anual a partir dos 40 anos reduz risco de perda visual avançada em 60% (AAO Guidelines, 2024).
4. Histórico familiar aumenta o risco em 4-9x — triagem familiar é subutilizada no Brasil (SciELO, Araújo et al., 2023).
5. Novas terapias com colírios sem conservantes mostram melhor adesão ao tratamento (Cochrane Review, 2024).
6. Pressão intraocular não é o único fator — glaucoma de pressão normal representa 30% dos casos (JAMA Ophthalmology, 2023).

## Trending Angles
1. "Cegueira silenciosa" — o apelo emocional do diagnóstico tardio conecta com público leigo
2. Mitos sobre glaucoma — "só afeta idosos" é o mito mais comum nas redes sociais
3. Checklist de prevenção — conteúdo prático gera saves e compartilhamentos

## Sources Table
| # | Title | Source | Type | Date | Relevance |
|---|-------|--------|------|------|-----------|
| 1 | Global prevalence of glaucoma | WHO Report | Relatório | 2023 | Alta |
| 2 | Diretrizes de rastreamento | CBO | Guideline | 2024 | Alta |
| 3 | Primary Open-Angle Glaucoma Screening | AAO | Guideline | 2024 | Alta |
| 4 | Triagem familiar para glaucoma no Brasil | SciELO | Estudo | 2023 | Alta |
| 5 | Preservative-free eye drops adherence | Cochrane | Revisão | 2024 | Média |
| 6 | Normal-tension glaucoma prevalence | JAMA Ophthalmol | Estudo | 2023 | Média |
| 7 | Glaucoma awareness in Latin America | Rev Bras Oftalmol | Estudo | 2024 | Alta |
| 8 | AI-assisted glaucoma detection | Nature Medicine | Estudo | 2024 | Média |

## Recommendations
- Ângulo "cegueira silenciosa" é o mais forte para gerar engajamento emocional
- Dados brasileiros (CBO, SciELO) dão credibilidade local
- Formato listicle ou mito vs realidade funcionam bem para este tema

## Gaps
- Dados específicos de Manaus/Amazonas sobre prevalência de glaucoma são escassos
- Poucas fontes sobre custo de tratamento no SUS para contextualização
```

## Veto Conditions

- **REJEITAR** se houver achados sem fonte identificada
- **REJEITAR** se opiniões forem apresentadas como fatos científicos
- **REJEITAR** se houver menos de 5 fontes no total
- **REJEITAR** se nenhuma fonte for de órgão médico reconhecido (CBO, AAO, WHO, etc.)
- **REJEITAR** se o brief não incluir pelo menos 3 trending angles

## Quality Criteria

- Todas as afirmações possuem referência rastreável
- Fontes incluem pelo menos 2 guidelines de sociedades médicas
- Trending angles são relevantes para formato Instagram
- Brief é completo o suficiente para um redator criar conteúdo sem pesquisa adicional
- Recomendações são específicas e acionáveis, não genéricas
