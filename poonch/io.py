import serial, sys
SERIAL_PORT = 'COM4'
BAUD_RATE = 57600

try:
    try_conn = serial.Serial(
        port = SERIAL_PORT, 
        baudrate = BAUD_RATE,
        timeout = 0.1,
        bytesize = 8, #serial.EIGHTBITS,
        #parity = serial.PARITY_NONE,
        stopbits = 1,) #serial.STOPBITS_ONE)
    print('Open')

except serial.SerialException as exp : 
   print ('Cannot open serial port!')
   sys.exit(-1)


