import serial as Serial
from time import sleep

if __name__ == '__mian__':
    ser = Serial.Serial('COM4')
    if not ser.isOpen():
        ser.open()
    try:
        if ser.isOpen():
            print('Serial com is opened')

            while True:
                print('Polling...')
                sleep(0.5)
                if ser.inWaiting() > 0:
                    msg = ser.read(ser.inWaiting())
                    ser.flushInput()
                    print('>> ',msg)
                    #msg = ('\<\<',msg)
                    ser.write(msg + '\r\n')
                    ser.flushOutput
    except KeyboardInterrupt:
        ser.close()
        if not ser.isOpen():
            print('User,Serial COMM is closed')
    finally:
        ser.close()
        if not ser.isOpen():
            print('Program,Serial COMM is closed')
