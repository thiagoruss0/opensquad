---
execution: inline
agent: squads/instagram-carousel/agents/redator
inputFile: squads/instagram-carousel/output/research-brief.md
outputFile: squads/instagram-carousel/output/angles.md
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/research-brief.md` — Selected topic from research
- `squads/instagram-carousel/pipeline/data/tone-of-voice.md` — Available tones of voice
- `squads/instagram-carousel/pipeline/data/output-examples.md` — Reference carousels
- `_opensquad/_memory/company.md` — Company context (CEDOA, Dr. Thiago Russo)

## Instructions

### Process

1. **Read `tone-of-voice.md`** and present the 6 available tones to the user. Recommend the best tone for this specific topic based on the subject matter and target audience. The 6 tones are:
   - Educador Acessivel (didatico, acolhedor)
   - Autoridade Cientifica (dados, evidencias)
   - Provocador Consciente (questionador, quebra mitos)
   - Narrador Empatico (historias, conexao emocional)
   - Pratico Direto (objetivo, acionavel)
   - Inspirador Motivacional (positivo, empoderador)

   Ask the user to choose one tone before proceeding.

2. **Generate 5 distinct angles (angulos)** for the selected topic. Each angle MUST use a different emotional perspective:
   - **Medo** — O que pode acontecer se ignorar? (consequencias, urgencia)
   - **Oportunidade** — O que voce ganha ao agir? (beneficios, vantagens)
   - **Educacional** — O que voce nao sabe sobre isso? (curiosidade, aprendizado)
   - **Contrario** — O que todo mundo acredita esta errado? (mitos, surpreendente)
   - **Inspiracional** — Quem ja superou isso? (historias, motivacao)

3. **For each angle**, write:
   - A **hook** (titulo do primeiro slide) — maximo 8 palavras, parada de scroll
   - A **descricao da abordagem** — como o carrossel vai se desenrolar (3-4 frases)
   - Uma **justificativa** — por que esse angulo funciona para o publico

## Output Format

```markdown
# Angulos para Carrossel: [Topic]

**Tom de voz escolhido:** [tone]

## Angulo 1: MEDO
**Hook:** [titulo do slide 1]
**Abordagem:** [como o carrossel se desenrola]
**Por que funciona:** [justificativa]

## Angulo 2: OPORTUNIDADE
**Hook:** [titulo do slide 1]
**Abordagem:** [como o carrossel se desenrola]
**Por que funciona:** [justificativa]

## Angulo 3: EDUCACIONAL
**Hook:** [titulo do slide 1]
**Abordagem:** [como o carrossel se desenrola]
**Por que funciona:** [justificativa]

## Angulo 4: CONTRARIO
**Hook:** [titulo do slide 1]
**Abordagem:** [como o carrossel se desenrola]
**Por que funciona:** [justificativa]

## Angulo 5: INSPIRACIONAL
**Hook:** [titulo do slide 1]
**Abordagem:** [como o carrossel se desenrola]
**Por que funciona:** [justificativa]
```

## Output Example

```markdown
# Angulos para Carrossel: Glaucoma e Prevencao

**Tom de voz escolhido:** Educador Acessivel

## Angulo 1: MEDO
**Hook:** Voce pode estar perdendo a visao agora
**Abordagem:** Abre com dado chocante (50% nao sabem que tem). Mostra progressao silenciosa do glaucoma em 4 slides visuais. Compara visao normal vs. visao com glaucoma avancado. Fecha com urgencia: "quando voce percebe, ja perdeu 40% do campo visual."
**Por que funciona:** Medo de perda irreversivel e o gatilho mais forte para agendar consulta. Dado do "50% nao diagnosticados" gera compartilhamento.

## Angulo 2: OPORTUNIDADE
**Hook:** Um exame de 15min salva sua visao
**Abordagem:** Foca na simplicidade da prevencao. Slide a slide mostra o que acontece no exame oftalmologico. Destaca que deteccao precoce = 95% de preservacao visual. CTA forte para agendamento.
**Por que funciona:** Remove a barreira do medo do exame. Transforma prevencao em algo facil e acessivel. Tom positivo gera saves.

## Angulo 3: EDUCACIONAL
**Hook:** 5 fatos sobre glaucoma que surpreendem
**Abordagem:** Lista format com fatos contra-intuitivos: pressao normal tambem causa, jovens tambem tem, colirio nao cura mas preserva, cirurgia existe, genetica importa. Cada slide um fato com explicacao curta.
**Por que funciona:** Formato lista e o mais salvo no Instagram. "Surpreendem" gera curiosidade para deslizar. Educacao pura sem tom de venda.

## Angulo 4: CONTRARIO
**Hook:** Glaucoma nao e so pressao alta no olho
**Abordagem:** Desmonta o mito mais comum. Explica glaucoma de pressao normal (30% dos casos). Mostra outros fatores de risco que as pessoas ignoram. Conclui: "por isso o exame completo importa mais que medir pressao."
**Por que funciona:** Quebra de crenca gera engajamento ("eu nao sabia!"). Posiciona o medico como autoridade que vai alem do obvio. Alto potencial de compartilhamento.

## Angulo 5: INSPIRACIONAL
**Hook:** Ela descobriu a tempo e nao perdeu a visao
**Abordagem:** Caso (anonimizado) de paciente que fez exame de rotina, descobriu glaucoma precoce, tratou e preservou visao. Timeline: antes, diagnostico, tratamento, hoje. Mensagem: "sua historia tambem pode ter final feliz."
**Por que funciona:** Storytelling gera conexao emocional. Mostra resultado real do cuidado preventivo. Humaniza o consultorio e gera confianca.
```

## Veto Conditions

- **REJECT** if fewer than 5 angles are presented
- **REJECT** if angles are merely different subtopics (not different emotional perspectives on the same topic)
- **REJECT** if any angle contains language that violates CFM (Conselho Federal de Medicina) — no result guarantees, no superlatives like "o melhor", no before/after promises
- **REJECT** if hooks exceed 8 words or are generic/weak
- **REJECT** if tone of voice was not confirmed with user before generating

## Quality Criteria

- Each angle is clearly distinct in emotional approach
- Hooks are specific, concrete, and scroll-stopping
- Abordagem descriptions are detailed enough to visualize the full carousel
- Justificativas reference audience behavior (saves, shares, comments)
- All content maintains medical accuracy from the research brief
- Language is natural Brazilian Portuguese, not formal/academic
