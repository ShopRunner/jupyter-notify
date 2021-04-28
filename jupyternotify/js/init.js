if (!("Notification" in window)) {
    alert("This browser does not support desktop notifications, so the %%notify magic will not work.");
} else if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {
        if(!('permission' in Notification)) {
            Notification.permission = permission;
        }
    })
}

// Detect if the window is out of focus.
window.jupyterNotifyIsInBackground = undefined;
(function() {
    // Check document.hidden support
    var hidden;
    if (typeof document.hidden !== "undefined") { // Opera 12.10 and Firefox 18 and later support
      hidden = "hidden";
    } else if (typeof document.msHidden !== "undefined") {
      hidden = "msHidden";
    } else if (typeof document.webkitHidden !== "undefined") {
      hidden = "webkitHidden";
    }

    // Set initial background state
    if (document[hidden]) {
      window.jupyterNotifyIsInBackground = true;
    } else {
      window.jupyterNotifyIsInBackground = false;
    }

    window.addEventListener('blur', function() { window.jupyterNotifyIsInBackground = true; }, false);
    window.addEventListener('focus', function() { window.jupyterNotifyIsInBackground = false; }, false);
})();
