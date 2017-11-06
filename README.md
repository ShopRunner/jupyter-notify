[![pypiv](https://img.shields.io/pypi/v/jupyternotify.svg)](https://pypi.python.org/pypi/jupyternotify)
[![pyv](https://img.shields.io/pypi/pyversions/jupyternotify.svg)](https://pypi.python.org/pypi/jupyternotify)
[![License](https://img.shields.io/pypi/l/jupyternotify.svg)](https://github.com/ShopRunner/jupyter-notify/blob/master/LICENSE.txt)
[![Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/mdagost)

<img src="https://s3.amazonaws.com/shoprunner-github-logo/shoprunner-logo.svg" alt="ShopRunner logo" width="300"/>

# A Jupyter Magic For Browser Notifications of Cell Completion

<img src="https://s3.amazonaws.com/shoprunner-github-logo/jupyter_chrome.png" alt="Jupyter notebook notification in Chrome" width="750"/>
<img src="https://s3.amazonaws.com/shoprunner-github-logo/jupyter_firefox.png" alt="Jupyter notebook notification in Firefox" width="750"/>

This package provides a Jupyter notebook cell magic `%%notify` that notifies the user upon completion of a potentially long-running cell via a browser push notification. Use cases include long-running machine learning models, grid searches, or Spark computations. This magic allows you to navigate away to other work (or even another Mac desktop entirely) and still get a notification when your cell completes.

### Supported browsers
The extension has currently been tested in Chrome (Version:  58.0.3029) and Firefox (Version: 53.0.3). 

Note: Firefox also makes an audible bell sound when the notification fires (the sound can be turned off in OS X as described [here](https://stackoverflow.com/questions/27491672/disable-default-alert-sound-for-firefox-web-notifications)).

## Import the repo
To use the package, install it via pip directly:

```
pip install jupyternotify
```

or add it to the requirements.txt of your repo.

To install directly from source:

``` bash
git clone git@github.com:ShopRunner/jupyter-notify.git
cd jupyter-notify/
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Usage
### Load inside a Jupyter notebook:
``` python
import jupyternotify
ip = get_ipython()
ip.register_magics(jupyternotify.JupyterNotifyMagics)
```

### Automatically load in all notebooks
Add the following lines to your ipython startup file:
```
c.InteractiveShellApp.exec_lines = [
	'import jupyternotify',
	'ip = get_ipython()',
	'ip.register_magics(jupyternotify.JupyterNotifyMagics)'
]
```
The .ipython startup file can be generated with `ipython profile create [profilename]` and will create a configuration file at `~/.ipython/profile_[profilename]/ipython_config.py'`. Leaving [profilename] blank will create a default profile (see [this](http://ipython.org/ipython-doc/dev/config/intro.html) for more info).

To test the extension, try

```
%%notify
import time
time.sleep(5)
```

## Options

You may specify options while loading the magic:

```python
import jupyternotify
ip = get_ipython()
ip.register_magics(jupyternotify.JupyterNotifyMagics(
    ip,
    option_name="option_value"
))
```

The following options exist:
- `require_interaction` - Boolean, default False. When this is true,
  notifications will remain on screen until dismissed. This feature is currently
  only available in Google Chrome.
  
## Custom Message

You may specify what message you wish the notification to display:

```python
%%notify -m "sleep for 5 secs"
import time
time.sleep(5)
```

<img src="https://s3.amazonaws.com/shoprunner-github-logo/jupyter_custom_message.png" alt="Jupyter notebook notification with custom message" width="750"/>

## Fire notification mid-cell

You may also fire a notification in the middle of a cell using line magic.

```python
import time
time.sleep(5)
%notify -m "slept for 5 seconds."
time.sleep(6)
%notify -m "slept for 6 seconds."
time.sleep(2)
```


## Automatically trigger notification after a certain cell execution time

Using the `autonotify` line magic, you can have notifications automatically trigger on **cell finish** if the execution time is longer than some threshold (in seconds) using `%autonotify --after <seconds>` or `%autonotify -a <seconds>`. 

```python
import numpy as np
import time
# autonotify on completion for cells that run longer than 30 seconds
%autonotify -a 30
```

Then later...

```python
# no notification
time.sleep(29)
```

```python
# sends notification on finish
time.sleep(31)
```
`autonotify` also takes the arguments `--message` / `-m` and `--output` / `-o`.

## Use cell output as message

You may use the last line of the cell's output as the notification message using `--output` or `-o`. 

```python
%%notify -o
answer = 42
'The answer is {}.'.format(answer)
```
Notification message: The answer is 42.
