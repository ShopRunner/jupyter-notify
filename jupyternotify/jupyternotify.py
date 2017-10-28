# see https://ipython.org/ipython-doc/3/config/custommagics.html
# for more details on the implementation here
import json
import uuid
import time

from IPython.core.getipython import get_ipython
from IPython.core.magic import cell_magic, Magics, magics_class, line_cell_magic, line_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from IPython.display import display, Javascript
from pkg_resources import resource_filename


@magics_class
class JupyterNotifyMagics(Magics):
    run_start_time = None
    _events = None, None

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
        "-m",
        "--message",
        default="Cell Execution Has Finished!!",
        help="Custom notification message"
    )
    @line_cell_magic
    def notify(self, line, cell=None):

        # Duplicate options to allow notifications running in the same cell to
        # have separate messages.
        options = dict(self.options)

        # custom message
        args = parse_argstring(self.notify, line)
        options["body"] = args.message.lstrip("\'\"").rstrip("\'\"")

        # generate a uuid so that we only deliver this notification once, not again
        # when the browser reloads (we append a div to check that)
        notification_uuid = uuid.uuid4()

        # Run cell if its cell magic
        if cell is not None:
            output = get_ipython().run_cell(cell)

        # display our browser notification using javascript
        self.display_notification(options, notification_uuid)


    def display_notification(self, options=None, notification_uuid=None):
        if options is None:
            options = self.options
        if notification_uuid is None:
            notification_uuid = uuid.uuid4()

        # display our browser notification using javascript
        with open(resource_filename("jupyternotify", "js/notify.js")) as jsFile:
            jsString = jsFile.read()
        display(Javascript(jsString % {
            "notification_uuid": notification_uuid,
            "options": json.dumps(options),
        }))


    @magic_arguments()
    @argument(
        "-a", "--after", default=None,
        help="Send notification if cell execution is longer than x seconds"
    )
    @argument(
        "-m",
        "--message",
        default="Cell Execution Has Finished!!",
        help="Custom notification message"
    )
    @line_magic
    def autonotify(self, line):
        # Record options
        args = parse_argstring(self.autonotify, line)
        self.options["body"] = args.message.lstrip("\'\"").rstrip("\'\"")
        self.options['autonotify_after'] = args.after

        ### Register events
        ip = get_ipython()

        # Remove events if they're already registered
        # This is necessary because jupyter makes a new instance everytime
        pre, post = self.__class__._events
        if pre and pre in ip.events.callbacks['pre_run_cell']:
            ip.events.callbacks['pre_run_cell'].remove(pre)
        if post and post in ip.events.callbacks['post_run_cell']:
            ip.events.callbacks['post_run_cell'].remove(post)

        # Register new events
        ip.events.register('pre_run_cell', self.pre_run_cell)
        ip.events.register('post_run_cell', self.post_run_cell)
        self.__class__._events = self.pre_run_cell, self.post_run_cell

    def pre_run_cell(self):
        # Initialize autonotify
        if self.options.get('autonotify_after'):
            self.run_start_time = time.time()

    def post_run_cell(self):
        # Check autonotify options and perform checks
        if self.check_after():
            self.display_notification()
        # maybe add other triggers too

    def check_after(self):
        # Check if the time elapsed is over the specified time.
        now, start = time.time(), self.run_start_time
        threshold = float(self.options.get('autonotify_after', -1))
        return threshold >= 0 and start and (now - start) >= threshold
