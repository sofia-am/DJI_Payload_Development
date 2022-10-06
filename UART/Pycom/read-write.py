from machine import UART
uart = UART(1, 9600, pins=("P8", "P4")) # P8=Tx, P4=Rx

modo = 'read'

print('Esperando por mensajes ...')

while True:
    if modo == 'read':
        binary_msg = uart.read()
        if binary_msg != None:
            buf = binary_msg.decode('ascii').rstrip()
            print('Mensaje recibido: ', buf)
            if buf == 'write':
                modo = buf
            else:
                print('Si quiere cambiar de modo escriba <write>')
    else:
        buf = input('Si quiere cambiar a lectura escriba <read> sino ingrese otro mensaje\n')
        n_bytes = uart.write(buf + '\n')
        print('Se enviaron %d bytes via UART' % n_bytes)
        if buf == 'read':
                modo = buf