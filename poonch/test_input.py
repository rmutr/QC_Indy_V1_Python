x = input('Key = ')
                #x = ser.readline()
group_id = (x[3:5]) #bytes to string
channel = (x[5:7])
data = float(x[8:19])
print(x)
print('\nGroup ID = ',group_id,'\nChannel  = ',channel,'\nData     = ',"%.2f" % data +' mm')