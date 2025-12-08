from tkinter import*
import random #random for integer randomizer
from PIL import ImageTk 
from tkinter import messagebox
import pygame #pygame for audio

main = Tk()
main.config(bg="#FFFFFF")
main.title("THE QUIZ OF ALL AGES")
main.geometry('950x700')
main.resizable(False, False) #unresizable window
main.iconphoto(False, ImageTk.PhotoImage(file="icon.jpg")) #app icon

pygame.init() #pygame sfx mixer that handles the audios
pygame.mixer.init()
audio = pygame.mixer.Sound("SFX/bgm.mp3") #background music plays on run
audio.play(-1)

inpunt = IntVar() #holds the container for the inputted integer for the system to use for calculation

totscore = 0 #global score variable
total_questions = 0 #amount of questions successfully answered
current_solution = 0 #variable to hold the correct solution for each question provided
ewrongs = 0 #"blunder" counter, holds the amount of mistakes the user made that will be displayed in the results after the quiz

#function to switch frames
def frameswitch(frame):
    frame.tkraise()

#NOTICE
#the differences of all 3 difficulties are the gradual additions of each operators
#easy mode only has addition and subtraction
#medium mode introduces multiplication
#hard more introduces division, while expanding the integer range from 10 to 99

# EASYMODE FUNCTION
def EASYMODE():

    #function for returning to menu
    def returnto():
        ejudgetext.config(text="wanna try again?")
        entry1.delete(0, END)
        frameswitch(menu)  

    #easymode's question generator
    def egenq():
            num1 = random.randint(1, 10) #the variables for the math problems displayed
            num2 = random.randint(1, 10) #as shown, the integers for the problems are in the range of 1-10
            operators = ['+', '-',]
            operator = random.choice(operators) #will choose between the two

            problem = f"{num1} {operator} {num2}" #the variable for the math problem that will be displayed

            try: #to form the solution for the displayed math problems which will be used for the checker
                if operator == '+':
                    solution = num1 + num2
                elif operator == '-':
                    solution = num1 - num2
                else:
                 return egenq()
            except: #in the event it fails, it regenerates the question
                return egenq()

            return problem, solution
    
    #answer checker
    def echecker():
        global totscore, total_questions, current_solution, ewrongs #the global variables from above being used
        if total_questions <= 10: #this ensures the entire system functions if total_questions didnt reach the limit (10)
            try:
                checker = int(entry1.get())
                if checker == current_solution:
                    totscore += 1
                    ejudger.config(text="CORRECT!!!", fg="green")
                else:
                    ejudger.config(text=f"INCORRECT!!! The answer was {current_solution}", fg="red")
                    ewrongs += 1
                total_questions += 1
                escor.config(text=f"Score: {totscore}/10")
                entry1.delete(0, END)
                edisplaynq()
            except ValueError:
                messagebox.showerror("INVALID", "Enter a Number")
        else: #else, if it reaches 10 it will trigger the returning function
            ereturner()

    def ereturner(): #this is triggered if the player quits the quiz or has successfully answered 10 questions
        global total_questions
        returnto() #returnto function triggered to return to menu
        messagebox.showinfo(f"Result", f"EASY MODE: Answered {totscore} with {ewrongs} blunder(s)")
        total_questions = 0 #will revert total_questions to 0 to reset the system incase the user wants to retry

    def edisplaynq(): #function for displaying the generated question above to the quiz interface
        global current_solution
        problem, solution = egenq()
        ejudgetext.config(text=problem)
        current_solution = solution  

    ezmode = Frame(main,bg="#0F5829") #frame bgcolor

    equiztitle = Label(ezmode, text="QUIZ OF ALL AGES - EASY", font=('Roboto',30),bg= "#0F5829", fg='#ffffff')
    equiztitle.pack(pady=30) #title
    ejudgetext = Label(ezmode, text=f"Prepare...", font=('Roboto',50),bg= "#113026", fg='#ffffff')
    ejudgetext.pack(pady=20) #this text will display the math problems generated via the edisplaynq() function
    entry1 = Entry(ezmode, font=('Roboto',45),bg= '#113026', fg='#ffffff', textvariable = inpunt)
    entry1.pack(pady=5) #entry for user input
    ejudger = Label(ezmode, text=f"Will you get them right?", font=('Roboto',30),bg= "#113026", fg='#ffffff')
    ejudger.pack(pady=10) #feedback text
    escor = Label(ezmode, text=f"0/10", font=('Roboto',25),bg= "#113026", fg='#ffffff')
    escor.pack(pady=10) #score display
    einputbut = Button(ezmode, text="SUBMIT",command=echecker,fg="#113026",bg="#00FF33",width=20,font=('Roboto',20))
    einputbut.pack(pady=10) #submit button
    eexitb = Button(ezmode, text="QUIT",fg="#ffffff",bg="#0F5829", command=ereturner,width=20,font=('Roboto',25))
    eexitb.pack(pady=50) #quit button
    eexitb.config(width=10)
    ezmode.place(x=0,y=0, width=950,height=700)

    edisplaynq() #this is to trigger the quiz system upon entering the respectful mode

# MEDIUM MODE FUNCTION, all the same but with the addition of multiplication
def MEDMODE():

    def returnto():
        mjudgetext.config(text="wanna try again?")
        entry2.delete(0, END)
        frameswitch(menu)  

    def mgenq():
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operators = ['+', '-', '*']
            operator = random.choice(operators)

            problem = f"{num1} {operator} {num2}"

            try:
                if operator == '+':
                    solution = num1 + num2
                elif operator == '-':
                    solution = num1 - num2
                elif operator == '*': #multiplication
                    solution = num1 * num2
                else:
                    return mgenq() 
            except:
                return mgenq()

            return problem, solution

    def mchecker():
        global totscore, total_questions, current_solution, ewrongs
        if total_questions <= 10:
            try:
                checker = float(entry2.get())
                if checker == current_solution:
                    totscore += 1
                    mjudger.config(text="CORRECT!!!", fg="green")
                else:
                    mjudger.config(text=f"INCORRECT!!! The answer was {current_solution}", fg="red")
                    ewrongs += 1
                total_questions += 1
                mscor.config(text=f"Score: {totscore}/10")
                entry2.delete(0, END)
                mdisplaynq()
            except ValueError:
                messagebox.showerror("INVALID", "Enter a Number")
        else: 
            mreturner()

    def mreturner():
        global total_questions
        returnto()
        messagebox.showinfo(f"Result", f"MEDIUM MODE: Answered {totscore} with {ewrongs} blunder(s)")
        total_questions = 0

    def mdisplaynq():
        global current_solution
        problem, solution = mgenq()
        mjudgetext.config(text=problem)
        current_solution = solution 

    memode = Frame(main,bg="#583D0F")

    mquiztitle = Label(memode, text="QUIZ OF ALL AGES - MEDIUM", font=('Roboto',30),bg= "#583D0F", fg='#ffffff')
    mquiztitle.pack(pady=30)
    mjudgetext = Label(memode, text=f"Prepare...", font=('Roboto',50),bg= "#333000", fg='#ffffff')
    mjudgetext.pack(pady=20)
    entry2 = Entry(memode, font=('Roboto',45),bg= '#333000', fg='#ffffff', textvariable = inpunt)
    entry2.pack(pady=5)
    mjudger = Label(memode, text=f"Will you get them right?", font=('Roboto',30),bg= "#333000", fg='#ffffff')
    mjudger.pack(pady=10)
    mscor = Label(memode, text=f"0/10", font=('Roboto',25),bg= "#333000", fg='#ffffff')
    mscor.pack(pady=10)
    minputbut = Button(memode, text="SUBMIT",command=mchecker,fg="#333000",bg="#FFFF00",width=20,font=('Roboto',20))
    minputbut.pack(pady=10)
    mexitb = Button(memode, text="QUIT",fg="#ffffff",bg="#583D0F", command=mreturner,width=20,font=('Roboto',25))
    mexitb.pack(pady=50)
    mexitb.config(width=10)
    memode.place(x=0,y=0, width=950,height=700)

    mdisplaynq()

# HARD MODE FUNCTION, all the same but with the expansion of the integer range from 10 to 99, and the implementation of division.
def HARMODE():

    def returnto():
        ejudgetext.config(text="wanna try again?")
        entry3.delete(0, END)
        frameswitch(menu)  

    def hgenq():
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)
            operators = ['+', '-', '*', '/']
            operator = random.choice(operators)

            problem = f"{num1} {operator} {num2}"

            try:
                if operator == '+':
                    solution = num1 + num2
                elif operator == '-':
                    solution = num1 - num2
                elif operator == '*':
                    solution = num1 * num2
                else: #division
                    if num2 == 0:
                        return hgenq() 
                    solution = num1 / num2
            except ZeroDivisionError: #this is a counter in the event that the system presents a problem dividing by zero
                return hgenq()

            return problem, solution

    def hchecker():
        global totscore, total_questions, current_solution, ewrongs
        if total_questions <= 10:
            try:
                checker = float(entry3.get())
                if checker == current_solution:
                    totscore += 1
                    ejudger.config(text="CORRECT!!!", fg="green")
                else:
                    ejudger.config(text=f"INCORRECT!!! The answer was {current_solution}", fg="red")
                    ewrongs += 1
                total_questions += 1
                escor.config(text=f"Score: {totscore}/10")
                entry3.delete(0, END)
                hdisplaynq()
            except ValueError:
                messagebox.showerror("INVALID", "Enter a Number")
        else: 
            hreturner()

    def hreturner():
        global total_questions
        returnto()
        messagebox.showinfo(f"Result", f"HARD MODE: Answered {totscore} with {ewrongs} blunder(s)")
        total_questions = 0

    def hdisplaynq():
        global current_solution
        problem, solution = hgenq()
        ejudgetext.config(text=problem)
        current_solution = solution

    harmode = Frame(main,bg="#580F0F")

    equiztitle = Label(harmode, text="QUIZ OF ALL AGES - HARDCORE", font=('Roboto',30),bg= "#580F0F", fg='#ffffff')
    equiztitle.pack(pady=30)
    ejudgetext = Label(harmode, text=f"Prepare...", font=('Roboto',50),bg= "#1A0303", fg='#ffffff')
    ejudgetext.pack(pady=20)
    entry3 = Entry(harmode, font=('Roboto',45),bg= '#1A0303', fg='#ffffff', textvariable = inpunt)
    entry3.pack(pady=5)
    ejudger = Label(harmode, text=f"Will you get them right?", font=('Roboto',30),bg= "#1A0303", fg='#ffffff')
    ejudger.pack(pady=10)
    escor = Label(harmode, text=f"0/10", font=('Roboto',25),bg= "#1A0303", fg='#ffffff')
    escor.pack(pady=10)
    einputbut = Button(harmode, text="SUBMIT",command=hchecker,fg="#1A0303",bg="#FF0000",width=20,font=('Roboto',20))
    einputbut.pack(pady=10)
    eexitb = Button(harmode, text="QUIT",fg="#ffffff",bg="#580F0F", command=hreturner,width=20,font=('Roboto',25))
    eexitb.pack(pady=50)
    eexitb.config(width=10)
   
    harmode.place(x=0,y=0, width=950,height=700)

    hdisplaynq()
    
# instruction function for the user to understand
def instrucion():
        messagebox.showinfo("instruction", "its not rocket science, challenge yourself by going through the selected difficulties, click the designated button to begin the quiz and answer away!")

#menuframe
menu = Frame(main, bg="#0d0d36" )

titletext = Label(menu, text="THE QUIZ OF ALL AGES", font=('Roboto',50), bg='#0d0d36', fg='#ffffff') #title
titletext.pack(pady=50) #title padding
ezbutton = Button(menu, text="EASY MODE", font=("tacoma", 25), fg="#000000",bg="#00FF33", command=lambda: EASYMODE(),)
ezbutton.pack(pady=15) #easymode button that activates the EASYMODE() function
mebutton = Button(menu, text="MEDIUM MODE", font=("tacoma", 25), fg="#000000",bg="#FBFF00", command=lambda: MEDMODE(),)
mebutton.pack(pady=15) #ditto, but medium mode
harbutton = Button(menu, text="HARD MODE", font=("tacoma", 25), fg="#000000",bg="#FF0000", command=lambda: HARMODE(),)
harbutton.pack(pady=15) #ditto, but hard mode
lvbtt = Button(menu, text="quit", font=("tacoma", 45), bg= '#234567', fg='#ffffff', command=main.destroy,)
lvbtt.place(x=50, y=550, height=100, width=150) #quit button
inbtt = Button(menu, text="instructions", font=("tacoma", 45), bg= '#234567', fg='#ffffff', command=instrucion,)
inbtt.place(x=550, y=550, height=100, width=350) #instruction button that activates the instrucion() function

menu.place(x=0,y=0, width=950,height=700) #menuframe placement

frameswitch(menu) #on run, the menu frame will be switched on default

main.mainloop() #tkinter mainloop to put it all together.