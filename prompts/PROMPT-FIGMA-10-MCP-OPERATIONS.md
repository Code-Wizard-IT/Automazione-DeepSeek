# PROMPT DEEPSEEK: CATALOGO FIGMA-MCP-OPERATIONS v1

## ISTRUZIONI PER IL MODELLO

Genera una guida operativa COMPLETA per usare Figma tramite MCP (Model Context Protocol) da un LLM come Claude: tool disponibili, formato colori API Figma, tipi di nodo, workflow di analisi e creazione design, traduzione concept→istruzioni Figma programmatiche, template di brief, checklist informazioni necessarie prima di iniziare un progetto.

**Contesto:** Claude accede a Figma Desktop tramite MCP con tool: get_design_context, get_screenshot, get_metadata, get_variable_defs, get_code_connect_map, add_code_connect_map, create_design_system_rules. L'obiettivo è guidare e automatizzare la creazione di design professionali.

---

## SEZIONI RICHIESTE

### §1. TOOL MCP DISPONIBILI

```
Tabella COMPLETA con tutti i tool:

| Tool | Input | Output | Quando Usare |

- get_design_context: nodeId opzionale → UI code + struttura design
  → analizzare struttura di un componente, leggere proprietà
- get_screenshot: nodeId opzionale → screenshot nodo/selezione
  → verificare visivamente il risultato, controllare layout
- get_metadata: nodeId opzionale → XML con ID, tipi, nomi, posizioni, dimensioni
  → ottenere overview struttura pagina, trovare nodeId specifici
- get_variable_defs: nodeId opzionale → definizioni variabili (es: colori, spacing)
  → leggere design tokens esistenti, verificare palette
- get_code_connect_map: nodeId opzionale → mapping nodeId→componente codice
  → collegare design a codebase
- add_code_connect_map: nodeId opzionale → crea collegamento design↔codice
  → associare componente Figma a file nel repo
- create_design_system_rules: nessuno → prompt per generare regole DS
  → creare documentazione design system
```

### §2. FIGMA API — FORMATI DATI

**2.1 Formato Colori API Figma**
```
CRITICO — Figma API usa valori RGBA normalizzati 0-1, NON HEX:

| Formato | Esempio Rosso | Esempio Blu | Come Convertire |

- Figma API: {r: 1.0, g: 0.0, b: 0.0, a: 1.0} → valore/255 = decimale
- HEX: #FF0000 → divide ogni coppia hex per FF (255)
- RGB: rgb(255, 0, 0) → dividi per 255

Conversione HEX → Figma:
#3B82F6 → r: 0x3B/255 = 0.231, g: 0x82/255 = 0.510, b: 0xF6/255 = 0.965

Tabella conversione rapida per colori comuni:
| Colore | HEX | Figma r | Figma g | Figma b |
- Bianco #FFFFFF → 1.0, 1.0, 1.0
- Nero #000000 → 0.0, 0.0, 0.0
- Rosso brand #EF4444 → 0.937, 0.267, 0.267
- Blu brand #3B82F6 → 0.231, 0.510, 0.965
- Verde success #22C55E → 0.133, 0.773, 0.369
- Grigio testo #374151 → 0.216, 0.255, 0.318
- Grigio chiaro #F3F4F6 → 0.953, 0.957, 0.965
(almeno 20 colori comuni pre-calcolati)
```

**2.2 Tipi di Nodo Figma**
```
| Node Type | Descrizione | Proprietà Chiave | Uso nel Design |

- FRAME: contenitore con Auto Layout → width, height, padding, gap
- RECTANGLE: rettangolo → fills, strokes, cornerRadius, effects
- ELLIPSE: cerchio/ellisse → arcData, fills
- TEXT: nodo testo → characters, fontSize, fontFamily, fontWeight, textAlignHorizontal
- GROUP: raggruppamento semplice → children
- COMPONENT: componente riutilizzabile → componentProperties, variants
- INSTANCE: istanza di componente → componentId, overrides
- VECTOR: forma vettoriale → vectorPaths
- BOOLEAN_OPERATION: operazione booleana → booleanOperation (UNION, SUBTRACT, INTERSECT, EXCLUDE)
- LINE: linea → strokeWeight, strokes
- SECTION: sezione organizzativa → children
- COMPONENT_SET: set di varianti → children (varianti)
```

**2.3 Proprietà Layout**
```
| Proprietà | Tipo | Valori | Nota |

- layoutMode: "HORIZONTAL" | "VERTICAL" | "NONE" → Auto Layout direction
- primaryAxisAlignItems: "MIN" | "CENTER" | "MAX" | "SPACE_BETWEEN"
- counterAxisAlignItems: "MIN" | "CENTER" | "MAX" | "BASELINE"
- paddingLeft/Right/Top/Bottom: number (px)
- itemSpacing: number (px) → gap
- layoutSizingHorizontal: "FIXED" | "HUG" | "FILL"
- layoutSizingVertical: "FIXED" | "HUG" | "FILL"
- layoutWrap: "WRAP" | "NO_WRAP"
- constraints: horizontal/vertical → "MIN" | "MAX" | "CENTER" | "SCALE" | "STRETCH"
```

### §3. WORKFLOW OPERATIVO

**3.1 Analisi Design Esistente**
```
| Step | Tool | Azione | Output Atteso |

1. get_metadata → leggere struttura pagina → lista nodi con ID
2. get_screenshot → catturare visuale → immagine per analisi
3. get_design_context (su nodo specifico) → leggere proprietà dettagliate
4. get_variable_defs → leggere token/variabili → palette, spacing
5. Sintetizzare → produrre report con: colori, font, dimensioni, layout
```

**3.2 Creazione Design da Brief**
```
| Step | Azione | Dettaglio |

1. RACCOLTA INFO: checklist brief (§4) → cosa, per chi, dove, stile
2. SCELTA TEMPLATE: in base a settore + formato → ref Catalogo 14
3. DEFINIZIONE TOKEN: colori, font, spacing → ref Catalogo 3, 2
4. COMPOSIZIONE: layout e gerarchia → ref Catalogo 4
5. ISTRUZIONI FIGMA: tradurre in operazioni Figma specifiche
6. VERIFICA: get_screenshot → controllo visivo
7. ITERAZIONE: aggiustamenti basati su feedback
8. EXPORT: configurazione export settings → ref Catalogo 1 §5
```

**3.3 Traduzione Concept → Istruzioni Figma**
```
Tabella di traduzione linguaggio naturale → proprietà Figma:

| Richiesta Utente | Traduzione Figma | Parametri |

"Fai un post Instagram" → Frame 1080×1080, Auto Layout V, Center
"Testo centrato" → textAlignHorizontal: CENTER, AL counterAxis: CENTER
"Sfondo scuro" → Fill #0F172A oppure #1A1A2E
"Testo bianco" → Fill #FFFFFF
"Aggiungi ombra" → Drop Shadow X:0 Y:4 Blur:12 #0000001A
"Angoli arrotondati" → cornerRadius: 12 (card) o 8 (button) o 9999 (pill)
"Sovrapponi testo su foto" → Overlay rectangle #000000 opacity 40-60%
"Più spazio" → padding +8/16px, gap +8px
"Meno spazio" → padding -8px, gap -4px
"Più grande" → fontSize +4-8px (testo) o scale +20% (elemento)
"Più piccolo" → fontSize -4px o scale -20%
"Effetto vetro" → Background Blur 20-40, Fill #FFFFFF 15%, Border #FFFFFF20
"Logo piccolo" → height 32-48px, opacity 60-80%
"Colori del brand" → ref palette settore dal Catalogo 3/14
```

### §4. TEMPLATE BRIEF — CHECKLIST INFO NECESSARIE

**4.1 Brief Minimo (Quick Design)**
```
| Campo | Domanda | Esempio | Obbligatorio |

- Formato: "Cosa devo creare?" → Post IG 1080×1080 → ✅
- Settore: "Di che settore si tratta?" → Ristorante → ✅
- Messaggio: "Qual è il messaggio principale?" → "Menu pranzo €12" → ✅
- CTA: "Cosa deve fare chi vede?" → "Prenota ora" → ✅
- Stile: "Che mood vuoi?" → Elegante, caldo → ❌ (default da settore)
- Colori: "Hai colori brand?" → #8B5E3C + #F5F0EB → ❌ (default da settore)
- Font: "Hai font preferiti?" → Playfair Display → ❌ (default da settore)
- Logo: "Hai un logo?" → Sì, nel file → ❌
- Immagini: "Hai foto?" → Sì, piatto pasta → ❌
```

**4.2 Brief Completo (Brand Project)**
```
| Sezione | Campi |

IDENTITÀ:
- Nome brand
- Settore/nicchia
- Target (età, genere, interessi)
- Competitor (2-3 nomi)
- Valori brand (3-5 parole)

STILE:
- Mood (3 aggettivi: es. "elegante, moderno, minimalista")
- Colori brand (HEX) o preferenze colore
- Font brand o preferenze
- Riferimenti visivi ("mi piace lo stile di...")

CONTENUTO:
- Messaggio principale (max 10 parole)
- Messaggio secondario
- CTA (azione desiderata)
- Informazioni extra (indirizzo, tel, sito, social)
- Logo (file/posizione in Figma)
- Foto/Immagini (file/posizione)

OUTPUT:
- Formato (IG post, story, volantino, biglietto...)
- Quantità (1 design o serie)
- Varianti (colori diversi, A/B test)
- Deadline
```

### §5. PATTERN DI ISTRUZIONE PER FIGMA MCP

**5.1 Pattern: Creare un Frame con Contenuto**
```
Pseudocodice istruzioni standard:

1. CREATE Frame [width]×[height]
2. SET Fill [colore] o Gradient [stops]
3. SET Auto Layout direction=[V/H] padding=[top,right,bottom,left] gap=[px]
4. SET Alignment primary=[CENTER] counter=[CENTER]
5. ADD child Rectangle (decorazione) width=[px] height=[px] fill=[colore]
6. ADD child Text "[contenuto]" font=[family] size=[px] weight=[700] fill=[colore]
7. ADD child Text "[sub]" font=[family] size=[px] weight=[400] fill=[colore] opacity=[80%]
8. ADD child Rectangle (CTA) fill=[accent] radius=[px] padding=[v,h]
   ADD child Text "[cta]" inside CTA
9. EXPORT PNG 1x sRGB
```

**5.2 Pattern: Analizzare e Migliorare Design Esistente**
```
1. get_metadata → inventario elementi
2. get_screenshot → valutazione visiva
3. VALUTARE:
   - Gerarchia visiva chiara? (3+ livelli)
   - Contrasto WCAG rispettato?
   - White space sufficiente? (≥30%)
   - Allineamento su grid?
   - Font leggibile? (min 24px @1080px)
4. SUGGERIRE modifiche con parametri esatti
5. IMPLEMENTARE correzioni
6. get_screenshot → verifica risultato
```

**5.3 Mappa Cross-Reference Cataloghi**
```
| Domanda/Esigenza | Cataloghi da Consultare |

"Che dimensioni uso?" → 01-Fundamentals §2
"Che font metto?" → 02-Typography §2 + §5
"Che colori uso per un ristorante?" → 03-Color §3 + 12-Industry §restaurant
"Come imposto il layout?" → 04-Composition §3
"Come faccio un post IG?" → 05-Social §2 + 01 §2.1
"Come preparo per la stampa?" → 06-Print §1 + §5
"Come creo un logo?" → 07-Brand §2 + §3
"Come faccio una landing page?" → 08-Web §4
"Come faccio effetto vetro?" → 09-Advanced §3.2
"Che trend seguire?" → 11-Resources-Trends §1
"Hai un template per parrucchieri?" → 12-Industry §beauty
```

### §6. GESTIONE ERRORI E LIMITI

```
| Limite | Descrizione | Workaround |

- No creazione nodi: MCP legge/analizza ma non crea direttamente → 
  Claude fornisce istruzioni precise, l'utente esegue in Figma
- No image upload: MCP non carica immagini → utente inserisce,
  Claude posiziona/ridimensiona
- Solo RGB: Figma API solo RGB 0-1 → convertire da HEX con formula
- No font install: MCP non installa font → usare solo Google Fonts
  già disponibili o font già installati
- No plugin: MCP non attiva plugin → istruzioni manuali per plugin
- Rate limit: rispettare pause tra chiamate MCP
- Precisione screenshot: verificare sempre visivamente dopo modifiche
```

### §7. CHECKLIST OPERATIVA MCP

```
PRE-DESIGN
□ Brief raccolto (minimo: formato, settore, messaggio, CTA)
□ Catalogo settore identificato
□ Palette colori definita (HEX)
□ Font pairing scelto (Google Fonts)
□ Dimensioni frame corrette (ref §2 Catalogo 01)

DURANTE IL DESIGN
□ get_metadata per struttura esistente
□ get_screenshot per verifica visiva
□ Istruzioni con parametri ESATTI (px, HEX, font name, weight)
□ Verifica contrasto testo/sfondo (≥4.5:1)
□ Verifica gerarchia (3+ livelli)
□ Verifica white space (≥30%)

POST-DESIGN
□ get_screenshot finale
□ Export settings configurati (formato, DPI, profilo colore)
□ Naming file export corretto
□ Tutte le varianti prodotte (se richieste)

CONSEGNA
□ File organizzato con naming convention
□ Export pronti nella cartella corretta
□ Brief e specifiche documentate
```

---

## OUTPUT ATTESO

Genera **1000-1400 righe** con workflow MCP dettagliati, tabelle conversione colori complete, pattern di istruzione riutilizzabili, cross-reference a tutti gli altri cataloghi. Orientato a permettere a un LLM di operare come graphic designer via Figma MCP.
