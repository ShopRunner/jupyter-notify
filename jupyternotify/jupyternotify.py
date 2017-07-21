# see https://ipython.org/ipython-doc/3/config/custommagics.html
# for more details on the implementation here
import uuid

from IPython.core.getipython import get_ipython
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.display import display, Javascript
from pkg_resources import resource_filename


@magics_class
class JupyterNotifyMagics(Magics):
    def __init__(self, shell):
        super(JupyterNotifyMagics, self).__init__(shell)
        with open(resource_filename("jupyternotify", "js/init.js")) as jsFile:
            jsString = jsFile.read()
        display(Javascript(jsString))

    @cell_magic
    def notify(self, line, cell):
        # generate a uuid so that we only deliver this notification once, not again
        # when the browser reloads (we append a div to check that)
        notification_uuid = uuid.uuid4()

        output = get_ipython().run_cell(cell)

        # display our browser notification using javascript
        with open(resource_filename("jupyternotify", "js/notify.js")) as jsFile:
            jsString = jsFile.read()
        display(Javascript(jsString % {"notification_uuid": notification_uuid}))

        # finally, if we generated an exception, print the traceback
        if output.error_in_exec is not None:
            output.raise_error()
