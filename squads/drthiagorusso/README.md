# Squad — Dr. Thiago Russo Oftalmologia

Squad de produção e publicação automática de carrosséis educativos de oftalmologia para o Instagram **@drthiagorusso**.

## Visão Geral

Este squad orquestra 6 agentes especializados em pipeline sequencial, desde a pesquisa científica até a publicação automática no Instagram via API Manus.

## Agentes

| Agente | Ícone | Função | Modelo |
|--------|-------|--------|--------|
| Pesquisador | 🔬 | Pesquisa científica e tendências | fast |
| Estrategista | 🧭 | Estratégia de conteúdo e persona | powerful |
| **Copywriter** | **✍️** | **Copy ético e persuasivo** | **powerful** |
| Designer | 🎨 | Imagens 1080×1350px | powerful |
| Revisor | 🔍 | Controle de qualidade e ética | powerful |
| Publisher | 📲 | Publicação via API Manus | fast |

## Pipeline

```
🔬 Pesquisador
    ↓ research-brief.md
🧭 Estrategista
    ↓ strategy-brief.yaml
✅ CHECKPOINT — Aprovar estratégia
    ↓
✍️ Copywriter
    ↓ copy-draft.md
✅ CHECKPOINT — Aprovar copy
    ↓
🎨 Designer
    ↓ images/ (7 slides JPEG)
🔍 Revisor
    ↓ review-report.md
✅ CHECKPOINT — Confirmar publicação
    ↓
📲 Publisher → @drthiagorusso
```

## Como Executar

### Via Manus (Recomendado)

Na interface da Manus, execute:

```
/opensquad rode o squad drthiagorusso
```

Ou com tema específico:

```
/opensquad rode o squad drthiagorusso com o tema "catarata e medo de cirurgia"
```

### Via IDE (Claude Code, Cursor, etc.)

```
/opensquad run drthiagorusso
```

## Checkpoints

O squad pausa em 3 momentos para sua aprovação:

1. **Após Estrategista** — Aprovar persona, gancho e estrutura dos slides
2. **Após Copywriter** — Aprovar copy completo antes de gerar imagens
3. **Antes de publicar** — Confirmação final antes de postar no Instagram

## Publicação no Instagram

A publicação usa a **API Manus (MCP Instagram)** — já autenticada com @drthiagorusso. Não é necessário configurar tokens externos.

Para publicar manualmente (fora do pipeline):

```bash
python3 squads/drthiagorusso/tools/publish-manus.py \
  --images "squads/drthiagorusso/output/images/slide-01.jpg,...,slide-07.jpg" \
  --caption "Sua legenda aqui"
```

Para testar sem publicar:

```bash
python3 squads/drthiagorusso/tools/publish-manus.py \
  --images "..." --caption "..." --dry-run
```

## Estrutura de Arquivos

```
squads/drthiagorusso/
├── README.md                    # Este arquivo
├── squad.yaml                   # Configuração do squad
├── squad-party.csv              # Lista de agentes
├── _memory/
│   └── memories.md              # Contexto e histórico
├── agents/
│   ├── researcher/
│   │   └── researcher.agent.md
│   ├── strategist/
│   │   └── strategist.agent.md
│   ├── copywriter/              # ← AGENTE COPYWRITER
│   │   └── copywriter.agent.md
│   ├── designer/
│   │   └── designer.agent.md
│   ├── reviewer/
│   │   └── reviewer.agent.md
│   └── publisher/
│       └── publisher.agent.md
├── pipeline/
│   ├── pipeline.yaml            # Definição do pipeline
│   └── data/
│       └── tone-of-voice.md     # Tom de voz da marca
├── output/                      # Saídas de cada execução
│   ├── research-brief.md
│   ├── strategy-brief.yaml
│   ├── copy-draft.md
│   ├── review-report.md
│   ├── publish-result.md
│   └── images/
│       ├── slide-01.jpg
│       ├── ...
│       └── slide-07.jpg
└── tools/
    └── publish-manus.py         # Script de publicação via API Manus
```

## Identidade Visual

| Elemento | Valor |
|----------|-------|
| Cor primária | Azul-marinho #0B2A4A |
| Background | Cinza-claro #F2F4F7 |
| Acento | Dourado #C9A24D |
| Contraste | Branco #FFFFFF |
| Título | Montserrat Bold / Poppins Bold |
| Corpo | Lato Regular / Open Sans Regular |
| Dimensão | 1080×1350px (4:5) |

## Personas Suportadas

| Código | Nome | Tema | Tom |
|--------|------|------|-----|
| C1 | "Adia por medo" | Catarata | Calmo, acolhedor |
| C2 | "Ativo e funcional" | Catarata | Direto, prático |
| C3 | "Comparadora e exigente" | Catarata | Técnico, honesto |
| R1 | "Pânico do descolamento" | Retina | Tranquilizador |
| R2 | "Quer entender o OCT" | Retina | Educativo, técnico |
| R3 | "Paciente + filha resolutiva" | Retina | Acolhedor, prático |

## Ética Médica

O squad respeita rigorosamente as diretrizes do **CFM** e do **CBO**. O Revisor verifica automaticamente:

- Sem promessas de cura ou resultado específico
- Sem urgência artificial
- Sem comparações com outros médicos
- Sem diagnóstico online
- Frase-âncora obrigatória em todos os posts

## Limites do Instagram

- Máximo 10 imagens por carrossel
- Caption: máximo 2200 caracteres
- Rate limit: 25 posts publicados via API por 24 horas
