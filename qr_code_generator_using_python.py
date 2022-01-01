from tkinter import*
from tkinter.font import BOLD
window=Tk()

# set geometry and title
window.geometry("900x500+300+50")
window.title('Qr Code Generator')
window.resizable(False,False)

# set the name of project title
title=Label(window,text="  Qr Code Generator",font=('Arial',40),bg='#07325A',fg='white',
anchor='w').place(x=0,y=0,relwidth=1)

# divide the window for user to give the message or link and add message or link label
message_frame=Frame(window,bg='white',bd=2,relief=RAISED).place(x=50,y=100,width=480,height=380)

link_label=Label(message_frame,text='Link or Message',
font=('Arial',20,BOLD),fg='blue',bg='white').place(x=180,y=150)

# create entry box for link
link_entry=Entry(message_frame,
font=('Arial',20),bg='lightyellow').place(x=130,y=215)

qr_button=Button(message_frame,text='Qr Generate',
font=('times new roman',20,BOLD),fg='white',bg='#0096B4').place(x=130,y=300,width=160,height=50)

clear_button=Button(message_frame,text='claar',
font=('times new roman',20,BOLD),fg='white',bg='#69855D').place(x=300,y=300,width=130,height=50)

window.mainloop()