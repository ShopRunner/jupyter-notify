# Jupyter Magic: Browser Notifications When Cell Execution Finishes

This package provides a jupyter notebook cell magic `%%notify` that notifies the user upon completion of a potentially long-running cell.  It makes use of browser push notifications and has currently been tested in Chrome and Firefox.  Use cases include long-running machine learning models or grid searches, or long-running spark computations.  This magic allows you to navigate away to other work (and even another Mac desktop entirely) and still get a notification when your cell completes.

## Installation
```
git clone https://github.com/ShopRunner/jupyter-notify.git
cd jupyter-notify/
pip install -r requirements.txt
jupyter notebook
```

Inside of the notebook:
```
import jupyternotify
ip = get_ipython()
ip.register_magics(jupyternotify.JupyterNotifyMagics)
```

Or, to automatically load the notifications magic every time the notebook starts, add the following lines to your .ipython startup file:
```
c.InteractiveShellApp.exec_lines = [
	'import jupyternotify',
	'ip = get_ipython()',
	'ip.register_magics(jupyternotify.JupyterNotifyMagics)'
]
```
The .ipython startup file can be generated with `ipython profile create [profilename]` and will create a configuration file at `~/.ipython/profile_[profilename]/ipython_config.py'`.  Leaving [profilename] blank will create a default profile (see [this](http://ipython.org/ipython-doc/dev/config/intro.html) for more info).

To test the extension, try

```
%%notify
import time
time.sleep(5)
```