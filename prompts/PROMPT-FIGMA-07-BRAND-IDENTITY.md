# PROMPT DEEPSEEK: CATALOGO BRAND-IDENTITY v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO per la creazione di brand identity e logo design con Figma: anatomia brand system, tipi di logo, principi logo design, costruzione in Figma, varianti, clear space, minimum size, brand book, deliverable di export.

**Contesto:** Guida operativa per creare un sistema di identità visiva completo da consegnare a un cliente, interamente in Figma.

---

## SEZIONI RICHIESTE

### §1. ANATOMIA BRAND IDENTITY SYSTEM

**1.1 Componenti**
```
| Componente | Definizione | Deliverable | Priorità (1-5) |

- Logo (Marchio): simbolo + logotipo → SVG + PNG → ⭐⭐⭐⭐⭐
- Logotipo: nome brand in font specifico → parte del logo
- Pittogramma/Icona: simbolo senza testo → favicon, avatar
- Palette Colori: primari, secondari, accent, neutri → HEX/RGB/CMYK/Pantone
- Tipografia: font primario + secondario + regole → font files + type scale
- Pattern/Texture: elementi decorativi ripetibili → seamless pattern
- Iconografia: set icone coerente → SVG
- Brand Guidelines: documento completo → PDF/Figma
```

**1.2 Tipi di Logo**
```
| Tipo | Descrizione | Vantaggi | Svantaggi | Esempio Famoso | Ideale Per |

- Wordmark (Logotipo): solo nome con font custom → Google, Coca-Cola
- Lettermark (Monogramma): iniziali → IBM, HBO
- Pictorial Mark: icona riconoscibile → Apple, Twitter
- Abstract Mark: forma geometrica astratta → Nike swoosh
- Combination Mark: icona + testo → Burger King, Lacoste
- Emblem: testo dentro forma → Starbucks, Harley-Davidson
- Mascot: personaggio → KFC, Mailchimp
```

### §2. PRINCIPI LOGO DESIGN

```
| Principio | Regola | Test di Verifica |

- Semplicità: max 2-3 forme → "disegnalo a memoria dopo 5 sec"
- Scalabilità: 16px → 5 metri → testare a 16, 32, 64, 200, 1000px
- Versatilità: B/N, colore, sfondo chiaro/scuro → 4 test
- Memorabilità: riconoscibile dopo 1 esposizione
- Atemporalità: no trend effimeri → "funziona tra 10 anni?"
- Appropriatezza: comunica settore e tono
- Unicità: no somiglianza competitor → ricerca Google Immagini
```

### §3. LOGO IN FIGMA

**3.1 Setup File**
```
| Page | Contenuto | Naming |

📐 Grid & Construction → griglia, proporzioni
✏️ Sketches → exploration, varianti
🎨 Refinement → confronti A/B
✅ Final → logo definitivo in tutte le varianti
📏 Guidelines → clear space, min size, uso DO/DON'T
📦 Export → tutti i formati
```

**3.2 Varianti Richieste**
```
| Variante | Descrizione | Formato | Use Case |

- Primary Orizzontale: pittogramma + logotipo affiancati → header, email
- Primary Verticale/Stacked: pittogramma sopra, logotipo sotto → social, app
- Pittogramma Solo: solo simbolo → favicon, avatar, watermark
- Logotipo Solo: solo nome → firme email, footer
- Monocromo Nero: su trasparente → stampa B/N
- Monocromo Bianco: su trasparente → sfondo scuro, foto
- Con Tagline: logo + tagline sotto → brochure, presentazioni
- Responsive/Compact: ridotta per piccole dimensioni → app bar
```

**3.3 Clear Space e Minimum Size**
```
Clear Space:
- Unità base "x" = altezza della "o" minuscola del logotipo
- Minimo 1.5x — 2x attorno a tutti i lati
- Figma: Auto Layout con padding = 2x
- Eccezione favicon: 0.5x o 0

Minimum Size:
| Contesto | Min Logo Completo | Min Pittogramma |
- Digitale: 120px / 24px
- Stampa: 25mm / 8mm
- Favicon: N/A / 16px (multipli fino a 512)
```

### §4. BRAND BOOK — STRUTTURA

**4.1 Indice**
```
| Sezione | Contenuto | N. Pagine |

1. Introduzione: mission, vision, valori → 2-4
2. Logo: varianti, costruzione, clear space, min size → 6-10
3. Uso Corretto/Scorretto: DO e DON'T → 2-4
4. Colori: palette completa con tutti i codici → 3-5
5. Tipografia: font, scala, regole → 3-5
6. Fotografia: stile, mood, DO/DON'T → 2-4
7. Iconografia: stile, grid, dimensioni → 2-3
8. Pattern/Texture: pattern brand, regole d'uso → 1-2
9. Applicazioni: mockup biglietto, carta intestata, social, web → 6-10
10. Contatti: chi contattare per uso brand → 1
```

**4.2 Logo DO / DON'T**
```
✅ DO:
- Usare solo varianti ufficiali
- Rispettare clear space
- Usare su sfondi approvati
- Mantenere proporzioni

❌ DON'T:
- Stirare o deformare
- Aggiungere ombre/bordi/effetti
- Mettere su sfondi a basso contrasto
- Cambiare colori arbitrariamente
- Ruotare o inclinare
- Rimuovere parti del logo
```

### §5. DELIVERABLE EXPORT

**5.1 File da Consegnare**
```
| Formato | Estensione | Uso | Dettagli |

- Vettoriale: .svg → web, scalabile → outline text
- PNG Trasparente: .png → social, presentazioni → @1x, @2x, @4x
- PNG su Bianco: .png → documenti, email → @2x
- PDF Vettoriale: .pdf → stampa → CMYK, outline
- Favicon Pack: .png → browser → 16, 32, 48, 64, 128, 192, 512px
- Social Kit: .png → avatar, copertine → dimensioni per piattaforma
```

**5.2 Naming Convention**
```
[brand]-logo-[variant]-[color]-[size].[ext]

Esempi:
- acme-logo-horizontal-color-1x.svg
- acme-logo-stacked-white-2x.png
- acme-icon-color-512.png
- acme-favicon-32.png
```

### §6. CHECKLIST BRAND IDENTITY

```
LOGO
□ Almeno 4 varianti (horizontal, stacked, icon, mono)
□ Testato a 16px, 64px, 200px, 1000px
□ Funziona in B/N e colore
□ Clear space definito e documentato
□ Minimum size definito

BRAND SYSTEM
□ Palette colori completa (primary, secondary, accent, neutral, semantic)
□ Font pairing definito (heading + body)
□ Type scale creata
□ Pattern/texture brand (opzionale)

BRAND BOOK
□ Logo guidelines (varianti, DO/DON'T, clear space)
□ Color guidelines con tutti i codici
□ Typography guidelines
□ Pagine applicazioni con mockup

EXPORT
□ SVG per ogni variante logo
□ PNG @1x @2x @4x trasparente
□ PDF vettoriale per stampa
□ Favicon pack completo
□ Social avatar kit
□ File organizzati con naming convention
```

---

## OUTPUT ATTESO

Genera **1000-1400 righe** con struttura completa brand identity system, tutte le varianti logo con specifiche, template brand book, export completo. Orientato alla consegna professionale al cliente.
