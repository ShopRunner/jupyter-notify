# see https://ipython.org/ipython-doc/3/config/custommagics.html
# for more details on the implementation here
import json
import uuid

from IPython.core.getipython import get_ipython
from IPython.core.magic import cell_magic, Magics, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from IPython.display import display, Javascript
from pkg_resources import resource_filename


@magics_class
class JupyterNotifyMagics(Magics):
    def __init__(self, shell, require_interaction=False):
        super(JupyterNotifyMagics, self).__init__(shell)
        with open(resource_filename("jupyternotify", "js/init.js")) as jsFile:
            jsString = jsFile.read()
        display(Javascript(jsString))
        self.options = {
            "requireInteraction": require_interaction,
            "icon": "/static/base/images/favicon.ico",
        }

    @magic_arguments()
    @argument(
        "message", 
        nargs="?",
        default="Cell Execution Has Finished!!", 
        help="Custom notification message"
    )
    @cell_magic
    def notify(self, line, cell):

        # custom message
        args = parse_argstring(self.notify, line)
        self.options["body"] = args.message.lstrip("\'\"").rstrip("\'\"")       

        # generate a uuid so that we only deliver this notification once, not again
        # when the browser reloads (we append a div to check that)
        notification_uuid = uuid.uuid4()

        output = get_ipython().run_cell(cell)

        # display our browser notification using javascript
        with open(resource_filename("jupyternotify", "js/notify.js")) as jsFile:
            jsString = jsFile.read()
        display(Javascript(jsString % {
            "notification_uuid": notification_uuid,
            "options": json.dumps(self.options),
        }))

        # finally, if we generated an exception, print the traceback
        if output.error_in_exec is not None:
            output.raise_error()
