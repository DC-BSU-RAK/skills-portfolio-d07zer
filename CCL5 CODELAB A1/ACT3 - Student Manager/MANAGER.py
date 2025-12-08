from tkinter import*
from tkinter import messagebox, scrolledtext
from PIL import ImageTk, Image

class TheManager: #class for handling the entirety of the system operations
    def __init__(self, master):
        self.master = master
        master.title("THE UNIVERSITY OF ALL AGES STUDENT MANAGER") #title

        self.data_file = "thelist.txt" #txt doc as file

        #GUI elements
        self.label = Label(master, text="THE DATA MANAGER OF ALL AGES", font=('tacoma', 35), bg="#22263d", fg="#ffffff")
        self.label.pack(pady=35) #title

        self.txtarea = scrolledtext.ScrolledText(master, width=75, height=15, font=("tacoma", 15), bg="#000000", fg="#00ff00")
        self.txtarea.pack() #text area to display data

        self.indframe = Frame(master, bg="#22263d") #frame to hold entry and button for individual records
        self.indframe.pack(pady=5)
        self.id_label = Label(self.indframe, text="Student ID:", font=("tacoma", 15), bg="#22263d", fg="#ffffff")
        self.id_label.pack(side=LEFT) 
        self.id_entry = Entry(self.indframe, font=("tacoma", 15), fg="#22263d", bg="#ffffff")
        self.id_entry.pack(side=LEFT, padx=25) #entry and label to search individual records by student id
        
        self.view_individual_button = Button(self.indframe, text="View Individual Record", font=("tacoma", 15), command=self.indivrecord, bg="#22263d", fg="#ffffff")
        self.view_individual_button.pack(pady=5) #button to search individual records by student id

        self.viewall = Button(master, text="View All Records", font=("tacoma", 15), command=self.viewall, bg="#22263d", fg="#ffffff", width=50)
        self.viewall.pack(pady=5) #button to view all student records
        
        self.score_stats_button = Button(master, text="Show Lowest / Highest Score",font=("tacoma", 15), command=self.scorestats, bg="#22263d", fg="#ffffff",width=50)
        self.score_stats_button.pack(pady=5) #button to show scores highest to lowest      

    def dataload(self): #function for handling the data
        records = []
        try:
            with open(self.data_file, 'r') as f:
                header = f.readline().strip().split(',') #reads txtdoc header
                for line in f:
                    data = line.strip().split(',')
                    records.append(dict(zip(header, data)))
            return records
        except FileNotFoundError: #in the event of the file not available, will send this.
            messagebox.showerror("Error", f"Data file '{self.data_file}' not found.")
            return []

    def viewall(self): #function for the viewall button
        records = self.dataload() #variable to handle the records
        self.txtarea.delete(1.0, END)
        if records:
            for record in records: #the layout of the insert for the text area for display
                self.txtarea.insert(END, f"ID: {record['ID']}, Name: {record['Name']}, Scores: {record['ExScore1']}, {record['ExScore2']}, {record['ExScore3']}, {record['FinalScore']}\n")
        else:
            self.txtarea.insert(END, "none found.\n") #returned if there is no valid record available

    def indivrecord(self): #function for individual records
        student_id = self.id_entry.get()
        if not student_id:
            messagebox.showwarning("Input Error", "enter a proper id.") #if the given id is not a number
            return

        records = self.dataload() #variable to handle the records
        self.txtarea.delete(1.0, END)
        found = False
        for record in records: #if succeessful, will display this on the text area
            if record['ID'] == student_id:
                self.txtarea.insert(END, f"ID: {record['ID']}, Name: {record['Name']}, Scores: {record['ExScore1']}, {record['ExScore2']}, {record['ExScore3']}, {record['FinalScore']}\n")
                found = True
                break
        if not found: #if the id is not found within the doc, will return this
            self.txtarea.insert(END, f"student with ID '{student_id}' not found.\n")

    def scorestats(self): #functions for handling the scores
        records = self.dataload()
        if not records: #if given anything invalid will return this
            self.txtarea.delete(1.0, END)
            self.txtarea.insert(END, "none found.\n")
            return

        all_scores = [] #variable to handle all scores
        for record in records: 
            try:
                all_scores.extend([int(record['ExScore1']), int(record['ExScore2']), int(record['ExScore3']), int(record['FinalScore'])])
            except ValueError: #if what is given is not a number, will return this
                messagebox.showwarning("Data Error", "insert a number")

        if all_scores:
            lowest_score = min(all_scores)
            highest_score = max(all_scores)
            self.txtarea.delete(1.0, END)
            self.txtarea.insert(END, f"Lowest Score: {lowest_score}\n")
            self.txtarea.insert(END, f"Highest Score: {highest_score}\n")
        else:
            self.txtarea.delete(1.0, END) #if there is no valid data within the doc
            self.txtarea.insert(END, "none found.\n")

def instrucion(): #function for instructions for the user to understand the system
    messagebox.showinfo("instruction", "search for student id by individual as inputted on the entry, or view all data, or check scores from lowest to highest, it's not rocket science!")
    
main = Tk()
app = TheManager(main) #commences the app on run
main.geometry("900x650")
main.resizable(False, False) #fixed size
main.iconphoto(False, ImageTk.PhotoImage(file="icon.png"))
main['bg']='#22263d'

inttt = Button(main, text="instructions", font=("tacoma", 15), command=instrucion,)
inttt.place(x=25, y=550, height=30, width=125) #instruction button

quitbt = Button(main, text="quit", font=("tacoma", 15), command=main.destroy,)
quitbt.place(x=25, y=600, height=30, width=125) #quit button that closes the app

main.mainloop()