import sys
import serial
import numpy 
import psycopg2
import time
import datetime

#now = datetime.now()
#timestamp = datetime.timestamp(now)

#group_id = StringVar()
#channal = StringVar()
#data = StringVar()



try :
        conn = psycopg2.connect(database='ProjectDB', 
                            user='postgres', 
                            password='postgres', 
                            host='localhost', 
                            port='5432')
        print('Database connected successfully')
        
except:
        print('Database not connected!!!')

cur = conn.cursor()
if (cur.isConnect()):
    while (1) :
      if conn.inWaiting() > 0:
         insert_command = "insert into datatb values (now(), now(), '" + str(group_id) + "' , '" + str(channel) + "' , " + str(data) + ", '')"
         cur.execute(insert_command)
         conn.commit()


def ser_conn(group_id,channel,data):
    try:
        ser = serial.Serial(port='COM4',
                    baudrate=57600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE,
                    timeout=1)
        ser.isOpen()
        print('Serial port is opened')
    except:
        print('Error!!!')
        exit()

    if (ser.isOpen()):
        while (1):
            if ser.inWaiting() > 0:
                x = ser.readline()
                group_id = (x[3:5].decode()) #bytes to string
                channel = (x[5:7].decode())
                data = float(x[8:19])
                
            
                unit = (x[19:20].decode())
                if unit == 'I': #inch to mm
                    data = (data/0.039370)

                print(x)
                print('\nGroup ID = ',group_id,'\nChannel  = ',channel,'\nData     = ',"%.2f" % data +' mm')

        return group_id
        return channel
        return data 
    else:
        print('Cannot open serial port')  

     


####################################################
ser_conn(group_id,channel,data)






