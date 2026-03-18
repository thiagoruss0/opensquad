---
type: checkpoint
---

# Step 10: Aprovação Final

## Checkpoint: Revisar resultado da revisão e aprovar para publicação

Apresente o resultado da revisão de qualidade e o carrossel final ao usuário.

### Se o resultado for APPROVE:

> "O carrossel foi aprovado pela revisora com nota X.X/10.
>
> Resumo da revisão:
> [Scoring table resumida]
>
> Sugestões opcionais:
> [Lista de sugestões non-blocking]
>
> Deseja publicar no Instagram?"
>
> 1. Publicar — prosseguir para publicação via Graph API
> 2. Aplicar sugestões — incorporar melhorias antes de publicar
> 3. Cancelar — não publicar agora

### Se o resultado for REJECT:

> "O carrossel foi rejeitado pela revisora com nota X.X/10.
>
> Problemas encontrados:
> [Lista de required changes]
>
> Caminho para aprovação:
> [Path to approval steps]
>
> O que deseja fazer?"
>
> 1. Corrigir e reenviar — voltar ao step-06 com as correções
> 2. Ignorar revisão e publicar — override manual (não recomendado)
> 3. Cancelar — descartar este carrossel

### Se o resultado for CONDITIONAL APPROVE:

> "O carrossel foi aprovado com condições (nota X.X/10).
>
> Correções menores necessárias:
> [Lista de ajustes]
>
> 1. Aplicar correções e publicar
> 2. Publicar sem correções
> 3. Cancelar"
