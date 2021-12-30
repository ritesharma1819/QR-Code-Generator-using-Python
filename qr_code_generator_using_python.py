from tkinter import*
window=Tk()

# set geometry and title
window.geometry("900x500+200+50")
window.title('Qr Code Generator')
window.resizable(False,False)

title=Label(window,text="  Qr Code Generator",font=('Arial',40),bg='#07325A',fg='white',
anchor='w').place(x=0,y=0,relwidth=1)


window.mainloop()