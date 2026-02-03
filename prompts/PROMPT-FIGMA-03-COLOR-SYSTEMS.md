# PROMPT DEEPSEEK: CATALOGO COLOR-SYSTEMS v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO sulla teoria del colore applicata al graphic design: armonie cromatiche, psicologia del colore, palette pronte all'uso per 10+ settori, sistema variabili colore Figma, gradienti, opacità, contrasto WCAG. Ogni colore DEVE avere HEX, RGB e CMYK approssimato.

**Contesto:** Produzione grafica multi-formato (social, stampa, web) in Figma. Colori HEX sempre a 6 cifre. Rapporti contrasto in formato X:1.

---

## SEZIONI RICHIESTE

### §1. COLOR THEORY FUNDAMENTALS

**1.1 Armonie Cromatiche**
```
Tabella con 7 armonie:

| Armonia | Descrizione | Come Costruirla (ruota HSL) | Mood/Effetto |
  Quando Usarla | Esempio 3 HEX |

- Monocromatica: variazioni di un solo hue
- Complementare: 2 colori opposti 180°
- Analoga: 3 colori adiacenti ±30°
- Triadica: 3 colori a 120°
- Split-Complementare: 1 + 2 adiacenti al complementare
- Tetradic/Rettangolare: 4 colori in rettangolo
- Square: 4 colori a 90°

Per ogni armonia: 3 colori HEX di esempio concreti
```

**1.2 Psicologia del Colore per Settore**
```
Tabella con almeno 11 colori:

| Colore (HEX) | Emozioni Positive | Emozioni Negative | Settori Ideali |
  Settori da Evitare | Associazioni Culturali (Occidente) |

Rosso, Arancione, Giallo, Verde, Blu, Indigo, Viola, Rosa,
Nero, Bianco, Grigio — con HEX specifico per ognuno
```

### §2. CONTRASTO WCAG

**2.1 Requisiti Minimi**
```
| Combinazione | AA Testo Normale | AA Testo Grande | AAA |
- Testo su sfondo: 4.5:1 / 3:1 / 7:1
- Componenti UI: 3:1
```

**2.2 Combinazioni Testo/Sfondo Testate**
```
Tabella con almeno 14 combinazioni SICURE:

| Background HEX | Text HEX | Rapporto | WCAG Level | Use Case |

Coprire: light mode, dark mode, card, info box, error box,
success box, warning box — con rapporti ESATTI
```

### §3. PALETTE PRONTE PER SETTORE

```
Per OGNI settore, una palette completa con 8 ruoli:
Primary, Secondary, Accent, Neutral Dark, Neutral Light,
Success, Warning, Error

Colonne: Ruolo | Nome Colore | HEX | RGB | Use Case

SETTORI (almeno 8 palette complete):
- Ristorazione / Food & Beverage
- Studio Legale / Professionale
- Tech / Startup / SaaS
- Beauty / Wellness / Spa
- Sport / Fitness / Energia
- Bambini / Education / Playful
- Immobiliare / Architettura
- Moda / Luxury / Premium
- Healthcare / Medico
- Eco / Green / Sostenibilità
```

### §4. COLOR SYSTEM PER FIGMA

**4.1 Struttura Variabili Colore in Figma**
```
Tabella con 3 livelli:

| Collection | Gruppo | Token Name | Valore Light | Valore Dark | Semantica |

- Primitives: colori raw (blue/50, blue/100... blue/900)
- Semantic: bg/primary, bg/secondary, text/primary, text/secondary,
  text/accent, border/default, border/focus,
  status/success, status/warning, status/error, status/info
- Con mapping Light → Dark mode per ogni token
```

**4.2 Regola del 60-30-10**
```
| Proporzione | Ruolo | Dove Applicare | Esempio |
- 60% dominante (neutro/bg)
- 30% secondario (brand)
- 10% accento (CTA)
```

**4.3 Gradient Recipes per Figma**
```
Tabella con almeno 8 gradienti pronti:

| Nome | Tipo | Stop 1 (HEX %) | Stop 2 (HEX %) | Stop 3 | Angle | Use Case |

- Sunset Warm, Ocean Deep, Forest Mist, Royal Night,
  Golden Hour, Ice Blue, Dark Glass, Mesh Pink
```

**4.4 Opacità Standard**
```
| Livello | Opacità % | HEX Suffix | Use Case |
- Overlay Heavy 80% CC
- Overlay Medium 60% 99
- Overlay Light 40% 66
- Hover 8% 14
- Pressed 12% 1F
- Disabled 40% 66
- Border Subtle 10% 1A
- Background Tint 5% 0D
```

### §5. COLORI PER CONTESTO

**5.1 Social Media — Colori che Performano**
```
| Piattaforma | Colori Alto Engagement | Colori Basso Engagement | Note |
Per Instagram, LinkedIn, Facebook, TikTok, Pinterest, X
```

**5.2 Stampa — Attenzione CMYK**
```
Tabella colori PROBLEMATICI in conversione RGB → CMYK:
| Colore RGB | HEX | Risultato CMYK | Problema | Soluzione |
- Arancio neon, viola elettrico, verde lime, cyan puro, magenta puro
```

### §6. CHECKLIST COLORI

```
PALETTE
□ Primary, Secondary, Accent definiti con HEX
□ Neutral Dark e Light definiti
□ Semantic colors (success, warning, error, info)
□ Palette testata in combinazione

CONTRASTO
□ Testo body su sfondo: rapporto ≥ 4.5:1 (WCAG AA)
□ Testo heading su sfondo: rapporto ≥ 3:1
□ Testato su sfondo chiaro E scuro

FIGMA
□ Color Variables create (Primitives + Semantic)
□ Light/Dark mode configurati come Modes
□ Color Styles applicati ai componenti

PRODUZIONE
□ Colori verificati per resa CMYK (stampa)
□ Nessun colore neon/fuori gamut per materiale stampato
□ Gradient testati in export PNG e PDF
```

---

## OUTPUT ATTESO

Genera **1200-1500 righe** con palette COMPLETE per tutti i settori, ogni colore con HEX+RGB, combinazioni WCAG testate, gradienti con parametri Figma esatti. Nessuna cella vuota.
