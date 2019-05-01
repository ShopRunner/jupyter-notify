if (!("Notification" in window)) {
    alert("This browser does not support desktop notifications, so the %%notify magic will not work.");
} else if (Notification.permission !== 'granted' && Notification.permission !== 'denied') {
    Notification.requestPermission(function (permission) {
        if(!('permission' in Notification)) {
            Notification.permission = permission;
        }
    })
}

if(!window.jQuery) {
    var jq = document.createElement('script');
    jq.src = "//ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
    document.getElementsByTagName('head')[0].appendChild(jq);
}