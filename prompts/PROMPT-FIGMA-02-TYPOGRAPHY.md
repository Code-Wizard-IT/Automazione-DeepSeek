# PROMPT DEEPSEEK: CATALOGO TYPOGRAPHY-DESIGN v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO sulla tipografia per graphic design professionale: scale tipografiche per social/stampa/web, i 20 migliori font pairing gratuiti, regole di gerarchia visiva, leggibilità e tecniche per testo su immagini in Figma.

**Contesto:** Tutti i font devono essere GRATUITI (Google Fonts o Fontshare). Misure in px per digitale, pt per stampa. Ogni valore deve essere specifico e utilizzabile in produzione.

---

## SEZIONI RICHIESTE

### §1. TYPE SCALE SYSTEM

**1.1 Type Scale per Social Media (px, contesto 1080px wide)**
```
Tabella COMPLETA con ruoli tipografici per social:

Ruoli: Display Hero, Headline Primary, Headline Secondary, Subheading,
  Body Large, Body Regular, Body Small, Caption, CTA Button, Tag/Label

Colonne: Ruolo | Font Size px | Line Height (ratio) | Letter Spacing (em) |
  Font Weight | Max Caratteri/Riga | Use Case

- Display Hero: 96-120px, LH 1.0-1.05, LS -0.03em, W 800-900
- Body Regular: 24-28px, LH 1.4-1.5, LS 0em, W 400
- CTA Button: 28-36px, LH 1.0, LS 0.05em, W 700
- (completare TUTTI i ruoli con valori esatti)
```

**1.2 Type Scale per Stampa (pt)**
```
Tabella con ruoli per stampa:
- Display (48-72pt), Headline (28-36pt), Subheading (18-24pt)
- Body Large (12-14pt), Body Standard (10-11pt), Body Small (8-9pt)
- Caption (7-8pt), Micro (6pt — MINIMO leggibile)
- Biglietto visita: Nome (10-12pt), Ruolo (8-9pt), Contatti (7-8pt)

Stesse colonne della 1.1 ma valori in pt
```

**1.3 Type Scale per Web (px)**
```
Hero Heading, Section Heading, Card Heading, Body, Small/Meta, Button, Nav Link
Con valori specifici per ciascuno
```

### §2. FONT PAIRING CATALOG

**2.1 Top 20 Font Pairing (tutti gratuiti)**
```
Tabella con 20 combinazioni heading+body:

Colonne: # | Font Heading | Font Body | Stile/Mood | Settore Ideale |
  Perché Funzionano

Esempi da includere:
1. Playfair Display + Inter → Elegante moderno → Fashion, Luxury
2. Montserrat + Open Sans → Pulito professionale → Corporate, Tech
3. Poppins + Nunito → Friendly, giovane → Startup, Education
4. Oswald + Lato → Bold, impattante → Sport, Fitness
5. DM Serif Display + DM Sans → Contemporaneo raffinato → Restaurant, Boutique
(continuare fino a 20 con mix Serif+Sans, Sans+Sans, Display+Body)
```

**2.2 Font Pairing per Settore**
```
Tabella con almeno 12 settori:
- Ristorazione Fine Dining, Pizzeria/Casual Food, Studio Legale,
  Palestra/Fitness, Salone Bellezza, Startup Tech, Agenzia Immobiliare,
  Negozio Bambini, Enoteca/Vini, Studio Dentistico, Architetto, Fotografo

Colonne: Settore | Heading Font | Body Font | Mood Keywords |
  Colore Primario Suggerito (HEX)
```

### §3. GERARCHIA VISIVA TIPOGRAFICA

**3.1 Regole di Gerarchia**
```
Tabella con principi applicabili in Figma:

| Principio | Regola Specifica | Esempio Figma | Impatto Visivo |
- Scala: titolo almeno 2x il body
- Peso: differenza minima 200 in weight
- Colore: heading più scuro, body leggermente più chiaro (dare HEX)
- Spaziatura: heading LS stretto, body neutro
- Interlinea: body 1.4-1.6, heading 1.0-1.2
- Contrasto Tipo: serif heading + sans body (o viceversa)
- Max Larghezza: body text max 60-75 char/riga → frame max-width 680px
- Allineamento: heading center/left, body left (MAI justify digitale)
```

**3.2 Errori Tipografici Comuni**
```
Tabella almeno 8 errori:
| Errore | Perché è Sbagliato | Soluzione Corretta |

- Testo tutto UPPERCASE lungo → max 1-3 parole uppercase
- Line-height troppo stretta body → minimo 1.4
- Troppi font (>3) → max 2 font (heading+body)
- Font size <20px su social 1080px → minimo 24px body
- Testo bianco su foto senza overlay → overlay 40-60%
- Kerning non regolato display → LS negativo -0.02/-0.03em
- Testo centrato per paragrafi lunghi → center solo titoli
- Font decorativo per body → decorativi SOLO per display/heading brevi
```

### §4. TESTO SU IMMAGINI (TECNICHE FIGMA)

**4.1 Tecniche per Leggibilità Testo su Foto**
```
Tabella con almeno 8 tecniche:

| Tecnica | Come Fare in Figma | Parametri Esatti | Quando Usare |

- Overlay Scuro: Rectangle #000000 Opacity 40-60%
- Overlay Gradient: Linear Gradient #000000 60% → transparent, angle 180°
- Overlay Colore Brand: Rectangle brand color Opacity 70-85%, Blend Multiply
- Text Shadow: Drop Shadow X:0 Y:2 Blur:8 Color:#00000080
- Box Behind Text: Rectangle #000000 Op.60%, Radius 8px, Padding 16px
- Background Blur: Layer Blur 20-40px (frosted glass)
- Zona Solid: Split layout 50/50 o 60/40 (metà colore, metà foto)
- Scurire Foto: pre-processing esterno (Figma non ha exposure nativo)
```

### §5. TIPOGRAFIA PER SETTORE — QUICK REFERENCE

```
Per ogni settore, fornire il "kit tipografico" completo:

| Settore | Heading Font | Body Font | Display Size Social | Body Size Social |
  Heading Size Stampa | Body Size Stampa | Mood |

Almeno 12 settori con valori ESATTI pronti all'uso
```

### §6. CHECKLIST TIPOGRAFIA

```
TYPE SCALE
□ Scale definita per social (px)
□ Scale definita per stampa (pt)
□ Scale definita per web (px)
□ Salvata come Figma Text Styles

FONT PAIRING
□ Heading font selezionato (Google Fonts)
□ Body font selezionato (Google Fonts)
□ Testato il pairing su titolo+paragrafo
□ Verificato che entrambi supportano i caratteri necessari (accenti, numeri)

GERARCHIA
□ Almeno 3 livelli di gerarchia chiari
□ Contrasto peso heading vs body ≥ 200
□ Line-height body ≥ 1.4
□ Max caratteri per riga ≤ 75

LEGGIBILITÀ
□ Font size body social ≥ 24px su 1080px
□ Font size body stampa ≥ 10pt
□ Contrasto testo/sfondo WCAG AA (4.5:1)
□ Testo su foto: overlay o tecnica applicata
```

---

## OUTPUT ATTESO

Genera **1000-1500 righe** con tutte le tabelle COMPLETE, font SOLO gratuiti (Google Fonts/Fontshare), valori ESATTI in px/pt/em, nessuna cella vuota.
