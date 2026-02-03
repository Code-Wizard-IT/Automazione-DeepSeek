# 🎨 Automazione DeepSeek — Figma Graphic Design Catalogs

Automazione completa per generare cataloghi di Graphic Design su DeepSeek Chat, con esportazione diretta su disco.

## Versione corrente: v2.1

### Novità v2.1 (rispetto a v2.0)
- **Anti-detection**: jitter randomizzato sul typing delay (30-90ms), pause inter-prompt randomizzate (10-30s)
- **Pause periodiche**: break automatico di 3-5 minuti ogni 8 prompt (simulazione comportamento umano)
- **Error recovery**: rilevamento automatico "Server is busy" e "Too many messages" con retry + backoff
- **Selector aggiornato**: compatibile con le nuove classi CSS di DeepSeek (`.ds-markdown`)

### Archivio
La versione precedente (v2.0) è disponibile nella cartella [`old/`](old/).

---

## Struttura del progetto

```
├── build_script_v2.1.py              # Build script (assembla template + prompt)
├── prompts/                           # 15 file markdown con i prompt
│   ├── PROMPT-FIGMA-01-FUNDAMENTALS.md
│   ├── PROMPT-FIGMA-02-TYPOGRAPHY.md
│   └── ... (12 principali + 3 master/knowledge)
├── old/                               # Versione precedente (v2.0)
│   ├── build_script_v2.py
│   ├── deepseek-automation-template.user.js
│   └── README.md
├── README.md                          # Questo file
└── .gitignore
```

## Quick Start

### Metodo 1: Build Script (consigliato)

1. Clona il repo
2. Posiziona i file prompt nella cartella `prompts/`
3. Modifica i percorsi nel build script se necessario
4. Esegui: `python build_script_v2.1.py`
5. Lo script genera `figma-deepseek-automation-v2.1.user.js`
6. Installa come UserScript (Tampermonkey) oppure inietta direttamente nella console

### Metodo 2: Iniezione diretta (Proposal A)

1. Apri `chat.deepseek.com` nel browser
2. Apri la console sviluppatore (F12)
3. Incolla il contenuto dello script generato
4. Il pannello UI appare in basso a sinistra
5. Seleziona la cartella di output cliccando l'indicatore 📁
6. Clicca "▶ Start All"

---

## Configurazione

| Parametro | Default | Descrizione |
|---|---|---|
| `TYPING_DELAY_MIN/MAX` | 30-90ms | Range jitter digitazione |
| `INTER_PROMPT_PAUSE_MIN/MAX` | 10-30s | Pausa randomizzata tra prompt |
| `LONG_BREAK_EVERY` | 8 | Break lungo ogni N prompt |
| `LONG_BREAK_MIN/MAX` | 3-5 min | Durata break lungo |
| `POLL_INTERVAL` | 3000ms | Intervallo polling risposta |
| `MAX_POLL_CYCLES` | 200 | Cicli max di polling |
| `STALE_THRESHOLD` | 5 | Cicli stallo prima di "Continua" |
| `TRIPLE_LOCK_REQUIRED` | 5 | Conferme consecutive per completamento |
| `RATE_LIMIT_WAIT` | 60s | Attesa su rate limit |
| `SERVER_BUSY_WAIT` | 30s | Attesa su server busy |
| `ERROR_MAX_RETRIES` | 10 | Max tentativi per errore |

## Formato prompt

Ogni prompt **deve** contenere nella risposta attesa il marker di completamento:

```
===PROMPT_{N}_COMPLETATO===
```

Il sistema Triple-Lock verifica:
1. ✅ Marker presente nel testo
2. ✅ Marker nelle ultime 500 caratteri
3. ✅ Generazione terminata (nessun pulsante "Stop" visibile)

Solo dopo 5 conferme consecutive il prompt è considerato completato.

## Output

I file vengono salvati nella struttura:
```
output-folder/
├── 01-FIGMA-01-FUNDAMENTALS/
│   ├── FIGMA-01-FUNDAMENTALS-parte-1.txt
│   └── FIGMA-01-FUNDAMENTALS-parte-2.txt  (se continua)
├── 02-FIGMA-02-TYPOGRAPHY/
│   └── FIGMA-02-TYPOGRAPHY-parte-1.txt
└── ...
```

## Anti-Detection

Lo script simula un comportamento umano naturale:
- **Jitter typing**: ogni messaggio ha un delay randomizzato (30-90ms)
- **Pause inter-prompt**: 10-30 secondi casuali tra un prompt e l'altro
- **Break periodici**: 3-5 minuti di pausa ogni 8 prompt completati
- **Error recovery**: se DeepSeek risponde "too frequently" o "server busy", lo script attende e riprova automaticamente

## Console API

```javascript
FIGMA_AUTO.start(1)     // Avvia dal prompt 1
FIGMA_AUTO.start(5)     // Avvia dal prompt 5
FIGMA_AUTO.stop()       // Ferma l'esecuzione
FIGMA_AUTO.status()     // Stato corrente
FIGMA_AUTO.zip()        // Esporta ZIP di tutti i cached
FIGMA_AUTO.selectFolder() // Seleziona cartella output
FIGMA_AUTO.clearCache() // Pulisci cache localStorage
```

## Licenza

MIT
