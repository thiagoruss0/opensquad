---
task: "Create Design System"
order: 1
input:
  - carousel-draft.md
  - company.md
output: design-system.yaml
---

## Process

1. **Read Brand Context**: Load `company.md` to extract brand colors, visual identity, logo rules, and typography preferences for CEDOA. Identify brand personality (professional, approachable, clinical) to guide design decisions.

2. **Define Color Palette**: Select max 5 colors with specific roles — primary (brand anchor, dark backgrounds), secondary (complementary tone), accent (highlights, CTAs), text (high-contrast readable), muted (subtle backgrounds, dividers). Specify in HEX. Default to dark navy + coral for medical/ophthalmology when brand is unspecified.

3. **Define Typography Scale**: Choose Inter or Montserrat via Google Fonts. Size scale for 1080x1440px: Hero >= 58px (titles), Heading >= 43px (section headers), Body >= 34px (explanatory text), Caption >= 24px (disclaimers, labels). Define weights: Bold/SemiBold for Hero/Heading, Regular/Medium for Body/Caption.

4. **Define Spacing and Grid**: Base unit 24px. Horizontal margins 72px each side (936px content width). Single-column vertical layout. Vertical padding between blocks as multiples of base unit. Define safe zones for Instagram UI overlay.

5. **Verify WCAG Contrast**: Test every text-on-background combination. Minimum 4.5:1 for normal text, 3:1 for large text (Hero/Heading). Document each ratio. Adjust colors until compliant.

6. **Compile Design System**: Assemble all decisions into structured YAML covering colors, typography, spacing, grid, and visual_elements.

## Output Format

```yaml
design_system:
  colors:
    primary: { hex: "#XXXXXX", usage: "string" }
    secondary: { hex: "#XXXXXX", usage: "string" }
    accent: { hex: "#XXXXXX", usage: "string" }
    text: { hex: "#XXXXXX", usage: "string" }
    muted: { hex: "#XXXXXX", usage: "string" }
  typography:
    font_family: "string"
    scale: { hero: {}, heading: {}, body: {}, caption: {} }
  spacing: { base_unit: "Xpx", margins: "Xpx", content_width: "Xpx" }
  grid: { columns: 1, safe_zone: { top: "Xpx", bottom: "Xpx" } }
  contrast_checks:
    - { pair: "text on primary", ratio: "X.X:1", passes: true }
```

## Output Example

```yaml
design_system:
  colors:
    primary: { hex: "#1B2A4A", usage: "Fundos de slide, cabecalhos" }
    secondary: { hex: "#2D4A7A", usage: "Fundos secundarios, cards" }
    accent: { hex: "#E8654A", usage: "CTAs, destaques, icones" }
    text: { hex: "#F5F5F5", usage: "Texto sobre fundos escuros" }
    muted: { hex: "#8A9BBD", usage: "Legendas, textos secundarios" }
  typography:
    font_family: "Montserrat"
    scale:
      hero: { size: "62px", weight: 700, line_height: "1.15" }
      heading: { size: "46px", weight: 600, line_height: "1.2" }
      body: { size: "36px", weight: 400, line_height: "1.45" }
      caption: { size: "26px", weight: 400, line_height: "1.4" }
  spacing: { base_unit: "24px", margins: "72px", content_width: "936px" }
  grid: { columns: 1, safe_zone: { top: "96px", bottom: "120px" } }
  contrast_checks:
    - { pair: "#F5F5F5 on #1B2A4A", ratio: "12.8:1", passes: true }
    - { pair: "#F5F5F5 on #2D4A7A", ratio: "7.2:1", passes: true }
    - { pair: "#E8654A on #1B2A4A", ratio: "4.6:1", passes: true }
```

## Quality Criteria

1. **Color Count**: Exactly 5 colors with distinct documented roles. No additional colors.
2. **Contrast Compliance**: Every text-on-background pair meets WCAG AA 4.5:1. All checks documented.
3. **Font Size Minimums**: Hero >= 58px, Heading >= 43px, Body >= 34px, Caption >= 24px.
4. **Brand Alignment**: Colors and typography consistent with `company.md` identity.

## Veto Conditions

1. Any font size below 20px at 1080x1440px viewport.
2. Any text-background contrast ratio below 4.5:1.
3. More than 5 colors in the palette.
