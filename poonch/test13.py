from tkinter import *
window = Tk()
window.title('mindphp')
canvas = Canvas(window, width = 300, height = 230)
canvas.pack()
my_image = PhotoImage(file ='C:\\New folder\\LISA.png')
canvas.create_image(0, 0, anchor = NW, image=my_image)
window.mainloop()