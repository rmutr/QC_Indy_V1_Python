#import sys
import serial

ser = serial.Serial(port='COM4',
                    baudrate=57600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    timeout=2)
try:
    ser.isOpen()
    print('Serial port is opened')
except:
    print('Error')
    exit()

if (ser.isOpen()):
    try:
        
        while (1):
            x = ser.readline()
            group_id = x[3:5]
            channel = x[5:7]
            data = x[8:20]
            print('\nGroup ID = ',group_id,'\nChannel  = ',channel,'\nData     = ',data)

    except Exception:
        print('Error')
else:
    print('Cannot open serial port')




