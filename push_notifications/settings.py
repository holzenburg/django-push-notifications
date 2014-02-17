from django.conf import settings

PUSH_NOTIFICATIONS_SETTINGS = getattr(settings, "PUSH_NOTIFICATIONS_SETTINGS", {})

for k in PUSH_NOTIFICATIONS_SETTINGS.keys():

    # GCM
    PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("GCM_POST_URL", "https://android.googleapis.com/gcm/send")
    PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("GCM_MAX_RECIPIENTS", 1000)


    # APNS
    PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("APNS_PORT", 2195)
    if settings.DEBUG:
    	PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("APNS_HOST", "gateway.sandbox.push.apple.com")
    	PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("APNS_WEB_HOST", "gateway.push.apple.com")
    else:
    	PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("APNS_HOST", "gateway.push.apple.com")
    	PUSH_NOTIFICATIONS_SETTINGS[k].setdefault("APNS_WEB_HOST", "gateway.push.apple.com")
