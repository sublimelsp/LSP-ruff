# LSP-ruff

This is a helper package that automatically installs and updates [ruff](https://github.com/astral-sh/ruff) for you. Ruff is an extremely fast Python linter and code transformation tool, written in Rust.

## Requirements

To use this package, you must have:

- An executable `python` (on Windows) or `python3` (on Linux/macOS)
- The [LSP](https://packagecontrol.io/packages/LSP) package
- For Ubuntu and Debian users, you must also install python3-venv with apt
- It's recommended to also install the [LSP-json](https://packagecontrol.io/packages/LSP-json) package which will provide auto-completion and validation for this package's settings.

## Configuration

There are multiple ways to configure the package and the language server.

- Global configuration: `Preferences > Package Settings > LSP > Servers > LSP-ruff`
- Project-specific configuration:
  From the Command Palette run `Project: Edit Project` and add your settings in:

	```js
	{
		"settings": {
			"LSP": {
				"LSP-ruff": {
					"initializationOptions": {
						"settings": {
							// Put your settings here
						}
					}
				}
			}
		}
	}
	```

## Code Actions on Save

The following "code actions on save" are supported:

 - `source.fixAll`
 - `source.organizeImports`
 - `source.fixAll.ruff`
 - `source.organizeImports.ruff`

You can use those with the `lsp_code_actions_on_save` LSP Setting to automatically apply specific actions on saving the file.
