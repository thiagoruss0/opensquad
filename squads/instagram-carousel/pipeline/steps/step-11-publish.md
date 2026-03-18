---
execution: inline
agent: squads/instagram-carousel/agents/publicador
inputFile: squads/instagram-carousel/output/slides/rendered/manifest.json
outputFile: squads/instagram-carousel/output/publish-report.md
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/slides/rendered/manifest.json` — Rendered slide images and paths
- `squads/instagram-carousel/output/carousel-draft.md` — Caption and hashtags
- `squads/instagram-carousel/output/review-result.md` — Must be APPROVE or user override

## Instructions

### Process

1. **Validate all images** from manifest.json:
   - Format: JPEG or PNG (convert to JPEG if needed for Instagram)
   - Dimensions: 1080x1440 pixels (Instagram portrait ratio 4:5)
   - Count: between 2 and 10 images (Instagram carousel limits)
   - File size: each under 8MB
   - All files exist and are readable

2. **Validate caption** from carousel-draft.md:
   - Total length under 2200 characters
   - Hashtags present (max 30, recommended 5)
   - No broken formatting or encoding issues
   - Hook visible in first 125 characters

3. **Present structured publish preview** to user:
   - Number of slides
   - Caption preview (first 125 chars + full)
   - Hashtags
   - Account: @drthiagorusso
   - Estimated publish time

4. **Execute dry-run first** (--dry-run flag):
   - Simulate the full publish flow without actually posting
   - Validate API authentication
   - Validate image upload capability
   - Validate caption formatting
   - Report any errors or warnings

5. **Report dry-run results** and request final confirmation:
   - Show dry-run status (PASS / FAIL)
   - If FAIL: show errors and stop
   - If PASS: ask user for final "Publicar agora?" confirmation

6. **Publish live** via instagram-publisher skill:
   - Upload all slides in order
   - Set caption with hashtags
   - Publish as carousel post
   - Wait for confirmation from API

7. **Report results:**
   - Post URL (permalink)
   - Post ID
   - Timestamp of publication
   - Rate limit status (remaining calls)
   - Any warnings

8. **Save complete publish report** to `output/publish-report.md`.

## Output Format

```markdown
# Publish Report

**Status:** [SUCCESS / FAILED]
**Date:** [timestamp]
**Account:** @drthiagorusso

## PREVIEW

- Slides: [N] images ([format], [dimensions])
- Caption: [character count] characters
- Hashtags: [count] hashtags
- Account: @drthiagorusso

## DRY-RUN RESULT

- Status: [PASS / FAIL]
- Authentication: [OK / FAILED]
- Image validation: [OK / FAILED - details]
- Caption validation: [OK / FAILED - details]
- Errors: [none / list of errors]
- Warnings: [none / list of warnings]

## PUBLISH RESULT

- Status: [SUCCESS / FAILED]
- Post URL: [permalink]
- Post ID: [id]
- Published at: [ISO timestamp]
- Rate limit: [remaining]/[total] calls
- Errors: [none / details]

## SUMMARY

[1-2 sentence summary of the publish outcome]
```

## Output Example

```markdown
# Publish Report

**Status:** SUCCESS
**Date:** 2026-03-18T15:45:00-04:00
**Account:** @drthiagorusso

## PREVIEW

- Slides: 9 images (JPEG, 1080x1440)
- Caption: 1847 characters
- Hashtags: 5 hashtags (#glaucoma #saudeocular #oftalmologia #prevencao #cedoamanaus)
- Account: @drthiagorusso

## DRY-RUN RESULT

- Status: PASS
- Authentication: OK (token valid until 2026-04-17)
- Image validation: OK (9 images, all JPEG, all 1080x1440, largest 256KB)
- Caption validation: OK (1847/2200 chars, hook in first 125 chars, 5 hashtags)
- Errors: none
- Warnings: none

## PUBLISH RESULT

- Status: SUCCESS
- Post URL: https://www.instagram.com/p/ABC123xyz/
- Post ID: 17890012345678901
- Published at: 2026-03-18T15:45:12-04:00
- Rate limit: 187/200 calls remaining (resets in 58 minutes)
- Errors: none

## SUMMARY

Carrossel "5 fatos sobre glaucoma que surpreendem" publicado com sucesso na conta @drthiagorusso. 9 slides em formato 1080x1440, caption com 1847 caracteres. Post disponivel em https://www.instagram.com/p/ABC123xyz/.
```

## Veto Conditions

- **REJECT** if publication is attempted without explicit user confirmation
- **REJECT** if publication is attempted without a successful dry-run first
- **REJECT** if the publish report does not include the post URL on success
- **REJECT** if images fail validation (wrong dimensions, too large, wrong format) and publish proceeds anyway
- **REJECT** if caption exceeds 2200 characters and publish proceeds
- **REJECT** if review-result.md shows REJECT and there is no user override on record

## Quality Criteria

- All validations run before any publish attempt
- Dry-run catches issues before live publish
- User has explicit final confirmation opportunity
- Publish report is complete with all fields populated
- Error handling is graceful (failures reported clearly, no silent errors)
- Rate limit is tracked and reported to avoid API throttling
- Post URL is verified accessible after publish
