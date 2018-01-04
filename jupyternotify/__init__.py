from .jupyternotify import JupyterNotifyMagics


def load_ipython_extension(ipython):
    ipython.register_magics(JupyterNotifyMagics)
