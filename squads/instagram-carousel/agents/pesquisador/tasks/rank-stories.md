---
task: "Rank & Synthesize Stories"
order: 2
input: sources-list.yaml
output: research-brief.md
---

## Process

1. **Cross-Reference Claims**: Read all sources from the `sources-list.yaml` output of the previous task. For each major claim or finding, check whether it is corroborated by multiple sources. Note which claims appear in only a single source versus those supported by two or more independent references. Flag any contradictory findings between sources for special attention.

2. **Assign Confidence and Extract Findings**: Assign a confidence level to each claim based on source quality and corroboration:
   - **HIGH**: Supported by 2+ peer-reviewed sources or official guidelines
   - **MEDIUM**: Supported by 1 peer-reviewed source plus medical news coverage, or by 2+ medical news sources
   - **LOW**: Based on a single non-peer-reviewed source or preliminary/pre-print data
   Distill the most important 3-5 key findings from the full source set. Each finding should be a clear, actionable statement relevant to Dr. Thiago Russo's ophthalmology audience.

3. **Identify Trending Angles and Write Recommendations**: Identify 2-3 trending angles that would perform well as Instagram carousel content for CEDOA's audience. For each angle, assess its content lifecycle (breaking, trending, evergreen) and estimate audience relevance for ophthalmology patients in Manaus. Write actionable recommendations for which angles to prioritize in carousel creation. Document any gaps in the research where additional sources or expert input would strengthen the content.

## Output Format

```markdown
# Research Brief: <Topic>
**Date:** YYYY-MM-DD
**Researcher:** pesquisador
**Sources Analyzed:** <number>

## Key Findings
1. **<Finding title>** (Confidence: HIGH/MEDIUM/LOW)
   <2-3 sentence summary with source references>

## Trending Angles
| # | Angle | Lifecycle | Audience Fit | Priority |
|---|-------|-----------|-------------|----------|
| 1 | <angle> | <breaking/trending/evergreen> | <high/medium/low> | <1-5> |

## Sources Table
| # | Title | Type | Relevance | Used In |
|---|-------|------|-----------|---------|
| 1 | <title> | <type> | <score>/10 | Finding 1, 3 |

## Recommendations
- <actionable recommendation>

## Gaps
- <identified gap in research>
```

## Output Example

```markdown
# Research Brief: Glaucoma Prevention
**Date:** 2026-03-18
**Researcher:** pesquisador
**Sources Analyzed:** 6

## Key Findings

1. **Early IOP reduction significantly slows glaucomatous progression** (Confidence: HIGH)
   A prospective study of 1,200 patients demonstrated that reducing intraocular pressure by 30% early in diagnosis slowed visual field loss over 3 years. This is corroborated by the updated AAO screening guidelines that emphasize early detection. Directly relevant for patient education on the importance of early treatment adherence.

2. **Universal screening recommended from age 40** (Confidence: HIGH)
   The AAO now recommends comprehensive eye exams including tonometry and OCT for all adults over 40, a significant shift from the previous age-55 threshold for low-risk groups. The SBO has published a parallel consensus for the Brazilian context, proposing telemedicine triage in SUS primary care units.

3. **Neuroprotective therapies show promising results beyond IOP control** (Confidence: MEDIUM)
   Emerging evidence supports neuroprotective agents including Rho-kinase inhibitors as adjunct therapy. A Phase III trial showed positive results, but long-term data is still pending. This represents a paradigm shift from IOP-only treatment approaches.

4. **Lifestyle modifications provide measurable IOP reduction** (Confidence: MEDIUM)
   Meta-analysis data shows regular aerobic exercise reduces IOP by 2-4 mmHg on average. Mediterranean diet adherence correlates with lower glaucoma incidence. These findings are especially actionable for patient-facing content.

## Trending Angles

| # | Angle | Lifecycle | Audience Fit | Priority |
|---|-------|-----------|-------------|----------|
| 1 | "Why your eye exam should start at 40, not 55" — new AAO guidelines | Trending | High | 5 |
| 2 | "Exercise as medicine for your eyes" — lifestyle and IOP | Evergreen | High | 4 |
| 3 | "Beyond eye drops: the future of glaucoma treatment" — neuroprotection | Evergreen | Medium | 3 |

## Sources Table

| # | Title | Type | Relevance | Used In |
|---|-------|------|-----------|---------|
| 1 | Efficacy of Early IOP Reduction in Preventing Glaucomatous Progression | Peer-reviewed | 9/10 | Finding 1 |
| 2 | New AAO Guidelines Recommend Universal Glaucoma Screening After Age 40 | Peer-reviewed | 9/10 | Finding 2 |
| 3 | Neuroprotective Strategies in Glaucoma: Beyond IOP Lowering | Peer-reviewed | 8/10 | Finding 3 |
| 4 | SBO consenso sobre rastreamento de glaucoma no Brasil | Peer-reviewed | 8/10 | Finding 2 |
| 5 | Lifestyle Factors and Glaucoma Risk: Exercise, Diet, and Sleep | Medical-news | 7/10 | Finding 4 |
| 6 | How to Protect Your Eyes from Glaucoma | Health-media | 5/10 | Finding 4 |

## Recommendations

- **Lead with the AAO screening age change** — this is the most newsworthy angle and directly impacts patient behavior. Frame as "what changed and why it matters for you."
- **Pair lifestyle content with clinical data** — the exercise/diet angle is highly shareable on Instagram and backed by meta-analysis data. Use specific numbers (2-4 mmHg reduction) for credibility.
- **Save neuroprotection for a follow-up carousel** — the topic is compelling but more technical. Better suited for a dedicated deep-dive carousel targeting fellow ophthalmologists.

## Gaps

- No sources found specifically addressing glaucoma prevention in tropical or equatorial climates, which would be directly relevant for the Manaus patient population.
- Limited data on glaucoma screening access and outcomes in the Amazon region or Norte do Brasil specifically.
- No patient-reported outcome studies found on lifestyle intervention adherence in Brazilian populations.
```

## Quality Criteria

1. **Confidence Levels Required**: Every key finding must have an explicitly assigned confidence level (HIGH, MEDIUM, or LOW) with a clear justification based on source quality and corroboration.
2. **Multi-Source Corroboration**: Each key finding must reference at least 2 sources from the sources table. Single-source findings must be flagged as LOW confidence.
3. **Gaps Section Present and Substantive**: The gaps section must identify at least 2 specific areas where the research is incomplete, with actionable suggestions for how to address them.
4. **Trending Angles Assessed**: Each trending angle must include lifecycle classification and audience fit rating to guide content prioritization decisions.
5. **Source Traceability**: The sources table must clearly map which findings each source contributed to, enabling full traceability from recommendation back to original evidence.

## Veto Conditions

1. **Unsourced Findings**: Any key finding is presented without referencing specific sources from the analyzed set. All claims must be traceable to the sources table.
2. **Opinions as Facts**: Subjective editorial opinions are presented as research findings without being clearly labeled as interpretation or recommendation. Findings must be evidence-based.
3. **Missing Gaps Section**: The research brief omits the gaps section entirely or includes only generic placeholder text. Gaps must be specific and relevant to the topic and audience context.
