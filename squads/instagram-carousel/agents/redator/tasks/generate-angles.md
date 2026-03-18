---
task: "Generate Content Angles"
order: 1
input:
  - research-brief.md
  - tone-of-voice.md
output: angles.md
---

## Process

### 1. Definir Tom de Voz

Leia o arquivo `tone-of-voice.md` e analise o posicionamento do Dr. Thiago Russo e da CEDOA.
Com base nisso, recomende um tom adequado ao tema selecionado em `research-brief.md`.
Apresente 6 opções de tom ao usuario:
- Educativo-acolhedor
- Autoritativo-acessivel
- Urgente-empático
- Conversacional-tecnico
- Inspirador-clinico
- Direto-pragmatico

Aguarde a escolha do usuario antes de prosseguir.

### 2. Gerar 5 Angulos com Drivers Emocionais Distintos

Para o tema selecionado no `research-brief.md`, crie 5 angulos utilizando perspectivas emocionais diferentes:
- **Medo**: Consequencias de ignorar o problema.
- **Oportunidade**: Beneficios de agir agora.
- **Educacional**: Curiosidade e aprendizado puro.
- **Contrario**: Desafiar uma crenca popular sobre o tema.
- **Inspiracional**: Historia ou caso motivador (sem expor pacientes).

Cada angulo deve abordar o MESMO tema, apenas sob perspectivas diferentes.

### 3. Estruturar Cada Angulo

Para cada um dos 5 angulos, elabore:
- **Hook**: Titulo do primeiro slide (maximo 20 palavras, linguagem de parada de scroll).
- **Abordagem**: Descricao em 2-3 frases de como o carrossel se desenvolveria.
- **Racional**: Justificativa de por que esse angulo funciona para o publico-alvo.

## Output Format

```yaml
tom_escolhido: "[tom selecionado pelo usuario]"
tema: "[tema do research-brief]"
angulos:
  - name: "[nome do angulo]"
    emotional_driver: "Medo | Oportunidade | Educacional | Contrario | Inspiracional"
    hook: "[titulo do primeiro slide]"
    approach: "[descricao da abordagem]"
    rationale: "[justificativa]"
```

## Output Example

```yaml
tom_escolhido: "Educativo-acolhedor"
tema: "Prevencao do glaucoma"
angulos:
  - name: "O ladrao silencioso"
    emotional_driver: "Medo"
    hook: "Voce pode estar perdendo a visao agora sem sentir nada"
    approach: "Mostrar como o glaucoma avanca sem sintomas, usando dados de prevalencia em Manaus e no Brasil. Fechar com sinais de alerta e frequencia ideal de consultas."
    rationale: "O medo de perda silenciosa gera urgencia. Publico leigo subestima doencas assintomaticas."
  - name: "Enxergar bem aos 80"
    emotional_driver: "Oportunidade"
    hook: "3 exames simples que protegem sua visao por decadas"
    approach: "Focar nos beneficios do diagnostico precoce. Apresentar exames acessiveis e o impacto positivo na qualidade de vida a longo prazo."
    rationale: "Framing positivo motiva acao preventiva. Mostra que prevenção e simples e acessivel."
  - name: "Como o olho envelhece"
    emotional_driver: "Educacional"
    hook: "O que acontece dentro do seu olho depois dos 40 anos"
    approach: "Explicar a fisiologia do humor aquoso e pressao intraocular de forma didatica. Conectar o mecanismo biologico com a importancia do acompanhamento."
    rationale: "Conteudo educativo puro gera salvamentos e compartilhamentos. Posiciona o doutor como referencia."
  - name: "Mito do colirio"
    emotional_driver: "Contrario"
    hook: "Colirio nao cura glaucoma e voce precisa saber por que"
    approach: "Desmontar a crenca de que colirios resolvem tudo. Explicar o papel real da medicacao vs. acompanhamento continuo e possivel cirurgia."
    rationale: "Contrariar crencas populares gera debate e engajamento. Combate automedicacao."
  - name: "A consulta que mudou tudo"
    emotional_driver: "Inspiracional"
    hook: "Ele quase perdeu a visao mas um exame de rotina salvou tudo"
    approach: "Contar um caso anonimizado de diagnostico precoce bem-sucedido na CEDOA. Humanizar a prevencao com narrativa real sem expor dados do paciente."
    rationale: "Historias reais criam conexao emocional e reduzem a barreira para agendar consultas."
```

## Quality Criteria

- Exatamente 5 angulos distintos, cada um com um driver emocional diferente.
- Hooks com no maximo 20 palavras, escritos em linguagem acessivel e de parada de scroll.
- Abordagens claras que permitam ao proximo agente desenvolver o carrossel sem ambiguidade.
- Todos os angulos abordam o mesmo tema central, variando apenas a perspectiva.
- Linguagem adequada ao tom escolhido pelo usuario.

## Veto Conditions

- Menos de 5 angulos apresentados.
- Angulos que mudam de tema em vez de mudar de perspectiva (ex: um sobre glaucoma e outro sobre catarata).
- Violacao do CFM: promessas de cura, superlativos ("o melhor", "unico"), exposicao de pacientes ou resultados garantidos.
- Hooks com mais de 20 palavras.
