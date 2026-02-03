# PROMPT DEEPSEEK: CATALOGO PRINT-DESIGN v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO per la progettazione e produzione di materiale stampato con Figma: biglietti da visita, volantini, brochure, poster, menu, packaging. Workflow da file Figma alla tipografia, calcolo DPI, bleed, safe zone, specifiche carta, finiture, checklist pre-stampa.

**Contesto:** Figma come strumento di pre-stampa. Misure in mm E px @300DPI. Formula: 1mm = 11.811px @300DPI. Include conversione CMYK.

---

## SEZIONI RICHIESTE

### §1. WORKFLOW PRINT DA FIGMA

**1.1 Pipeline Completa**
```
| Step | Azione | Tool | Note Critiche |

1. Imposta frame a 300DPI (mm × 11.811 = px)
2. Aggiungi bleed (frame = finale + bleed×2 per lato)
3. Crea guide safe zone (rettangolo a 5mm dal bordo taglio)
4. Progetta il design (elementi al bordo → estendi fino a bleed)
5. Esporta PDF alta risoluzione
6. Converti RGB → CMYK (Acrobat Pro / Affinity / GIMP)
7. Verifica con tipografo
8. Approva prova colore
```

**1.2 Calcolo Dimensioni Figma @300DPI**
```
Tabella COMPLETA per ogni prodotto:

| Prodotto | Finale mm | Bleed mm | Con Bleed mm | Frame Figma px @300DPI |
  Safe Zone mm |

- Biglietto visita: 85×55 → bleed 3 → 91×61 → 1075×720px, safe 5mm
- Volantino A6: 105×148 → 111×154 → 1311×1819px
- Volantino A5: 148×210 → 154×216 → 1819×2551px
- Volantino A4: 210×297 → 216×303 → 2551×3579px
- Flyer DL: 99×210 → 105×216 → 1240×2551px
- Brochure Bifold A4 aperta: 420×297 → 426×303 → 5031×3579px
- Brochure Trifold A4 aperta: 630×297 → 636×303 → 7512×3579px
- Poster 50×70: 500×700 → 510×710 → 6024×8386px
- Poster 70×100: 700×1000 → 710×1010 → 8386×11929px
- Menu A4: come Volantino A4 con safe 12mm
- Cartolina A6: 148×105 → 154×111 → 1819×1311px
- Roll-up 85×200cm: 850×2000 → @150DPI → 5039×11811px, safe 30mm
```

### §2. TEMPLATE PRODOTTI STAMPATI

**2.1 Biglietto da Visita — Fronte + Retro**
```
Per Fronte e Retro separatamente:

| Elemento | Dettaglio |
- Frame: 1075×720px
- Area taglio: rettangolo guida a 35px dal bordo (3mm bleed)
- Safe zone: rettangolo guida a 95px dal bordo (3mm+5mm)
- Layout Fronte: Logo + Nome (10-12pt/40-48px) + Ruolo (8-9pt/32-36px)
- Layout Retro: Tel, Email, Web (7-8pt/28-32px) + QR Code (min 177×177px = 15mm)
- Font minimo: 7pt = 28px @300DPI
- Carte: 350g/m² patinata opaca, 400g/m² soft-touch, 300g/m² riciclata
```

**2.2 Volantino A5 — Struttura**
```
| Zona | Posizione y (px) | Contenuto | Font |
- Headline: top 25% (y:153-638) → 28-36pt
- Visual: centro 40% (y:638-1658) → foto/illustrazione
- Info: bottom 25% (y:1658-2398) → dettagli, contatti
- CTA: barra inferiore (y:2200-2398) → CTA + contatto
```

**2.3 Brochure Trifold A4 — Struttura**
```
Frame unico orizzontale 7512×3579px

| Pannello | Da (mm) | Larghezza mm | Larghezza px | Contenuto |
- Interno sx: 0-197mm → 2327px → info secondaria
- Interno centro: 197-407mm → 2480px → contenuto principale
- Interno dx: 407-630mm → 2634px → contatti, CTA
- Esterno sx: retro copertina
- Esterno centro: pannello nascosto
- Esterno dx: COPERTINA

NOTA: pannello che si piega dentro = 2-3mm più stretto
Linee piega: guide verticali a 197mm e 407mm
Fronte e Retro = 2 frame separati
```

### §3. CARTA E FINITURE

**3.1 Tipi di Carta**
```
| Tipo | Grammatura | Finitura | Uso Ideale | Costo |

- Patinata Lucida 130-170g → volantini promo, cataloghi foto → €€
- Patinata Opaca 130-170g → brochure eleganti → €€
- Uso Mano 80-120g → documenti, flyer economici → €
- Cartoncino 250-400g → biglietti visita, cartoline → €€€
- Riciclata 100-300g → brand eco, wedding → €€
- Kraft 120-300g → packaging, menu rustici → €€
- Adesiva 80-135g → etichette, sticker → €€
```

**3.2 Finiture di Stampa**
```
| Finitura | Effetto | Costo Extra | Quando Usare |

- Laminazione Lucida: colori vivaci, protetto → +15-20%
- Laminazione Opaca: elegante, premium → +15-25%
- Soft-Touch: ultra premium, vellutato → +25-35%
- Vernice UV Spot: contrasto lucido/opaco su dettagli → +30-50%
- Hot Foil (oro/argento/rame): lusso massimo → +40-60%
- Embossing: rilievo tattile → +30-50%
- Debossing: incasso → +30-50%
- Fustellatura: taglio forma custom → +50-100%
- Bordi Colorati: dettaglio sul taglio laterale → +20-40%
```

### §4. NERO PER STAMPA

```
CRITICO — due tipi di nero:

| Tipo Nero | Quando | Figma HEX | CMYK | Perché |
- Nero Testo (piccolo): K100 puro → #000000 → C:0 M:0 Y:0 K:100
  → Evita fuori registro su testo sottile
- Nero Ricco (aree grandi): CMYK misto → #1A1A1A →C:60 M:40 Y:40 K:100
  → Nero profondo, non appare grigio

ERRORE FATALE: nero K100 su aree grandi = grigio slavato
ERRORE FATALE: nero ricco su testo piccolo = sfocato/fuori registro
```

### §5. CHECKLIST PRE-STAMPA

```
DIMENSIONI
□ Frame = finale + bleed (3mm standard, 5mm poster)
□ Calcolato @300DPI correttamente
□ Fronte e Retro come frame separati (se applicabile)

BLEED & SAFE ZONE
□ Background/immagini estesi fino al bleed
□ NESSUN testo entro 5mm dal bordo di taglio
□ Guide bleed e safe zone visibili nel file

COLORE
□ Colori neon/elettrici evitati (fuori gamut CMYK)
□ Nero testo = K100 puro
□ Nero fondi/aree grandi = nero ricco
□ File pronto per conversione CMYK post-export

TESTO
□ Font minimo 7pt (28px @300DPI)
□ Testo outline (flatten) se richiesto dal tipografo
□ Nessun testo justify

IMMAGINI
□ Tutte le immagini ≥ 300 PPI a dimensione di stampa
□ Nessuna immagine pixelata (zoom 100% check)
□ Nessuna immagine da web (72DPI troppo basso)

EXPORT
□ PDF alta risoluzione (scale 1x se frame già @300DPI)
□ Conversione CMYK effettuata
□ Prova colore approvata prima della tiratura
```

---

## OUTPUT ATTESO

Genera **1000-1400 righe** con calcoli DPI esatti, template per ogni prodotto con coordinate px, specifiche carta e finiture complete. Tutto orientato alla produzione reale in tipografia.
