import time
import pycom
import logging

delay = 1

log = logging.getLogger('log_boi')

red = 0x7f0000
green = 0x007f00
blue = 0x00007f
yellow = 0x7f7f00
white = 0x7f7f7f
pink = 0x7f007f
cian = 0x007f7f
orange = 0xd35400

pycom.heartbeat(False)

for cycles in range(5):
    pycom.rgbled(red)
    time.sleep(delay)
    log.error('Toy rojo')

    pycom.rgbled(green)
    log.info('Toy verde')
    time.sleep(delay)

    pycom.rgbled(blue)
    time.sleep(delay)

    pycom.rgbled(yellow)
    log.warning('Toy amarillo')
    time.sleep(delay)

    pycom.rgbled(white)
    time.sleep(delay)

    pycom.rgbled(pink)
    time.sleep(delay)

    pycom.rgbled(cian)
    time.sleep(delay)

    pycom.rgbled(orange)
    time.sleep(delay)
    
del log