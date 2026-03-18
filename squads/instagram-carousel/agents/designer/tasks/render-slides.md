---
task: "Render Carousel Slides"
order: 2
input: design-system.yaml, carousel-draft.md
output: manifest.json
---

## Process

1. **Build Cover Slide HTML**: Create `slide-01.html` applying the design system from `design-system.yaml`. The HTML file must be fully self-contained: all CSS inline within a `<style>` tag, no external stylesheets except a single Google Fonts `@import` for the specified font family. Set `body` dimensions to exactly `1080x1440px` with `overflow: hidden` and `margin: 0`. The cover slide must include the hook text (Hero typography), brand logo or name, topic indicator, and slide counter (e.g., "1/7"). Use the primary color as background and text color for maximum contrast.

2. **Render and Verify Cover Slide**: Start a local HTTP server (`python3 -m http.server` or equivalent) to serve the HTML file. Use the Playwright browser to navigate to the file URL. Resize the viewport to exactly `1080x1440px`. Take a screenshot of the page. Visually inspect the screenshot to verify: text is not clipped or overflowing, font sizes match the design system, colors render correctly, layout is balanced with proper margins, and safe zones are respected. If any issue is detected, fix the HTML and re-render before proceeding.

3. **Generate Remaining Slide HTML Files**: Once the cover slide passes visual verification, create HTML files for all remaining slides (`slide-02.html` through `slide-NN.html`). Each slide must use the same design system, maintaining consistent header placement, font sizes, spacing, and color usage. Content slides should use Heading and Body typography. The CTA/closing slide should emphasize the call-to-action with accent color and clear next-step instructions.

4. **Batch Render All Slides**: Navigate the browser sequentially to each slide HTML file at the `1080x1440px` viewport. Take a screenshot of each slide, saving as PNG (preferred) or JPEG with quality >= 90%. Name files consistently: `slide-01.png`, `slide-02.png`, etc. Verify each screenshot has exact dimensions of `1080x1440px`.

5. **Create Manifest**: Generate `manifest.json` documenting all rendered slides with their metadata. Include file paths, dimensions, file sizes, slide roles (cover, content, cta), and rendering status. Save the manifest alongside the slide files in the squad output directory.

## Output Format

```json
{
  "carousel_id": "<unique identifier>",
  "total_slides": <number>,
  "viewport": { "width": 1080, "height": 1440 },
  "render_date": "YYYY-MM-DD",
  "design_system": "<path to design-system.yaml>",
  "slides": [
    {
      "index": <number>,
      "file": "<filename.png>",
      "html_source": "<filename.html>",
      "role": "<cover | content | cta>",
      "dimensions": { "width": <px>, "height": <px> },
      "file_size_kb": <number>,
      "status": "<rendered | failed>"
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
  "render_date": "2026-03-18",
  "design_system": "design-system.yaml",
  "slides": [
    {
      "index": 1,
      "file": "slide-01.png",
      "html_source": "slide-01.html",
      "role": "cover",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 284,
      "status": "rendered"
    },
    {
      "index": 2,
      "file": "slide-02.png",
      "html_source": "slide-02.html",
      "role": "content",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 312,
      "status": "rendered"
    },
    {
      "index": 3,
      "file": "slide-03.png",
      "html_source": "slide-03.html",
      "role": "content",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 298,
      "status": "rendered"
    },
    {
      "index": 4,
      "file": "slide-04.png",
      "html_source": "slide-04.html",
      "role": "content",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 305,
      "status": "rendered"
    },
    {
      "index": 5,
      "file": "slide-05.png",
      "html_source": "slide-05.html",
      "role": "content",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 291,
      "status": "rendered"
    },
    {
      "index": 6,
      "file": "slide-06.png",
      "html_source": "slide-06.html",
      "role": "content",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 318,
      "status": "rendered"
    },
    {
      "index": 7,
      "file": "slide-07.png",
      "html_source": "slide-07.html",
      "role": "cta",
      "dimensions": { "width": 1080, "height": 1440 },
      "file_size_kb": 267,
      "status": "rendered"
    }
  ]
}
```

## Quality Criteria

1. **Self-Contained HTML**: Every slide HTML file must render correctly without network access (except the Google Fonts @import). No external CSS frameworks, JavaScript libraries, or image URLs that could break.
2. **Exact Viewport Dimensions**: All rendered screenshots must be exactly 1080x1440px. Any deviation in dimensions causes inconsistent carousel display on Instagram.
3. **Cover Slide Verified First**: The first slide must be visually verified and approved before generating the remaining slides. This prevents cascading design errors across all slides.
4. **Design Consistency**: All slides must use the same font family, color palette, spacing, and layout grid from the design system. Slide-to-slide visual consistency is essential for a professional carousel.

## Veto Conditions

1. **External Dependencies**: Any slide HTML file that references external CSS, JavaScript, or image resources (beyond the single Google Fonts @import) is rejected. Slides must render reliably in isolation.
2. **Font Below Minimum Size**: Any text element rendered below the design system minimums (Hero 58px, Heading 43px, Body 34px, Caption 24px) triggers an automatic rejection. Readability on mobile devices is mandatory.
3. **Clipped or Overflowing Content**: Any slide where text or visual elements extend beyond the 1080x1440px viewport boundary, causing clipping or hidden content, must be rejected and re-rendered.
4. **Inconsistent Design Across Slides**: Visible differences in font sizes, colors, margins, or layout structure between slides that are not intentional design choices. The carousel must feel like a cohesive unit.
