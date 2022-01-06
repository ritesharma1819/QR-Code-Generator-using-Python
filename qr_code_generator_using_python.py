from tkinter import*
from tkinter import font
import qrcode
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
# var_link=StringVar()



link_title=Label(window,text="  Link  ",font=('Arial',30,BOLD))
link_title.grid(row=0,column=0)

link_entry=Entry(window,font=('times in roman',25))
link_entry.grid(row=0,column=1)

qr_button=Button(window,text='Qr Generator',font=('Times in roman',20,BOLD),fg='white',bg='#434AA8')
qr_button.grid(row=0,column=2)

clear_button=Button(window,text='Clear',font=('Times in roman',20,BOLD),fg='white',bg='#6D6D15')
clear_button.grid(row=1,column=2)




window.mainloop()