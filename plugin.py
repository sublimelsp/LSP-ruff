from __future__ import annotations
from LSP.plugin import ClientConfig
from lsp_utils import GenericClientHandler, UvVenvManager
from pathlib import Path
from typing import final
from typing_extensions import override
import sublime


@final
class RuffLsp(GenericClientHandler):
    package_name = str(__package__)
    uv_venv_manager: UvVenvManager | None = None

    @classmethod
    @override
    def is_applicable(cls, view: sublime.View, config: ClientConfig) -> bool:
        return bool(
            super().is_applicable(view, config)
            # REPL views (https://github.com/sublimelsp/LSP-pyright/issues/343)
            and not view.settings().get("repl")
            # Python-like syntax test files
            and not view.substr(sublime.Region(0, 20)).startswith("# SYNTAX TEST ")
        )

    @classmethod
    @override
    def needs_update_or_installation(cls) -> bool:
        if not cls.uv_venv_manager:
            cls.uv_venv_manager = UvVenvManager(cls.package_name, 'pyproject.toml', Path(cls.storage_path()))
        return cls.uv_venv_manager.needs_install_or_update()

    @classmethod
    @override
    def install_or_update(cls) -> None:
        if not cls.uv_venv_manager:
            raise Exception('Expected UvVenvManager to be initialized')
        cls.uv_venv_manager.install()

    @classmethod
    @override
    def get_additional_variables(cls) -> dict[str, str]:
        variables = super().get_additional_variables()
        if cls.uv_venv_manager:
            variables.update({
                'managed_ruff_path': str(cls.uv_venv_manager.venv_bin_path / 'ruff')
            })
        return variables


def plugin_loaded() -> None:
    RuffLsp.setup()


def plugin_unloaded() -> None:
    RuffLsp.cleanup()
