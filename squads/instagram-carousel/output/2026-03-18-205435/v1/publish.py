#!/usr/bin/env python3
"""Instagram Carousel Publisher via curl subprocess calls."""
import subprocess, json, time, sys, os

IMGBB_KEY = "a85aca5816f0b6885e9fea5cba269f6b"
IG_TOKEN = os.environ.get("INSTAGRAM_ACCESS_TOKEN", "")
IG_USER = os.environ.get("INSTAGRAM_USER_ID", "")
IG_BASE = "https://graph.facebook.com/v21.0"
JPEG_DIR = "squads/instagram-carousel/output/2026-03-18-205435/v1/slides/rendered/jpeg"
DRY_RUN = "--dry-run" in sys.argv

CAPTION = """O que é DMRI seca? 90% das pessoas não sabem — e ela é a forma mais comum de degeneração macular.

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

#dmri #saudeocular #oftalmologista #cedoamanaus #degeneracaomacular"""

def curl_post(url, form_data=None, data=None):
    cmd = ["curl", "-s", "--max-time", "60", "-X", "POST", url]
    if form_data:
        for k, v in form_data:
            cmd += ["--form", f"{k}={v}"]
    if data:
        for k, v in data:
            cmd += ["--data-urlencode", f"{k}={v}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return json.loads(result.stdout)

def curl_get(url, params):
    qs = "&".join(f"{k}={v}" for k, v in params)
    full = f"{url}?{qs}"
    result = subprocess.run(["curl", "-s", "--max-time", "30", full], capture_output=True, text=True)
    return json.loads(result.stdout)

# Step 1: Upload images
print("📸 Uploading 9 images to imgbb...")
image_urls = []
for i in range(1, 10):
    filepath = f"{JPEG_DIR}/slide-{i:02d}.jpg"
    resp = curl_post("https://api.imgbb.com/1/upload", form_data=[
        ("key", IMGBB_KEY),
        ("image", f"@{filepath}"),
        ("expiration", "600"),
    ])
    url = resp["data"]["url"]
    image_urls.append(url)
    print(f"   [{i}] {url}")

# Step 2: Create child containers
print("\n📦 Creating Instagram media containers...")
child_ids = []
for url in image_urls:
    resp = curl_post(f"{IG_BASE}/{IG_USER}/media", data=[
        ("image_url", url),
        ("is_carousel_item", "true"),
        ("access_token", IG_TOKEN),
    ])
    if "id" not in resp:
        print(f"   ERROR: {resp}")
        sys.exit(1)
    child_ids.append(resp["id"])
print(f"   Container IDs: {', '.join(child_ids)}")

# Step 3: Poll containers
print("\n⏳ Waiting for containers to process...")
for cid in child_ids:
    for _ in range(20):
        resp = curl_get(f"{IG_BASE}/{cid}", [("fields", "status_code"), ("access_token", IG_TOKEN)])
        status = resp.get("status_code", "UNKNOWN")
        if status == "FINISHED":
            break
        if status == "ERROR":
            print(f"   ERROR on container {cid}")
            sys.exit(1)
        time.sleep(3)
print("   All containers ready.")

# Step 4: Create carousel
print("\n🎠 Creating carousel container...")
children_csv = ",".join(child_ids)
resp = curl_post(f"{IG_BASE}/{IG_USER}/media", data=[
    ("media_type", "CAROUSEL_ALBUM"),
    ("children", children_csv),
    ("caption", CAPTION),
    ("access_token", IG_TOKEN),
])
if "id" not in resp:
    print(f"   ERROR: {resp}")
    sys.exit(1)
carousel_id = resp["id"]
print(f"   Carousel ID: {carousel_id}")

# Poll carousel
for _ in range(20):
    resp = curl_get(f"{IG_BASE}/{carousel_id}", [("fields", "status_code"), ("access_token", IG_TOKEN)])
    if resp.get("status_code") == "FINISHED":
        break
    time.sleep(3)

if DRY_RUN:
    print("\n✅ DRY RUN complete — carousel ready but not published.")
    print(f"   Carousel container: {carousel_id}")
    sys.exit(0)

# Step 5: Publish
print("\n🚀 Publishing to Instagram...")
resp = curl_post(f"{IG_BASE}/{IG_USER}/media_publish", data=[
    ("creation_id", carousel_id),
    ("access_token", IG_TOKEN),
])
if "id" not in resp:
    print(f"   ERROR: {resp}")
    sys.exit(1)
post_id = resp["id"]

# Get permalink
resp = curl_get(f"{IG_BASE}/{post_id}", [("fields", "permalink"), ("access_token", IG_TOKEN)])
permalink = resp.get("permalink", "N/A")

print(f"\n✅ Published successfully!")
print(f"   Post ID: {post_id}")
print(f"   URL: {permalink}")
