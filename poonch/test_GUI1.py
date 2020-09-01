from tkinter import *
from tkinter import ttk

GUI = Tk() #หน้าต่างหลัก
GUI.geometry('400x400') #กำหนดขนาด
GUI.title('QC INDY')

def Save(event = None):
    ms = message.get()
    pr = float(price.get())

    print('รายการ',ms)
    print('ราคา',pr)

    result.set(f'รายการ : {ms} \nราคา : {pr :,.2f} บาท ')

    message.set('')
    price.set('')

    E1.focus()

Font1 = ('',24, 'bold')
Font2 = ('',18, 'bold')
message = StringVar()
price = StringVar()

L1 = ttk.Label(GUI, text = 'กรุณากรอก', font = Font1).pack()
E1 = ttk.Entry(GUI, textvariable = message, font = Font2)
E1.pack()

L2 = ttk.Label(GUI, text = 'ราคา', font = Font1).pack()
E2 = ttk.Entry(GUI, textvariable = price, font = Font2)
E2.pack()
E2.bind('<Return>',Save)

#F1 = Frame(GUI)
#F1.place(x=160, y=180)
B1 = ttk.Button(GUI, text = 'Save', command = Save).pack()

result = StringVar()
L3 = ttk.Label(GUI, textvariable = result, font = Font2, foreground = 'deep sky blue').pack()


GUI.mainloop()