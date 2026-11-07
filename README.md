# Zin Ko Htet — AI Assistant & Automation Portfolio

A practical portfolio of small, transparent AI and automation projects, maintained by **Zin Ko Htet**.

## Projects

### Personal AI Assistant (starter)
A safe local Python scaffold that separates user input from assistant logic. The current version is intentionally simple and does not call external services or perform account actions.

## Quick start

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Repository structure

```text
assistant/       Assistant logic
tests/           Automated tests
main.py          Local command-line entry point
.env.example     Example environment configuration
```

## Safety principles

- Never commit API keys, passwords, or personal tokens.
- Keep external actions disabled until explicitly approved and tested.
- Prefer dry runs and clear logs for future automation workflows.

## Roadmap

- [x] Initial Python project scaffold
- [x] Basic unit tests
- [ ] Burmese and Japanese language preferences
- [ ] Optional model API integration
- [ ] Documented n8n automation examples
- [ ] Releases with test notes

## Maintainer

**Zin Ko Htet** — project owner and maintainer.

Commits in this repository document actual changes made to the project. No fabricated activity or release history is used.
