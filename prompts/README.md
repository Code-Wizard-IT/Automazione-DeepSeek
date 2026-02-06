# Prompts Directory

Place your prompt `.md` files here.

## Naming Convention

Files must follow this pattern:
```
{PROMPT_FILE_PREFIX}{NN}-{TOPIC}.md
```

Where:
- `{PROMPT_FILE_PREFIX}` is defined in `config.py` (default: `PROMPT-PROJECT-`)
- `{NN}` is a two-digit number (01, 02, 03...)
- `{TOPIC}` is a descriptive name for the prompt

## Examples

With default config:
```
PROMPT-PROJECT-01-INTRO.md
PROMPT-PROJECT-02-CONTENT.md
PROMPT-PROJECT-03-CONCLUSION.md
```

With custom prefix `PROMPT-MYAPP-`:
```
PROMPT-MYAPP-01-SETUP.md
PROMPT-MYAPP-02-FEATURES.md
PROMPT-MYAPP-03-DEPLOYMENT.md
```

## Configuration

Update these values in `config.py`:
- `PROMPT_DIR`: Path to this directory
- `PROMPT_FILE_PREFIX`: Your custom prefix
- `PROMPT_COUNT`: Total number of prompts
