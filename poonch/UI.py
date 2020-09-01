from tkinter import *
def mConnect():
    mText=Label(text="QC INDY",fg="deep sky blue",bg="hot pink").pack(anchor=W)

#สร้างBOX
gui=Tk()
gui.geometry("450x450")
gui.title("QC INDY")

#สร้างLabel
mlabel=Label(text="QC INDY",fg="deep sky blue",bg="hot pink").pack(fill=Y)

#สร้างBotton
mButton=Button(text="OK",fg="green",bg="hot pink",command=mConnect).pack()

#สร้างTextbox
objEntry=Entry().pack()

#สร้างManubar
menubar=Menu(gui)
fileMenu=Menu(menubar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save..As")
fileMenu.add_command(label="Close")
menubar.add_cascade(label="File",menu=fileMenu)
gui.config(menu=menubar)
gui.mainloop()


