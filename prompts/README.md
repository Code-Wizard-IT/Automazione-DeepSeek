# Prompts Folder

Place your prompt `.md` files here.

## Naming Convention

Files must follow this pattern:
```
{PREFIX}{NN}-{TOPIC}.md
```

Where:
- `{PREFIX}` matches `PROMPT_FILE_PREFIX` in `config.py` (default: `PROMPT-FIGMA-`)
- `{NN}` is the zero-padded prompt number (01, 02, 03...)
- `{TOPIC}` is the topic name (used in output folder names)

## Examples

```
PROMPT-FIGMA-01-FUNDAMENTALS.md
PROMPT-FIGMA-02-TYPOGRAPHY.md
PROMPT-FIGMA-03-COLOR-SYSTEMS.md
```

## Custom naming

To use different naming, edit `config.py`:

```python
PROMPT_FILE_PREFIX = "PROMPT-REACT-"    # your prefix
PROMPT_COUNT = 8                         # how many prompts
DISPLAY_PREFIX = "REACT-"               # display name prefix
```

Then create files like:
```
PROMPT-REACT-01-BASICS.md
PROMPT-REACT-02-HOOKS.md
...
```
