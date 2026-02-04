# 🎨 PROMPT DEEPSEEK: KNOWLEDGE BASE GRAPHIC DESIGN & FIGMA MASTERY

## ⚠️ ISTRUZIONI CRITICHE PER L'USO

### Prima di usare qualsiasi prompt:
1. **Apri una NUOVA chat** in DeepSeek (non continuare conversazioni esistenti)
2. **Copia il prompt INTERO** incluso il blocco SYSTEM INSTRUCTION
3. **NON modificare** nulla nel prompt
4. **Se l'output viene troncato:** scrivi esattamente `CONTINUA` (senza altro testo)
5. **Salva l'output** in un file `.md` con nome: `RICERCA-FIGMA-[SEZIONE].md`

### Struttura di ogni prompt:
- **SYSTEM INSTRUCTION:** Regole che il modello DEVE seguire
- **TASK:** Cosa deve produrre
- **OUTPUT FORMAT:** Struttura ESATTA richiesta
- **ANTI-PATTERNS:** Cosa NON fare

### Obiettivo Finale:
Questi prompt servono a costruire un **knowledge base completo** che permetterà a Claude (con accesso a Figma MCP) di operare come un **graphic designer professionista**, creando:
- Post per social media (Instagram, Facebook, LinkedIn, TikTok, X/Twitter)
- Volantini e brochure
- Biglietti da visita
- Grafiche per siti web (hero, banner, card, CTA)
- Loghi e brand identity
- Presentazioni
- Infografiche

---

# ═══════════════════════════════════════════════════════════════════════════════
# CATALOGO 1: FIGMA FUNDAMENTALS & DESIGN SYSTEM SETUP
# ═══════════════════════════════════════════════════════════════════════════════

## PROMPT 1.1: Architettura Figma per Graphic Design Professionale

```
=== SYSTEM INSTRUCTION ===
Sei un Senior Product Designer e Figma Expert con 12+ anni di esperienza in graphic design professionale (print + digital). Hai lavorato in agenzie creative top (Pentagram, IDEO, Landor) e conosci ogni dettaglio di Figma come strumento di produzione grafica.

REGOLE OUTPUT:
1. TUTTE le tabelle devono essere COMPLETE (nessuna cella vuota)
2. Ogni valore numerico DEVE essere specifico (px, mm, pt, DPI esatti)
3. NESSUNA frase introduttiva o conclusiva
4. Inizia DIRETTAMENTE con "## 1. FIGMA FILE ARCHITECTURE"
5. Ogni sezione DEVE contenere specifiche ESATTE utilizzabili in produzione

REGOLE SPECIFICHE:
- Misure in px per digitale, mm per stampa
- Colori SEMPRE in HEX + RGB
- Font SEMPRE con fallback stack
- Ogni parametro deve essere un valore CONCRETO, mai "a piacere" o "variabile"

=== TASK ===
Produci una reference tecnica completa sull'architettura di un file Figma professionale per produzione grafica multi-formato (social media, stampa, web).

=== OUTPUT FORMAT (SEGUI ESATTAMENTE) ===

## 1. FIGMA FILE ARCHITECTURE

### 1.1 Struttura File per Progetto Grafico

| Livello | Nome Page | Contenuto | Naming Convention |
|---------|-----------|-----------|-------------------|
| Page 1 | 🎨 Cover | Cover page del progetto con metadata | [CLIENT]-[PROJECT]-Cover |
| Page 2 | 📐 Design System | Tokens, stili, componenti base | [CLIENT]-DS |
| Page 3 | 📱 Social Media | Tutti i formati social | [CLIENT]-Social-[PLATFORM] |
| Page 4 | 🖨️ Print | Biglietti da visita, volantini, brochure | [CLIENT]-Print-[TYPE] |
| Page 5 | 🌐 Web Graphics | Hero, banner, card, CTA | [CLIENT]-Web-[SECTION] |
| Page 6 | 📊 Infografiche | Data visualization, schemi | [CLIENT]-Infographic-[TOPIC] |
| Page 7 | ✅ Export Ready | Versioni finali pronte per export | [CLIENT]-Final-[FORMAT] |
| Page 8 | 📝 Archive | Versioni precedenti e bozze scartate | [CLIENT]-Archive-v[N] |

### 1.2 Layer Naming Convention

| Tipo Elemento | Pattern Nome | Esempio | Note |
|---------------|-------------|---------|------|
| Frame principale | [Format]/[Platform]/[Variant] | Post/Instagram/Feed-Square | Sempre con / per organizzazione |
| Background | _bg/[type] | _bg/gradient, _bg/solid, _bg/image | Underscore per layer utility |
| Testo heading | txt/h[1-6] | txt/h1, txt/h2 | Gerarchia numerica |
| Testo body | txt/body-[size] | txt/body-lg, txt/body-sm | Size esplicito |
| Immagine | img/[role] | img/hero, img/product, img/avatar | Ruolo funzionale |
| Icona | ico/[name] | ico/arrow-right, ico/check | Nome funzionale |
| Shape decorativa | deco/[type] | deco/circle, deco/blob, deco/line | Prefisso deco |
| CTA/Button | btn/[variant] | btn/primary, btn/ghost | Variante esplicita |
| Container | container/[name] | container/card, container/section | Wrapper logico |
| Spacer | spacer/[size] | spacer/16, spacer/24, spacer/48 | Dimensione in px |

### 1.3 Figma Auto Layout Settings per Tipo di Contenuto

| Tipo Contenuto | Direction | Padding (top/right/bottom/left) | Gap | Alignment | Sizing |
|----------------|-----------|----------------------------------|-----|-----------|--------|
| Social Post | Vertical | 40/40/40/40 px | 24 px | Center | Fixed (piattaforma) |
| Story/Reel | Vertical | 60/32/80/32 px | 16 px | Center | Fixed 1080x1920 |
| Biglietto da visita | Vertical | 8mm/10mm/8mm/10mm | 3mm | Left/Center | Fixed 85x55mm |
| Volantino A5 | Vertical | 15mm/15mm/15mm/15mm | 8mm | Top-Left | Fixed A5 |
| Volantino A4 | Vertical | 20mm/20mm/20mm/20mm | 10mm | Top-Left | Fixed A4 |
| Web Hero | Vertical | 80/120/80/120 px | 32 px | Center | Fill container |
| Web Banner | Horizontal | 24/32/24/32 px | 16 px | Center | Fill/Hug |
| Web Card | Vertical | 24/24/24/24 px | 16 px | Top-Left | Hug content |
| Infografica | Vertical | 40/40/40/40 px | 24 px | Center | Fixed (custom) |

## 2. FRAME DIMENSIONS MASTER TABLE

### 2.1 Social Media Dimensions (px) - 2024/2025

| Piattaforma | Tipo Contenuto | Larghezza (px) | Altezza (px) | Aspect Ratio | Safe Zone (margine interno) | Note |
|-------------|---------------|----------------|--------------|--------------|----------------------------|------|
| Instagram | Post Feed Quadrato | 1080 | 1080 | 1:1 | 60px per lato | Formato classico |
| Instagram | Post Feed Verticale | 1080 | 1350 | 4:5 | 60px per lato | Massima visibilità feed |
| Instagram | Post Feed Orizzontale | 1080 | 566 | 1.91:1 | 60px per lato | Meno engagement |
| Instagram | Story/Reel | 1080 | 1920 | 9:16 | Top 200px, Bottom 250px | Zone UI Instagram |
| Instagram | Carosello (ogni slide) | 1080 | 1080 | 1:1 | 60px per lato | Max 10 slide |
| Instagram | Immagine Profilo | 320 | 320 | 1:1 | Circolare, 10px margin | Display 110px |
| Instagram | Highlight Cover | 1080 | 1920 | 9:16 | Centro 800x800 | Visibile solo centro |
| Facebook | Post Feed | 1200 | 630 | 1.91:1 | 50px per lato | Dimensione raccomandata |
| Facebook | Post Quadrato | 1080 | 1080 | 1:1 | 50px per lato | Buon engagement |
| Facebook | Cover Page | 1640 | 924 | 16:9 | Centro safe 1200x450 | Crop variabile mobile |
| Facebook | Cover Gruppo | 1640 | 856 | ~1.91:1 | Centro safe 1200x450 | Simile a page cover |
| Facebook | Cover Evento | 1920 | 1005 | ~1.91:1 | Centro safe 1200x450 | Crop mobile differente |
| Facebook | Story | 1080 | 1920 | 9:16 | Top 150px, Bottom 200px | Zone UI Facebook |
| Facebook | Ad Image | 1200 | 628 | 1.91:1 | 50px per lato | Regola 20% testo |
| LinkedIn | Post Feed | 1200 | 627 | 1.91:1 | 50px per lato | Professionale |
| LinkedIn | Post Quadrato | 1080 | 1080 | 1:1 | 50px per lato | Buon engagement |
| LinkedIn | Post Verticale | 1080 | 1350 | 4:5 | 50px per lato | Massima visibilità |
| LinkedIn | Banner Profilo | 1584 | 396 | 4:1 | Centro safe 1200x300 | Crop su mobile |
| LinkedIn | Banner Company | 1128 | 191 | ~5.9:1 | Centro safe 900x150 | Molto stretto |
| LinkedIn | Articolo Cover | 1200 | 644 | 1.86:1 | 50px per lato | Per articoli LinkedIn |
| TikTok | Video/Immagine | 1080 | 1920 | 9:16 | Top 150px, Bottom 270px | Zone UI pesanti |
| X/Twitter | Post Image | 1200 | 675 | 16:9 | 40px per lato | Display nel feed |
| X/Twitter | Post Quadrato | 1080 | 1080 | 1:1 | 40px per lato | Alternativa |
| X/Twitter | Header Profile | 1500 | 500 | 3:1 | Centro safe 1200x400 | Crop mobile |
| YouTube | Thumbnail | 1280 | 720 | 16:9 | 50px per lato, evita angolo dx basso | Durata video sovrapposta |
| YouTube | Channel Banner | 2560 | 1440 | 16:9 | Safe area 1546x423 centro | Varia per device |
| Pinterest | Pin Standard | 1000 | 1500 | 2:3 | 40px per lato | Formato ideale |
| Pinterest | Pin Lungo | 1000 | 2100 | ~1:2.1 | 40px per lato | Infografiche |
| WhatsApp | Status | 1080 | 1920 | 9:16 | Top 120px, Bottom 160px | Simile a story |
| Threads | Post | 1080 | 1080 | 1:1 | 50px per lato | Come Instagram |

### 2.2 Print Dimensions (mm e px @300DPI)

| Formato | Larghezza mm | Altezza mm | Larghezza px @300DPI | Altezza px @300DPI | Bleed (mm) | Safe Zone (mm dal bordo) |
|---------|-------------|------------|---------------------|-------------------|------------|--------------------------|
| Biglietto da visita Standard | 85 | 55 | 1004 | 650 | 3 | 5 |
| Biglietto da visita US | 88.9 | 50.8 | 1050 | 600 | 3 | 5 |
| Volantino A6 | 105 | 148 | 1240 | 1748 | 3 | 8 |
| Volantino A5 | 148 | 210 | 1748 | 2480 | 3 | 10 |
| Volantino A4 | 210 | 297 | 2480 | 3508 | 3 | 15 |
| Volantino A3 | 297 | 420 | 3508 | 4960 | 3 | 15 |
| Flyer DL (⅓ A4) | 99 | 210 | 1169 | 2480 | 3 | 8 |
| Brochure Bifold A4 (aperta) | 420 | 297 | 4960 | 3508 | 3 | 15 |
| Brochure Trifold A4 (aperta) | 630 | 297 | 7441 | 3508 | 3 | 15 |
| Poster 50x70 | 500 | 700 | 5906 | 8268 | 5 | 20 |
| Poster 70x100 | 700 | 1000 | 8268 | 11811 | 5 | 20 |
| Menu Ristorante A4 | 210 | 297 | 2480 | 3508 | 3 | 12 |
| Cartolina A6 | 148 | 105 | 1748 | 1240 | 3 | 8 |
| Segnalibro | 50 | 150 | 591 | 1772 | 3 | 5 |
| Badge/Pass | 86 | 54 | 1016 | 638 | 3 | 5 |
| Etichetta CD | 120 (diametro) | 120 | 1417 | 1417 | 2 | 5 |
| Roll-up Banner | 850 | 2000 | 10039 | 23622 | 0 | 30 |

### 2.3 Web Graphics Dimensions (px)

| Tipo | Larghezza (px) | Altezza (px) | Aspect Ratio | Use Case |
|------|----------------|--------------|--------------|----------|
| Hero Full-width | 1920 | 1080 | 16:9 | Homepage hero, above fold |
| Hero Compact | 1920 | 600 | ~3.2:1 | Landing page, inner pages |
| Banner Leaderboard | 728 | 90 | ~8:1 | Ad banner standard |
| Banner Medium Rectangle | 300 | 250 | 6:5 | Ad sidebar |
| Banner Skyscraper | 160 | 600 | ~1:3.75 | Ad sidebar verticale |
| Open Graph (og:image) | 1200 | 630 | 1.91:1 | Link preview social |
| Favicon | 512 | 512 | 1:1 | Browser tab, bookmarks |
| App Icon iOS | 1024 | 1024 | 1:1 | App Store |
| Email Header | 600 | 200 | 3:1 | Newsletter header |
| Email Banner | 600 | 300 | 2:1 | Newsletter promo |
| Blog Featured Image | 1200 | 675 | 16:9 | Blog post header |
| Product Card Image | 800 | 800 | 1:1 | E-commerce |
| Thumbnail | 400 | 300 | 4:3 | Gallery, grid |

## 3. DESIGN TOKENS PER FIGMA

### 3.1 Spacing Scale (usabile in Figma Variables)

| Token Name | Valore (px) | Figma Variable | Use Case |
|------------|-------------|----------------|----------|
| space/0 | 0 | spacing/0 | Reset |
| space/1 | 4 | spacing/4 | Micro-gap (icona-testo inline) |
| space/2 | 8 | spacing/8 | Gap stretto tra elementi correlati |
| space/3 | 12 | spacing/12 | Padding interno compatto |
| space/4 | 16 | spacing/16 | Gap standard tra elementi |
| space/5 | 20 | spacing/20 | Padding bottone |
| space/6 | 24 | spacing/24 | Padding card, gap sezioni piccole |
| space/8 | 32 | spacing/32 | Gap tra blocchi di contenuto |
| space/10 | 40 | spacing/40 | Padding social post |
| space/12 | 48 | spacing/48 | Gap tra sezioni |
| space/16 | 64 | spacing/64 | Padding sezione grande |
| space/20 | 80 | spacing/80 | Margine hero |
| space/24 | 96 | spacing/96 | Spaziatura massima |

### 3.2 Border Radius Scale

| Token Name | Valore (px) | Figma Variable | Use Case |
|------------|-------------|----------------|----------|
| radius/none | 0 | radius/0 | Elementi sharp (print, corporate) |
| radius/sm | 4 | radius/4 | Input, small chips |
| radius/md | 8 | radius/8 | Card, bottoni standard |
| radius/lg | 12 | radius/12 | Card prominenti, modal |
| radius/xl | 16 | radius/16 | Card hero, feature highlight |
| radius/2xl | 24 | radius/24 | Elementi arrotondati |
| radius/full | 9999 | radius/full | Cerchi, pill buttons, avatar |

### 3.3 Shadow Scale

| Token Name | Figma Shadow Value | Use Case |
|------------|-------------------|----------|
| shadow/sm | X:0 Y:1 Blur:2 Spread:0 Color:#0000000D | Elevazione minima, input |
| shadow/md | X:0 Y:4 Blur:6 Spread:-1 Color:#0000001A | Card default |
| shadow/lg | X:0 Y:10 Blur:15 Spread:-3 Color:#0000001A | Card hover, dropdown |
| shadow/xl | X:0 Y:20 Blur:25 Spread:-5 Color:#0000001A | Modal, popup |
| shadow/2xl | X:0 Y:25 Blur:50 Spread:-12 Color:#00000040 | Elementi floating |
| shadow/inner | X:0 Y:2 Blur:4 Spread:0 Color:#0000000D (inner) | Input focus, well |

## 4. GRID SYSTEMS

### 4.1 Grid per Social Media in Figma

| Piattaforma | Grid Type | Columns | Gutter | Margin | Note |
|-------------|-----------|---------|--------|--------|------|
| Instagram Feed 1080x1080 | Columns | 4 | 20px | 40px | Simmetrico, centrato |
| Instagram Feed 1080x1350 | Columns | 4 | 20px | 40px | Più spazio verticale |
| Instagram Story 1080x1920 | Columns | 3 | 16px | 32px | Safe zone top/bottom |
| Facebook 1200x630 | Columns | 6 | 16px | 40px | Panoramico |
| LinkedIn 1200x627 | Columns | 6 | 16px | 40px | Come Facebook |
| YouTube Thumb 1280x720 | Columns | 4 | 24px | 48px | Focus testo grande |

### 4.2 Grid per Print in Figma

| Formato | Grid Type | Columns | Gutter (mm) | Margin (mm) | Note |
|---------|-----------|---------|-------------|-------------|------|
| Biglietto da visita | Columns | 2 | 4 | 5 | Pochissimo spazio |
| Volantino A5 | Columns | 3 | 5 | 10 | Versatile |
| Volantino A4 | Columns | 4 | 5 | 15 | Standard editoriale |
| Brochure A4 bifold | Columns | 4 per pannello | 5 | 12 | Grid per pannello |
| Poster 50x70 | Columns | 6 | 8 | 20 | Ampio, modulare |

## 5. EXPORT SETTINGS

### 5.1 Export Configuration per Destinazione

| Destinazione | Formato | Scala/DPI | Qualità | Profilo Colore | Naming |
|-------------|---------|-----------|---------|----------------|--------|
| Instagram/Social | PNG | 1x (72 DPI) | Massima | sRGB | [project]-[platform]-[type]-[date] |
| Instagram/Social (alt) | JPG | 1x (72 DPI) | 85-95% | sRGB | [project]-[platform]-[type]-[date] |
| Web Hero/Banner | WebP | 1x + 2x | 80% | sRGB | [section]-hero-[breakpoint] |
| Web Icons/Logo | SVG | Vector | N/A | sRGB | [brand]-logo-[variant] |
| Favicon | PNG | 1x | Massima | sRGB | favicon-[size] |
| Stampa Tipografica | PDF | 300 DPI | Massima | CMYK (ISO Coated v2) | [project]-print-[type]-CMYK |
| Stampa Digitale | PDF | 150-300 DPI | Alta | sRGB o CMYK | [project]-print-[type]-[DPI] |
| Stampa Grande Formato | PDF | 150 DPI | Alta | CMYK | [project]-largeformat-[size] |
| Presentazione | PDF | 150 DPI | Alta | sRGB | [project]-presentation-[date] |

### 5.2 Nota CMYK in Figma
```
IMPORTANTE: Figma lavora SOLO in RGB. Per produzione stampa professionale:

1. Progetta in Figma usando i colori RGB più vicini ai CMYK desiderati
2. Esporta in PDF ad alta risoluzione
3. Converti il profilo colore in CMYK usando:
   - Adobe Acrobat Pro (Preflight > Convert Colors)
   - Affinity Publisher (importa PDF > converti a CMYK)
   - GIMP + plugin Separate+ (gratuito)
4. Verifica i colori con il tuo tipografo

Tabella conversione colori critici RGB → CMYK approssimativo:
| Nome | RGB HEX | RGB Values | CMYK Approssimato | Note |
|------|---------|------------|-------------------|------|
| Nero Ricco | #1A1A1A | 26,26,26 | C:60 M:40 Y:40 K:100 | Nero profondo per stampa |
| Nero Testo | #000000 | 0,0,0 | C:0 M:0 Y:0 K:100 | Solo per testo piccolo |
| Rosso Vivo | #E53E3E | 229,62,62 | C:0 M:90 Y:80 K:5 | Attenzione: varia in stampa |
| Blu Elettrico | #3182CE | 49,130,206 | C:80 M:40 Y:0 K:0 | Varia molto RGB→CMYK |
| Verde Smeraldo | #38A169 | 56,161,105 | C:70 M:0 Y:60 K:10 | Controllare prova colore |
```

=== ANTI-PATTERNS (NON FARE) ===
❌ NON usare dimensioni approssimative - ogni px/mm deve essere esatto
❌ NON omettere le safe zone - sono critiche per social media
❌ NON dimenticare il bleed per formati stampa
❌ NON lasciare celle vuote nelle tabelle
❌ NON usare "dipende" o "varia" - dare valori specifici
❌ NON ignorare la conversione RGB/CMYK per stampa
```


---

# ═══════════════════════════════════════════════════════════════════════════════
# CATALOGO 2: TIPOGRAFIA & FONT PAIRING PER GRAPHIC DESIGN
# ═══════════════════════════════════════════════════════════════════════════════

## PROMPT 2.1: Typography Masterclass per Design Grafico

```
=== SYSTEM INSTRUCTION ===
Sei un Typography Director con 15+ anni in agenzie creative internazionali (Pentagram, Wolff Olins, Sagmeister & Walsh). Sei esperto di tipografia per print, digital e brand identity. Conosci ogni sfumatura di leggibilità, gerarchia visiva e font pairing.

REGOLE OUTPUT:
1. TUTTE le tabelle devono essere COMPLETE
2. Font DEVONO essere disponibili GRATUITAMENTE su Google Fonts (o system fonts)
3. Ogni valore tipografico DEVE essere specifico (px, pt, rem, line-height esatti)
4. NESSUNA frase introduttiva o conclusiva
5. Inizia DIRETTAMENTE con "## 1. TYPE SCALE SYSTEM"

REGOLE SPECIFICHE:
- Ogni font pairing DEVE includere: nome font heading + nome font body + perché funzionano insieme
- Le misure per social DEVONO essere in px
- Le misure per stampa DEVONO essere in pt
- Line-height in rapporto (es: 1.2, 1.5)
- Letter-spacing in em (es: 0.02em, -0.01em)

=== TASK ===
Produci un catalogo tipografico COMPLETO per graphic design professionale, coprendo social media, stampa e web.

=== OUTPUT FORMAT (SEGUI ESATTAMENTE) ===

## 1. TYPE SCALE SYSTEM

### 1.1 Type Scale per Social Media (valori in px, contesto: 1080px wide)

| Ruolo | Font Size (px) | Line Height | Letter Spacing | Font Weight | Max Caratteri/Riga | Use Case |
|-------|---------------|-------------|----------------|-------------|---------------------|----------|
| Display Hero | 96-120px | 1.0-1.05 | -0.03em | 800-900 | 8-12 | Una parola d'impatto, titolo evento |
| Headline Primary | 64-80px | 1.05-1.1 | -0.02em | 700-800 | 12-18 | Titolo principale post |
| Headline Secondary | 48-56px | 1.1-1.15 | -0.015em | 600-700 | 18-25 | Sottotitolo, claim |
| Subheading | 32-40px | 1.15-1.2 | -0.01em | 600 | 25-35 | Sottosezione, bullet point grande |
| Body Large | 28-32px | 1.4-1.5 | 0em | 400-500 | 35-45 | Testo principale leggibile |
| Body Regular | 24-28px | 1.4-1.5 | 0em | 400 | 40-50 | Corpo del testo |
| Body Small | 20-24px | 1.35-1.45 | 0.01em | 400 | 50-60 | Didascalie, dettagli |
| Caption | 16-18px | 1.3-1.4 | 0.02em | 400-500 | 60+ | Credits, piccole note |
| CTA Button | 28-36px | 1.0 | 0.05em | 700 | 15-20 | Pulsante call-to-action |
| Tag/Label | 18-22px | 1.0 | 0.08em | 600 | 15-20 | Etichette, badge, uppercase |

### 1.2 Type Scale per Stampa (valori in pt)

| Ruolo | Font Size (pt) | Line Height | Letter Spacing | Font Weight | Use Case |
|-------|---------------|-------------|----------------|-------------|----------|
| Display | 48-72pt | 1.0-1.05 | -0.02em | 700-900 | Titolo poster, copertina |
| Headline | 28-36pt | 1.1-1.15 | -0.01em | 600-700 | Titolo volantino, brochure |
| Subheading | 18-24pt | 1.15-1.2 | 0em | 500-600 | Sottotitolo sezione |
| Body Large | 12-14pt | 1.4-1.5 | 0em | 400 | Testo principale volantino |
| Body Standard | 10-11pt | 1.4-1.55 | 0em | 400 | Corpo testo brochure |
| Body Small | 8-9pt | 1.35-1.45 | 0.01em | 400 | Note, condizioni |
| Caption | 7-8pt | 1.3-1.4 | 0.02em | 400 | Credits, informazioni legali |
| Micro | 6pt | 1.3 | 0.03em | 400 | Disclaimer (MINIMO leggibile) |
| Biglietto - Nome | 10-12pt | 1.2 | 0.05em | 600-700 | Nome su business card |
| Biglietto - Ruolo | 8-9pt | 1.3 | 0.02em | 400 | Qualifica su business card |
| Biglietto - Contatti | 7-8pt | 1.4 | 0.01em | 400 | Tel, email, indirizzo |

### 1.3 Type Scale per Web Graphics (valori in px)

| Ruolo | Font Size (px) | Line Height | Letter Spacing | Font Weight | Use Case |
|-------|---------------|-------------|----------------|-------------|----------|
| Hero Heading | 48-72px | 1.05-1.1 | -0.02em | 700-800 | Hero section heading |
| Section Heading | 32-40px | 1.1-1.2 | -0.01em | 600-700 | Titolo sezione |
| Card Heading | 20-24px | 1.2-1.3 | -0.005em | 600 | Titolo card |
| Body | 16-18px | 1.5-1.6 | 0em | 400 | Testo leggibile web |
| Small/Meta | 12-14px | 1.4-1.5 | 0.01em | 400 | Date, autore, meta |
| Button | 14-18px | 1.0 | 0.02em | 600 | CTA buttons |
| Nav Link | 14-16px | 1.0 | 0.01em | 500 | Menu navigation |

## 2. FONT PAIRING CATALOG

### 2.1 Top 20 Font Pairing (tutti Google Fonts gratuiti)

| # | Font Heading | Font Body | Stile/Mood | Settore Ideale | Perché Funzionano |
|---|-------------|-----------|-----------|----------------|-------------------|
| 1 | Playfair Display (Serif) | Inter (Sans-serif) | Elegante moderno | Fashion, Luxury, Hospitality | Contrasto alto/basso, classico+contemporaneo |
| 2 | Montserrat (Sans-serif) | Open Sans (Sans-serif) | Pulito professionale | Corporate, Tech, SaaS | Geometrico+neutro, massima leggibilità |
| 3 | Poppins (Sans-serif) | Nunito (Sans-serif) | Friendly, giovane | Startup, App, Educazione | Rotondo+morbido, approachable |
| 4 | Oswald (Sans-serif) | Lato (Sans-serif) | Bold, impattante | Sport, Fitness, Automotive | Condensato+humanist, forza+leggibilità |
| 5 | Merriweather (Serif) | Source Sans 3 (Sans-serif) | Editoriale autorevole | Media, Publishing, Legal | Serif largo+sans neutro, credibilità |
| 6 | Raleway (Sans-serif) | Roboto (Sans-serif) | Minimal elegante | Architettura, Design, Gallery | Thin-weight elegante+neutro versatile |
| 7 | DM Serif Display (Serif) | DM Sans (Sans-serif) | Contemporaneo raffinato | Branding, Restaurant, Boutique | Stessa famiglia DM, armonia naturale |
| 8 | Space Grotesk (Sans-serif) | Space Mono (Mono) | Tech futuristico | Tech, Crypto, Gaming | Famiglia coerente, estetica tech |
| 9 | Libre Baskerville (Serif) | Libre Franklin (Sans-serif) | Classico editoriale | Editoria, Cultura, Musei | Famiglie Libre complementari |
| 10 | Work Sans (Sans-serif) | Work Sans (Sans-serif) | Versatile, moderno | Multi-purpose, Agency | Single font multi-weight, coerenza |
| 11 | Lora (Serif) | Roboto (Sans-serif) | Caldo editoriale | Blog, Food, Lifestyle | Serif calligrafico+geometrico neutro |
| 12 | Bebas Neue (Sans-serif) | Roboto Flex (Sans-serif) | Impattante bold | Eventi, Musica, Street | Uppercase condensato+flessibile |
| 13 | Cormorant Garamond (Serif) | Proza Libre (Sans-serif) | Luxury classico | Gioielleria, Vino, Hotel | Alto contrasto serif+humanist sans |
| 14 | Archivo (Sans-serif) | Archivo (Sans-serif) | Corporate moderno | Finanza, Consulting, B2B | Variable font, 1 solo file, tutti i pesi |
| 15 | Fraunces (Serif) | Commissioner (Sans-serif) | Quirky premium | Caffetteria, Craft, Indie | Optical-size serif+geometric clean |
| 16 | Sora (Sans-serif) | IBM Plex Sans (Sans-serif) | Tech premium | AI, Data, Enterprise | Geometrico moderno+IBM heritage |
| 17 | Bricolage Grotesque (Sans-serif) | Inter (Sans-serif) | Bold creativo | Creative agency, Portfolio | Display impattante+corpo perfetto |
| 18 | Vollkorn (Serif) | Fira Sans (Sans-serif) | Accademico caldo | Educazione, Ricerca, ONG | Serif robusto+humanist chiaro |
| 19 | Cabinet Grotesk (via Fontshare) | Satoshi (via Fontshare) | Trendy 2024 | Social media, Branding giovane | Geometric+grotesk, estetica corrente |
| 20 | Instrument Serif (Serif) | Instrument Sans (Sans-serif) | Editoriale moderno | Magazine, Editorial, Moda | Stessa famiglia, armonia perfetta |

### 2.2 Font Pairing per Settore

| Settore | Heading Font | Body Font | Mood Keywords | Colore Primario Suggerito |
|---------|-------------|-----------|---------------|---------------------------|
| Ristorazione Fine Dining | Cormorant Garamond | Inter | Eleganza, Raffinatezza | #1A1A2E (navy scuro) |
| Pizzeria/Casual Food | Fredoka (rounded) | Nunito | Calore, Convivialità | #D35400 (arancione) |
| Studio Legale | Libre Baskerville | Source Sans 3 | Autorità, Affidabilità | #1B2A4A (blu scuro) |
| Palestra/Fitness | Oswald | Roboto | Energia, Potenza | #E63946 (rosso) |
| Salone Bellezza | Playfair Display | Lato | Eleganza, Femminilità | #B8860B (gold) |
| Startup Tech | Space Grotesk | Inter | Innovazione, Modernità | #6366F1 (indigo) |
| Agenzia Immobiliare | Montserrat | Open Sans | Solidità, Professionalità | #2D5016 (verde scuro) |
| Negozio Bambini | Poppins | Nunito | Giocosità, Morbidezza | #FF6B9D (rosa) |
| Enoteca/Vini | DM Serif Display | DM Sans | Tradizione, Premium | #722F37 (bordeaux) |
| Studio Dentistico | Raleway | Roboto | Pulizia, Fiducia | #0EA5E9 (celeste) |
| Architetto/Interior | Sora | IBM Plex Sans | Minimalismo, Precisione | #1A1A1A (nero) |
| Fotografo | Instrument Serif | Instrument Sans | Arte, Storytelling | #374151 (grigio scuro) |

## 3. GERARCHIA VISIVA TIPOGRAFICA

### 3.1 Regole di Gerarchia (applicabili in Figma)

| Principio | Regola Specifica | Esempio Figma | Impatto Visivo |
|-----------|-----------------|---------------|----------------|
| Scala | Il titolo deve essere almeno 2x il body | H1: 64px, Body: 28px (ratio 2.28) | Chiara distinzione ruoli |
| Peso | Differenza minima 200 in weight | H1: Bold 700, Body: Regular 400 | Contrasto forza/leggerezza |
| Colore | Heading più scuro, body leggermente più chiaro | H: #111827, Body: #374151 | Priorità di lettura |
| Spaziatura | Heading: letter-spacing stretto, Body: neutro | H: -0.02em, Body: 0em | Titoli compatti, body ariosi |
| Interlinea | Body: 1.4-1.6, Heading: 1.0-1.2 | Auto layout gap coerente | Leggibilità body, compattezza heading |
| Contrasto Tipo | Serif heading + Sans body o viceversa | Playfair + Inter | Separazione chiara dei ruoli |
| Max Larghezza | Body text max 60-75 caratteri per riga | Frame max-width: 680px per body | Leggibilità ottimale |
| Allineamento | Heading: center o left, Body: left (MAI justify) | Text align left per body | Leggibilità naturale |

### 3.2 Errori Tipografici Comuni (da evitare)

| Errore | Perché è Sbagliato | Soluzione Corretta |
|--------|--------------------|--------------------|
| Testo tutto in UPPERCASE lungo | Illeggibile sopra le 3-4 parole | Uppercase SOLO per label, CTA brevi, titoli 1-3 parole |
| Line-height troppo stretta nel body | Affatica la lettura, claustrofobico | Minimo 1.4 per body text |
| Troppi font diversi (>3) | Caos visivo, mancanza di coerenza | Max 2 font (1 heading + 1 body), max 3 in casi estremi |
| Font size troppo piccolo su social | Illeggibile su mobile (device reale) | Minimo 24px per body su 1080px social |
| Testo bianco su foto senza overlay | Illeggibile in zone chiare | Aggiungere overlay scuro 40-60% o ombra testo |
| Kerning non regolato su display | Spaziature irregolari evidenti in grande | Letter-spacing negativo (-0.02/-0.03em) per display |
| Testo centrato per paragrafi lunghi | Difficile seguire l'inizio riga | Center SOLO per titoli e testi brevi (max 3 righe) |
| Font decorativo per body text | Illeggibile per testi lunghi | Font decorativi SOLO per display/heading brevi |

## 4. TESTO SU IMMAGINI (TECNICHE FIGMA)

### 4.1 Tecniche per Rendere il Testo Leggibile su Foto

| Tecnica | Come Fare in Figma | Parametri | Quando Usare |
|---------|---------------------|-----------|--------------|
| Overlay Scuro | Rectangle sopra foto, Fill #000000, Opacity 40-60% | Blend: Normal, Opacity: 50% default | Foto chiare, testo bianco |
| Overlay Gradient | Rectangle con Linear Gradient da #000000 60% a trasparente | Angle: 180° (bottom-up) o 0° (top-down) | Testo in basso o in alto |
| Overlay Colore Brand | Rectangle con colore brand, Opacity 70-85% | Blend: Multiply o Normal | Brand forte, effetto duotone |
| Text Shadow | Effetto Drop Shadow sul layer testo | X:0 Y:2 Blur:8 Color:#00000080 | Testo su foto variegate |
| Box Behind Text | Rectangle con background dietro il testo | Fill #000000 Op.60%, Radius 8px, Padding 16px | Testo breve, tag, label |
| Blur Background | Foto duplicata + Layer Blur dietro testo | Background Blur: 20-40px | Effetto frosted glass |
| Zona Solid | Metà frame colore solido + metà foto | Split layout 50/50 o 60/40 | Design editoriale pulito |
| Scurire Foto | Exposure/Brightness ridotta sulla foto | Figma: non nativo, preparare foto esternamente | Foto come texture di fondo |

=== ANTI-PATTERNS (NON FARE) ===
❌ NON suggerire font a pagamento senza alternative gratuite
❌ NON usare size generici come "grande" o "piccolo"
❌ NON omettere il line-height per nessun livello della scala
❌ NON proporre più di 3 font per un singolo progetto
❌ NON dimenticare la leggibilità su mobile reale
❌ NON ignorare le differenze px (screen) vs pt (stampa)
```
