# LSP-ruff-lsp

This is a helper package that automatically installs and updates [ruff-lsp](https://github.com/charliermarsh/ruff-lsp) for you. Ruff is an extremely fast Python linter and code transformation tool, written in Rust.

## Requirements

To use this package, you must have:

- An executable `python` (on Windows) or `python3` (on Linux/macOS)
- The [LSP](https://packagecontrol.io/packages/LSP) package
- For Ubuntu and Debian users, you must also install python3-venv with apt
- It's recommended to also install the [LSP-json](https://packagecontrol.io/packages/LSP-json) package which will provide auto-completion and validation for this package's settings.

## Code Actions on Save

The following "code actions on save" are supported:

 - `source.fixAll`
 - `source.organizeImports`
 - `source.fixAll.ruff`
 - `source.organizeImports.ruff`

You can use those with the `lsp_code_actions_on_save` LSP Setting to automatically apply specific actions on saving the file.
