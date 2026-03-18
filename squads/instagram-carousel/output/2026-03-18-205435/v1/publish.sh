#!/bin/bash
# Instagram Carousel Publisher (curl-based)
set -euo pipefail

source .env

IMGBB_KEY="$IMGBB_API_KEY"
IG_TOKEN="$INSTAGRAM_ACCESS_TOKEN"
IG_USER="$INSTAGRAM_USER_ID"
IG_BASE="https://graph.facebook.com/v21.0"
JPEG_DIR="squads/instagram-carousel/output/2026-03-18-205435/v1/slides/rendered/jpeg"
DRY_RUN="${1:-}"

CAPTION='O que é DMRI seca? 90% das pessoas não sabem — e ela é a forma mais comum de degeneração macular.

A DMRI seca representa 9 em cada 10 casos de degeneração macular relacionada à idade. No Brasil, 3 milhões de pessoas convivem com essa condição.

Ela não dói. Não dá sintomas claros no início. E não tem cura.

Mas tem como retardar a progressão. E quanto mais cedo você descobre, mais visão preserva.

Nesse carrossel, reuni 5 fatos atualizados sobre a DMRI seca que podem mudar a forma como você cuida dos seus olhos:

- 90% dos casos de DMRI são da forma seca
- Suplementação AREDS retarda a progressão (não é qualquer vitamina)
- A visão central é afetada, mas a periférica é preservada
- Fotobiomodulação (luz, sem agulha) foi aprovada em 2024
- O teste de Amsler detecta mudanças em 30 segundos, em casa

Conhecimento é a melhor prevenção. Salve para consultar depois e mande para quem precisa saber.

Se faz tempo que você não fez um exame completo, agende sua avaliação. Link na bio.

Dr. Thiago Russo — CRM/AM
Oftalmologista — CEDOA Manaus

#dmri #saudeocular #oftalmologista #cedoamanaus #degeneracaomacular'

# Step 1: Upload images to imgbb
echo "📸 Uploading 9 images to imgbb..."
IMAGE_URLS=()
for i in $(seq -w 1 9); do
  FILE="$JPEG_DIR/slide-${i}.jpg"
  RESP=$(curl -s -X POST "https://api.imgbb.com/1/upload" \
    --form "key=$IMGBB_KEY" \
    --form "image=@$FILE" \
    --form "expiration=600")
  URL=$(echo "$RESP" | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['url'])")
  IMAGE_URLS+=("$URL")
  echo "   [$i] $URL"
done

# Step 2: Create child containers
echo ""
echo "📦 Creating Instagram media containers..."
CHILD_IDS=()
for URL in "${IMAGE_URLS[@]}"; do
  RESP=$(curl -s -X POST "$IG_BASE/$IG_USER/media" \
    --data-urlencode "image_url=$URL" \
    --data-urlencode "is_carousel_item=true" \
    --data-urlencode "access_token=$IG_TOKEN")
  CID=$(echo "$RESP" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
  CHILD_IDS+=("$CID")
done
echo "   Container IDs: ${CHILD_IDS[*]}"

# Step 3: Wait for containers
echo ""
echo "⏳ Waiting for containers to process..."
for CID in "${CHILD_IDS[@]}"; do
  for attempt in $(seq 1 20); do
    STATUS=$(curl -s "$IG_BASE/$CID?fields=status_code&access_token=$IG_TOKEN" | python3 -c "import sys,json; print(json.load(sys.stdin).get('status_code','UNKNOWN'))")
    if [ "$STATUS" = "FINISHED" ]; then break; fi
    if [ "$STATUS" = "ERROR" ]; then echo "   ERROR on container $CID"; exit 1; fi
    sleep 3
  done
done
echo "   All containers ready."

# Step 4: Create carousel
echo ""
echo "🎠 Creating carousel container..."
CHILDREN_CSV=$(IFS=,; echo "${CHILD_IDS[*]}")
RESP=$(curl -s -X POST "$IG_BASE/$IG_USER/media" \
  --data-urlencode "media_type=CAROUSEL_ALBUM" \
  --data-urlencode "children=$CHILDREN_CSV" \
  --data-urlencode "caption=$CAPTION" \
  --data-urlencode "access_token=$IG_TOKEN")
CAROUSEL_ID=$(echo "$RESP" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
echo "   Carousel ID: $CAROUSEL_ID"

# Wait for carousel
for attempt in $(seq 1 20); do
  STATUS=$(curl -s "$IG_BASE/$CAROUSEL_ID?fields=status_code&access_token=$IG_TOKEN" | python3 -c "import sys,json; print(json.load(sys.stdin).get('status_code','UNKNOWN'))")
  if [ "$STATUS" = "FINISHED" ]; then break; fi
  sleep 3
done

if [ "$DRY_RUN" = "--dry-run" ]; then
  echo ""
  echo "✅ DRY RUN complete — carousel ready but not published."
  echo "   Carousel container: $CAROUSEL_ID"
  exit 0
fi

# Step 5: Publish
echo ""
echo "🚀 Publishing to Instagram..."
RESP=$(curl -s -X POST "$IG_BASE/$IG_USER/media_publish" \
  --data-urlencode "creation_id=$CAROUSEL_ID" \
  --data-urlencode "access_token=$IG_TOKEN")
POST_ID=$(echo "$RESP" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Get permalink
PERMALINK=$(curl -s "$IG_BASE/$POST_ID?fields=permalink&access_token=$IG_TOKEN" | python3 -c "import sys,json; print(json.load(sys.stdin).get('permalink','N/A'))")

echo ""
echo "✅ Published successfully!"
echo "   Post ID: $POST_ID"
echo "   URL: $PERMALINK"
