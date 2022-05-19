from tkinter import *

root = Tk() # Creates main Application window

root.geometry("1000x800") # Sets the dimensions of the Application window to 1440 x 720
root.title("Hangman") # Sets the Title of the Application window to "Hangman"
root.resizable(False, False) # Sets it so that the Application window can't be resized

Frame_top = Frame( root, bg='red', width=960, height=60) # Creates Frame for Title
Frame_Lmiddle1 = Frame( root, bg='blue', width=450, height=500 ) # Creates Frame for the Picture
Frame_Lmiddle2 = Frame( root, bg='green', width=450, height=160 ) # Creates Frame for where the word will be guessed
Frame_Rmiddle = Frame( root, bg='yellow', width=450, height=350) # Creates Frame for where the wrong letters will appear

# Places the Frames
Frame_top.place(x=20, y=20)
Frame_Lmiddle1.place(x=40, y=100)
Frame_Lmiddle2.place(x=40, y=620)
Frame_Rmiddle.place(x=510, y=275)

root.mainloop() # Runs the Application window

