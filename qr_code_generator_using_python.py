from tkinter import*
from typing import Generator
import qrcode
from PIL import ImageTk,Image
from tkinter.font import BOLD
from resizeimage import resizeimage
window=Tk()

# set geometry and title
window.geometry("900x500+300+50")
window.title('Qr Code Generator')
window.resizable(False,False)

# delartion of variable
var_link=StringVar()


# function of clear
def clear():
    var_link.set('')
    msg=''
    lbl_msg.config(text=msg)



# qr_generated function definition
def qr_generated():
    if var_link.get()=='':
            msg='Please give the link !!'
            lbl_msg.config(text=msg,fg='red')
    else:
        # updating qr code Generator
        qr=(f"link or message:{var_link.get()}")
        qr_code_generated=qrcode.make(qr)
        qr_code_generated=resizeimage.resize_cover(qr_code_generated,[180,180])
        qr_code_generated.save("D:\python\project\QR Code Generator using Python\qr_code_generator_using_python.py"+str(var_link.get())+'.png')
        # im=ImageTk.PhotoImage(file="D:\python\project\QR Code Generator using Python\qr_code_generator_using_python.py"+str(var_link.get())+'.png')
        # qr_code=Label(qr_frame,image=im).place(x=615,y=215)
        
        msg='Qr generated sucessfully !!'
        lbl_msg.config(text=msg,fg='green')
        


    #set the name of project title
title=Label(window,text="  Qr Code Generator",font=('Arial',40),bg='#07325A',fg='white',
    anchor='w').place(x=0,y=0,relwidth=1)

    # divide the window for user to give the message or link and add message or link label
message_frame=Frame(window,bg='white',bd=2,relief=RAISED).place(x=50,y=100,width=480,height=380)
    
link_title=Label(message_frame,text="                           Link Box                          ",
font=('times new roman',20),bg='#07325A',
fg='white').place(x=50,y=100)

link_label=Label(message_frame,text='Link or Message',
font=('Arial',20,BOLD),fg='blue',bg='white').place(x=180,y=150)

# create entry box for link
link_entry=Entry(message_frame,
font=('Arial',20),bg='lightyellow',textvariable=var_link).place(x=130,y=215)

qr_button=Button(message_frame,text='Qr Generate',
font=('times new roman',20,BOLD),fg='white',
bg='#0096B4',command=qr_generated).place(x=130,y=300,width=160,height=50)

clear_button=Button(message_frame,text='clear',
font=('times new roman',20,BOLD),fg='white',bg='#69855D',command=clear).place(x=300,y=300,width=130,height=50)

# write message on screen when qr code generated or not
msg='Qr generated sucessfully !!'
lbl_msg=Label(message_frame,text=msg,
font=('times new roman',25),fg='green',bg='white')
lbl_msg.place(x=115,y=380)
    


# making qr code frame 
qr_frame=Frame(window,bg='white',bd=2,relief=RAISED).place(x=550,y=100,width=310,height=380)
    
qr_title=Label(qr_frame,text="             Qr Code Box          ",font=('times new roman',20),bg='#07325A',
fg='white').place(x=550,y=100)
qr_code=Label(qr_frame,text='No Qr\n Available',
font=('Arial',20),fg='white',bg='#62A586').place(x=615,y=215,width=180,height=180)





window.mainloop()