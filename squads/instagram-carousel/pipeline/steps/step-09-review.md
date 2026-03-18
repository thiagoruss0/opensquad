---
execution: subagent
agent: squads/instagram-carousel/agents/revisora
inputFile: squads/instagram-carousel/output/carousel-draft.md
outputFile: squads/instagram-carousel/output/review-result.md
model_tier: powerful
---

# Step 09: Revisão de Qualidade

## Context Loading

Load these files before executing:
- `squads/instagram-carousel/output/carousel-draft.md` — Carousel content (slides + caption)
- `squads/instagram-carousel/output/slides/rendered/manifest.json` — Rendered images metadata
- `squads/instagram-carousel/pipeline/data/quality-criteria.md` — Scoring criteria
- `squads/instagram-carousel/pipeline/data/anti-patterns.md` — What to avoid
- `squads/instagram-carousel/output/research-brief.md` — Sources for fact-checking
- `_opensquad/_memory/company.md` — Brand guidelines

## Instructions

### Process

1. **Load quality criteria** from quality-criteria.md. Understand each criterion and its scoring rubric before reading the content.

2. **Read the carousel content thoroughly** — every slide, the full caption, hashtags. Note initial impressions but do not score until the full read is complete.

3. **Score each criterion** on a 1-10 scale with written justification:
   - Medical Accuracy (critical — hard reject below 4)
   - CFM Compliance (critical — hard reject below 4)
   - Hook Effectiveness
   - Slide Content Quality
   - CTA & Engagement Design
   - Caption Quality
   - Visual Design Quality (from manifest.json metadata)
   - Brand Alignment

4. **Fact-check medical claims** against research-brief.md sources. Flag any claim without a verifiable source.

5. **Check CFM compliance**: no result guarantees, no superlatives, no patient identification, educational framing present.

6. **Compile verdict**: Calculate overall average. Apply decision rules:
   - APPROVE: overall >= 7/10 AND no criterion below 4/10
   - REJECT: overall < 7/10 OR any criterion below 4/10
   - CONDITIONAL APPROVE: overall >= 7 with minor non-critical issues

7. **Write structured review** with verdict, scoring table, detailed feedback, required changes (if reject), and non-blocking suggestions.

## Output Format

```
==============================
 REVIEW VERDICT: [APPROVE/REJECT/CONDITIONAL APPROVE]
==============================

Content: "[Carousel title]"
Type: Instagram Carousel ([N] slides)
Review Date: YYYY-MM-DD
Revision: [N] of 3

------------------------------
 SCORING TABLE
------------------------------
| Criterion              | Score  | Summary                                |
|------------------------|--------|----------------------------------------|
| Medical Accuracy       | X/10   | [One-line summary]                     |
| CFM Compliance         | X/10   | [One-line summary]                     |
| Hook Effectiveness     | X/10   | [One-line summary]                     |
| Slide Content Quality  | X/10   | [One-line summary]                     |
| CTA & Engagement       | X/10   | [One-line summary]                     |
| Caption Quality        | X/10   | [One-line summary]                     |
| Visual Design          | X/10   | [One-line summary]                     |
| Brand Alignment        | X/10   | [One-line summary]                     |
------------------------------
 OVERALL: X.X/10
------------------------------

DETAILED FEEDBACK:

Strength: [Specific positive observation with reference]

Required change: [Specific issue, location, and fix — only if REJECT]

Suggestion (non-blocking): [Optional improvement]

VERDICT: [Final verdict with summary rationale]
```

## Output Example

```
==============================
 REVIEW VERDICT: APPROVE
==============================

Content: "5 sinais de que seus olhos estão pedindo ajuda"
Type: Instagram Carousel (7 slides)
Review Date: 2026-03-18
Revision: 1 of 3

------------------------------
 SCORING TABLE
------------------------------
| Criterion              | Score  | Summary                                         |
|------------------------|--------|-------------------------------------------------|
| Medical Accuracy       | 9/10   | All claims verified against SBO and AAO sources  |
| CFM Compliance         | 10/10  | No violations detected, educational framing used |
| Hook Effectiveness     | 8/10   | Strong curiosity hook, works within 125 chars    |
| Slide Content Quality  | 8/10   | Good two-layer hierarchy, 45-70 words per slide  |
| CTA & Engagement       | 7/10   | Save + share CTA present, could be more specific |
| Caption Quality        | 8/10   | SEO keywords present, good line breaks           |
| Visual Design          | 8/10   | Consistent system, meets all font minimums       |
| Brand Alignment        | 9/10   | CEDOA identity clear, empathetic tone maintained  |
------------------------------
 OVERALL: 8.4/10
------------------------------

DETAILED FEEDBACK:

Strength: The hook "5 sinais de que seus olhos estão pedindo ajuda" creates
immediate personal relevance. The personification of eyes "pedindo ajuda"
is an effective emotional trigger that drives curiosity to swipe.

Strength: Slide 4 about moscas volantes includes the critical urgency
distinction (usually harmless vs. possible retinal detachment), which
demonstrates responsible medical communication.

Suggestion (non-blocking): The CTA on slide 7 reads "Salve esse carrossel."
Consider making it more share-oriented: "Manda esse carrossel para alguém
que vive reclamando de dor de cabeça." Share CTAs generate higher algorithmic
distribution than save CTAs alone.

Suggestion (non-blocking): Caption could include "Dr. Thiago Russo, CRM/AM XXXXX"
at the end to reinforce physician authority in the caption itself, not just
the profile bio.

VERDICT: APPROVE — Content meets all quality criteria with strong medical
accuracy and CFM compliance. Non-blocking suggestions provided for optimization.
```

## Veto Conditions

Reject and redo if ANY are true:
1. Review delivered without scoring every criterion from quality-criteria.md
2. Rejection without actionable fixes (specific location + specific change)
3. Approval without thorough content read (missing detail in feedback)
4. Scores contradict the verdict (all 8+ but REJECT, or 3/10 but APPROVE)

## Quality Criteria

- [ ] Every criterion from quality-criteria.md is scored with justification
- [ ] Every rejected criterion includes specific fix with location reference
- [ ] At least one "Strength:" item is present, even in REJECT reviews
- [ ] Non-blocking suggestions clearly labeled and separated from required changes
- [ ] Verdict matches the scores mathematically
- [ ] Medical claims fact-checked against research-brief.md sources
- [ ] CFM compliance explicitly verified
