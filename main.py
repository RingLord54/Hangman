from tkinter import *
from tkinter import simpledialog
import random
import Utilities
import words

wrong = ""  # characters that are wrong
Turns_Left = 10  # Used for displaying the amount of turns the Player has
rn = random.randint(0, len(words.words) - 1)  # selects a random word from the above list
root = Tk()  # Creates main Application window


root.geometry("1000x800")  # Sets the dimensions of the Application window to 1440 x 720
root.config(bg="#ebeef2")  # Sets the background colour for the application window to a light-grey
root.title("Hangman")  # Sets the Title of the Application window to "Hangman"
root.resizable(False, False)  # Sets it so that the Application window can't be resized


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


# Creates Turn Box
# ----------------------------------
T4 = Text(root, width=14, height=1)
T4.place(x=590, y=243)
T4.config(font=("Courier", 32, "bold"), bg="#ebeef2", highlightthickness=0, borderwidth=0)
T4.configure(state="normal")
T4.insert(END, f"Turns Left: {Turns_Left}")


# Creates the Image for the Hangman Game
# ----------------------------------
img = PhotoImage(file='Images/Hangman_S7.png')
L1 = Label(root, image=img, width=450, height=500)
L1.place(x=40, y=100)


# Functions allows player to make a guess
# ----------------------------------
def make_guess():
    secret = words.words[rn]  # Declare a variable to store the secret word for easy readability
    choice = Utilities.user_input()  # Gets the letter guessed by the Player
    places = Utilities.find_indices(secret, choice)  # Gets an Array of the index positions where the guessed letter appears in the secret word

    # If the letter guessed exists in the word
    if len(places) > 0:
        # Replace the * characters with the guessed letter
        # Also check to see if the word has been guessed correctly yet or not
        Utilities.update_secret_word(root, END, choice, places, letters, secret)

    # If the letter guessed does not exist in the word
    else:
        global wrong  # Crate global variable for the Wrong Answers string
        wrong = Utilities.update_wrong_answers(choice, T3, END, wrong)  # Add to Wrong Answers

    global Turns_Left  # Create global variable for the Turn Count
    Turns_Left = Utilities.update_turn_count(Turns_Left, T4, END)  # Update the Displayed Turn Count

    # If the Player has no Turns left
    if Turns_Left == 0:
        Utilities.end_game(root, secret, letters, END)  # Display the Correct word in red and end the game


# Creates a Button that will allow the player to make a guess
# ----------------------------------
B1 = Button(root, text="Make A Guess", command=make_guess)
B1.config(font=('Courier', 20, 'bold'), bg="#b8b6b6", highlightthickness=0, borderwidth=2)
B1.place(x=155, y=710)


root.mainloop()  # Runs the Application window
