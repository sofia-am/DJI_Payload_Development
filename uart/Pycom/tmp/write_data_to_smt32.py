from time import sleep
from machine import UART

uart = UART(1, 9600, pins=('P8', 'P4')) # Pin10 = P8 = Tx, Pin9 = P4 = Rx

while True:
    n_bytes = uart.write('Sending data from FyPy to SMT32\r\n')
    print('Se enviaron %d bytes via UART' % n_bytes)
    sleep(5)