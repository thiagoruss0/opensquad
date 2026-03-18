#!/usr/bin/env node
// Instagram Carousel Publisher
// Usage:
//   node --env-file=.env publish.js --images "slide1.jpg,slide2.jpg" --caption "..." [--dry-run]
//   node --env-file=.env publish.js --dir ./slides/jpeg --caption-file caption.txt [--dry-run]
//   node --env-file=.env publish.js --dir ./slides/jpeg --caption "..." [--dry-run]

import { readFileSync, readdirSync, statSync } from 'node:fs';
import { resolve, join, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

// ── Argument parsing ──────────────────────────────────────────

export function parseArgs(argv) {
  const args = { images: [], caption: '', dryRun: false, dir: '' };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--images') {
      if (i + 1 < argv.length) args.images = argv[++i].split(',').map(s => s.trim());
    }
    else if (argv[i] === '--dir') {
      if (i + 1 < argv.length) args.dir = argv[++i];
    }
    else if (argv[i] === '--caption') {
      if (i + 1 < argv.length) args.caption = argv[++i];
    }
    else if (argv[i] === '--caption-file') {
      if (i + 1 < argv.length) args.caption = readFileSync(argv[++i], 'utf-8').trim();
    }
    else if (argv[i] === '--dry-run') args.dryRun = true;
  }

  // If --dir provided and no --images, scan directory for images
  if (args.dir && !args.images.length) {
    const dir = resolve(args.dir);
    const exts = ['.jpg', '.jpeg', '.png'];
    args.images = readdirSync(dir)
      .filter(f => exts.includes(extname(f).toLowerCase()))
      .sort()
      .map(f => join(dir, f));
  }

  return args;
}

// ── Image upload (imgbb) ──────────────────────────────────────

export async function uploadToImgbb(imagePath, apiKey) {
  const absolutePath = resolve(imagePath);
  const base64 = readFileSync(absolutePath).toString('base64');
  const body = new URLSearchParams({ image: base64 });
  const res = await fetch(`https://api.imgbb.com/1/upload?key=${apiKey}`, {
    method: 'POST',
    body,
  });
  if (!res.ok) throw new Error(`imgbb upload failed [${res.status}]: ${await res.text()}`);
  const json = await res.json();
  return json.data.url;
}

// ── Instagram Graph API ───────────────────────────────────────

const IG_BASE = 'https://graph.facebook.com/v21.0';

export async function createChildContainer(userId, imageUrl, accessToken) {
  const params = new URLSearchParams({
    image_url: imageUrl,
    is_carousel_item: 'true',
    access_token: accessToken,
  });
  const res = await fetch(`${IG_BASE}/${userId}/media?${params}`, { method: 'POST' });
  if (!res.ok) throw new Error(`createChildContainer failed [${res.status}]: ${await res.text()}`);
  return (await res.json()).id;
}

export async function createSingleContainer(userId, imageUrl, caption, accessToken) {
  const params = new URLSearchParams({
    image_url: imageUrl,
    caption,
    access_token: accessToken,
  });
  const res = await fetch(`${IG_BASE}/${userId}/media?${params}`, { method: 'POST' });
  if (!res.ok) throw new Error(`createSingleContainer failed [${res.status}]: ${await res.text()}`);
  return (await res.json()).id;
}

export async function getContainerStatus(containerId, accessToken) {
  const params = new URLSearchParams({ fields: 'status_code', access_token: accessToken });
  const res = await fetch(`${IG_BASE}/${containerId}?${params}`);
  if (!res.ok) throw new Error(`getContainerStatus failed [${res.status}]: ${await res.text()}`);
  return (await res.json()).status_code;
}

export async function pollUntilFinished(containerId, accessToken, timeoutMs = 60_000, intervalMs = 3_000) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const status = await getContainerStatus(containerId, accessToken);
    if (status === 'FINISHED') return;
    if (status === 'ERROR') throw new Error(`Container ${containerId} entered ERROR state`);
    await new Promise(r => setTimeout(r, intervalMs));
  }
  throw new Error(`Container ${containerId} timed out after ${timeoutMs}ms`);
}

export async function createCarouselContainer(userId, childIds, caption, accessToken) {
  const params = new URLSearchParams({
    media_type: 'CAROUSEL_ALBUM',
    children: childIds.join(','),
    caption,
    access_token: accessToken,
  });
  const res = await fetch(`${IG_BASE}/${userId}/media?${params}`, { method: 'POST' });
  if (!res.ok) throw new Error(`createCarouselContainer failed [${res.status}]: ${await res.text()}`);
  return (await res.json()).id;
}

export async function publishMedia(userId, containerId, accessToken) {
  const params = new URLSearchParams({ creation_id: containerId, access_token: accessToken });
  const res = await fetch(`${IG_BASE}/${userId}/media_publish?${params}`, { method: 'POST' });
  if (!res.ok) throw new Error(`publishMedia failed [${res.status}]: ${await res.text()}`);
  return (await res.json()).id;
}

export async function getPermalink(mediaId, accessToken) {
  const params = new URLSearchParams({ fields: 'permalink', access_token: accessToken });
  const res = await fetch(`${IG_BASE}/${mediaId}?${params}`);
  if (!res.ok) return null;
  const json = await res.json();
  return json.permalink ?? null;
}

// ── Main ──────────────────────────────────────────────────────

async function main() {
  const { images, caption, dryRun } = parseArgs(process.argv);

  if (!images.length) throw new Error('--images or --dir is required');
  if (!caption) throw new Error('--caption or --caption-file is required');
  if (images.length > 10) {
    throw new Error(`Instagram allows max 10 images per post (got ${images.length})`);
  }
  if (caption.length > 2200) {
    throw new Error(`Caption exceeds Instagram's 2200-character limit (got ${caption.length})`);
  }

  const { IMGBB_API_KEY, INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_USER_ID } = process.env;
  if (!IMGBB_API_KEY) throw new Error('IMGBB_API_KEY is not set in environment');
  if (!INSTAGRAM_ACCESS_TOKEN) throw new Error('INSTAGRAM_ACCESS_TOKEN is not set in environment');
  if (!INSTAGRAM_USER_ID) throw new Error('INSTAGRAM_USER_ID is not set in environment');

  // Validate images exist
  for (const img of images) {
    try { statSync(resolve(img)); } catch {
      throw new Error(`Image not found: ${img}`);
    }
  }

  const isSingle = images.length === 1;
  const postType = isSingle ? 'single image' : `carousel (${images.length} slides)`;

  console.log(`📸 Uploading ${images.length} image(s) to imgbb...`);
  const imageUrls = [];
  for (let i = 0; i < images.length; i++) {
    const url = await uploadToImgbb(images[i], IMGBB_API_KEY);
    imageUrls.push(url);
    console.log(`   [${i + 1}] ${url}`);
  }

  let containerId;

  if (isSingle) {
    // Single image post
    console.log('\n📦 Creating Instagram media container...');
    containerId = await createSingleContainer(INSTAGRAM_USER_ID, imageUrls[0], caption, INSTAGRAM_ACCESS_TOKEN);
    console.log(`   Container ID: ${containerId}`);

    console.log('\n⏳ Waiting for container to process...');
    await pollUntilFinished(containerId, INSTAGRAM_ACCESS_TOKEN);
    console.log('   Container ready.');
  } else {
    // Carousel post (2-10 images)
    console.log('\n📦 Creating Instagram media containers...');
    const childIds = [];
    for (const url of imageUrls) {
      const id = await createChildContainer(INSTAGRAM_USER_ID, url, INSTAGRAM_ACCESS_TOKEN);
      childIds.push(id);
    }
    console.log(`   Container IDs: ${childIds.join(', ')}`);

    console.log('\n⏳ Waiting for containers to finish processing...');
    await Promise.all(childIds.map(id => pollUntilFinished(id, INSTAGRAM_ACCESS_TOKEN)));
    console.log('   All containers ready.');

    console.log('\n🎠 Creating carousel container...');
    containerId = await createCarouselContainer(
      INSTAGRAM_USER_ID, childIds, caption, INSTAGRAM_ACCESS_TOKEN
    );
    await pollUntilFinished(containerId, INSTAGRAM_ACCESS_TOKEN);
    console.log(`   Carousel container ID: ${containerId}`);
  }

  if (dryRun) {
    console.log(`\n✅ DRY RUN complete — ${postType} ready but not published.`);
    console.log(`   Container: ${containerId}`);
    return;
  }

  console.log('\n🚀 Publishing to Instagram...');
  const postId = await publishMedia(INSTAGRAM_USER_ID, containerId, INSTAGRAM_ACCESS_TOKEN);
  const permalink = await getPermalink(postId, INSTAGRAM_ACCESS_TOKEN);
  console.log(`\n✅ Published successfully!`);
  console.log(`   Type: ${postType}`);
  console.log(`   Post ID: ${postId}`);
  if (permalink) console.log(`   URL: ${permalink}`);
}

// Run only when executed directly (not when imported for tests)
const isMain = process.argv[1] === fileURLToPath(import.meta.url);
if (isMain) {
  main().catch(err => {
    console.error(`\n❌ ${err.message}`);
    process.exit(1);
  });
}
