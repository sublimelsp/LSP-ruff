from __future__ import annotations
from typing import final, override
from lsp_utils.pip_client_handler import PipClientHandler
import sublime


@final
class RuffLsp(PipClientHandler):
    package_name = str(__package__)
    requirements_txt_path = "requirements.txt"
    server_filename = "ruff"

    @classmethod
    @override
    def should_ignore(cls, view: sublime.View) -> bool:
        return bool(
            # REPL views (https://github.com/sublimelsp/LSP-pyright/issues/343)
            view.settings().get("repl")
            # Python-like syntax test files
            or view.substr(sublime.Region(0, 20)).startswith("# SYNTAX TEST ")
        )


def plugin_loaded() -> None:
    RuffLsp.setup()


def plugin_unloaded() -> None:
    RuffLsp.cleanup()
