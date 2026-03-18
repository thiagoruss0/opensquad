---
task: "Generate Review Feedback"
order: 2
input: |
  - scoring-table: Scored criteria from score-content task
  - carousel-draft.md: Content being reviewed
  - quality-criteria.md: Reference criteria
output: |
  - verdict: APPROVE / REJECT / CONDITIONAL APPROVE
  - detailed-feedback: Structured review with strengths, required changes, suggestions
---

# Generate Review Feedback

Transform the scoring table into a structured review verdict with actionable feedback. Apply decision rules strictly. Provide specific, useful feedback that helps the content creator improve.

## Process

1. **Apply decision rules** to the scoring table:
   - **APPROVE**: Overall average >= 7.0 AND no individual criterion below 4/10
   - **REJECT**: Overall average < 7.0 OR any individual criterion below 4/10
   - **CONDITIONAL APPROVE**: Overall >= 7.0 with non-critical criteria between 4-6/10
   - If any critical criterion (Medical Accuracy or CFM Compliance) is below 4: automatic REJECT regardless of average.

2. **Write "Strength:" items** (minimum 1, even in REJECT reviews):
   - Identify the strongest aspects of the content
   - Be specific: reference exact slides, phrases, or design choices
   - Explain WHY it works, not just that it's good

3. **Write "Required change:" items** (for REJECT or CONDITIONAL APPROVE):
   - Identify the specific location (slide number, paragraph, element)
   - Describe the exact problem
   - Provide a concrete fix or rewrite suggestion
   - One change per item, not bundled

4. **Write "Suggestion (non-blocking):" items** (for all verdicts):
   - Optional improvements that would enhance quality
   - Clearly labeled as non-blocking (won't affect verdict)
   - Still specific and actionable

5. **Compile the final review** in the structured format with verdict, scoring table, detailed feedback sections (Medical Accuracy, CFM Compliance, Content Quality, Visual Quality), required changes (if any), and suggestions.

## Output Format

```yaml
verdict: "APPROVE | REJECT | CONDITIONAL APPROVE"
overall_score: X.X
revision_number: N
max_revisions: 3

strengths:
  - "Strength: [specific positive observation with reference to content]"

required_changes:
  - location: "Slide N / Caption paragraph X / Hashtag"
    problem: "What is wrong"
    fix: "How to fix it"

suggestions:
  - "Suggestion (non-blocking): [optional improvement]"

summary: "1-2 sentence verdict rationale"
```

## Output Example

```yaml
verdict: "APPROVE"
overall_score: 8.4
revision_number: 1
max_revisions: 3

strengths:
  - "Strength: The hook 'Seus olhos estão tentando te avisar alguma coisa?' creates immediate personal relevance. The question format forces the reader to self-reflect, which is one of the highest-engagement hook patterns for medical content."
  - "Strength: Slide 4 about moscas volantes correctly distinguishes between benign floaters and emergency retinal detachment. This responsible nuance builds credibility and demonstrates medical expertise without fear-mongering."

required_changes: []

suggestions:
  - "Suggestion (non-blocking): The CTA 'Salve esse carrossel' on slide 7 could be strengthened to 'Manda esse carrossel para alguém que vive reclamando de dor de cabeça'. Share CTAs generate higher algorithmic distribution than save CTAs."
  - "Suggestion (non-blocking): Consider adding 'Dr. Thiago Russo, CRM/AM XXXXX' at the end of the caption to reinforce physician authority beyond just the profile bio."

summary: "Carousel meets all quality criteria with strong medical accuracy (9/10) and full CFM compliance (10/10). Two non-blocking suggestions provided for engagement optimization."
```

## Quality Criteria

- [ ] Verdict strictly follows the decision rules (no subjective overrides)
- [ ] At least 1 "Strength:" item present, even in REJECT reviews
- [ ] Every required change includes specific location, problem, and fix
- [ ] Suggestions are clearly labeled as non-blocking
- [ ] Summary is concise (1-2 sentences) and matches the verdict
- [ ] Revision number is tracked (max 3 before escalation)

## Veto Conditions

Reject and redo if ANY are true:
1. Verdict contradicts the scores (e.g., APPROVE with a 3/10 criterion)
2. REJECT verdict has zero required changes (must provide path to approval)
3. Review contains no "Strength:" items (even bad content has something positive)
