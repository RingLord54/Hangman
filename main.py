import random
import Utilities
import words
from tkinter import *
from tkinter import simpledialog

wrong = ""  # characters that are wrong
count = 1  # Used for moving through the images
root = Tk()  # Creates main Application window
root.geometry("1000x800")  # Sets the dimensions of the Application window to 1440 x 720
root.config(bg="#ebeef2")  # Sets the background colour for the application window to a light-grey
root.title("Hangman")  # Sets the Title of the Application window to "Hangman"
root.resizable(False, False)  # Sets it so that the Application window can't be resized
rn = random.randint(0, len(words.words) - 1)  # selects a random word from the above list

# Creates Title Text Box
# ----------------------------------
T1 = Text(root, width=12, height=1)
T1.place(x=340, y=23)
T1.config(font=("Courier", 32, "bold"), bg="#ebeef2", highlightthickness=0, borderwidth=0)
T1.configure(state="normal")
T1.insert(END, "Hangman Game")

# Creates Text Boxes for the Word that has to be guessed
# ----------------------------------
ranges = [145, 195, 245, 295, 345]
letters = []
for i in range(0, 5):
    T2 = Text(root, width=12, height=1)
    T2.place(x=ranges[i], y=620)
    T2.config(font=("Courier", 32, "bold"), bg="#ebeef2", highlightthickness=0, borderwidth=0)
    T2.configure(state="normal")
    T2.insert(END, "*")
    T2.configure(state="disabled")
    letters.append(T2)

# Creates Text Box for Wrong Answers
# ----------------------------------
T3 = Text(root, width=13, height=4)
T3.place(x=590, y=323)
T3.config(font=("Courier", 32, "bold"), bg="#bec0c2", borderwidth=2)
T3.configure(state="normal")
T3.insert(END, "")

# Creates the Image for the Hangman Game
# ----------------------------------
img = PhotoImage(file='Images/Hangman_S7.png')
L1 = Label(root, image=img, width=450, height=500)
L1.place(x=40, y=100)


# Functions allows player to make a guess
# ----------------------------------
def make_guess():
    while True:
        choice = simpledialog.askstring("Hangman", "Guess a Letter")
        if choice is not None and len(choice) == 1:
            break
    places = Utilities.find_indices(words.words[rn], choice)
    if len(places) > 0:
        for i in places:
            Utilities.change(letters[i], END, choice.upper())
        newLetters = Utilities.new_letters(letters)
        newWord = Utilities.new_word(newLetters)
        if newWord == words.words[rn].upper():
            simpledialog.messagebox.showinfo("Hangman", "Congratulations! You Won! Thank you for playing")
            root.destroy()
    else:
        global wrong
        if choice not in wrong:
            wrong += " " + choice.upper()
            Utilities.change(T3, END, wrong)


# Creates a Button that will allow the player to make a guess
# ----------------------------------
B1 = Button(root, text="Make A Guess", command=make_guess)
B1.config(font=('Courier', 20, 'bold'), bg="#b8b6b6", highlightthickness=0, borderwidth=2)
B1.place(x=155, y=710)


root.mainloop()  # Runs the Application window
