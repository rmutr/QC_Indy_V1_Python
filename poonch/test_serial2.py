import serial
ser = serial.Serial('COM4',57600)
while 1:
    if ser.inWaiting():
        data = ser.readline(ser.inWaiting())
        print(data)
        
