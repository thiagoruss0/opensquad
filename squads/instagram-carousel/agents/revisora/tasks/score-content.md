---
task: "Score Content Quality"
order: 1
input:
  - carousel-draft.md
  - manifest.json
  - quality-criteria.md
output: scoring-table.md
---

## Process

1. **Load quality criteria** — Read `quality-criteria.md` in full before examining any content. Understand the definition, weight, and passing threshold for each of the 8 criteria. Internalize what a score of 1, 5, and 10 means for each criterion.

2. **Read carousel content thoroughly** — Examine every slide in `carousel-draft.md`: cover text, body content, data points, quotes, CTA text, full caption, and hashtags. Cross-reference with `manifest.json` to confirm slide count and roles match the draft.

3. **Score each criterion (1-10)** — Evaluate the 8 criteria independently:
   - **Precisao Medica** — Are all medical claims accurate, evidence-based, and appropriate for public health education? No misleading statements.
   - **Conformidade CFM** — Does the content comply with CFM (Conselho Federal de Medicina) advertising rules? No before/after, no guarantees, no sensationalism.
   - **Eficacia do Gancho** — Does the cover slide hook stop the scroll? Is it curiosity-driven, specific, and relevant to the target audience?
   - **Qualidade do Conteudo** — Are the content slides clear, well-structured, educational, and appropriately detailed for a lay audience?
   - **CTA e Engajamento** — Is the call-to-action clear, compelling, and compliant? Does it encourage saves, shares, or comments?
   - **Qualidade da Legenda** — Is the caption well-written in pt-BR, with proper formatting, hashtags (15-25), and a conversational yet professional tone?
   - **Design Visual** — Do the rendered slides look professional, readable, and visually appealing at mobile scale?
   - **Alinhamento de Marca** — Does the carousel reflect CEDOA's brand identity, Dr. Thiago Russo's voice, and the ophthalmology positioning?

4. **Write justifications** — For each score, write a specific justification referencing concrete elements in the content (slide numbers, exact text, visual details). Avoid generic praise or criticism.

5. **Calculate overall average** — Sum all 8 scores and divide by 8. Round to one decimal place. This is the final overall score.

## Output Format

```markdown
# Avaliacao de Qualidade — [Carousel Title]

| # | Criterio | Nota | Justificativa |
|---|----------|------|---------------|
| 1 | Precisao Medica | X/10 | [specific justification] |
| 2 | Conformidade CFM | X/10 | [specific justification] |
| 3 | Eficacia do Gancho | X/10 | [specific justification] |
| 4 | Qualidade do Conteudo | X/10 | [specific justification] |
| 5 | CTA e Engajamento | X/10 | [specific justification] |
| 6 | Qualidade da Legenda | X/10 | [specific justification] |
| 7 | Design Visual | X/10 | [specific justification] |
| 8 | Alinhamento de Marca | X/10 | [specific justification] |

**Media Geral: X.X/10**
```

## Output Example

```markdown
# Avaliacao de Qualidade — 5 Sinais de Alerta para sua Visao

| # | Criterio | Nota | Justificativa |
|---|----------|------|---------------|
| 1 | Precisao Medica | 9/10 | Todos os 5 sinais listados sao clinicamente reconhecidos (flashes, floaters, perda de campo, visao dupla, dor ocular). Referencia a consulta com especialista e precisa. Slide 4 poderia citar prevalencia com fonte. |
| 2 | Conformidade CFM | 10/10 | Nenhuma promessa de resultado, sem antes/depois, sem sensacionalismo. Linguagem educativa com tom de conscientizacao. CTA direciona para consulta, nao para venda. |
| 3 | Eficacia do Gancho | 8/10 | "5 Sinais de que voce precisa ir ao oftalmologista URGENTE" gera curiosidade e urgencia. Numero especifico e relevancia pessoal fortes. Palavra "URGENTE" pode ser excessiva para CFM. |
| 4 | Qualidade do Conteudo | 8/10 | Slides bem estruturados com um sinal por slide. Explicacoes claras para leigos. Slide 5 esta um pouco denso comparado aos outros — considerar dividir. |
| 5 | CTA e Engajamento | 7/10 | CTA "Salve este post e compartilhe com quem precisa" e direto. Poderia incluir pergunta no slide final para estimular comentarios. |
| 6 | Qualidade da Legenda | 8/10 | Legenda bem escrita em pt-BR, tom profissional-acessivel. 18 hashtags relevantes. Poderia incluir emoji de olho para quebrar texto visualmente. |
| 7 | Design Visual | 9/10 | Paleta coesa navy/coral, tipografia legivel, espacamento confortavel. Icones complementam sem poluir. Contraste excelente em todos os slides. |
| 8 | Alinhamento de Marca | 8/10 | Cores e tipografia consistentes com identidade CEDOA. Logo presente no cover e CTA. Tom do Dr. Russo bem representado. Poderia reforcar localizacao Manaus no CTA. |

**Media Geral: 8.4/10**
```

## Quality Criteria

1. **Complete coverage** — All 8 criteria must be scored. No criterion may be skipped or marked as "N/A".
2. **Specific justifications** — Each justification must reference concrete elements (slide numbers, exact phrases, visual details). Generic statements like "bom conteudo" are not acceptable.
3. **Mathematical accuracy** — The overall average must be the correct arithmetic mean of all 8 scores, rounded to one decimal place.
4. **Calibrated scoring** — Scores must reflect genuine quality differentiation. A perfect 10 requires zero issues; a score below 5 indicates serious problems requiring rework.

## Veto Conditions

1. Any criterion is scored without a written justification.
2. Any of the 8 criteria is omitted from the scoring table.
3. The overall average is mathematically incorrect (does not match the sum of scores divided by 8).
