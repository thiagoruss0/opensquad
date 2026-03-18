---
execution: inline
agent: squads/instagram-carousel/agents/designer
inputFile: squads/instagram-carousel/output/carousel-draft.md
outputFile: squads/instagram-carousel/output/slides/rendered/manifest.json
---

## Context Loading

Load the following files before executing:

- `squads/instagram-carousel/output/carousel-draft.md` — Approved carousel content
- `_opensquad/_memory/company.md` — Brand identity (CEDOA, colors, logo)
- `squads/instagram-carousel/pipeline/data/domain-framework.md` — Design guidelines and specifications

## Instructions

### Process

1. **Define the design system** based on CEDOA brand identity:
   - Primary colors from company.md (brand palette)
   - Typography: sans-serif stack — Inter or Montserrat (clean, modern, medical)
   - Font sizes: headline 48-64px, subheadline 32-40px, body 24-28px, caption 18-20px
   - Spacing: 80px margins, 40px padding between elements
   - Grid: centered single-column layout, 1080x1440px (Instagram portrait)
   - Visual elements: subtle gradient backgrounds, rounded containers, medical iconography

2. **Create slide-01.html** (cover/hook slide):
   - Apply the full design system
   - Headline prominently centered
   - Subtitle/supporting text below
   - Brand watermark (CEDOA or @drthiagorusso) in footer
   - Background treatment (gradient, pattern, or solid from palette)

3. **Start HTTP server, render, and verify:**
   - Start a local HTTP server (e.g., `python -m http.server 8080`)
   - Navigate browser to `http://localhost:8080/slide-01.html`
   - Resize viewport to 1080x1440
   - Take screenshot to verify visual quality
   - Check: text readability, alignment, brand consistency, contrast

4. **If slide 1 looks good, generate remaining slides:**
   - Create slide-02.html through slide-NN.html using the same design system
   - Maintain visual consistency (same fonts, colors, spacing)
   - Vary background slightly per slide (alternating shades, subtle variation)
   - Ensure last slide (CTA) has distinct visual treatment (stronger color, emphasis)

5. **Batch render all slides to PNG:**
   - Screenshot each slide at 1080x1440
   - Save to `squads/instagram-carousel/output/slides/rendered/slide-01.png` etc.
   - Verify each rendered image for quality

6. **Create manifest.json** listing all rendered images:

```json
{
  "carousel_id": "[generated-id]",
  "created_at": "[timestamp]",
  "total_slides": N,
  "dimensions": { "width": 1080, "height": 1440 },
  "slides": [
    {
      "slide_number": 1,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-01.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 0,
      "type": "cover"
    }
  ]
}
```

## Output Format

The output is `manifest.json` with the following structure:

```json
{
  "carousel_id": "string",
  "created_at": "ISO 8601 timestamp",
  "total_slides": "number",
  "dimensions": { "width": 1080, "height": 1440 },
  "format": "PNG",
  "design_system": {
    "primary_color": "string",
    "secondary_color": "string",
    "font_family": "string",
    "headline_size": "string",
    "body_size": "string"
  },
  "slides": [
    {
      "slide_number": "number",
      "path": "string",
      "width": 1080,
      "height": 1440,
      "size_bytes": "number",
      "type": "cover | content | cta"
    }
  ]
}
```

## Output Example

```json
{
  "carousel_id": "glaucoma-prevencao-20260318",
  "created_at": "2026-03-18T14:30:00-04:00",
  "total_slides": 9,
  "dimensions": { "width": 1080, "height": 1440 },
  "format": "PNG",
  "design_system": {
    "primary_color": "#0D5C63",
    "secondary_color": "#00B4D8",
    "background_color": "#F0F7F8",
    "accent_color": "#FF6B35",
    "font_family": "Inter, sans-serif",
    "headline_size": "56px",
    "body_size": "26px"
  },
  "slides": [
    {
      "slide_number": 1,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-01.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 245780,
      "type": "cover"
    },
    {
      "slide_number": 2,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-02.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 198340,
      "type": "content"
    },
    {
      "slide_number": 3,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-03.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 201450,
      "type": "content"
    },
    {
      "slide_number": 4,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-04.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 195600,
      "type": "content"
    },
    {
      "slide_number": 5,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-05.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 210890,
      "type": "content"
    },
    {
      "slide_number": 6,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-06.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 189230,
      "type": "content"
    },
    {
      "slide_number": 7,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-07.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 203100,
      "type": "content"
    },
    {
      "slide_number": 8,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-08.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 197560,
      "type": "content"
    },
    {
      "slide_number": 9,
      "path": "squads/instagram-carousel/output/slides/rendered/slide-09.png",
      "width": 1080,
      "height": 1440,
      "size_bytes": 256890,
      "type": "cta"
    }
  ]
}
```

## Veto Conditions

- **REJECT** if any text is below minimum readable font size (24px for body text)
- **REJECT** if contrast ratio between text and background is below 4.5:1 (WCAG AA)
- **REJECT** if design system is inconsistent across slides (different fonts, colors, or spacing)
- **REJECT** if any text is clipped, overflowing, or cut off at edges
- **REJECT** if slides are not exactly 1080x1440 pixels
- **REJECT** if brand elements (logo, handle, colors) are missing or incorrect

## Quality Criteria

- Design is clean, modern, and appropriate for a medical professional
- Typography hierarchy is clear (headline > subheadline > body)
- Color palette is cohesive and brand-consistent
- White space is used effectively (not cramped, not empty)
- Each slide is visually scannable in under 3 seconds
- CTA slide stands out from content slides
- All text is fully legible at mobile viewing size
- Visual consistency creates a polished, professional carousel
