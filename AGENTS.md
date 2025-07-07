# AGENTS.md

This file provides guidance to coding agents (Claude Code, Codex CLI, Gemini CLI) when working with code in this repository.

## Project Overview

This is a Python project that filters Swedish word lists from SAOL 14 to create a compatible word list for WordFeud. The main purpose is to process the comprehensive Swedish Academy word list (SAOL 14) and remove words that are not valid in WordFeud according to specific rules.

## Key Architecture

The project consists of:
- `wordfeud_filtrering.py`: Main filtering module with functions for different filtering stages
- `tests/test_hashes.py`: Hash validation tests to ensure data integrity
- Data files: `saol_wordlist.txt`, `saol2018clean.csv`, `WordFeud_ordlista.txt`

The filtering pipeline processes words through several stages:
1. Remove words with word class "namn" (proper nouns)
2. Clean invalid characters and handle diacritical marks
3. Filter by word length (2-15 characters)
4. Remove duplicates and sort

## Code

- Keep the code short. Avoid non-essential error handling.
- Assume Python 3.13 or later.

## Development Commands

### Running the main script
```bash
python wordfeud_filtrering.py
# With custom files:
python wordfeud_filtrering.py --saol saol_wordlist.txt --saol-csv saol2018clean.csv --output WordFeud_ordlista.txt
```

### Running tests
```bash
# Run hash validation tests
python -m pytest tests/test_hashes.py
```

### Code quality and formatting
```bash
# Format code with black
black wordfeud_filtrering.py tests/

# Type checking with mypy
mypy wordfeud_filtrering.py tests/

# Run pre-commit hooks
pre-commit run --all-files
```

## Word Filtering Rules

WordFeud excludes words that:
- Have word class "namn" (proper nouns)
- Are shorter than 2 or longer than 15 characters
- Contain Q, W, Ê, Ñ, Ç, Ü, Æ, hyphens, colons, slashes, apostrophes, numbers, or spaces
- Are parts of compound words with spaces (e.g., "priori" from "a priori")

Diacritical marks É, È, À are converted to E, E, A respectively.

## Data Files

- `saol_wordlist.txt`: Full SAOL 14 word list with all word forms
- `saol2018clean.csv`: SAOL 14 without all forms, used to identify proper nouns
- `WordFeud_ordlista.txt`: Final filtered word list for WordFeud

The project uses git hash validation to ensure data file integrity.
