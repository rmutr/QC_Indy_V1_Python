from tkinter import *
from tkinter import ttk

GUI = Tk() #หน้าต่างหลัก
GUI.geometry('400x400') #กำหนดขนาด
GUI.title('QC INDY')

B1 = Button(GUI,text="OK")
B1.pack(pady = 50) #ระยะห่างของปุ่ม

B2 = ttk.Button(GUI, text = 'HELLO')
B2.pack(ipadx=20, ipady=10) #ขนาดของปุ่ม

#######################################################

F1 = Frame(GUI)
F1.place(x=50, y=50)

B3 = ttk.Button(F1, text = 'BYE')
B3.pack(ipadx=20, ipady=10)

#####################Funtion##########################
def num1():
    print('1')

def num2():
    print('2')

######################################################

F2 = Frame(GUI)
F2.place(x=100, y=200)

B4 = ttk.Button(F2, text = '111', command = num1)
B4.grid(row = 0, column = 0, ipadx=20, ipady=10, padx=50)

B5 = ttk.Button(F2, text = '222', command = num2)
B5.grid(row = 0, column = 1, ipadx=20, ipady=10, padx=50)

B6 = ttk.Button(F2, text = '333')
B6.grid(row = 1, column = 0, ipadx=20, ipady=10, padx=50)

B7 = ttk.Button(F2, text = '444')
B7.grid(row = 1, column = 1, ipadx=20, ipady=10, padx=50)


GUI.mainloop()
