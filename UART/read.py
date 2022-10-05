from machine import UART
uart1 = UART(1, 9600, pins=("P8", "P4")) # 10-P8=Tx, 9-P4=Rx

print("Arranque")

while True:
    cant_bytes = uart1.read()
    
    if cant_bytes != None:
        print(cant_bytes)
