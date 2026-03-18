---
execution: inline
agent: squads/instagram-carousel/agents/redator
inputFile: squads/instagram-carousel/output/research-brief.md
outputFile: squads/instagram-carousel/output/angles.md
---

## Context Loading

Load the following files before starting:

- `squads/instagram-carousel/output/research-brief.md` — Selected topic and research data
- `squads/instagram-carousel/pipeline/data/tone-of-voice.md` — Available tones and guidelines
- `squads/instagram-carousel/pipeline/data/output-examples.md` — Reference carousels
- `_opensquad/_memory/company.md` — Company context (CEDOA, Dr. Thiago Russo)

## Instructions

### Process

1. **Read tone-of-voice.md** and recommend the best tone for this specific topic. Present all 6 available options to the user:
   - 1. **Educacional Acessível** — Informativo, linguagem clara, sem jargão
   - 2. **Autoridade Médica** — Técnico mas acessível, reforça credibilidade
   - 3. **Empático e Acolhedor** — Foco na jornada do paciente, emocional
   - 4. **Direto e Urgente** — Alertas, prevenção, call-to-action forte
   - 5. **Conversacional** — Tom de conversa, como se falasse com um amigo
   - 6. **Storytelling** — Narrativo, casos (anonimizados), jornada do paciente
   Ask the user to choose one.

2. **Generate 5 distinct angles** for the selected topic. Each angle MUST use a different emotional perspective:
   - **Medo**: O que pode acontecer se ignorar? (sem ser alarmista — CFM compliance)
   - **Oportunidade**: O que há de novo? Avanços, tecnologias, esperança
   - **Educacional**: O que as pessoas não sabem? Dados surpreendentes
   - **Contrário**: Qual mito precisa ser derrubado? Visão oposta ao senso comum
   - **Inspiracional**: Histórias de prevenção bem-sucedida, qualidade de vida

3. **For each angle**, write:
   - **Hook** (título do primeiro slide) — máximo 8 palavras, deve parar o scroll
   - **Abordagem** — Descrição de como o carrossel se desenvolve (3-4 frases)
   - **Por que funciona** — Justificativa de engajamento e relevância (2-3 frases)

## Output Format

```markdown
# Ângulos para Carrossel: [Tema]

## Tom de Voz Selecionado
[Tom escolhido pelo usuário]

---

### Ângulo 1 — Medo
**Hook**: "[título do slide 1]"
**Abordagem**: [descrição da narrativa do carrossel]
**Por que funciona**: [justificativa]

### Ângulo 2 — Oportunidade
**Hook**: "[título do slide 1]"
**Abordagem**: [descrição]
**Por que funciona**: [justificativa]

[... ângulos 3-5 ...]
```

## Output Example

```markdown
# Ângulos para Carrossel: Glaucoma Prevenção

## Tom de Voz Selecionado
Direto e Urgente

---

### Ângulo 1 — Medo
**Hook**: "Você pode estar perdendo a visão agora"
**Abordagem**: Começar com o dado impactante de que 50% dos pacientes não sabem que têm glaucoma. Cada slide revela um "sinal invisível" que passa despercebido. Finalizar com a importância do exame preventivo e CTA para agendamento.
**Por que funciona**: O medo de perder a visão é universal. Dados concretos evitam sensacionalismo e mantêm compliance com CFM. Gera urgência para agendar consulta.

### Ângulo 2 — Oportunidade
**Hook**: "Glaucoma tem tratamento — e ele evoluiu"
**Abordagem**: Apresentar os avanços recentes: colírios sem conservantes, laser SLT, diagnóstico com IA. Cada slide mostra uma evolução tecnológica. Fechar com esperança e acessibilidade do tratamento.
**Por que funciona**: Conteúdo positivo gera compartilhamentos. Posiciona o Dr. Thiago como atualizado. Quebra a narrativa de que "glaucoma = cegueira inevitável".

### Ângulo 3 — Educacional
**Hook**: "6 fatos sobre glaucoma que surpreendem"
**Abordagem**: Formato listicle com dados pouco conhecidos — glaucoma de pressão normal, fator genético 4-9x, prevalência em jovens. Cada slide é um fato com dado + fonte resumida.
**Por que funciona**: Formato listicle gera curiosidade slide a slide. Dados surpreendentes motivam saves e compartilhamentos. Posiciona como fonte confiável de informação.

### Ângulo 4 — Contrário
**Hook**: "Glaucoma não é doença de idoso"
**Abordagem**: Começar derrubando o mito mais comum. Cada slide confronta um mito com a realidade baseada em dados. Incluir faixa etária real de risco, fatores genéticos, e tipos menos conhecidos.
**Por que funciona**: Conteúdo "mito vs realidade" é um dos formatos com maior engajamento no Instagram médico. Gera comentários de pessoas que se identificam.

### Ângulo 5 — Inspiracional
**Hook**: "Ela descobriu a tempo. Você também pode"
**Abordagem**: Narrativa de um caso anonimizado de paciente que descobriu glaucoma em exame de rotina. Mostrar a jornada: sintomas imperceptíveis → exame preventivo → diagnóstico precoce → tratamento → qualidade de vida preservada.
**Por que funciona**: Storytelling humaniza a medicina. Casos reais (anonimizados) geram identificação. CTA natural para prevenção.
```

## Veto Conditions

- **REJEITAR** se houver menos de 5 ângulos distintos
- **REJEITAR** se ângulos forem apenas temas diferentes (devem ser perspectivas emocionais diferentes sobre o MESMO tema)
- **REJEITAR** se qualquer ângulo violar normas do CFM (promessas de resultado, antes/depois, sensacionalismo médico)
- **REJEITAR** se hooks tiverem mais de 8 palavras
- **REJEITAR** se não houver seleção de tom de voz

## Quality Criteria

- Cada ângulo usa uma perspectiva emocional genuinamente diferente
- Hooks são concisos, provocativos e param o scroll
- Abordagens descrevem uma narrativa clara de início, meio e fim do carrossel
- Justificativas conectam com métricas de engajamento do Instagram (saves, shares, comments)
- Todos os ângulos são viáveis dentro das normas do CFM
- Tom de voz é consistente dentro de cada ângulo
