A Jupyter Magic For Browser Notifications of Cell Completion
============================================================

This package provides a Jupyter notebook cell magic ``%%notify`` that
notifies the user upon completion of a potentially long-running cell via
a browser push notification. Use cases include long-running machine
learning models, grid searches, or Spark computations. This magic allows
you to navigate away to other work (or even another Mac desktop
entirely) and still get a notification when your cell completes.

Supported browsers
~~~~~~~~~~~~~~~~~~

The extension has currently been tested in Chrome (Version: 58.0.3029)
and Firefox (Version: 53.0.3).

Note: Firefox also makes an audible bell sound when the notification
fires (the sound can be turned off in OS X as described
`here <https://stackoverflow.com/questions/27491672/disable-default-alert-sound-for-firefox-web-notifications>`__).

Import the repo
---------------

To use the package, add it to the requirements.txt of your repo and pip
install

git+ssh://git@github.com/ShopRunner/jupyter-notify.git#egg=jupyternotify

Install locally
---------------

.. code:: bash

    git clone git@github.com:ShopRunner/jupyter-notify.git
    cd jupyter-notify/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    jupyter notebook

Usage
-----

Load inside a Jupyter notebook:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import jupyternotify
    ip = get_ipython()
    ip.register_magics(jupyternotify.JupyterNotifyMagics)

Automatically load in all notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following lines to your ipython startup file:

::

    c.InteractiveShellApp.exec_lines = [
        'import jupyternotify',
        'ip = get_ipython()',
        'ip.register_magics(jupyternotify.JupyterNotifyMagics)'
    ]

The .ipython startup file can be generated with
``ipython profile create [profilename]`` and will create a configuration
file at ``~/.ipython/profile_[profilename]/ipython_config.py'``. Leaving
[profilename] blank will create a default profile (see
`this <http://ipython.org/ipython-doc/dev/config/intro.html>`__ for more
info).

To test the extension, try

::

    %%notify
    import time
    time.sleep(5)
