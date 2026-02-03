# PROMPT DEEPSEEK: CATALOGO COMPOSITION-LAYOUT v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO sui principi di composizione, layout e gerarchia visiva per graphic design: regola dei terzi, sezione aurea, pattern di lettura, spazio negativo, principi Gestalt, template di composizione per social/stampa/web con coordinate esatte in px. Tutto implementabile in Figma.

**Contesto:** Ogni principio deve tradursi in azioni concrete in Figma (posizioni px/%, alignment, grid, Auto Layout). Proporzioni come rapporti numerici.

---

## SEZIONI RICHIESTE

### §1. PRINCIPI DI COMPOSIZIONE

**1.1 Regola dei Terzi**
```
Per ogni formato, calcolare i 4 punti focali:

| Formato | Dimensione | Top-Left (x,y) | Top-Right (x,y) |
  Bottom-Left (x,y) | Bottom-Right (x,y) |

- 1080×1080 (IG Feed): 360,360 / 720,360 / 360,720 / 720,720
- 1080×1350 (IG Feed 4:5): 360,450 / 720,450 / 360,900 / 720,900
- 1080×1920 (Story): calcolare
- 1200×627 (LinkedIn): calcolare
- 1280×720 (YouTube Thumb): calcolare

Come attivare in Figma: Grid Rows=3, Columns=3, Stretch, Gutter=0
Quando usare / quando NON usare
```

**1.2 Sezione Aurea (Golden Ratio 1:1.618)**
```
| Formato | Larghezza Totale | Blocco Grande (61.8%) | Blocco Piccolo (38.2%) |

- 1080px: 667px + 413px
- 1200px: 742px + 458px
- 1920px: 1187px + 733px
- A4 (210mm): 130mm + 80mm

Come usare in Figma: constraint Fixed con misure calcolate
Applicazioni: split testo/immagine, proporzione headline/body
```

**1.3 Gerarchia Visiva — I 6 Livelli**
```
| Livello | Elemento | Tecnica in Figma | Esempio |

1. (Max) Headline/Hero Image → font max, bold, colore primario
2. Subheading → 60% del livello 1, semibold
3. Body/Info chiave → font standard, regular, neutral dark
4. CTA → dimensione media MA colore accento
5. Dettagli secondari → font ridotto, neutral medio
6. (Min) Legalese/Credits → font minimo, grigio chiaro
```

**1.4 Pattern di Lettura**
```
| Pattern | Descrizione | Quando Si Attiva | Layout Consigliato |
  Implementazione Figma |

- F-Pattern: scan orizzontale top → scende a sx → scan più brevi
- Z-Pattern: alto-sx → alto-dx → basso-sx → basso-dx
- Gutenberg: 4 quadranti (primary optical, strong fallow, weak fallow, terminal)
- Center Focus: simmetria, singolo punto focale
```

### §2. SPAZIO E PROSSIMITÀ

**2.1 White Space**
```
| Tipo | Definizione | Quantità Consigliata | Come in Figma |

- Macro White Space: tra sezioni → 48-96px (AL gap)
- Micro White Space: tra elementi correlati → 8-24px
- Padding Interno: contenuto-bordo → 24-40px card, 40-80px sezione
- Active White Space: vuoto deliberato → almeno 30% frame vuoto
- Passive White Space: interlinea → line-height 1.4-1.6
```

**2.2 Principi Gestalt**
```
Tabella con 5 principi:
| Principio | Descrizione | Regola Pratica | Implementazione Figma |

- Prossimità: gap interno < 50% gap esterno al gruppo
- Similitudine: stessi stili per stessa categoria
- Continuità: allinea su assi invisibili (grid, baseline)
- Chiusura: suggerisci forme senza completarle
- Figura/Sfondo: contrasto foreground/background
```

### §3. TEMPLATE COMPOSIZIONI PER FORMATO

**3.1 Post Social 1080×1080 — 10 Layout**
```
Tabella con 10 layout:

| Layout Name | Struttura | Zona Testo (coordinate) |
  Zona Immagine (coordinate) | Best For |

1. Hero Centrato: testo centro + sfondo foto + overlay
2. Split Orizzontale: top 50% foto, bottom 50% testo
3. Split Verticale: left 45% testo, right 55% foto
4. Top Banner: top 30% fascia colore, bottom 70% foto
5. Bottom Banner: top 75% foto, bottom 25% fascia CTA
6. Frame Within: foto con cornice decorativa
7. Grid 2×2: 4 quadranti
8. Diagonal Split: linea diagonale
9. Minimal Center: un elemento centrato su fondo piatto
10. Text Only: solo tipografia su colore/gradient

Con coordinate px ESATTE per zona testo e zona immagine
```

**3.2 Story/Reel 1080×1920 — 5 Layout**
```
5 layout con safe zone rispettate (top 200px, bottom 250px):

| Layout | Struttura | Safe Zone | Best For |
```

**3.3 Print — Composizioni per Volantino/Brochure**
```
Layout specifici per A5/A4 con zone in mm:
| Layout | Zona Headline | Zona Visual | Zona Info | Zona CTA |
```

### §4. VISUAL WEIGHT & BALANCE

**4.1 Fattori di Peso Visivo**
```
| Fattore | Peso Maggiore | Peso Minore | Come Bilanciare |

- Dimensione, Colore, Contrasto, Densità, Posizione, Isolamento, Forma
Con regola pratica per ciascuno
```

**4.2 Tipi di Bilanciamento**
```
| Tipo | Descrizione | Effetto | Quando Usare | Esempio |

- Simmetrico: ordine, formalità → wedding, legal, luxury
- Asimmetrico: dinamismo, modernità → social, creative
- Radiale: focus, energia → infografiche, menu
```

### §5. SCALE E PROPORZIONI

```
Tabella delle proporzioni musicali/geometriche:

| Rapporto | Nome | Moltiplicatore | Uso | Esempio base 16px |

- 1:1.125 Major Second ×1.125 → scala conservativa
- 1:1.250 Major Third ×1.250 → scala versatile ⭐
- 1:1.333 Perfect Fourth ×1.333 → scala pronunciata
- 1:1.500 Perfect Fifth ×1.500 → scala drammatica
- 1:1.618 Golden Ratio ×1.618 → scala classica ⭐
- 1:2.000 Octave ×2.000 → scala massima
```

### §6. CHECKLIST COMPOSIZIONE

```
LAYOUT
□ Regola dei terzi o sezione aurea applicata
□ Gerarchia visiva a 3+ livelli
□ Pattern di lettura rispettato (Z o F)
□ White space ≥ 30% del frame

ALLINEAMENTO
□ Grid attivata nel frame
□ Elementi allineati su asse (no "a occhio")
□ Body text allineato a sinistra (no justify)

BILANCIAMENTO
□ Pesi visivi bilanciati (simmetrico o asimmetrico)
□ Max 3 punti focali per frame
□ CTA in posizione "terminal area" (basso-dx)

SAFE ZONE
□ Social: safe zone piattaforma rispettate
□ Print: nessun testo entro 5mm dal bordo taglio
□ Story/Reel: top 200px e bottom 250px liberi
```

---

## OUTPUT ATTESO

Genera **1000-1400 righe** con coordinate ESATTE in px per ogni layout, principi con implementazione Figma specifica, nessuna indicazione generica. Tutto deve essere direttamente applicabile.
