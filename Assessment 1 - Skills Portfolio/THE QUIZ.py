from tkinter import*
from random import randrange
import time

root = Tk()
root.config(bg="#FFFFFF")
root.title("THE QUIZ OF ALL TIME")
root.geometry('950x700')
label_title = Label(root, text="will you get this RIGHT", font=('Roboto',18), bg='#FFFFFF',fg='#234567')
label_title.place(x=40, y=0)

inpunt = IntVar()


num1 = int(randrange(1000))
num2 = int(randrange(1000))
add = num1 + num2

def switch_to_frame(frame):
    frame.tkraise()

def returnto():
    thetext.config(text="wanna try again?")
    labbl.config(text="will you guess this right this time")
    entry1.config(text=" ")
    switch_to_frame(menu)  

def beggin():
    thetext.config(text=f"what is {num1} + {num2}")

def calc():
    checker = int(inpunt.get())

    if checker == add:
        labbl.config(text="CORRECT!!!")
    else:
        labbl.config(text="WRONG!!!!")

menu = Frame(root, bg="#0000ff" )

label2 = Label(menu, text="THE QUIZ OF ALL AGES", font=('Roboto',16),bg= 'green', fg='#ffffff')
label2.pack(pady=10)


button2 = Button(menu, text="BEGIN",fg="#ffffff",bg="#234567", command=lambda: switch_to_frame(quiz1),)
button2.pack()

menu.place(x=0,y=0, width=950,height=700)

quiz1 = Frame(root,bg="#234567")

beginbut = Button(quiz1, text="shall we begin", fg="#ffffff",bg="#0000ff",command=beggin,width=20, font=('Roboto',12))
label1 = Label(quiz1, text="QUIZ OF ALL AGES", font=('Roboto',16),bg= '#234567', fg='#ffffff')
label1.pack(pady=5)
thetext = Label(quiz1, text=f"you havent begun yet", font=('Roboto',30),bg= '#234567', fg='#ffffff')
thetext.pack(pady=5)
entry1 = Entry(quiz1, font=('Roboto',12),bg= '#234567', fg='#ffffff', textvariable = inpunt)
entry1.pack(pady=5)
inputbut = Button(quiz1, text="im confident this is my answer",command=calc,fg="#ffffff",bg="#234567",width=40,font=('Roboto',20))
button1 = Button(quiz1, text="QUIT",fg="#ffffff",bg="#234567", command=returnto,width=20,font=('Roboto',12))
button1.pack(pady=10)
inputbut.place(x=150,y=150)
button1.place(x=350,y=300)
labbl = Label(quiz1, text = "can you guess this right?", bg='#0000ff',fg='#ffffff',font=("tahoma",12))
labbl.place(x=350,y=200)
beginbut.place(x=350,y=350)
quiz1.place(x=0,y=0, width=950,height=700)

switch_to_frame(menu)

root.mainloop()