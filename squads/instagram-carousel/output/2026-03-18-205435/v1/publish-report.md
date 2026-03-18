# Publish Report — DMRI Seca: 5 Fatos

**Carousel ID:** dmri-seca-5fatos-20260318
**Date:** 2026-03-18
**Status:** BLOCKED — Egress policy prevents Graph API calls from this environment

---

## Validation Results

| Check | Status |
|-------|--------|
| Image format (JPEG) | PASS |
| Image dimensions (1080x1440) | PASS |
| Image count (9, within 2-10) | PASS |
| File sizes (all < 8MB) | PASS |
| Caption length (1,163 / 2,200 max) | PASS |
| Hashtags (5 / 30 max) | PASS |
| imgbb upload | PASS — all 9 images uploaded |
| Instagram Graph API | BLOCKED — egress policy |

## imgbb URLs (valid for 10 minutes)

1. https://i.ibb.co/zTqcnB1f/slide-01.jpg
2. https://i.ibb.co/WwZ3DWV/slide-02.jpg
3. https://i.ibb.co/jPZ8jTZF/slide-03.jpg
4. https://i.ibb.co/qF3Vh7N1/slide-04.jpg
5. https://i.ibb.co/DHxNLTV2/slide-05.jpg
6. https://i.ibb.co/mVQt3LbS/slide-06.jpg
7. https://i.ibb.co/qYZ96hh4/slide-07.jpg
8. https://i.ibb.co/j9RhfyYH/slide-08.jpg
9. https://i.ibb.co/Jjkp8S4B/slide-09.jpg

## To Publish Locally

Run from your local machine (with network access to graph.facebook.com):

```bash
cd opensquad
python3 squads/instagram-carousel/output/2026-03-18-205435/v1/publish.py
```

Or use the Node.js publisher:

```bash
node --env-file=.env skills/instagram-publisher/scripts/publish.js \
  --images "squads/instagram-carousel/output/2026-03-18-205435/v1/slides/rendered/jpeg/slide-01.jpg,slide-02.jpg,...,slide-09.jpg" \
  --caption "..."
```

## Files Ready

- **JPEG slides:** `squads/instagram-carousel/output/2026-03-18-205435/v1/slides/rendered/jpeg/slide-01.jpg` ... `slide-09.jpg`
- **Caption + Hashtags:** `squads/instagram-carousel/output/2026-03-18-205435/v1/carousel-draft.md`
- **Publish script:** `squads/instagram-carousel/output/2026-03-18-205435/v1/publish.py`
