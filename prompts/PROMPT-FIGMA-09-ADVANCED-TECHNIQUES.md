# PROMPT DEEPSEEK: CATALOGO FIGMA-ADVANCED v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO delle tecniche avanzate Figma per graphic design: Auto Layout nesting, Component system con varianti, Variables e Styles, effetti visivi (glassmorphism, neumorphism, aurora, duotone), Boolean operations per logo/icone, shortcut essenziali.

**Contesto:** Proprietà Figma ESATTE come appaiono nel Design panel. Shortcut Mac + Windows. Ogni tecnica con: cosa ottenere, come farlo, errori comuni.

---

## SEZIONI RICHIESTE

### §1. AUTO LAYOUT AVANZATO

**1.1 Configurazioni per Graphic Design**
```
| Configurazione | Direction | Spacing | Padding | Alignment | Sizing | Use Case |

- Stack Verticale Standard: V, Fixed gap, Uniforme, Top-Left, Hug×Hug → card
- Stack Centrato: V, Fixed gap, Uniforme, Center-Center, Fixed W×Hug H → post social
- Barra Orizzontale: H, Space Between, Uniforme, Center-Left, Fill W×Fixed H → navbar
- Grid di Card (Wrap): Wrap, Fixed gap, 0, Top-Left, Fill×Hug → gallery
```

**1.2 Auto Layout Nesting**
```
| Livello | Contenuto | Direction | Alignment | Sizing | Esempio |

1 (Root): container → V, Center-Center, Fixed (1080×1080)
2 (Sezioni): blocchi → V, Center, Fill W×Hug H → header/body/footer
3 (Righe): elementi stessa riga → H, Center-Left, Fill W×Hug H
4 (Atomi): singoli elementi → N/A → testo, icona, immagine
```

**1.3 Absolute Positioning dentro Auto Layout**
```
Come attivare: seleziona layer → icona "Absolute position" nel Design panel
Use case: badge su avatar, decorazioni angolari, floating
Constraints: Top/Bottom/Left/Right/Center
Z-Index: ordine nel panel Layers
```

### §2. COMPONENT SYSTEM

**2.1 Architettura Atomic Design**
```
| Livello | Nome | Descrizione | Esempio |

- Atoms: elementi base → colore, icona, testo, shape
- Molecules: 2+ atomi → bottone, input
- Organisms: 2+ molecole → card, navbar
- Templates: layout riutilizzabili → Template/Social/Instagram-Feed
- Pages: istanze personalizzate → [Client]-IG-Post-001
```

**2.2 Component Variants Naming**
```
| Property | Valori Possibili | Esempio |

- Type: primary, secondary, ghost, destructive
- Size: sm, md, lg, xl
- State: default, hover, active, disabled, focused
- Theme: light, dark
- Platform: instagram, facebook, linkedin, print
- Orientation: horizontal, vertical, stacked
- HasIcon: true, false
- HasImage: true, false
```

**2.3 Component Properties**
```
| Property Type | Controlla | Come Creare | Esempio |

- Boolean: mostra/nascondi → right-click layer → showIcon: true/false
- Instance Swap: scambia componente → right-click istanza → icon: Arrow/Check
- Text: espone testo → right-click testo → title: "Default Title"
- Variant: cambia variante → crea variante → state: default/hover
```

### §3. EFFETTI VISIVI

**3.1 Effetti Figma Nativi**
```
| Effetto | Proprietà | Parametri Tipici | Use Case |

- Drop Shadow: X:0 Y:4 Blur:12 Spread:0 #0000001A → elevazione
- Inner Shadow: X:0 Y:2 Blur:4 Spread:0 #0000000D → rilievo interno
- Layer Blur: 8-40px → sfocatura sfondo
- Background Blur: 20-40px → glassmorphism
- Blend Mode: Multiply, Screen, Overlay, Soft Light → overlay colore
```

**3.2 Glassmorphism Step-by-Step**
```
| Step | Azione | Parametri |

1. Rettangolo sopra immagine/gradiente
2. Fill: #FFFFFF Opacity 10-20%
3. Background Blur: 20-40px
4. Border: 1px #FFFFFF Opacity 20-30%
5. Radius: 16-24px
6. Drop Shadow: X:0 Y:8 Blur:32 #0000001A
```

**3.3 Neumorphism Step-by-Step**
```
1. Background frame: #E0E5EC
2. Rettangolo: Fill #E0E5EC (uguale bg)
3. Shadow 1 (luce): X:-8 Y:-8 Blur:16 #FFFFFF 70%
4. Shadow 2 (ombra): X:8 Y:8 Blur:16 #A3B1C6 50%
5. Radius: 16-24px, No border
```

**3.4 Aurora/Gradient Mesh**
```
1. Frame bg: #0F0F1A
2. Ellisse 1: Fill #6366F1, Layer Blur 200px, Opacity 40%, 600×400px
3. Ellisse 2: Fill #EC4899, Layer Blur 200px, Opacity 30%, 500×500px
4. Ellisse 3: Fill #06B6D4, Layer Blur 200px, Opacity 30%, 400×600px
5. Blob sovrapposti e decentrati
6. Opzionale: grain overlay Blend Overlay, Opacity 5-10%
```

**3.5 Duotone Image**
```
1. Inserisci foto
2. Desatura (plugin o pre-processing)
3. Rettangolo colore scuro sopra → Blend: Multiply
4. Rettangolo colore chiaro sopra → Blend: Screen
5. Regola opacità per risultato
```

### §4. FIGMA VARIABLES & STYLES

```
| Feature | Styles | Variables | Quando |

- Colori: ✅ Color Style / ✅ Color Variable → Variables per light/dark
- Tipografia: ✅ Text Style / ❌ → Sempre Styles
- Effetti: ✅ Effect Style / ❌ → Sempre Styles
- Spaziature: ❌ / ✅ Number Variable → Sempre Variables
- Border Radius: ❌ / ✅ Number Variable
- Booleani: ❌ / ✅ Boolean Variable
- Stringhe: ❌ / ✅ String Variable → multi-lingua

Struttura Variables:
- Primitives: valori raw (blue/500: #3B82F6) → nessun Mode
- Semantic: significato (bg/primary: {white}) → Modes: Light, Dark
- Component: specifici (button/padding: {space/6}) → per componente
```

### §5. BOOLEAN OPERATIONS

```
| Operazione | Shortcut Mac | Shortcut Win | Risultato | Use Case |

- Union: Cmd+Alt+U / Ctrl+Alt+U → unisce forme → logo, icone
- Subtract: Cmd+Alt+S / Ctrl+Alt+S → sottrae → ritagli, cutout
- Intersect: Cmd+Alt+I / Ctrl+Alt+I → solo sovrapposizione → Venn
- Exclude: Cmd+Alt+X / Ctrl+Alt+X → rimuove sovrapposizione → XOR
- Flatten: Cmd+E / Ctrl+E → vettore unico → export SVG

Tecniche per Logo:
- Lettera Negativa: shape + lettera sopra → Subtract
- Icona da Forme Base: cerchi + rettangoli → Union → Subtract dettagli
- Logo Interlocking: forme sovrapposte → Intersect + colora
- Pattern Cutout: base + pattern piccoli → Subtract
```

### §6. SHORTCUT ESSENZIALI

```
Tabella con almeno 25 shortcut:

| Azione | Mac | Windows | Categoria |

SELEZIONE:
- Seleziona tutto: Cmd+A / Ctrl+A
- Seleziona child: Enter
- Seleziona parent: Shift+Enter (o Esc)
- Deep select: Cmd+Click / Ctrl+Click

TRASFORMAZIONE:
- Scala proporzionale: K (poi drag)
- Duplica: Alt+Drag
- Flip orizzontale: Shift+H
- Flip verticale: Shift+V

TESTO:
- Bold: Cmd+B / Ctrl+B
- Italic: Cmd+I / Ctrl+I
- Increase size: Cmd+Shift+> / Ctrl+Shift+>

COMPONENTI:
- Crea componente: Cmd+Alt+K / Ctrl+Alt+K
- Detach instance: Cmd+Alt+B / Ctrl+Alt+B
- Go to main: Cmd+Alt+→

ZOOM:
- Zoom to fit: Cmd+1 / Ctrl+1
- Zoom 100%: Cmd+0 / Ctrl+0
- Zoom to selection: Shift+2

EXPORT:
- Export: Cmd+Shift+E / Ctrl+Shift+E
```

### §7. CHECKLIST FIGMA AVANZATO

```
COMPONENTI
□ Atomic design: Atoms → Molecules → Organisms → Templates
□ Naming convention: Category/Type/Variant
□ Varianti con State, Size, Type, Theme
□ Properties: Boolean, Instance Swap, Text configurati

VARIABLES & STYLES
□ Color Variables: Primitives + Semantic
□ Modes configurati (Light/Dark)
□ Text Styles per ogni ruolo tipografico
□ Effect Styles per shadow scale
□ Number Variables per spacing e radius

EFFETTI
□ Glassmorphism: testato su background complesso
□ Shadow scale: sm → 2xl consistente
□ Blend modes: usati con parsimonia

BOOLEAN
□ Logo costruito con operazioni booleane
□ Flatten applicato solo su elementi finali
□ SVG export testato dopo flatten
```

---

## OUTPUT ATTESO

Genera **1200-1500 righe** con step-by-step Figma precisi per ogni tecnica, parametri esatti, shortcut completi. Ogni effetto visivo con recipe riproducibile.
