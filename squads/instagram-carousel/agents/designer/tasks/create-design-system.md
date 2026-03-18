---
task: "Create Design System"
order: 1
input: carousel-draft.md, company.md
output: design-system.yaml
---

## Process

1. **Read Brand Context**: Load `company.md` to extract brand colors, visual identity guidelines, logo usage rules, and any existing typography preferences for CEDOA (Centro Especializado em Diagnóstico Oftalmológico da Amazônia). Identify the brand personality (professional, approachable, clinical) to guide design decisions.

2. **Define Color Palette**: Select a maximum of 5 colors with specific roles: primary (brand anchor, dark backgrounds), secondary (complementary tone), accent (highlights, CTAs, emphasis), text (high-contrast readable color for body text), and muted (subtle backgrounds, dividers). Each color must be specified in HEX format. Derive colors from the brand identity or, if not specified, default to a dark navy + coral palette appropriate for medical/ophthalmology content.

3. **Define Typography Scale**: Choose a font family from Google Fonts (Inter or Montserrat preferred for medical readability). Establish a strict size scale for 1080x1440px viewport: Hero (58px minimum, slide titles and cover text), Heading (43px minimum, section headers and key statements), Body (34px minimum, explanatory text and bullet points), Caption (24px minimum, disclaimers, source citations, small labels). Define font weights for each level (Bold/SemiBold for Hero/Heading, Regular/Medium for Body/Caption).

4. **Define Spacing and Grid**: Set base spacing unit at 24px. Define horizontal margins of 72px on each side (resulting in 936px content width). Use a single-column vertical layout optimized for mobile reading. Specify vertical padding between text blocks (multiples of the 24px base unit). Define safe zones to prevent content from being clipped by Instagram's UI overlay.

5. **Verify WCAG Contrast**: Test every text-color-on-background-color combination that will be used in slides. Each pair must meet WCAG AA minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text (Hero/Heading sizes). Document the contrast ratio for each combination. If any pair fails, adjust the color until compliance is achieved.

6. **Compile Design System Document**: Assemble all decisions into a structured YAML output covering colors, typography, spacing, grid, and visual_elements (icon style, border radius, shadow usage, image treatment).

## Output Format

```yaml
design_system:
  colors:
    primary: "<HEX>"
    secondary: "<HEX>"
    accent: "<HEX>"
    text: "<HEX>"
    muted: "<HEX>"
  typography:
    font_family: "<Google Font name>"
    scale:
      hero: { size: "<px>", weight: "<weight>", line_height: "<multiplier>" }
      heading: { size: "<px>", weight: "<weight>", line_height: "<multiplier>" }
      body: { size: "<px>", weight: "<weight>", line_height: "<multiplier>" }
      caption: { size: "<px>", weight: "<weight>", line_height: "<multiplier>" }
  spacing:
    base_unit: "<px>"
    margins: { horizontal: "<px>", vertical: "<px>" }
    content_width: "<px>"
  grid:
    columns: 1
    layout: "single-column"
    safe_zone: { top: "<px>", bottom: "<px>" }
  visual_elements:
    border_radius: "<px>"
    icon_style: "<style>"
    shadow: "<css shadow or none>"
  contrast_checks:
    - pair: "<text color> on <bg color>"
      ratio: "<ratio>"
      passes: <true|false>
```

## Output Example

```yaml
design_system:
  colors:
    primary: "#1B2A4A"
    secondary: "#2D4A7A"
    accent: "#E8654A"
    text: "#F5F5F5"
    muted: "#8A9BBD"
  typography:
    font_family: "Montserrat"
    scale:
      hero: { size: "62px", weight: "700", line_height: "1.15" }
      heading: { size: "46px", weight: "600", line_height: "1.2" }
      body: { size: "36px", weight: "400", line_height: "1.45" }
      caption: { size: "26px", weight: "400", line_height: "1.4" }
  spacing:
    base_unit: "24px"
    margins: { horizontal: "72px", vertical: "48px" }
    content_width: "936px"
  grid:
    columns: 1
    layout: "single-column"
    safe_zone: { top: "96px", bottom: "120px" }
  visual_elements:
    border_radius: "16px"
    icon_style: "outlined, 3px stroke"
    shadow: "0 4px 24px rgba(0,0,0,0.15)"
  contrast_checks:
    - pair: "#F5F5F5 on #1B2A4A"
      ratio: "12.8:1"
      passes: true
    - pair: "#F5F5F5 on #2D4A7A"
      ratio: "7.2:1"
      passes: true
    - pair: "#E8654A on #1B2A4A"
      ratio: "4.6:1"
      passes: true
    - pair: "#1B2A4A on #F5F5F5"
      ratio: "12.8:1"
      passes: true
```

## Quality Criteria

1. **Color Count Limit**: The palette must contain exactly 5 colors, no more. Each color must have a distinct and documented role (primary, secondary, accent, text, muted).
2. **Contrast Compliance**: Every text-on-background combination used in the carousel must meet WCAG AA contrast ratio of 4.5:1 or higher. All checks must be documented with actual ratios.
3. **Minimum Font Sizes**: Hero >= 58px, Heading >= 43px, Body >= 34px, Caption >= 24px. No text in the carousel may fall below these thresholds at the 1080x1440px viewport.
4. **Brand Alignment**: Colors and typography must be consistent with the brand identity defined in `company.md`. Deviations must be justified with a rationale.

## Veto Conditions

1. **Font Size Below 20px**: Any text element defined below 20px at the 1080x1440px viewport is an automatic rejection. Instagram content must remain readable without zooming.
2. **Contrast Below 4.5:1**: Any text-background color pair that fails the WCAG AA 4.5:1 minimum contrast ratio triggers a veto. Accessibility is non-negotiable for medical content.
3. **Excessive Colors**: More than 5 colors defined in the palette. Visual consistency requires strict color discipline on carousel slides.
