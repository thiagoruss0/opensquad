---
execution: inline
agent: squads/instagram-carousel/agents/publicador
inputFile: squads/instagram-carousel/output/slides/rendered/manifest.json
outputFile: squads/instagram-carousel/output/publish-report.md
---

# Step 11: Publicação no Instagram

## Context Loading

Load these files before executing:
- `squads/instagram-carousel/output/slides/rendered/manifest.json` — Image files and metadata
- `squads/instagram-carousel/output/carousel-draft.md` — Caption and hashtags
- `squads/instagram-carousel/output/review-result.md` — Must be APPROVE or user override

## Instructions

### Process

1. **Verify review status**: Read review-result.md. Only proceed if verdict is APPROVE or user explicitly overrode a REJECT in step-10.

2. **Load images** from manifest.json. Verify each file exists and is accessible.

3. **Validate platform requirements**:
   - Image format: JPEG (convert from PNG if needed)
   - Image count: 2-10 images (carousel requirement)
   - Image dimensions: 1080x1440px
   - Caption length: under 2,200 characters
   - Hashtags: present and reasonable (5)

4. **Present structured publish preview** to user:
   ```
   PUBLISH PREVIEW
   Platform: Instagram (carousel)
   Account: @drthiagorusso
   Images: N slides (slide-01.jpg through slide-NN.jpg)
   Caption: [first 200 chars]... (X / 2,200 chars)
   Hashtags: #tag1 #tag2 ... (N)
   Validation: All checks passed
   ```

5. **Execute dry-run** using instagram-publisher skill with `--dry-run` flag:
   - Verify credentials (token not expired)
   - Upload images to imgbb
   - Create media containers
   - Create carousel container
   - Skip final publish

6. **Report dry-run results**:
   ```
   DRY-RUN RESULT
   Credentials: Valid (expires YYYY-MM-DD)
   Image upload: N/N uploaded to imgbb
   Containers: N/N created
   Carousel: Created successfully
   Publish: Skipped (dry-run mode)
   ```

7. **Request final confirmation**: "Dry-run passed. Confirma publicação no Instagram?"

8. **Publish live** and report results:
   ```
   PUBLISH RESULT
   Published successfully
   Post URL: https://www.instagram.com/p/XXXXX/
   Post ID: 1789XXXXXXX
   Published: YYYY-MM-DD HH:MM:SS UTC
   Rate limit: X/25 posts used in last 24h
   ```

9. **Save publish report** to output/publish-report.md with all details.

## Output Format

```
PUBLISH REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Squad: instagram-carousel
Date: YYYY-MM-DD HH:MM:SS UTC

PREVIEW
  Platform: Instagram (carousel)
  Account: @drthiagorusso
  Images: N slides
  Caption: X / 2,200 chars
  Hashtags: N hashtags
  Validation: [passed/failed]

DRY-RUN
  Credentials: [valid/expired]
  Upload: [N/N]
  Containers: [N/N]
  Status: [passed/failed]

PUBLISH
  Status: [success/failed]
  Post URL: [URL]
  Post ID: [ID]
  Rate limit: [X/25]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Output Example

```
PUBLISH REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Squad: instagram-carousel
Date: 2026-03-18 15:42:30 UTC

PREVIEW
  Platform: Instagram (carousel)
  Account: @drthiagorusso
  Images: 7 slides
    1. slide-01.jpg (1080x1440, JPEG, 312KB)
    2. slide-02.jpg (1080x1440, JPEG, 195KB)
    3. slide-03.jpg (1080x1440, JPEG, 213KB)
    4. slide-04.jpg (1080x1440, JPEG, 178KB)
    5. slide-05.jpg (1080x1440, JPEG, 201KB)
    6. slide-06.jpg (1080x1440, JPEG, 192KB)
    7. slide-07.jpg (1080x1440, JPEG, 244KB)
  Caption: "Seus olhos estão tentando te avisar alguma coisa?..." (1,234 / 2,200 chars)
  Hashtags: #oftalmologista #saudeocular #glaucoma #cedoa #manaus (5)
  Validation: All checks passed

DRY-RUN
  Credentials: Valid (expires 2026-05-17)
  Upload: 7/7 images uploaded to imgbb
  Containers: 7/7 media containers created
  Carousel container: Created successfully
  Status: PASSED

PUBLISH
  Status: SUCCESS
  Post URL: https://www.instagram.com/p/ABC123xyz/
  Post ID: 17899506834567890
  Published: 2026-03-18 15:42:30 UTC
  Rate limit: 4/25 posts used in last 24h
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Veto Conditions

Reject and redo if ANY are true:
1. Publishing attempted without explicit user confirmation
2. Publishing attempted without successful dry-run
3. Success reported without post URL/permalink
4. Review-result.md shows REJECT without user override

## Quality Criteria

- [ ] User confirmation received before live publish
- [ ] Dry-run executed and passed before live publish
- [ ] All platform validations passed (format, dimensions, caption length)
- [ ] Structured preview presented with complete details
- [ ] Success report includes post URL, post ID, and timestamp
- [ ] Rate limit status reported
- [ ] Complete publish report saved to output/publish-report.md
