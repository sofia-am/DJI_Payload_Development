import time
# from network import WLAN
import pycom
import logging
# import us_ntp

delay = 1

log = logging.getLogger('log_boi')
# rtc_res = us_ntp.connect_to_google_servers('LCD', WLAN.WPA2, '1cdunc0rd0ba')

red = 0x7f0000
green = 0x007f00
blue = 0x00007f
yellow = 0x7f7f00
white = 0x7f7f7f
pink = 0x7f007f
cian = 0x007f7f
orange = 0xd35400

pycom.heartbeat(False)

for cycles in range(10):
    pycom.rgbled(red)
    time.sleep(delay)
    log.info('Toy rojo')#us_ntp.ddmmyyyyHHmmss(-3)

    pycom.rgbled(green)
    time.sleep(delay)

    pycom.rgbled(blue)
    time.sleep(delay)

    pycom.rgbled(yellow)
    time.sleep(delay)

    pycom.rgbled(white)
    time.sleep(delay)

    pycom.rgbled(pink)
    time.sleep(delay)

    pycom.rgbled(cian)
    time.sleep(delay)

    pycom.rgbled(orange)
    time.sleep(delay)