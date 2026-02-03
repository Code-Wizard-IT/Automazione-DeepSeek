# PROMPT DEEPSEEK: CATALOGO SOCIAL-MEDIA-DESIGN v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo tecnico COMPLETO per il design di contenuti social media professionali: template step-by-step per Figma per ogni piattaforma, caroselli, story, reel cover, thumbnail YouTube, best practice engagement, regole per testo/CTA, content calendar visivo.

**Contesto:** Template realizzabili in Figma con istruzioni step-by-step. Font size verificati per mobile reale. Ogni template con coordinate px esatte.

---

## SEZIONI RICHIESTE

### §1. CONTENT TYPES PER PIATTAFORMA

**1.1 Instagram**
```
| Tipo | Formato | Dimensione px | Engagement | Obiettivo | Design Focus |

- Post Feed Singolo (1:1, 4:5)
- Carosello Educativo (4:5 × 10 slide)
- Carosello Prodotto (1:1 × 10 slide)
- Reel Cover (9:16)
- Story Interattiva (9:16)
- Highlight Cover (9:16 centro)
- Immagine Profilo (1:1)
```

**1.2 LinkedIn**
```
Stessa struttura per: Post Singolo, Carosello/PDF, Article Cover,
Banner Profilo, Banner Pagina, Newsletter Cover
```

**1.3 Facebook**
```
Post Feed, Post Quadrato, Cover Page, Ad Single Image,
Event Cover, Story
```

**1.4 TikTok / YouTube / Pinterest / X**
```
| Piattaforma | Tipo | Dimensione | Design Focus Chiave |
```

### §2. TEMPLATE STEP-BY-STEP FIGMA

**2.1 Post Instagram Feed 1080×1080 — "Quote/Motivazione"**
```
| Step | Azione in Figma | Parametri Esatti |

Step 1: Frame 1080×1080, Fill: colore brand primario
Step 2: Auto Layout Vertical, Padding 60px, Gap 32px, Center-Center
Step 3: Linea decorativa 80×3px, colore accent, opacity 60%
Step 4: Testo quote [Heading Font] 48-56px, 700, #FFFFFF, Center, max-w 840px
Step 5: Testo autore [Body Font] 24px, 400, #FFFFFF 80%, Center, UPPERCASE, LS 0.08em
Step 6: Linea decorativa bottom (come step 3)
Step 7: Logo 40px height, opacity 60%
Step 8: Export PNG 1x sRGB

Almeno 8 step con TUTTI i parametri
```

**2.2 Carosello Educativo Instagram (10 slide)**
```
Per OGNI slide:
| Slide | Contenuto | Layout | Font Size Heading | Font Size Body |

1-Cover: Titolo + "Swipe →" + avatar
2-Problema: statistica shock
3-8-Contenuto: un punto per slide, numerato
9-Recap: riassunto punti chiave
10-CTA: "Salva questo post!" + "Seguimi"
```

**2.3 Post LinkedIn Professionale 1200×627**
```
| Step | Azione | Parametri |

Split layout: Left 55% brand scuro + Right 45% immagine
Gradient overlay sull'immagine
Heading: Montserrat 700, 40px, #FFFFFF, x:50 y:80
Subheading: Open Sans 400, 22px, #E2E8F0
Data/Stats: Montserrat 700, 56px, accent #F59E0B
Logo+nome: 32px height, x:50 y:570, opacity 80%
```

**2.4 YouTube Thumbnail 1280×720**
```
| Step | Azione | Parametri |

- Foto soggetto mezzo busto, posizione destra (x:640-1280)
- Gradient radiale sfondo
- Testo: Oswald 800, 72-96px, #FFFFFF, posizione Left
- Keyword in colore accent con bg box
- Badge angolo superiore sx
- NO logo (YouTube lo mostra)
- TEST: leggibile a 120×67px
```

**2.5 Pinterest Pin 1000×1500**
```
Template step-by-step completo per pin verticale
```

**2.6 Facebook Cover Page 1640×924**
```
Template con safe zone centro per mobile (1200×450)
```

### §3. BEST PRACTICE ENGAGEMENT VISIVO

**3.1 Regole d'Oro**
```
| Regola | Spiegazione | Implementazione |

- Testo max 20% superficie (FB Ads penalizza)
- Primi 3 secondi: messaggio istantaneo
- Volti umani +38% engagement
- Consistenza visiva nel feed
- Mobile-first: font min 24px su 1080px
- Contrasto > estetica
- CTA singola per post
- Pattern interrupt per rompere lo scroll
```

**3.2 Errori Fatali**
```
| Errore | Conseguenza | Soluzione |

- Font <20px → illeggibile mobile
- No contrasto → testo invisibile
- Logo enorme → sembra pubblicità
- Troppi elementi → nessun focal point
- Colori fuori brand → profilo incoerente
- Safe zone ignorate → testo coperto da UI
- Export bassa qualità → immagine sgranata
```

### §4. CONTENT CALENDAR VISIVO

```
Template mix settimanale:

| Giorno | Tipo Contenuto | Formato | Template § | Obiettivo |

Lunedì: Motivazionale/Quote → 1080×1080
Martedì: Educativo/How-to → Carosello 1080×1350
Mercoledì: Behind the scenes → Story 1080×1920
Giovedì: Prodotto/Servizio → 1080×1080
Venerdì: Social proof/Recensione → 1080×1350
Sabato: Intrattenimento/Trend → Reel 1080×1920
Domenica: Community/Domanda → 1080×1080
```

### §5. CAROSELLI — GUIDA COMPLETA

**5.1 Struttura Narrativa Carosello**
```
| Tipo Carosello | N. Slide | Struttura | Obiettivo |

- Educativo: 8-10 slide, Cover→Problema→Punti→Recap→CTA
- Prodotto: 5-7 slide, Hero→Features→Dettagli→Prezzo→CTA
- Storytelling: 6-8 slide, Hook→Sviluppo→Climax→Resolution→CTA
- Prima/Dopo: 4-6 slide, Before→After alternati→CTA
- Checklist: 6-10 slide, Cover→Check items→Summary→CTA
```

**5.2 Regole Coerenza tra Slide**
```
- Stessa posizione titolo su tutte le slide
- Stessa palette colori
- Numerazione progressiva visibile
- Indicatore "Swipe →" sulla prima slide
- Ultima slide SEMPRE con CTA
```

### §6. CHECKLIST SOCIAL MEDIA DESIGN

```
PRE-DESIGN
□ Brief: piattaforma, messaggio, CTA, target
□ Formato corretto selezionato
□ Safe zone identificate

DESIGN
□ Font body ≥ 24px su 1080px
□ Max 3-4 elementi per frame
□ Gerarchia visiva 3+ livelli
□ CTA unica e chiara
□ Logo discreto (max 40-60px height)
□ Testo su foto: overlay applicato

EXPORT
□ PNG 1x per social
□ Qualità massima
□ Profilo sRGB
□ Naming: [client]-[platform]-[type]-[date]

VERIFICA
□ Testato zoom 50% (simula mobile)
□ Testo leggibile in 1 secondo
□ Safe zone rispettate
□ Consistente con feed/profilo esistente
```

---

## OUTPUT ATTESO

Genera **1200-1600 righe** con template step-by-step COMPLETI per Figma, coordinate px esatte, regole di engagement validate, content calendar. Nessun template generico.
