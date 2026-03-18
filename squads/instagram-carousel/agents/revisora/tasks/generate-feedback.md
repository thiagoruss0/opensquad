---
task: "Generate Review Feedback"
order: 2
input:
  - scoring-table.md
output: review-feedback.md
---

## Process

1. **Apply decision rules** to the scoring table:
   - **APROVADO**: Overall average >= 7.0 AND no individual criterion below 4.
   - **REPROVADO**: Overall average < 7.0 OR any individual criterion below 4.
   - **APROVADO COM RESSALVAS**: Overall >= 7.0, no criterion below 4, but at least one criterion between 4-6 indicating minor issues.

2. **Write strengths** (minimum 1, even in REPROVADO reviews): Identify strongest aspects with specific references to slides, phrases, or design choices. Explain WHY it works.

3. **Write required changes** (for REPROVADO or APROVADO COM RESSALVAS): For each criterion scored below 7, specify exact location (slide number, paragraph), describe the problem, and provide a concrete fix. One change per item.

4. **Write non-blocking suggestions** (for all verdicts): Optional improvements clearly labeled as non-blocking. Still specific and actionable.

5. **Compile final verdict** with summary rationale, scoring table reference, strengths, required changes, and suggestions. Rationale must explain why the verdict was chosen based on scores.

## Output Format

```markdown
# Revisao — [Carousel Title]
## Veredicto: [APROVADO | REPROVADO | APROVADO COM RESSALVAS]
**Resumo:** [One-sentence rationale]
## Pontos Fortes
- **[Area]:** [Specific description]
## Alteracoes Obrigatorias
- **[Slide/Section]:** [Problem] -> [Fix]
## Sugestoes (Nao Bloqueantes)
- **[Area]:** [Suggestion]
## Proximos Passos
[What happens next based on verdict]
```

## Output Example

```markdown
# Revisao — 5 Sinais de Alerta para sua Visao

## Veredicto: APROVADO

**Resumo:** Carrossel atinge media geral de 8.4/10 com nenhum criterio abaixo de 7, demonstrando qualidade consistente em conteudo medico, conformidade e design.

## Pontos Fortes

- **Conformidade CFM:** Linguagem inteiramente educativa sem promessas de resultado. Tom de conscientizacao exemplar.
- **Design Visual:** Paleta navy/coral com contraste excelente e tipografia hierarquizada. Legivel em tela pequena.

## Alteracoes Obrigatorias

Nenhuma. Todos os criterios atingiram nota 7 ou superior.

## Sugestoes (Nao Bloqueantes)

- **Slide 7 (CTA):** Adicionar pergunta interativa para estimular comentarios e aumentar engajamento.
- **Legenda:** Incluir CRM/AM do Dr. Thiago Russo ao final da legenda para reforcar autoridade medica.

## Proximos Passos

Carrossel aprovado para publicacao. Encaminhar para o agente publicador com sugestoes consideradas.
```

## Quality Criteria

1. **Verdict-score alignment**: Verdict strictly follows decision rules. No subjective overrides.
2. **Strengths always present**: Every review, including rejections, must have at least 1 specific strength.
3. **Actionable required changes**: Each change specifies location, problem, and concrete fix. No vague feedback.
4. **Clear next steps**: Review ends with explicit guidance on what happens next.

## Veto Conditions

1. Verdict contradicts scores (e.g., APROVADO with a criterion below 4, or REPROVADO when all >= 7 and average >= 7).
2. REPROVADO verdict issued without specific required changes with actionable fixes.
3. Review contains zero strengths — every carousel has at least one positive aspect to acknowledge.
