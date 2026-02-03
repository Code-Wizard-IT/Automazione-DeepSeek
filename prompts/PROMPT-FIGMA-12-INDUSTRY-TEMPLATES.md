# PROMPT DEEPSEEK: CATALOGO INDUSTRY-TEMPLATES v1

## ISTRUZIONI PER IL MODELLO

Genera un catalogo COMPLETO di template grafici pronti all'uso per 10 settori: per ogni settore fornisci brand kit (colori, font, mood), template step-by-step per Instagram Feed, Instagram Story, Biglietto da Visita, Volantino A5, Facebook Cover. Ogni step con parametri Figma ESATTI (px, HEX, font name, weight, posizione).

**Contesto:** Ogni template deve essere realizzabile in Figma da zero seguendo i passi. Font SOLO Google Fonts. Colori in HEX. Dimensioni in px.

**NOTA:** Questo catalogo è LUNGO. Se raggiungi il limite di output, fermati alla fine del settore corrente e scrivi "CONTINUA" — l'utente invierà "CONTINUA" per proseguire.

---

## SEZIONI RICHIESTE

### §1. SETTORE: RISTORAZIONE / FOOD & BEVERAGE

**1.1 Brand Kit**
```
| Elemento | Valore |
- Heading Font: DM Serif Display (Google Fonts)
- Body Font: DM Sans (Google Fonts)
- Primary: #8B4513 (Saddle Brown — caldo, terroso)
- Secondary: #F5F0EB (Crema chiaro)
- Accent: #D4A574 (Dorato caldo)
- Dark: #2C1810 (Marrone scurissimo)
- Light: #FFF8F0 (Bianco caldo)
- Mood: Caldo, invitante, autentico, appetitoso
- Icone stile: outline, stroke 1.5px, colore Primary
```

**1.2 Instagram Feed Post 1080×1080 — "Piatto del Giorno"**
```
| Step | Azione Figma | Parametri |

1. Frame 1080×1080, Fill #FFF8F0
2. Auto Layout Vertical, Padding 0, Gap 0, Align Center-Center
3. Immagine piatto: Rectangle 1080×650, Fill Image (Clip), posizione top
4. Overlay gradient su foto: Linear Gradient 180° → #2C1810 0% op.0 → #2C1810 100% op.70
5. Fascia bottom: Rectangle 1080×430, Fill #FFF8F0
6. Dentro fascia, Auto Layout Vertical, Padding 40 60 40 60, Gap 16, Center
7. Label: DM Sans 600, 18px, #D4A574, UPPERCASE, LS 0.12em → "PIATTO DEL GIORNO"
8. Nome piatto: DM Serif Display 400, 40px, #2C1810, Center → "Risotto ai Porcini"
9. Descrizione: DM Sans 400, 20px, #8B4513 80%, Center, max 2 righe
10. Linea: Rectangle 60×2, Fill #D4A574
11. Prezzo: DM Serif Display 400, 36px, #D4A574 → "€ 18"
12. Logo: 36px height, #8B4513 opacity 50%, bottom center
13. Export PNG 1x sRGB
```

**1.3 Instagram Story 1080×1920 — "Menu Speciale"**
```
| Step | Azione | Parametri |

1. Frame 1080×1920, Fill #2C1810
2. Safe zone: top 200px, bottom 250px liberi
3. Foto bg: Fill Image 1080×1920, Opacity 30%
4. Auto Layout Vertical, Padding 240 60 300 60, Gap 24, Center
5. Badge top: Pill shape (radius 9999), Fill #D4A574, Padding 12 24
   → DM Sans 600, 14px, #2C1810, UPPERCASE, LS 0.1em → "MENU SPECIALE"
6. Titolo: DM Serif Display, 52px, #FFF8F0, Center → "Cena di San Valentino"
7. Sottotitolo: DM Sans 400, 22px, #F5F0EB 80%, Center
8. Divider: decorativo 80×1, #D4A574
9. Menu items (×3): DM Sans 500, 20px, #FFF8F0, Center
10. Prezzo: DM Serif Display, 44px, #D4A574 → "€ 45 a persona"
11. CTA: DM Sans 600, 18px, #D4A574, UPPERCASE → "PRENOTA ORA"
12. Logo: 32px, #FFF8F0 opacity 40%, y:1700
```

**1.4 Biglietto da Visita 1075×720px (@300DPI = 91×61mm con bleed)**
```
FRONTE:
| Step | Azione | Parametri |
1. Frame 1075×720, Fill #FFF8F0
2. Guide bleed: 35px dal bordo, Guide safe zone: 95px dal bordo
3. Logo centrato: height 80px, #8B4513
4. Nome: DM Serif Display 400, 44px (#2C1810), Center, y:420
5. Ruolo: DM Sans 400, 24px (#8B4513), Center, y:480
6. Linea: 120×2, #D4A574, Center, y:520

RETRO:
1. Frame 1075×720, Fill #2C1810
2. Auto Layout Vertical, Padding 95, Gap 20, Left-Center
3. Telefono: DM Sans 400, 24px, #F5F0EB → "+39 02 1234567"
4. Email: DM Sans 400, 24px, #F5F0EB → "info@ristorante.it"
5. Web: DM Sans 400, 24px, #D4A574 → "www.ristorante.it"
6. Indirizzo: DM Sans 400, 20px, #F5F0EB 70% → "Via Roma 1, Milano"
7. QR Code: 180×180px, #FFF8F0, angolo bottom-right, 95px dal bordo
```

**1.5 Volantino A5 1819×2551px (@300DPI = 154×216mm con bleed)**
```
| Step | Azione | Parametri |

1. Frame 1819×2551, Fill #FFF8F0
2. Guide bleed: 35px, safe zone: 95px
3. Foto hero: 1819×1000, top, Fill Image Clip
4. Overlay gradient bottom: #FFF8F0 op.0 → #FFF8F0 100%
5. Logo: 100px height, Center, y:1050
6. Titolo: DM Serif Display, 72px, #2C1810, Center, y:1200
7. Sottotitolo: DM Sans 400, 28px, #8B4513, Center, y:1300
8. Divider: 160×2, #D4A574, Center, y:1370
9. 3 piatti (Auto Layout V, Gap 24, y:1420):
   → DM Sans 500, 24px, #2C1810 + prezzo DM Serif 24px #D4A574
10. CTA Box: Rectangle 500×80, Fill #8B4513, Radius 8, Center, y:1900
    → DM Sans 700, 24px, #FFF8F0 → "PRENOTA: 02 1234567"
11. Info: DM Sans 400, 20px, #8B4513 60%, Center, y:2050
12. Social icons: 24×24, #8B4513, gap 16, Center, y:2150
```

**1.6 Facebook Cover 1640×924**
```
| Step | Azione | Parametri |

1. Frame 1640×924, Fill #2C1810
2. Foto bg: Opacity 25%, Fill Image Cover
3. Auto Layout Vertical, Padding 200 120 200 120, Gap 24, Center
4. Logo: 80px height, #FFF8F0
5. Nome ristorante: DM Serif Display, 56px, #FFF8F0
6. Tagline: DM Sans 400, 24px, #D4A574
7. Safe zone mobile: contenuto entro x:400-1240 (centro 840px)
```

---

### §2. SETTORE: STUDIO LEGALE / PROFESSIONALE

**2.1 Brand Kit**
```
- Heading: Cormorant Garamond (Google Fonts)
- Body: Inter (Google Fonts)
- Primary: #1B365D (Navy scuro)
- Secondary: #F0EDE8 (Avorio)
- Accent: #C5A572 (Oro opaco)
- Dark: #0D1B2A (Quasi nero blu)
- Light: #F8F6F3 (Bianco caldo)
- Mood: Autorevole, affidabile, elegante, discreto
```

**2.2 Instagram Feed 1080×1080 — "Citazione Legale"**
```
| Step | Azione | Parametri |

1. Frame 1080×1080, Fill #0D1B2A
2. Border interno: Rectangle 1000×1000, No Fill, Stroke 1px #C5A572 20%, Center
3. Auto Layout V, Padding 80, Gap 24, Center-Center
4. Virgolette decorative: Cormorant Garamond 400, 120px, #C5A572 30% → "
5. Quote: Cormorant Garamond 400 Italic, 36px, #F8F6F3, Center, max 4 righe
6. Autore: Inter 500, 16px, #C5A572, UPPERCASE, LS 0.1em, Center
7. Linea: 60×1, #C5A572
8. Logo: 28px height, #F8F6F3 opacity 40%
```

**2.3 Story, Biglietto, Volantino, Facebook Cover**
```
Stessa struttura dettagliata del settore Ristorazione,
con parametri adattati al brand kit Legale.
Ogni deliverable con tutti gli step e parametri px esatti.
```

---

### §3. SETTORE: FITNESS / PALESTRA

**3.1 Brand Kit**
```
- Heading: Oswald (Google Fonts)
- Body: Lato (Google Fonts)
- Primary: #FF4500 (Arancio energia)
- Secondary: #1A1A2E (Blu notte)
- Accent: #00FF87 (Verde neon)
- Dark: #0F0F0F (Nero profondo)
- Light: #F5F5F5 (Grigio chiarissimo)
- Mood: Energico, potente, motivazionale, dinamico
```

**3.2 Instagram Feed 1080×1080 — "Offerta Abbonamento"**
```
| Step | Azione | Parametri |

1. Frame 1080×1080, Fill #0F0F0F
2. Foto atleta: Fill Image, Opacity 40%, Blend Multiply
3. Diagonal shape: Vector path angolato, Fill #FF4500, 30% frame bottom-left
4. Auto Layout V, Padding 60, Gap 20, Left-Bottom
5. Badge: Pill #00FF87, Padding 8 20 → Lato 700, 14px, #0F0F0F, UPPERCASE → "PROMO"
6. Headline: Oswald 700, 64px, #FFFFFF, UPPERCASE → "ABBONAMENTO ANNUALE"
7. Prezzo old: Lato 400, 28px, #FFFFFF 50%, text-decoration line-through → "€599"
8. Prezzo new: Oswald 700, 72px, #00FF87 → "€299"
9. CTA: Lato 700, 20px, #FF4500, UPPERCASE → "ISCRIVITI ORA →"
10. Logo: 40px, #FFFFFF opacity 60%, bottom-right
```

**3.3 Story, Biglietto, Volantino, Facebook Cover**
```
Struttura completa come Ristorazione, adattata al brand kit Fitness.
Step-by-step con coordinate px esatte.
```

---

### §4. SETTORE: BEAUTY / SALONE / SPA

**4.1 Brand Kit**
```
- Heading: Playfair Display (Google Fonts)
- Body: Nunito Sans (Google Fonts)
- Primary: #D4A5A5 (Rosa antico)
- Secondary: #F9F3F0 (Rosa pallido)
- Accent: #B8860B (Oro)
- Dark: #3C2A2A (Marrone rosato scuro)
- Light: #FFFBF9 (Bianco rosato)
- Mood: Femminile, lussuoso, rilassante, raffinato
```

**4.2-4.6 Template completi**
```
IG Feed, IG Story, Biglietto, Volantino, FB Cover
— struttura identica alla Ristorazione, parametri adattati
```

---

### §5. SETTORE: TECH / STARTUP / SAAS

**5.1 Brand Kit**
```
- Heading: Space Grotesk (Google Fonts)
- Body: Inter (Google Fonts)
- Primary: #6366F1 (Indigo)
- Secondary: #0F172A (Slate scurissimo)
- Accent: #22D3EE (Cyan)
- Dark: #020617 (Quasi nero)
- Light: #F8FAFC (Grigio chiarissimo)
- Mood: Innovativo, pulito, futuristico, affidabile
```

**5.2-5.6 Template completi**
```
IG Feed, IG Story, Biglietto, Volantino, FB Cover
— focus su design tech/minimal con accent neon
```

---

### §6. SETTORE: IMMOBILIARE / REAL ESTATE

**6.1 Brand Kit**
```
- Heading: Montserrat (Google Fonts)
- Body: Open Sans (Google Fonts)
- Primary: #1F4E79 (Blu corporate)
- Secondary: #F0F4F8 (Grigio azzurro)
- Accent: #E8A838 (Oro caldo)
- Dark: #1A202C (Antracite)
- Light: #FFFFFF
- Mood: Affidabile, professionale, aspirazionale, solido
```

**6.2-6.6 Template completi**
```
IG Feed (annuncio immobile), IG Story, Biglietto, Volantino, FB Cover
— con zona immagine immobile prominente + prezzo + m² + dettagli
```

---

### §7. SETTORE: HEALTHCARE / MEDICO / DENTISTA

**7.1 Brand Kit**
```
- Heading: Raleway (Google Fonts)
- Body: Source Sans 3 (Google Fonts)
- Primary: #0EA5E9 (Azzurro rassicurante)
- Secondary: #F0F9FF (Azzurro chiarissimo)
- Accent: #10B981 (Verde salute)
- Dark: #0C4A6E (Blu scuro)
- Light: #FFFFFF
- Mood: Rassicurante, pulito, competente, accessibile
```

**7.2-7.6 Template completi**

---

### §8. SETTORE: RETAIL / NEGOZIO / ECOMMERCE

**8.1 Brand Kit**
```
- Heading: Poppins (Google Fonts)
- Body: Nunito (Google Fonts)
- Primary: #7C3AED (Viola vivace)
- Secondary: #FEF3C7 (Giallo pallido)
- Accent: #F59E0B (Ambra)
- Dark: #1E1B4B (Viola scurissimo)
- Light: #FFFBEB (Crema)
- Mood: Vivace, giovane, attraente, conveniente
```

**8.2-8.6 Template completi — focus promo/sconto**

---

### §9. SETTORE: FOTOGRAFO / CREATIVO

**9.1 Brand Kit**
```
- Heading: Sora (Google Fonts) o Outfit
- Body: Work Sans (Google Fonts)
- Primary: #1A1A1A (Nero quasi puro)
- Secondary: #FAFAFA (Bianco quasi puro)
- Accent: #F97316 (Arancio creativo)
- Dark: #0A0A0A
- Light: #FFFFFF
- Mood: Minimal, artistico, elegante, visual-first
```

**9.2-9.6 Template completi — focus galleria immagini, minimal text**

---

### §10. SETTORE: EDUCAZIONE / FORMAZIONE / CORSI

**10.1 Brand Kit**
```
- Heading: Lexend (Google Fonts)
- Body: Atkinson Hyperlegible (Google Fonts)
- Primary: #2563EB (Blu accessibile)
- Secondary: #DBEAFE (Blu chiarissimo)
- Accent: #F97316 (Arancio energia)
- Dark: #1E3A5F (Blu navy)
- Light: #F8FAFC
- Mood: Accessibile, chiaro, stimolante, inclusivo
- Nota: Atkinson Hyperlegible → massima leggibilità, anche dislessia
```

**10.2-10.6 Template completi — focus chiarezza, leggibilità, CTA iscrizione**

---

### §11. TABELLA RIEPILOGATIVA CROSS-SETTORE

```
| Settore | Heading Font | Body Font | Primary | Secondary | Accent | Mood |

1. Ristorazione → DM Serif Display + DM Sans → #8B4513 #F5F0EB #D4A574
2. Legale → Cormorant Garamond + Inter → #1B365D #F0EDE8 #C5A572
3. Fitness → Oswald + Lato → #FF4500 #1A1A2E #00FF87
4. Beauty/Spa → Playfair Display + Nunito Sans → #D4A5A5 #F9F3F0 #B8860B
5. Tech/Startup → Space Grotesk + Inter → #6366F1 #0F172A #22D3EE
6. Immobiliare → Montserrat + Open Sans → #1F4E79 #F0F4F8 #E8A838
7. Healthcare → Raleway + Source Sans 3 → #0EA5E9 #F0F9FF #10B981
8. Retail → Poppins + Nunito → #7C3AED #FEF3C7 #F59E0B
9. Fotografo → Sora + Work Sans → #1A1A1A #FAFAFA #F97316
10. Educazione → Lexend + Atkinson Hyperlegible → #2563EB #DBEAFE #F97316
```

### §12. CHECKLIST PER SETTORE

```
PER OGNI NUOVO CLIENTE:
□ Identificare settore dalla tabella §11
□ Applicare Brand Kit (o personalizzare se ha già colori/font)
□ Selezionare template appropriato per ogni deliverable
□ Adattare testi, foto, logo
□ Verificare contrasto WCAG con colori scelti
□ Testare leggibilità mobile (zoom 50% su social)
□ Export con naming: [client]-[platform]-[type]-[YYYYMMDD]

PERSONALIZZAZIONE:
□ Se il cliente ha già colori brand → sostituire Primary/Secondary/Accent
□ Se il cliente ha già font → sostituire Heading/Body
□ Se il cliente ha logo → inserire al posto del placeholder
□ Mantenere la STRUTTURA del template anche con colori/font diversi
```

---

## OUTPUT ATTESO

Genera **1500-2500 righe**. Per i PRIMI 3 SETTORI (Ristorazione, Legale, Fitness) fornisci TUTTI i 5 template completi step-by-step con OGNI parametro. Per i settori 4-10 fornisci Brand Kit completo + Instagram Feed step-by-step completo + struttura degli altri 4 template con parametri chiave. Se raggiungi il limite, scrivi "CONTINUA".
