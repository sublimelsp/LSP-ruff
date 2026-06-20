from __future__ import annotations

from LSP.plugin import LspPlugin
from LSP.plugin import OnPreStartContext
from lsp_utils import UvVenvManager
from sublime_lib import ResourcePath
from typing import final
from typing_extensions import override
import os


@final
class RuffLsp(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        if not context.workspace_folders:
            context.working_directory = os.path.dirname(context.view.file_name())
        UvVenvManager.on_pre_start_async(
            context, cls.plugin_storage_path, ResourcePath('Packages', package_name), 'ruff')


def plugin_loaded() -> None:
    RuffLsp.register()


def plugin_unloaded() -> None:
    RuffLsp.unregister()
