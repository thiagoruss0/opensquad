---
task: "Render Carousel Slides"
order: 2
input:
  - design-system.yaml
  - carousel-draft.md
output: manifest.json
---

## Process

1. **Build Cover Slide HTML**: Create `slide-01.html` applying the design system. Fully self-contained: all CSS inline in `<style>`, no external resources except Google Fonts `@import`. Body set to `width: 1080px; height: 1440px; overflow: hidden; margin: 0`. Include hook text (Hero typography), brand name, topic indicator, and slide counter.

2. **Render and Verify Cover**: Start local HTTP server, navigate Playwright browser to the file, resize viewport to 1080x1440px, screenshot. Verify: no text clipping, correct font sizes and colors, proper margins, safe zones respected. Fix issues before proceeding.

3. **Generate Remaining Slides**: Once cover passes, create `slide-02.html` through `slide-NN.html`. Each uses the same design system with consistent header placement, fonts, spacing, and colors. Content slides use Heading/Body typography. CTA slide emphasizes accent color.

4. **Batch Render All Slides**: Screenshot each HTML at 1080x1440px viewport. Save as PNG (`slide-01.png`, `slide-02.png`, etc.). Verify exact dimensions on each output.

5. **Create Manifest**: Generate `manifest.json` with all slide metadata — file paths, dimensions, file sizes, roles (cover/content/cta), and rendering status.

## Output Format

```json
{
  "carousel_id": "<identifier>",
  "total_slides": 0,
  "viewport": { "width": 1080, "height": 1440 },
  "slides": [
    {
      "index": 1,
      "file": "slide-01.png",
      "html_source": "slide-01.html",
      "role": "cover|content|cta",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 0,
      "status": "rendered|failed"
    }
  ]
}
```

## Output Example

```json
{
  "carousel_id": "cedoa-glaucoma-2026-03-18",
  "total_slides": 7,
  "viewport": { "width": 1080, "height": 1440 },
  "slides": [
    { "index": 1, "file": "slide-01.png", "html_source": "slide-01.html", "role": "cover", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 284, "status": "rendered" },
    { "index": 2, "file": "slide-02.png", "html_source": "slide-02.html", "role": "content", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 312, "status": "rendered" },
    { "index": 3, "file": "slide-03.png", "html_source": "slide-03.html", "role": "content", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 298, "status": "rendered" },
    { "index": 4, "file": "slide-04.png", "html_source": "slide-04.html", "role": "content", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 305, "status": "rendered" },
    { "index": 5, "file": "slide-05.png", "html_source": "slide-05.html", "role": "content", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 291, "status": "rendered" },
    { "index": 6, "file": "slide-06.png", "html_source": "slide-06.html", "role": "content", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 318, "status": "rendered" },
    { "index": 7, "file": "slide-07.png", "html_source": "slide-07.html", "role": "cta", "dimensions": { "width": 1080, "height": 1440 }, "file_size_kb": 267, "status": "rendered" }
  ]
}
```

## Quality Criteria

1. **Self-Contained HTML**: Every slide renders without network access (except Google Fonts). No external CSS, JS, or images.
2. **Exact Viewport**: All screenshots exactly 1080x1440px. No deviation.
3. **Cover-First Verification**: Slide 01 visually verified before generating remaining slides.
4. **Design Consistency**: All slides use same font family, colors, spacing, and grid from design system.

## Veto Conditions

1. Any HTML references external CSS/JS/images beyond Google Fonts `@import`.
2. Any text rendered below design system minimums (Hero 58px, Heading 43px, Body 34px, Caption 24px).
3. Any slide has clipped, overflowing, or truncated text content.
4. Inconsistent design across slides (different colors, fonts, or spacing not justified by slide role).
