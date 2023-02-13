from lsp_utils.pip_client_handler import PipClientHandler


class RuffLsp(PipClientHandler):
    package_name = __package__
    requirements_txt_path = "requirements.txt"
    server_filename = "ruff-lsp"


def plugin_loaded() -> None:
    RuffLsp.setup()


def plugin_unloaded() -> None:
    RuffLsp.cleanup()
