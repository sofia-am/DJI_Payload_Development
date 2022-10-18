from network import WLAN
import utime
import machine

#Try connect to wifi network and get real time using google stp servers, return the rtc object if is successful else None
def connect_to_google_servers(bssid, auth, password):
    if bssid is None or bssid == '': return None
    
    wlan = WLAN(mode=WLAN.STA)
    rtc = machine.RTC(id=0)
    wlan.connect(bssid, auth=(auth, password))
    
    while not wlan.isconnected():
        machine.idle()
        
    print(wlan.ifconfig())
    print('WiFi connected succesfully')
    
    utime.sleep(1)
    rtc.ntp_sync("time.google.com", 360)
    utime.sleep(1)
    return rtc
