from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
import random

main = Tk()
main.title("THE COMEDIAN OF ALL AGES")
main.geometry("900x650")
main.resizable(False, False)
main['bg']='#22263d'
main.iconphoto(False, ImageTk.PhotoImage(file="icon.jpeg")) #app icon

pygame.init()
pygame.mixer.init()
laugh = pygame.mixer.Sound("SFX/giggle.mp3")
bgm = pygame.mixer.Sound("SFX/bgm.mp3")
bgm.play(-1)

#global variables to store the jokes
jokeli = []
currentjoke = ""
currentpunch = ""

def loadj(filename="thejokes.txt"): #function to load in the jokes from the txt file
    try:
        with open(filename, "r") as file:
            for line in file:
                jokec = line.strip()
                if jokec:
                    jokeli.append(jokec)
    except FileNotFoundError: #in the event of a file not available, it displays this
        messagebox.showerror("Error", f" {filename} isnt available")
        exit()
    except Exception as e: #in the rarer event the except is not an exception, it displays this
        messagebox.showerror("Error", f"uh oh {e}")
        exit()

def joke(): #function for the joke
    global currentjoke, currentpunch

    if not jokeli: #if it is not the exact file, it will return this txt
        txtarea.config(text="N/A")
        return

    randj = random.choice(jokeli) #joke selection randomizer
    if "|" in randj:
        parts = randj.split("|")
        currentjoke = parts[0].strip()
        currentpunch = parts[1].strip()
    else:
        currentjoke = randj.strip()
        currentpunch = "N/A"
        
    txtarea.config(text=currentjoke, foreground="black")
    puncher.config(state=NORMAL) #button states for proper orderly functioning
    joker.config(state=DISABLED) #if the joke button is clicked, it will be disabled and the punchline button is enabled instead

def punch(): #function for punchline display
    txtarea.config(text=f"{currentjoke}\n\n{currentpunch}", foreground="blue")
    puncher.config(state=DISABLED) #if punchline is clicked, it will be disabled
    joker.config(state=NORMAL) #joke button will be enabled again
    laugh.play()

def instrucion(): #function for instructions for the user to understand the system
    messagebox.showinfo("instruction", "its not rocket science, begin by clicking the joke button for our comedic genius' to begin joking, and click to reveal the punchline to get a good guffaw!")
    
titletext = Label(main, text="THE COMEDIAN OF ALL AGES", font=('Roboto',35), bg='#0d0d36', fg='#ffffff') #title
titletext.pack(pady=50)
txtarea = Label(main, text="Shall we begin?", width=40, height=50, font=("tacoma", 15)) #area that displays the joke/punchline
txtarea.place(x=100, y=175, height=225, width=700)

loadj() #on run, this function will be called to commence the system.

joker = Button(main, text="joke", command=joke, font=("tacoma", 15)) #button to initialize the jokes
joker.place(x=350, y=450, height=25, width=200) 
puncher = Button(main, text="reveal punchline", command=punch, font=("tacoma", 15), state=DISABLED) 
puncher.place(x=350, y=500, height=25, width=200,) #punchline button

inttt = Button(main, text="instructions", font=("tacoma", 15), command=instrucion,)
inttt.place(x=350, y=550, height=25, width=200) #instruction button

quitbt = Button(main, text="quit", font=("tacoma", 15), command=main.destroy,)
quitbt.place(x=350, y=600, height=25, width=200) #quit button that closes the app

main.mainloop()