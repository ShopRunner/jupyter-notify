# A Jupyter Notebook %%magic for Browser Notifications of Cell Completion

This package provides a jupyter notebook cell magic `%%notify` that notifies the user upon completion of a potentially long-running cell.  It makes use of browser push notifications and currently tested in Chrome and Firefox.  Use cases include long-running machine learning models or grid searches, or long-running spark computations.  This magic allows you to navigate away to other work (and even another Mac desktop) and still get a notification when your cell completes.

## Installation
```
pip install -r requirements.txt
jupyter notebook
```

Inside of the notebook:
```
import jupyternotify
ip = get_ipython)(
ip.register_magics(jupyternotify.JupyterNotifyMagics)
```

Or, to automatically load the notifications magic, add the following to your .ipython startup file (which can be generated with `ipython profile create [profilename]` and will create a configuration file at `~/.ipython/profile_[profilename]/ipython_config.py'` (leaving [profilename] blank will create a default profile...see [this](http://ipython.org/ipython-doc/dev/config/intro.html) for more info):
```
c.InteractiveShellApp.exec_lines = [
	'import jupyternotify',
	'ip = get_ipython()',
	'ip.register_magics(jupyternotify.JupyterNotifyMagics)'
]
```

To test the extension, try

```
%%notify
import time
time.sleep(5)
```