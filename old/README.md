# 🤖 Automazione DeepSeek

Tampermonkey userscript per automazione multi-prompt su [DeepSeek Chat](https://chat.deepseek.com/).

Invia automaticamente una sequenza di prompt a DeepSeek, rileva il completamento delle risposte con il sistema **Triple-Lock**, ed esporta ogni output come file `.txt` organizzati in cartelle sul disco locale.

## ✨ Funzionalità

- **Multi-prompt sequenziale**: invia N prompt in sequenza, ognuno in una nuova chat
- **Triple-Lock detection**: conferma il completamento della risposta con 3 condizioni simultanee verificate 5 volte
- **Export su disco**: salvataggio diretto tramite File System Access API (no download manuali)
- **Parti separate**: se la risposta viene troncata, esporta parti incrementali (`parte-1.txt`, `parte-2.txt`, ...)
- **Continue automatico**: rileva il tasto "Continue generating" e lo clicca automaticamente
- **Stale detection**: se la risposta si blocca, invia "Continua" come testo
- **Auto-resume**: riprende da dove si era interrotto dopo un refresh della pagina
- **UI integrata**: pannello di controllo draggable con stato, progresso e log

## 📁 Struttura Repository

```
├── deepseek-automation-template.user.js   # Script template (senza prompt)
├── build_script_v2.py                     # Build script Python — assembla template + prompt
├── prompts/                               # Prompt sorgente in Markdown
│   ├── PROMPT-FIGMA-01-FUNDAMENTALS.md
│   ├── PROMPT-FIGMA-02-TYPOGRAPHY.md
│   └── ...
└── README.md
```

## 🚀 Quick Start

### 1. Usa il template direttamente

1. Installa [Tampermonkey](https://www.tampermonkey.net/)
2. Copia il contenuto di `deepseek-automation-template.user.js`
3. Aggiungi i tuoi prompt nell'array `PROMPTS` seguendo il formato documentato nel file
4. Vai su https://chat.deepseek.com/ e clicca **Start All**

### 2. Usa il build script (consigliato per molti prompt)

1. Metti i tuoi prompt come file `.md` nella cartella `prompts/`
2. Modifica `build_script_v2.py` per puntare alla tua cartella prompt
3. Esegui: `python build_script_v2.py`
4. Installa il file `.user.js` generato in Tampermonkey

## 📝 Formato Prompt

Ogni prompt deve terminare con un marker di completamento:

```
Il tuo prompt qui...

Alla fine, scrivi esattamente questo marker:
===PROMPT_N_COMPLETATO===
```

Dove `N` è l'ID sequenziale del prompt (1, 2, 3, ...).

## ⚙️ Configurazione

Parametri principali in `CONFIG`:

| Parametro | Default | Descrizione |
|---|---|---|
| `TYPING_DELAY` | 50ms | Ritardo tra caratteri durante la digitazione |
| `POLL_INTERVAL` | 3000ms | Intervallo di polling per controllare la risposta |
| `MAX_POLL_CYCLES` | 200 | Cicli massimi prima del timeout |
| `STALE_THRESHOLD` | 5 | Cicli senza cambiamenti prima di inviare "Continua" |
| `TRIPLE_LOCK_REQUIRED` | 5 | Check consecutivi necessari per confermare il completamento |
| `CONTINUE_MAX_RETRIES` | 15 | Tentativi massimi di "Continue" |
| `MIN_PART_SIZE` | 100 | Caratteri minimi per salvare una parte |

## 📂 Output

L'output viene salvato nella cartella selezionata con questa struttura:

```
output/
├── 01-PROMPT-NAME/
│   ├── PROMPT-NAME-parte-1.txt
│   └── PROMPT-NAME-parte-2.txt
├── 02-ANOTHER-PROMPT/
│   └── ANOTHER-PROMPT-parte-1.txt
└── ...
```

## 🔒 Triple-Lock System

Il sistema Triple-Lock conferma il completamento verificando **3 condizioni simultaneamente, 5 volte consecutive** (con 2 secondi tra ogni check):

1. **Marker trovato** nel testo della risposta
2. **Marker negli ultimi 500 caratteri** (è davvero alla fine)
3. **Generazione fermata** (nessun bottone "Stop" attivo)

## 📄 Licenza

MIT
