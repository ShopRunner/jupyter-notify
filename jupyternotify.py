# see https://ipython.org/ipython-doc/3/config/custommagics.html
# for more details on the implementation here
import uuid
from IPython.core.getipython import get_ipython
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.display import display, Javascript

@magics_class
class JupyterNotifyMagics(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        display(Javascript(
            """
            if (!("Notification" in window)) {
                alert("This browser does not support desktop notifications, so the %%notify magic will not work.");
            } else if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
                Notification.requestPermission(function (permission) {
                    if(!('permission' in Notification)) {
                        Notification.permission = permission;
                    }
                })
            }
            """
        ))
    
    @cell_magic
    def notify(self, line, cell):
        # generate a uuid so that we only deliver this notification once, not again
        # when the browser reloads (we append a div to check that)
        notification_uuid = uuid.uuid4()

        output = get_ipython().run_cell(cell)

        # display our browser notification using javascript
        jsString = """
            $(document).ready(
                var notification_uuid ="%(notification_uuid)s";

                var Widget = { };
                Widget.create = function(document) {
                    var notificationPayload = {
                                icon: "/static/base/images/favicon.ico",
                                body: "Cell Execution Has Finished!!",
                    }
                    var notification = new Notification("Jupyter Notebook", notificationPayload)
                    var notifiedDiv = document.createElement("div")
                    notifiedDiv.id = notification_uuid;
                    document.body.append(notifiedDiv)
                };

                function() {
                    // only send notifications if the pageload is complete; this will
                    // help stop extra notifications when a saved notebook is loaded,
                    // which during testing gives us state "interactive", not "complete"
                    if (document.readyState === 'complete') {
                        // check for the div that signifies that the notification
                        // was already sent
                        if (document.getElementById(notification_uuid) === null) {
                            if (Notification.permission !== 'denied') {
                                if (Notification.permission !== 'granted') { 
                                    Notification.requestPermission(function (permission) {
                                        if(!('permission' in Notification)) {
                                            Notification.permission = permission
                                        }
                                        if (Notification.permission === 'granted') { 
                                            // append a div with our uuid so we can check that it's already
                                            // been sent and avoid duplicates on page reload
                                            Widget.create(document);    
                                        }
                                    })
                                } else if (Notification.permission === 'granted') { 
                                    // append a div with our uuid so we can check that it's already
                                    // been sent and avoid duplicates on page reload
                                    Widget.create(document);
                                }
                            }
                        }
                    }
                }
            )
            """
        display(Javascript(jsString % ({"notification_uuid":notification_uuid})))

        # finally, if we generated an exception, print the traceback
        if output.error_in_exec is not None:
            output.raise_error()
