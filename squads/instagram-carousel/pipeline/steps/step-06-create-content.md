---
execution: inline
agent: squads/instagram-carousel/agents/redator
format: instagram-feed
inputFile: squads/instagram-carousel/output/angles.md
outputFile: squads/instagram-carousel/output/carousel-draft.md
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/angles.md` — Selected angle and tone of voice
- `squads/instagram-carousel/output/research-brief.md` — Source data and findings
- `squads/instagram-carousel/pipeline/data/tone-of-voice.md` — Tone guidelines
- `squads/instagram-carousel/pipeline/data/anti-patterns.md` — What to avoid
- `squads/instagram-carousel/pipeline/data/output-examples.md` — Reference carousels
- `squads/instagram-carousel/pipeline/data/quality-criteria.md` — Scoring criteria
- `_opensquad/_memory/company.md` — CEDOA brand and identity

## Instructions

### Process

1. **Choose the best carousel format** for the selected angle. Options:
   - Editorial — opiniao fundamentada, posicionamento
   - Listicle — lista numerada de itens (3, 5, 7 fatos/dicas)
   - Tutorial — passo a passo pratico
   - Mito vs Realidade — desmonte de crencas populares
   - Problema → Solucao — identifica dor, apresenta solucao
   - Storytelling — narrativa com arco (inicio, meio, fim)

2. **Write 3 hook options** using different structural types:
   - Pergunta provocativa ("Voce sabia que...?")
   - Afirmacao chocante ("50% dos brasileiros...")
   - Comando direto ("Pare de ignorar este sintoma")
   Present the 3 hooks to the user for selection before continuing.

3. **After user selects hook, write the full carousel:**
   - **8-10 slides**, each with:
     - Headline (titulo principal, 3-7 palavras, impactante)
     - Supporting text (texto de apoio, 40-80 palavras, educativo)
   - **Slide 1:** Hook slide (titulo escolhido + subtitulo contextualizador)
   - **Slides 2-N-1:** Content slides (desenvolvimento do tema)
   - **Slide N:** CTA slide (chamada para acao clara)
   - **Full caption** (legenda completa):
     - Hook nos primeiros 125 caracteres (aparece antes do "mais")
     - Corpo com contexto, dados, e valor educativo
     - CTA final (salve, compartilhe, comente, agende)
     - Maximo 2200 caracteres
   - **5 hashtags** relevantes e estrategicas

4. **Apply the chosen tone of voice** consistently across all slides and caption.

5. **Ensure CFM compliance throughout:**
   - Sem garantias de resultado ("pode ajudar", nunca "vai curar")
   - Sem superlativos ("o melhor", "o unico", "revolucionario")
   - Enquadramento educativo, nao promocional
   - Sem fotos de antes/depois com promessas

6. **Run the optimize pass:**
   - Tighten copy 15-25% (remove filler words, redundancies)
   - Strengthen CTAs (specific, actionable)
   - Verify every medical claim against research-brief.md
   - Check slide flow (each slide must create desire to see the next)

## Output Format

```markdown
=== FORMAT ===
Tipo: [format chosen]
Tom: [tone of voice]
Slides: [number]
Angulo: [angle used]

=== SLIDES ===

### Slide 01 (Capa)
**[Headline]**
[Supporting text]

### Slide 02
**[Headline]**
[Supporting text]

[... remaining slides ...]

### Slide [N] (CTA)
**[Headline]**
[Supporting text]

=== CAPTION ===
[Full caption text, under 2200 characters]

=== HASHTAGS ===
#hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5
```

## Output Example

```markdown
=== FORMAT ===
Tipo: Listicle
Tom: Educador Acessivel
Slides: 9
Angulo: Educacional

=== SLIDES ===

### Slide 01 (Capa)
**5 fatos sobre glaucoma que surpreendem**
Voce acha que sabe tudo sobre essa doenca? Deslize e descubra o que a maioria das pessoas — e ate alguns profissionais — nao contam.

### Slide 02
**Nao doi. Nao avisa. Nao volta.**
O glaucoma e chamado de "ladrao silencioso da visao" porque nao apresenta sintomas ate estagios avancados. Quando voce percebe a perda, ate 40% do campo visual ja foi comprometido de forma irreversivel. A unica defesa e o diagnostico precoce.

### Slide 03
**Pressao normal nao significa seguranca**
30% dos casos de glaucoma no Brasil ocorrem com pressao intraocular dentro da faixa considerada "normal". Por isso, medir apenas a pressao nao basta — o exame completo do nervo optico e essencial.

### Slide 04
**Jovens tambem podem ter**
Embora seja mais comum apos os 40, o glaucoma congenito e juvenil existe. Criancas com olhos grandes, lacrimejamento excessivo ou sensibilidade a luz devem ser avaliadas. Nao e "doenca de idoso".

### Slide 05
**Genetica importa — e muito**
Se voce tem pai, mae ou irmaos com glaucoma, seu risco e 4 a 9 vezes maior. Mesmo assim, apenas 15% das pessoas com historico familiar fazem acompanhamento regular. Informe sua familia.

### Slide 06
**Colirio nao cura, mas preserva**
O tratamento com colirios reduz a pressao intraocular e desacelera a progressao. Nao reverte o dano ja feito, mas pode preservar a visao que resta. Adesao diaria ao tratamento e fundamental.

### Slide 07
**Miopia alta aumenta o risco**
Estudos recentes mostram que pessoas com miopia acima de -6 graus tem risco significativamente maior de desenvolver glaucoma. Se voce usa lentes grossas, fique atento ao acompanhamento.

### Slide 08
**Um exame de 15 minutos pode mudar tudo**
O exame oftalmologico completo — com avaliacao do nervo optico, campo visual e OCT — leva cerca de 15 minutos e pode detectar o glaucoma ate 5 anos antes dos sintomas. Indolor, rapido e decisivo.

### Slide 09 (CTA)
**Sua visao merece essa atencao**
Agende seu exame oftalmologico. Compartilhe este carrossel com quem voce ama — especialmente se tem mais de 40 anos ou historico familiar. Prevencao e o unico tratamento que funciona antes da doenca.

=== CAPTION ===
5 fatos sobre glaucoma que a maioria das pessoas desconhece — e que podem salvar sua visao.

O glaucoma e a principal causa de cegueira irreversivel no mundo. No Brasil, metade dos portadores nao sabe que tem a doenca.

Neste carrossel, reuni dados atualizados de fontes como a OMS, o Conselho Brasileiro de Oftalmologia e estudos publicados em 2025-2026 para compartilhar o que todo mundo deveria saber.

Alguns destaques que podem surpreender voce:
- Pressao ocular normal NAO descarta glaucoma
- Historico familiar aumenta o risco em ate 9x
- Miopia alta e um fator de risco pouco conhecido
- Um exame de 15 minutos detecta a doenca anos antes dos sintomas

Conhecimento e a melhor prevencao. Salve este post para consultar depois e compartilhe com quem precisa saber.

Agende sua avaliacao oftalmologica. Link na bio ou mande um direct.

Dr. Thiago Russo | CRM-AM 0000
Oftalmologista — CEDOA Manaus

=== HASHTAGS ===
#glaucoma #saudeocular #oftalmologia #prevencao #cedoamanaus
```

## Veto Conditions

- **REJECT** if the hook does not create genuine scroll-stopping impact
- **REJECT** if any slide has fewer than 40 words of supporting text
- **REJECT** if the carousel lacks a clear CTA slide
- **REJECT** if any content violates CFM guidelines (guarantees, superlatives, promotional tone)
- **REJECT** if the caption exceeds 2200 characters
- **REJECT** if medical claims cannot be traced to the research brief sources
- **REJECT** if slides do not flow logically (each should motivate swiping to the next)

## Quality Criteria

- Hook generates curiosity or urgency in under 8 words
- Each slide adds new value (no repetition or filler)
- Tone is consistent throughout all slides and caption
- Medical accuracy is maintained without being overly technical
- CTA is specific and actionable (not generic "siga para mais")
- Caption complements slides (does not merely repeat them)
- Hashtags are strategic (mix of broad reach and niche relevance)
- Total word count per slide is within 40-80 word range
