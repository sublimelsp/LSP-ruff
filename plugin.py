from __future__ import annotations

from LSP.plugin import IsApplicableContext
from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import UvVenvManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import final
from typing_extensions import override


@final
class RuffLsp(LspPlugin):

    @classmethod
    @override
    def is_applicable_async(cls, context: IsApplicableContext) -> bool:
        if super().is_applicable_async(context):
            return True
        file_name = context.view.file_name()
        return bool(file_name) and Path(file_name).name == 'pyproject.toml'

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        # WORKAROUND: ruff falls back to the process working directory when no workspace folders are provided
        # (e.g. a file opened outside of a project), so starting it in the Sublime Text installation directory
        # breaks some features. Start the server next to the opened file instead.
        # Remove once fixed upstream: https://github.com/astral-sh/ruff/issues/26182
        if not context.working_directory and (file_name := context.view.file_name()):
            context.working_directory = str(Path(file_name).parent)
        UvVenvManager.on_pre_start_async(
            context, cls.plugin_storage_path, ResourcePath('Packages', package_name), 'ruff')


def plugin_loaded() -> None:
    RuffLsp.register()


def plugin_unloaded() -> None:
    RuffLsp.unregister()
