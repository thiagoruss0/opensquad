---
task: "Optimize Carousel Copy"
order: 3
input:
  - carousel-draft.md
output: carousel-optimized.md
---

## Process

### 1. Reduzir Contagem de Palavras (15-25%)

Revise cada slide e a caption para eliminar:
- Palavras de enchimento (muito, realmente, basicamente, na verdade).
- Redundancias (repetir a mesma ideia com palavras diferentes).
- Frases passivas que podem ser ativas.
- Adjetivos desnecessarios que nao agregam significado.

Mantenha a substancia e o tom — corte gordura, nao musculo. Registre a contagem de palavras antes e depois de cada slide.

### 2. Fortalecer CTAs

Revise todos os CTAs (slide final e caption) para que sejam:
- **Especificos**: Dizer exatamente o que fazer (ex: "Agende pelo WhatsApp" em vez de "Entre em contato").
- **Acionaveis**: Usar verbos no imperativo (agende, salve, compartilhe, comente).
- **Urgentes sem ser apelativos**: Criar senso de oportunidade sem pressao excessiva.

### 3. Verificar Precisao Medica

Confronte cada afirmacao medica do carrossel com as fontes do `research-brief.md`:
- Dados estatisticos devem ter respaldo na pesquisa.
- Termos tecnicos devem estar corretos e acessiveis ao leigo.
- Nenhuma afirmacao nova deve ser adicionada sem fonte verificavel.
- Marque com [VERIFICAR] qualquer claim que nao encontre respaldo direto.

### 4. Checar Conformidade CFM

Revise todo o conteudo contra as diretrizes do CFM:
- Sem garantias de resultado ("voce vai enxergar melhor" -> "pode contribuir para a saude ocular").
- Sem superlativos ("o melhor tratamento" -> "um tratamento reconhecido").
- Enquadramento educativo, nao promocional.
- Sem exposicao de pacientes ou dados confidenciais.
- Sem comparacao com outros profissionais ou clinicas.

### 5. Teste de Parada de Scroll

Avalie o hook (slide 1) com os seguintes criterios:
- **Especificidade**: Evita termos vagos? Fala de algo concreto?
- **Tensao**: Cria uma lacuna de curiosidade?
- **Relevancia**: O publico-alvo se identifica imediatamente?
- Se o hook falhar em 2 ou mais criterios, reescreva e apresente alternativa.

### 6. Validar Caption Hook

Verifique se os primeiros 125 caracteres da caption:
- Funcionam como frase autonoma (fazem sentido sem o "ver mais").
- Geram curiosidade suficiente para o usuario expandir o texto.
- Nao repetem o hook do slide 1 literalmente (complementam, nao duplicam).

## Output Format

Mesmo formato do input (`=== FORMAT ===`, `=== SLIDES ===`, `=== CAPTION ===`, `=== HASHTAGS ===`), acrescido de:

```
=== OPTIMIZATION NOTES ===
Reducao total de palavras: [X]% ([antes] -> [depois])
Slides otimizados: [lista dos slides modificados]
CTAs fortalecidos: [descricao das mudancas]
Claims verificados: [quantidade] de [total] — [status]
Conformidade CFM: [Aprovado / Ajustes realizados]
Hook scroll-stop: [Aprovado / Reescrito]
Caption hook (125 chars): [Aprovado / Ajustado]
```

## Output Example

```
=== SLIDES ===
[Slide 3 — ANTES]
Headline: Dores de cabeça recorrentes
Texto: Cefaleia persistente, principalmente na regiao frontal, pode estar ligada a erros refrativos nao diagnosticados. Quando o olho forca para compensar, o cerebro paga o preco. Um exame oftalmologico simples pode resolver o que analgesicos apenas mascaram. (38 palavras)

[Slide 3 — DEPOIS]
Headline: Dor de cabeça que nao passa
Texto: Cefaleia frontal recorrente pode indicar erro refrativo nao corrigido. O olho forca, o cerebro sofre. Um exame oftalmologico identifica a causa que analgesicos so mascaram. (26 palavras — reducao de 32%)

=== OPTIMIZATION NOTES ===
Reducao total de palavras: 19% (487 -> 394)
Slides otimizados: 2, 3, 5, 6, 7
CTAs fortalecidos: Slide 8 — "agende sua consulta" substituido por "Mande um oi no WhatsApp da CEDOA e agende sua avaliacao"
Claims verificados: 7 de 7 — Todos com respaldo no research-brief
Conformidade CFM: Aprovado — nenhuma violacao encontrada
Hook scroll-stop: Aprovado — especifico, com tensao, relevante para publico 35+
Caption hook (125 chars): Ajustado — "Seus olhos dao sinais antes de qualquer sintoma grave aparecer" (63 chars)
```

## Quality Criteria

- Reducao de palavras entre 15% e 25% no total do carrossel.
- Todas as afirmacoes medicas verificadas contra fontes do research-brief.
- Conformidade total com diretrizes do CFM apos otimizacao.
- CTAs reescritos com verbo no imperativo e acao especifica.
- Hook do slide 1 aprovado nos 3 criterios de scroll-stop.
- Primeiros 125 caracteres da caption funcionam como frase autonoma.

## Veto Conditions

- Nenhuma otimizacao real realizada (output identico ao input).
- Afirmacao medica adicionada ou modificada sem respaldo em fonte verificavel.
- Violacao do CFM introduzida durante a otimizacao (garantia de resultado, superlativo, exposicao).
- Reducao de palavras abaixo de 15% ou acima de 25% (corte insuficiente ou perda de substancia).
