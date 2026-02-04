# Prompt per Automazione DeepSeek

Copia-incolla questo prompt in qualsiasi nuova chat Claude per avviare o gestire l'automazione.

---

## PROMPT (copia da qui sotto)

```
Ho un sistema di automazione DeepSeek che inietta prompt via Chrome DevTools Protocol.
Tutti i file sono sul mio PC Windows:

- Skill completa: C:\Users\cresc\Documents\Claude_Skills\deepseek-automation\SKILL.md
- Config: C:\Users\cresc\Desktop\Automazione-DeepSeek\config.py
- Launcher principale: C:\Users\cresc\Desktop\start_full_automation.py
- Build script: C:\Users\cresc\Desktop\Automazione-DeepSeek\build_template.py
- Status checker: C:\Users\cresc\Desktop\check_status.py
- Prompt folder: C:\Users\cresc\Desktop\Prompt\
- Output: C:\Users\cresc\Desktop\output deepseek\new\
- GitHub: https://github.com/Code-Wizard-IT/Automazione-DeepSeek

PRIMA DI FARE QUALSIASI COSA: leggi la skill SKILL.md con Desktop Commander per avere il contesto completo.

Comandi rapidi:
- Avvia tutto: python "C:\Users\cresc\Desktop\start_full_automation.py"
- Riprendi da prompt N: python "C:\Users\cresc\Desktop\start_full_automation.py" N
- Controlla stato: python "C:\Users\cresc\Desktop\check_status.py"
- Ricostruisci script: python "C:\Users\cresc\Desktop\Automazione-DeepSeek\build_template.py"

[LA TUA RICHIESTA QUI - es: "avvia dal prompt 5", "controlla lo stato", "modifica il prompt 3"]
```

---

## Esempi di uso

### Avviare l'automazione
```
[incolla il prompt sopra + sostituisci ultima riga con:]
Avvia l'automazione dal prompt 1
```

### Riprendere dal prompt 7
```
[incolla il prompt sopra + sostituisci ultima riga con:]
Riprendi l'automazione dal prompt 7
```

### Controllare lo stato
```
[incolla il prompt sopra + sostituisci ultima riga con:]
Controlla lo stato dell'automazione in corso
```

### Aggiungere nuovi prompt
```
[incolla il prompt sopra + sostituisci ultima riga con:]
Aggiungi un nuovo prompt FIGMA-13 sulla topic "UI Animation" e ricostruisci lo script
```

### Usare come template per altri progetti
```
[incolla il prompt sopra + sostituisci ultima riga con:]
Voglio creare un nuovo set di prompt su React. Modifica config.py per usare
PROMPT_FILE_PREFIX="PROMPT-REACT-", PROMPT_COUNT=8, DISPLAY_PREFIX="REACT-"
e creami i file prompt vuoti nella cartella
```
