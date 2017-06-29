if (!("Notification" in window)) {
    alert("This browser does not support desktop notifications, so the %%notify magic will not work.");
} else if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {
        if(!('permission' in Notification)) {
            Notification.permission = permission;
        }
    })
}
