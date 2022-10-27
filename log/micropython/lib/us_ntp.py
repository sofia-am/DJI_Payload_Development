import utime
import machine
from network import WLAN
from console_colors import bcolors as color


rtc = machine.RTC(id=0)

# Try connect to wifi network and get real time using google stp servers, return the rtc object if is successful else None


def connect_to_google_servers(bssid, auth, password):
    time_sleep = 0

    if bssid is None or bssid == '':
        return None

    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(bssid, auth=(auth, password))

    while not wlan.isconnected():
        machine.idle()

    print(wlan.ifconfig())
    print(color.INFO, 'WiFi connected successfully', color.RESET)

    while time_sleep < 8:
        rtc.ntp_sync("time.google.com", 360)
        utime.sleep(time_sleep)
        if rtc.now()[0] == 1970:
            time_sleep += 2
        else:
            break

    if time_sleep >= 8:
        print(color.ERROR, "Timeout: it couldn't connect to NTP server\n", color.RESET)
        return False

    print(color.INFO, 'NTP connected successfully: ', rtc.now(), color.RESET)

    return True


def ddmmyyyyHHmmss(gmt):
    rtc_now = rtc.now()

    date_str = '{dia:02d}-{mes:02d}-{año:04d} {hora:02d}:{min:02d}:{seg:02d}'.format(
        dia=rtc_now[2], mes=rtc_now[1], año=rtc_now[0], hora=rtc_now[3]+gmt, min=rtc_now[4], seg=rtc_now[5]
    )

    return date_str
