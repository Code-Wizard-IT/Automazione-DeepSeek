# PROMPT DEEPSEEK: CATALOGO WEB-GRAPHICS v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO per la progettazione di web graphics e UI elements in Figma: hero sections, banner, card, CTA, form, footer, landing page completa, Open Graph images. Con breakpoint responsive, stati interattivi (hover, active, disabled), e component specs.

**Contesto:** Figma come strumento per design di grafiche web. Breakpoint: Mobile 375px, Tablet 768px, Desktop 1440px. Scala base 4-8px.

---

## SEZIONI RICHIESTE

### §1. RESPONSIVE BREAKPOINTS

```
| Breakpoint | Nome | Frame Width | Grid Columns | Gutter | Margin |
  Max Content Width |

- Mobile S: 375 → 4 col, 16px gutter, 16px margin → 343px content
- Mobile L: 428 → 4 col, 16px, 16px → 396px
- Tablet: 768 → 8 col, 24px, 32px → 704px
- Desktop S: 1280 → 12 col, 24px, 64px → 1152px
- Desktop M: 1440 → 12 col, 24px, 80px → 1280px
- Desktop L: 1920 → 12 col, 24px, 120px → 1280px centrato
```

### §2. HERO SECTION PATTERNS

**2.1 Tipi di Hero**
```
| Pattern | Layout | Height Desktop | Height Mobile | Contenuto | Conversione |

- Hero Full-Screen: visual + overlay + testo centrato → 100vh
- Hero Split: 50% testo sx + 50% immagine dx → 600-800px
- Hero con Video: video bg + overlay + testo → 80vh
- Hero Minimal: solo headline su bg piatto → 500-600px
- Hero con Form: testo sx + form dx → 600-700px
- Hero con Stats: headline + statistiche → 500-600px
- Hero Testimonial: quote + avatar + CTA → 500-600px
```

**2.2 Hero Template Specifiche (Desktop 1440px)**
```
| Elemento | Proprietà | Valore |

- Frame: 1440 × 700px
- Container: max-width 1200px, Auto Layout Vertical, gap 32px
- Headline: 56-72px, 700, #0F172A
- Subheadline: 20-24px, 400, #475569
- CTA Primary: padding 16/32px, radius 8px, 16px 600, bg #6366F1, text #FFF
- CTA Secondary: padding 16/32px, radius 8px, border 1px #6366F1, text #6366F1
- Spacing headline→sub: 16-24px
- Spacing sub→CTA: 32-40px
- Section padding: 80-120px top/bottom
```

### §3. COMPONENTI UI — SPECS

**3.1 Card Component**
```
| Proprietà | Default | Hover | Compact |

- Width: 360px desktop / 100% mobile / 280px compact
- Padding: 24px / — / 16px
- Radius: 12px / — / 8px
- Border: 1px #E2E8F0 / 1px #CBD5E0
- Shadow default: 0 1px 3px rgba(0,0,0,0.1)
- Shadow hover: 0 10px 15px rgba(0,0,0,0.1) + translateY(-2px)
- Image height: 200px / — / 160px
- Title: 20px 600 #1A202C
- Body: 14-16px 400 #4A5568
- Gap image→title: 16px, title→body: 8px
```

**3.2 Button Component**
```
Tabella COMPLETA con TUTTI gli stati per ogni variante:

| Variante | BG | Text Color | Border | Padding | Font | Radius | Shadow |

- Primary Default: #6366F1, #FFF, none, 12/24px, 16px 600, 8px
- Primary Hover: #4F46E5, shadow colore
- Primary Active: #4338CA, inset shadow
- Primary Disabled: #6366F1 50%, #FFF 70%
- Secondary Default: #FFF, #6366F1, 1px #6366F1
- Secondary Hover: #EEF2FF, #4F46E5
- Ghost Default: transparent, #6366F1
- Ghost Hover: #6366F10A, #4F46E5
- Destructive: #EF4444, #FFF
- Size Small: padding 8/16px, 14px 500, radius 6px
- Size Large: padding 16/32px, 18px 600, radius 10px
```

**3.3 Form Elements**
```
| Elemento | Height | Padding | Border | Radius | Font | BG | Focus State |

- Text Input: 44px, 0/12px, 1px #E2E8F0, 8px, 16px 400, #FFF
  Focus: 2px #6366F1 + shadow 0 0 0 3px #6366F133
- Textarea: 120px min
- Select: 44px
- Checkbox: 20×20px, radius 4px, checked: bg #6366F1
- Radio: 20×20px, radius full
- Toggle: 44×24px, knob 20px
- Label: 14px 500 #374151
- Error: 12px 400 #EF4444
- Input Error: border 1px #EF4444, bg #FEF2F2
```

### §4. LANDING PAGE STRUCTURE

```
| Ordine | Sezione | Obiettivo | Height Desktop | Elementi Chiave |

1. Navbar: navigazione → 64-80px fixed → logo + nav + CTA
2. Hero: proposta di valore → 600-100vh → headline + sub + CTA + visual
3. Social Proof: credibilità → 80-120px → "Trusted by" + 5-8 loghi
4. Features: spiegare valore → 600-800px → 3-4 card con icone
5. How It Works: processo → 400-600px → 3 step numerati
6. Testimonials: fiducia → 400-500px → 2-3 quote con avatar
7. Pricing: conversione → 500-700px → 2-3 pricing card
8. FAQ: rimuovere obiezioni → 400-600px → 5-8 accordion
9. Final CTA: ultima chance → 300-400px → headline + CTA prominent
10. Footer: info legali → 200-400px → link columns + social
```

**4.1 Navbar**
```
| Proprietà | Desktop | Mobile |
- Height: 64-80px / 56-64px
- Position: fixed top
- Logo: 32-40px / 28-32px
- Nav Link: 14-16px 500 #374151, hover: #6366F1
- CTA: button small
- Mobile: hamburger 24×24px
```

**4.2 Footer**
```
| Proprietà | Desktop | Mobile |
- BG: #0F172A o #F8FAFC
- Padding: 64px 80px / 48px 16px
- Layout: 4 column grid + bottom bar / stack vertical
- Social icons: 24×24, gap 16px, #94A3B8 → hover #FFF
- Copyright: 12px #64748B
```

### §5. OPEN GRAPH & META IMAGES

```
Template og:image (1200×630):

| Elemento | Proprietà | Posizione |
- Frame: 1200×630, bg brand/gradient
- Logo: 40-48px height, top-left, padding 40px → x:40 y:40
- Headline: 40-48px 700 #FFF, max 60 char, max 2 righe → centro y:220-320
- Subheadline: 20-24px 400 #FFF 80% → sotto headline, gap 16px
- URL/Domain: 16px 400 #FFF 60% → bottom-left x:40 y:580
```

### §6. CHECKLIST WEB GRAPHICS

```
RESPONSIVE
□ Frame per Mobile (375), Tablet (768), Desktop (1440)
□ Grid 12 colonne (desktop) / 4 colonne (mobile)
□ Componenti testati su tutti i breakpoint

COMPONENTI
□ Card: default + hover + compact
□ Button: primary + secondary + ghost + destructive × 3 size × 4 stati
□ Form: input + textarea + select + checkbox + radio + toggle
□ Tutti con stato disabled

LANDING PAGE
□ Navbar fixed con logo + CTA
□ Hero con headline + CTA
□ Social proof (loghi)
□ Features + How It Works
□ Testimonials
□ Pricing
□ FAQ
□ Final CTA
□ Footer completo

META
□ Open Graph image 1200×630 creata
□ Favicon 512px creato
□ Touch icon 1024×1024 (se app)
```

---

## OUTPUT ATTESO

Genera **1200-1500 righe** con specs componenti COMPLETE per Figma (tutti gli stati, tutte le varianti), landing page structure, responsive breakpoints. Valori px esatti per tutto.
