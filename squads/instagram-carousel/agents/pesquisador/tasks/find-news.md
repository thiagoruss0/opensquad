---
task: "Find News & Topics"
order: 1
input: research-focus.md
output: sources-list.yaml
---

## Process

1. **Parse Research Focus**: Read `research-focus.md` to extract the user's chosen topic, any subtopic preferences, and the specified time range (e.g., last 30 days, last 6 months, last year). Identify relevant keywords and MeSH terms for ophthalmology-related searches.

2. **Search for Sources**: Use `web_search` to find 5-10 relevant sources about the topic. Execute multiple queries using different keyword combinations to maximize coverage. Prioritize sources in the following order:
   - **Tier 1 (Peer-reviewed)**: PubMed, AAO (American Academy of Ophthalmology), SBO (Sociedade Brasileira de Oftalmologia), ARVO journals, Ophthalmology journal, JAMA Ophthalmology
   - **Tier 2 (Medical news)**: Medscape Ophthalmology, EyeWire News, Review of Ophthalmology, Healio Ophthalmology
   - **Tier 3 (General health media)**: Medical News Today, Healthline, Mayo Clinic, reputable health sections of major news outlets

3. **Record and Filter Results**: For each source found, record the title, URL, publication date, source type (peer-reviewed, medical-news, health-media), and write a concise 2-line summary of the key finding or claim. Assign a relevance score from 1-10 based on how directly the source addresses the user's topic. Filter out any sources that fall outside the user's specified time range. Remove duplicates and sources behind hard paywalls without abstracts.

## Output Format

```yaml
topic: "<research topic>"
time_range: "<specified time range>"
search_date: "YYYY-MM-DD"
total_sources_found: <number>
sources:
  - title: "<article title>"
    url: "<full URL>"
    date: "YYYY-MM-DD"
    type: "<peer-reviewed | medical-news | health-media>"
    summary: "<2-line summary of key content>"
    relevance_score: <1-10>
```

## Output Example

```yaml
topic: "glaucoma prevention"
time_range: "last 6 months"
search_date: "2026-03-18"
total_sources_found: 6
sources:
  - title: "Efficacy of Early IOP Reduction in Preventing Glaucomatous Progression: A Prospective Study"
    url: "https://pubmed.ncbi.nlm.nih.gov/39284751/"
    date: "2026-01-12"
    type: "peer-reviewed"
    summary: "Prospective cohort study of 1,200 patients showing that early IOP reduction by 30% significantly slowed visual field loss over 3 years. Results support aggressive early intervention in ocular hypertension patients."
    relevance_score: 9
  - title: "New AAO Guidelines Recommend Universal Glaucoma Screening After Age 40"
    url: "https://www.aao.org/newsroom/news-releases/detail/glaucoma-screening-guidelines-2026"
    date: "2026-02-05"
    type: "peer-reviewed"
    summary: "Updated AAO practice guidelines now recommend comprehensive eye exams including tonometry and OCT for all adults over 40, regardless of risk factors. Previous guidelines recommended screening starting at age 55 for low-risk populations."
    relevance_score: 9
  - title: "Neuroprotective Strategies in Glaucoma: Beyond IOP Lowering"
    url: "https://jamanetwork.com/journals/jamaophthalmology/article-abstract/2826194"
    date: "2025-11-20"
    type: "peer-reviewed"
    summary: "Review article examining emerging neuroprotective agents including brimonidine, memantine, and CNTF for glaucomatous optic neuropathy. Highlights promising Phase III trial results for a novel Rho-kinase inhibitor."
    relevance_score: 8
  - title: "Lifestyle Factors and Glaucoma Risk: Exercise, Diet, and Sleep"
    url: "https://www.medscape.com/viewarticle/lifestyle-glaucoma-prevention-2026a100032f"
    date: "2026-03-01"
    type: "medical-news"
    summary: "Meta-analysis coverage showing regular aerobic exercise reduces IOP by 2-4 mmHg on average. Also discusses emerging evidence linking Mediterranean diet adherence to lower glaucoma incidence."
    relevance_score: 7
  - title: "SBO publica consenso sobre rastreamento de glaucoma no Brasil"
    url: "https://www.sboportal.org.br/consenso-glaucoma-rastreamento-2026"
    date: "2026-02-18"
    type: "peer-reviewed"
    summary: "Brazilian Ophthalmology Society consensus document addressing glaucoma screening barriers in the national health system (SUS). Proposes telemedicine-based triage using fundus photography in primary care units."
    relevance_score: 8
  - title: "How to Protect Your Eyes from Glaucoma: What Science Says in 2026"
    url: "https://www.healthline.com/health/eye-health/glaucoma-prevention-2026"
    date: "2026-01-28"
    type: "health-media"
    summary: "Consumer-oriented article summarizing current evidence on glaucoma prevention strategies. Covers regular screenings, medication adherence, and lifestyle modifications in accessible language."
    relevance_score: 5
```

## Quality Criteria

1. **Complete Metadata**: Every source must include a working URL, a publication date, and a correctly assigned type category. No fields may be left blank or marked as unknown.
2. **Minimum Source Count**: The output must contain at least 5 sources. Ideally 7-10 for comprehensive topic coverage.
3. **Source Diversity**: Sources must span at least 2 of the 3 tiers (peer-reviewed, medical-news, health-media) to ensure balanced perspective.
4. **Relevance Sorting**: Sources must be sorted by relevance_score in descending order, with the most directly relevant sources listed first.
5. **Recency Compliance**: All sources must fall within the user's specified time range. No outdated articles should be included.

## Veto Conditions

1. **Insufficient Sources**: The task output contains fewer than 5 sources. The researcher must continue searching with alternative queries until the minimum threshold is met.
2. **Missing URLs**: Any source is listed without a valid URL. Every source must be verifiable and accessible.
3. **Single-Source Dominance**: All sources originate from the same single website or publication. A minimum of 3 distinct domains must be represented in the final list.
