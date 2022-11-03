# boot.py -- run on boot-up
'''
from network import WLAN
import utime
from machine import RTC

wlan = WLAN(mode=WLAN.STA)
rtc = RTC(id=0)
wlan.connect('LCD', auth=(network.WLAN.WPA2, '1cdunc0rd0ba'))
while not wlan.isconnected():
    machine.idle()
if wlan.isconnected():
    print(wlan.ifconfig())
    print('WiFi connected succesfully')
    #rtc.init((2022, 10, 17, 19, 38, 0, 0, 0))
    rtc.ntp_sync("pool.ntp.org", 3600)
    print(rtc.now())
#utime.sleep_ms(2000)



#rtc.ntp_sync("pool.ntp.org", 360)
#utime.sleep_ms(5000)
#while not rtc.synced():
#    utime.sleep_ms(50)
#print(rtc.now())
#print("hi")
'''