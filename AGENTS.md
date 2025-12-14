# AGENTS.md

## Build/Lint/Test Commands
- **Run all tests**: `uv run apps/run_all.py`
- **Run single test**: `uv run apps/<framework>_hello_world.py`
- **Lint**: `ruff check .`
- **Format**: `ruff format .`
- **Type check**: `mypy .` (if configured)

## Code Style Guidelines
- **File Structure**: Framework files as `apps/<framework>_hello_world.py` (snake_case), use PEP 723 `/// script` metadata.
- **Imports**: Stdlib first, third-party second, one blank line between groups, no unused imports.
- **Naming**: Functions/variables: snake_case; constants: UPPER_CASE; files: snake_case.py.
- **Type Hints**: All functions with return annotations, use built-ins, import from typing as needed.
- **Formatting**: 4 spaces indent, 88 char max line, 2 blanks between functions/classes, 1 within.
- **Application**: Host 0.0.0.0, port 8000, response contains "Hello, World!", `def main() -> None:` with guard.
- **Error Handling**: Minimal in examples, use try/except when necessary.
- **Comments**: None unless complex, docstrings for public APIs, explain why not what.
- **Security**: Follow best practices; never expose or log secrets/keys; never commit secrets.
