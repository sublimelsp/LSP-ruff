# LSP-ruff-lsp

This is a helper package that automatically installs and updates [ruff-lsp](https://github.com/charliermarsh/ruff-lsp) for you. Ruff is an extremely fast Python linter and code transformation tool, written in Rust.

To use this package, you must have:

- An executable `python` (on Windows) or `python3` (on Linux/macOS)
- The [LSP](https://packagecontrol.io/packages/LSP) package
- For Ubuntu and Debian users, you must also install python3-venv with apt
- It's recommended to also install the [LSP-json](https://packagecontrol.io/packages/LSP-json) package which will provide auto-completion and validation for this package's settings.