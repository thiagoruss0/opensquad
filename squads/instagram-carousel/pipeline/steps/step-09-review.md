---
execution: subagent
agent: squads/instagram-carousel/agents/revisora
inputFile: squads/instagram-carousel/output/carousel-draft.md
outputFile: squads/instagram-carousel/output/review-result.md
model_tier: powerful
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/carousel-draft.md` — Full carousel content
- `squads/instagram-carousel/output/slides/rendered/manifest.json` — Rendered slide images
- `squads/instagram-carousel/pipeline/data/quality-criteria.md` — Scoring criteria definitions
- `squads/instagram-carousel/pipeline/data/anti-patterns.md` — Known mistakes to avoid
- `_opensquad/_memory/company.md` — CEDOA brand standards
- `squads/instagram-carousel/output/research-brief.md` — Original sources for fact-checking

## Instructions

### Process

1. **Score each quality criterion** from `quality-criteria.md` on a 1-10 scale:
   - For each criterion, provide a numeric score AND a written justification (2-3 sentences)
   - Be specific — reference actual slide content, word choices, or data points
   - Do not inflate scores; a 7 is "good, meets expectations"

2. **Check medical accuracy** against `research-brief.md`:
   - Every medical claim in the carousel must trace back to a source in the research brief
   - Flag any claim that is exaggerated, oversimplified beyond accuracy, or unsourced
   - Verify statistics and numbers match the original sources

3. **Check CFM compliance** against Conselho Federal de Medicina rules:
   - No guarantees of results (e.g., "vai curar", "resultado garantido")
   - No superlatives (e.g., "o melhor", "o unico", "revolucionario")
   - No before/after with promises
   - Educational framing, not promotional
   - Proper medical disclaimer or CRM identification

4. **Check visual quality** (if rendered images are accessible via manifest.json):
   - Text readability at mobile size
   - Brand consistency across slides
   - Contrast and accessibility
   - Professional appearance appropriate for medical content

5. **Compile the final verdict:**
   - **APPROVE** if: overall average score >= 7.0 AND no individual criterion scores below 4
   - **REJECT** if: overall average < 7.0 OR any criterion scores below 4
   - If REJECT: list required changes with specific instructions and clear path to approval
   - If APPROVE: list optional suggestions for improvement (non-blocking)

## Output Format

```markdown
# Review Result

**Verdict:** [APPROVE / REJECT]
**Overall Score:** [X.X / 10]
**Date:** [date]
**Reviewer:** Revisora (QA Agent)

## SCORING TABLE

| Criterion | Score | Justification |
|-----------|-------|---------------|
| [criterion 1] | X/10 | [justification] |
| [criterion 2] | X/10 | [justification] |
| ... | ... | ... |

**Average:** X.X/10

## DETAILED FEEDBACK

### Medical Accuracy
[Assessment of factual claims, source traceability, accuracy of statistics]

### CFM Compliance
[Assessment against CFM rules, any violations found]

### Content Quality
[Assessment of writing, flow, engagement potential, tone consistency]

### Visual Quality
[Assessment of design, readability, brand consistency]

## REQUIRED CHANGES (if REJECT)

1. [Specific change with instructions]
2. [Specific change with instructions]
...

**Path to approval:** [What needs to happen for this to pass]

## SUGGESTIONS (non-blocking)

1. [Optional improvement]
2. [Optional improvement]
...
```

## Output Example

```markdown
# Review Result

**Verdict:** APPROVE
**Overall Score:** 8.2 / 10
**Date:** 2026-03-18
**Reviewer:** Revisora (QA Agent)

## SCORING TABLE

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Hook Impact | 9/10 | "5 fatos sobre glaucoma que surpreendem" — forte uso de curiosidade e numero especifico. Gera vontade de deslizar. Dentro do limite de 8 palavras. |
| Medical Accuracy | 8/10 | Todos os dados rastreados ate fontes do research brief. Estatistica de "50% nao diagnosticados" confirmada pela OMS e CBO. Dado de "4-9x risco familiar" alinhado com o estudo EPIC-Brazil. |
| CFM Compliance | 9/10 | Sem garantias de resultado. Linguagem educativa consistente. "Pode preservar" em vez de "vai curar". CRM identificado na caption. Nenhuma violacao encontrada. |
| Slide Flow | 8/10 | Progressao logica de fatos surpreendentes, cada slide adicionando nova informacao. Transicao para CTA e natural. Slide 4 (jovens) poderia ter transicao mais forte para slide 5 (genetica). |
| Tone Consistency | 8/10 | Tom "Educador Acessivel" bem mantido. Linguagem acolhedora sem ser condescendente. Caption complementa os slides sem repetir. Slide 6 sobre colirios esta levemente mais tecnico que os demais. |
| CTA Effectiveness | 7/10 | "Agende sua avaliacao" e claro e acionavel. Poderia ser mais especifico (mencionar link na bio, WhatsApp). "Salve este post" e bom para algoritmo. |
| Caption Quality | 8/10 | Hook nos primeiros 125 caracteres funciona bem. Corpo adiciona contexto sem repetir slides. Dentro do limite de 2200 caracteres. Boa estrutura com bullet points. |
| Hashtag Strategy | 8/10 | Mix equilibrado: #glaucoma (amplo), #saudeocular (medio), #oftalmologia (nicho profissional), #prevencao (amplo saude), #cedoamanaus (marca local). |
| Visual Design | 8/10 | Paleta CEDOA aplicada consistentemente. Tipografia legivel. Bom uso de espaco branco. Contraste acima de 4.5:1 em todos os slides. CTA slide se destaca visualmente. |
| Engagement Potential | 9/10 | Formato lista e altamente salvavel. "Surpreendem" gera compartilhamento. Dados contra-intuitivos (pressao normal, jovens) geram comentarios. Potencial de salvar e compartilhar e alto. |

**Average:** 8.2/10

## DETAILED FEEDBACK

### Medical Accuracy
Todos os 7 dados medicos apresentados nos slides foram verificados contra o research brief. A estatistica de "30% de glaucoma de pressao normal" e do estudo EPIC-Brazil 2025, confirmada pelas diretrizes AAO 2026. O dado de "15 minutos" para o exame e uma estimativa razoavel para exame oftalmologico completo com OCT. Nenhuma afirmacao exagerada ou imprecisa encontrada.

### CFM Compliance
Nenhuma violacao do CFM identificada. O carrossel mantem framing educativo em todos os slides. Usos de "pode preservar", "pode mudar tudo" (possibilidade, nao garantia) estao adequados. O CRM esta presente na caption. Recomendacao: incluir "Consulte seu oftalmologista" em pelo menos um slide alem do CTA.

### Content Quality
Redacao clara e acessivel. Cada slide tem entre 42-68 palavras, dentro da faixa alvo. Transicoes entre slides sao logicas. O tom "Educador Acessivel" e mantido com consistencia. A caption complementa os slides adicionando contexto das fontes sem repetir o conteudo dos slides.

### Visual Quality
Design limpo e profissional. Paleta de cores CEDOA aplicada em todos os 9 slides. Hierarquia tipografica clara. Texto legivel em preview mobile. Slide CTA tem tratamento visual distinto (cor de destaque). Nenhum texto cortado ou overflow detectado.

## SUGGESTIONS (non-blocking)

1. Slide 6 (colirios): Simplificar "reduz a pressao intraocular e desacelera a progressao" para linguagem mais acessivel, ex: "ajuda a controlar a pressao dentro do olho"
2. CTA: Adicionar "Link na bio" ou "Mande um direct" para facilitar a acao
3. Caption: Considerar adicionar emoji estrategico (olho, seta) para quebra visual no feed
4. Hashtag: Considerar trocar #prevencao por #checkupocular — mais especifico e menos saturado
```

## Veto Conditions

- **REJECT the review** if it does not score every criterion from quality-criteria.md
- **REJECT the review** if a REJECT verdict lacks specific, actionable required changes
- **REJECT the review** if an APPROVE verdict was given without thorough content analysis
- **REJECT the review** if medical accuracy check does not reference specific claims and sources
- **REJECT the review** if CFM compliance check is superficial (must address each rule)

## Quality Criteria

- Every score has a specific, evidence-based justification
- Medical claims are individually verified against research brief sources
- CFM compliance check is thorough and references specific rules
- Feedback is constructive and actionable (not vague praise or criticism)
- The verdict follows the scoring rules strictly (no subjective overrides)
- Suggestions are genuinely useful improvements, not nitpicks
- The review demonstrates that the content was read thoroughly, not skimmed
