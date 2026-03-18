---
name: instagram-publisher
description: >
  Publishes Instagram posts (single image or carousel) from local images.
  Uploads images to imgbb for temporary public hosting, creates Instagram
  media containers via the Graph API, and publishes the post.
  Supports 1-10 images per post and retrieves the real post permalink.
  Works standalone (Claude/cowork) or inside Opensquad pipelines.
description_pt-BR: >
  Publica posts no Instagram (imagem única ou carrossel) a partir de imagens locais.
  Faz upload das imagens para o imgbb como hospedagem pública temporária,
  cria containers de mídia via Graph API e publica o post.
  Suporta de 1 a 10 imagens por post e obtém o permalink real.
  Funciona standalone (Claude/cowork) ou dentro de pipelines Opensquad.
description_es: >
  Publica posts en Instagram (imagen individual o carrusel) a partir de imágenes locales.
  Sube las imágenes a imgbb como hosting público temporal, crea
  contenedores de medios vía Graph API y publica el post.
  Soporta de 1 a 10 imágenes por post y obtiene el permalink real.
  Funciona standalone (Claude/cowork) o dentro de pipelines Opensquad.
type: script
version: "2.0.0"
script:
  path: scripts/publish.js
  runtime: node
  invoke: "node --env-file=.env {skill_path}/scripts/publish.js"
env:
  - INSTAGRAM_ACCESS_TOKEN
  - INSTAGRAM_USER_ID
  - IMGBB_API_KEY
categories: [social-media, publishing, instagram]
---

# Instagram Publisher

Skill para publicar posts no Instagram (imagem única ou carrossel) direto do terminal.

Funciona em qualquer contexto:
- **Standalone** — direto no Claude Code ou cowork, sem precisar de squad
- **Pipeline** — dentro de squads Opensquad como etapa de publicação

## Uso Rápido (Standalone)

### Publicar carrossel (2-10 imagens)

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --dir ./path/to/jpeg/folder \
  --caption "Sua caption aqui com #hashtags" \
  --dry-run
```

### Publicar imagem única

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --images "foto.jpg" \
  --caption "Sua caption aqui"
```

### Usando arquivo de caption

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --dir ./slides \
  --caption-file caption.txt
```

## Parâmetros

| Parâmetro | Descrição |
|-----------|-----------|
| `--images "a.jpg,b.jpg"` | Lista de imagens separadas por vírgula |
| `--dir ./pasta` | Pasta com imagens (JPG/PNG, ordem alfabética) |
| `--caption "texto"` | Caption do post (inline) |
| `--caption-file arquivo.txt` | Caption do post (de arquivo) |
| `--dry-run` | Testa tudo sem publicar de verdade |

**Regras:**
- Use `--images` OU `--dir` (não ambos)
- Use `--caption` OU `--caption-file` (não ambos)
- 1 imagem = post único; 2-10 imagens = carrossel
- Caption máx 2200 caracteres
- Recomendado: 5 hashtags

## Instruções para o Agente

Quando o usuário pedir para publicar no Instagram, siga este fluxo:

### 1. Localizar Imagens

Pergunte ou identifique onde estão as imagens:
- Se dentro de um squad: `squads/{nome}/output/slides/rendered/jpeg/`
- Se standalone: pergunte o caminho ou use o diretório atual

Verifique:
- Formato: JPEG ou PNG
- Quantidade: 1-10 imagens
- Tamanho: cada uma menor que 8MB

### 2. Obter Caption

Se o usuário não forneceu a caption:
- Procure por `carousel-draft.md` ou `caption.txt` no diretório de output
- Ou peça ao usuário

Verifique:
- Máximo 2200 caracteres
- Hook nos primeiros 125 caracteres
- Hashtags presentes

### 3. Apresentar Preview

Antes de qualquer ação, mostre ao usuário:

```
📱 PREVIEW

Tipo: Carrossel (N slides) / Imagem única
Imagens: lista dos arquivos
Caption (X/2200 chars):
"[primeiros 200 chars]..."
Hashtags: #tag1 #tag2 ...

Publicar? (dry-run primeiro / publicar direto / cancelar)
```

### 4. Dry-Run (Recomendado)

Execute com `--dry-run` primeiro:

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --dir "{caminho}" \
  --caption "{caption}" \
  --dry-run
```

Se passar: pergunte se quer publicar de verdade.
Se falhar: mostre o erro e sugira correção.

### 5. Publicar

Somente após confirmação explícita do usuário, execute sem `--dry-run`:

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --dir "{caminho}" \
  --caption "{caption}"
```

### 6. Reportar Resultado

No sucesso, mostre:
- Post URL (permalink)
- Post ID
- Tipo (carrossel / imagem única)
- Número de slides

No erro, mostre:
- Mensagem de erro
- Sugestão de correção

## Validações

| Check | Regra |
|-------|-------|
| Formato | JPEG ou PNG |
| Quantidade | 1-10 imagens |
| Tamanho arquivo | < 8MB cada |
| Caption | < 2200 caracteres |
| Hashtags | Máximo 30 (recomendado 5) |
| Env vars | IMGBB_API_KEY, INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID |

## Constraints

- **Nunca publique sem confirmação explícita do usuário**
- **Sempre faça dry-run antes da publicação real** (a menos que o usuário peça para pular)
- Conta Instagram Business obrigatória (não funciona com Personal ou Creator)
- Rate limit: 25 posts publicados via API por 24 horas
- Imagens no imgbb expiram — não reutilize URLs antigas

## Setup (primeira vez)

Configure as 3 variáveis no arquivo `.env`:

```
IMGBB_API_KEY=
INSTAGRAM_ACCESS_TOKEN=
INSTAGRAM_USER_ID=
```

### IMGBB_API_KEY

1. Acesse [https://api.imgbb.com/](https://api.imgbb.com/)
2. Clique em **"Get API Key"** e crie uma conta gratuita (sem cartão de crédito)
3. Após o login, sua chave aparece na própria página inicial
4. Copie e cole em `.env`

### INSTAGRAM_ACCESS_TOKEN

Pré-requisito: conta Instagram Business conectada a uma Página do Facebook, e um app criado em [developers.facebook.com](https://developers.facebook.com/) (tipo: **Empresa**).

**Para obter um token de longa duração (válido 60 dias):**

1. Acesse seu app → **Graph API Explorer**
2. No dropdown do topo, selecione seu app
3. Clique em **"Gerar token de acesso"**
4. Ative as permissões:
   - `instagram_content_publish`
   - `instagram_basic`
   - `pages_read_engagement`
5. Clique em **"Gerar token de acesso"** e autorize — você receberá um token de curta duração (1h)
6. Converta para longa duração (60 dias) com este GET:
   ```
   https://graph.facebook.com/oauth/access_token
     ?grant_type=fb_exchange_token
     &client_id={APP_ID}
     &client_secret={APP_SECRET}
     &fb_exchange_token={TOKEN_CURTO}
   ```
   _(APP_ID e APP_SECRET: seu app → Configurações → Básico)_
7. Copie o `access_token` da resposta e cole em `.env`

> O token expira em 60 dias. Repita o processo para renovar.

### INSTAGRAM_USER_ID

1. No Graph API Explorer (com o token acima), faça GET em:
   ```
   /me/accounts
   ```
2. Localize sua **Página do Facebook** na resposta e anote o `id`
3. Faça GET em:
   ```
   /{page-id}?fields=instagram_business_account
   ```
4. Copie o `id` dentro de `instagram_business_account` — esse é o seu User ID

## Operações Disponíveis

- **Publish Carousel** — Upload de 2-10 imagens e publicação como carrossel
- **Publish Single** — Upload de 1 imagem e publicação como post único
- **Dry Run** — Testa o fluxo completo sem publicar (use `--dry-run`)
- **Image Upload** — Upload de imagens locais para o imgbb
- **Status Check** — Monitora o status dos containers antes de publicar
