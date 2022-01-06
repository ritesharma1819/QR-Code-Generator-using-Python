from tkinter import*
from tkinter import messagebox
from tkinter import font
import pyqrcode
from PIL import ImageTk,Image
from tkinter.font import BOLD
from resizeimage import resizeimage
import os


window=Tk()

# set geometry and title
# window.geometry("900x500+300+50")
window.title('Qr Code Generator')
# window.resizable(False,False)

# delartion of variable
var_link=StringVar()


def qr_generator():
    if len(var_link.get())!=0:
        global qr , photo
        qr=pyqrcode.create(var_link.get())
        photo=BitmapImage(data=qr.xbm(scale=8))
    else:
        messagebox.showinfo("qr code generator" ,message="please enter the link")

def clear():
    pass


link_title=Label(window,text="  Link  ",font=('Arial',30,BOLD))
link_title.grid(row=0,column=0)

link_entry=Entry(window,font=('times in roman',25),textvariable=var_link)
link_entry.grid(row=0,column=1)

qr_button=Button(window,text='Qr Generator',font=('Times in roman',20,BOLD),
fg='white',bg='#434AA8',command=qr_generator)
qr_button.grid(row=0,column=2)

clear_button=Button(window,text='Clear',font=('Times in roman',20,BOLD),
fg='white',bg='#6D6D15',command=clear)
clear_button.grid(row=1,column=2)




window.mainloop()