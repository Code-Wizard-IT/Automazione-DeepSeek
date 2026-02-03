# PROMPT DEEPSEEK: CATALOGO FIGMA-FUNDAMENTALS v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO sull'architettura file Figma, dimensioni per ogni formato (social, stampa, web), grid system, design tokens e configurazioni di export per un graphic designer professionista.

**Contesto:** Figma come unico strumento di produzione grafica (digitale + pre-stampa). Output destinati a: social media, stampa tipografica, web design.

---

## SEZIONI RICHIESTE

### §1. FIGMA FILE ARCHITECTURE

| Livello | Nome Page | Contenuto | Naming Convention |
|---------|-----------|-----------|-------------------|
| Page 1 | 🎨 Cover | Cover progetto + metadata | [CLIENT]-[PROJECT]-Cover |
| Page 2 | 📐 Design System | Tokens, stili, componenti | [CLIENT]-DS |
| Page 3 | 📱 Social Media | Tutti i formati social | [CLIENT]-Social-[PLATFORM] |
| Page 4 | 🖨️ Print | Biglietti, volantini, brochure | [CLIENT]-Print-[TYPE] |
| Page 5 | 🌐 Web | Hero, banner, card, CTA | [CLIENT]-Web-[SECTION] |
| Page 6 | ✅ Export Ready | Finali pronti per export | [CLIENT]-Final-[FORMAT] |

**1.1 Layer Naming Convention**
```
Tabella COMPLETA con:
- Pattern di naming per OGNI tipo di layer (frame, bg, testo heading h1-h6,
  testo body, immagine, icona, shape decorativa, CTA/button, container, spacer)
- Colonna: Tipo Elemento | Pattern Nome | Esempio | Note
- Usare "/" per organizzazione gerarchica (es: txt/h1, img/hero, btn/primary)
- Prefissi: _bg/ per utility, deco/ per decorazioni, ico/ per icone
```

**1.2 Auto Layout Settings per Tipo di Contenuto**
```
Tabella con configurazione Auto Layout per:
- Social Post, Story/Reel, Biglietto da visita, Volantino A5/A4,
  Web Hero, Web Banner, Web Card, Infografica
- Colonne: Tipo | Direction | Padding (top/right/bottom/left) px | Gap px |
  Alignment | Sizing
- Valori ESATTI in px, nessun "variabile" o "dipende"
```

### §2. FRAME DIMENSIONS MASTER TABLE

**2.1 Social Media (px) — Aggiornato 2025**
```
Tabella con TUTTE le piattaforme e formati:

Instagram: Feed 1:1, Feed 4:5, Feed 1.91:1, Story/Reel 9:16,
  Carosello, Profilo, Highlight Cover
Facebook: Post Feed, Post Quadrato, Cover Page, Cover Gruppo,
  Cover Evento, Story, Ad Image
LinkedIn: Post Feed, Post Quadrato, Post Verticale, Banner Profilo,
  Banner Company, Articolo Cover
TikTok: Video/Immagine
X/Twitter: Post Image, Post Quadrato, Header Profile
YouTube: Thumbnail, Channel Banner
Pinterest: Pin Standard, Pin Lungo
WhatsApp: Status
Threads: Post

Colonne: Piattaforma | Tipo | Larghezza px | Altezza px | Aspect Ratio |
  Safe Zone (margine interno px) | Note
```

**2.2 Print (mm + px @300DPI)**
```
Tabella formati stampa:
- Biglietto visita Standard (85×55) e US (88.9×50.8)
- Volantino A6, A5, A4, A3
- Flyer DL (⅓ A4)
- Brochure Bifold e Trifold A4 (aperta)
- Poster 50×70 e 70×100
- Menu Ristorante A4, Cartolina A6, Segnalibro
- Badge/Pass, Roll-up Banner 85×200cm

Colonne: Formato | Larghezza mm | Altezza mm | Larghezza px @300DPI |
  Altezza px @300DPI | Bleed mm | Safe Zone mm dal bordo
- Formula: 1mm = 11.811px @300DPI
```

**2.3 Web Graphics (px)**
```
Tabella completa:
- Hero Full-width, Hero Compact
- Banner Leaderboard, Medium Rectangle, Skyscraper
- Open Graph (og:image), Favicon, App Icon iOS
- Email Header, Email Banner, Blog Featured Image
- Product Card Image, Thumbnail

Colonne: Tipo | Larghezza px | Altezza px | Aspect Ratio | Use Case
```

### §3. DESIGN TOKENS

**3.1 Spacing Scale**
```
Tabella con scala completa da 0 a 96px:
- Token Name | Valore px | Figma Variable Name | Use Case
- Scala: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96
```

**3.2 Border Radius Scale**
```
none=0, sm=4, md=8, lg=12, xl=16, 2xl=24, full=9999
Con use case per ciascuno
```

**3.3 Shadow Scale**
```
sm, md, lg, xl, 2xl, inner
- Parametri Figma ESATTI: X, Y, Blur, Spread, Color (HEX+opacity)
```

### §4. GRID SYSTEMS

**4.1 Grid per Social Media**
```
Tabella per ogni piattaforma/formato:
- Grid Type | Columns | Gutter px | Margin px
```

**4.2 Grid per Print**
```
Tabella per ogni formato stampa:
- Grid Type | Columns | Gutter mm | Margin mm
```

**4.3 Grid per Web (Responsive)**
```
Breakpoints: Mobile 375, Tablet 768, Desktop 1280, Desktop 1440, Wide 1920
- Columns, Gutter, Margin, Max Content Width per ciascuno
```

### §5. EXPORT SETTINGS

**5.1 Export per Destinazione**
```
Tabella:
- Instagram/Social → PNG 1x 72DPI sRGB
- Web Hero/Banner → WebP 1x+2x 80% sRGB
- Web Icons/Logo → SVG vector sRGB
- Favicon → PNG 1x (16,32,48,64,128,512)
- Stampa Tipografica → PDF 300DPI CMYK
- Stampa Digitale → PDF 150-300DPI
- Grande Formato → PDF 150DPI CMYK

Colonne: Destinazione | Formato | Scala/DPI | Qualità | Profilo Colore | Naming
```

**5.2 CMYK in Figma — Nota Critica**
```
Figma lavora SOLO in RGB. Workflow per stampa:
1. Progetta in RGB
2. Esporta PDF alta risoluzione
3. Converti CMYK con: Adobe Acrobat Pro / Affinity Publisher / GIMP

Tabella conversione colori critici:
- Nero Ricco (#1A1A1A) → C:60 M:40 Y:40 K:100
- Nero Testo (#000000) → C:0 M:0 Y:0 K:100
- Rosso Vivo (#E53E3E) → C:0 M:90 Y:80 K:5
- Blu Elettrico (#3182CE) → C:80 M:40 Y:0 K:0
- Verde Smeraldo (#38A169) → C:70 M:0 Y:60 K:10
```

### §6. CHECKLIST FILE SETUP

```
STRUTTURA FILE
□ Pages organizzate per tipo (Social, Print, Web)
□ Layer naming convention applicata
□ Cover page con metadata progetto

DESIGN TOKENS
□ Spacing scale configurata come Figma Variables
□ Radius scale configurata
□ Shadow styles creati

GRID
□ Grid applicata ad ogni frame
□ Safe zone verificate per social
□ Bleed aggiunto per formati stampa

EXPORT
□ Export settings pre-configurati per ogni formato
□ Naming convention file export definita
□ Profilo colore corretto per destinazione
```

---

## OUTPUT ATTESO

Genera **1000-1500 righe** con tutte le tabelle COMPLETE (nessuna cella vuota), valori ESATTI in px/mm, nessuna frase generica. Ogni valore deve essere utilizzabile direttamente in produzione.
