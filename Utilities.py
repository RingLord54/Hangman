from tkinter import simpledialog

# Used to Change the Text in the given Text Widget Object
def change(object, END, choice, colour=False):
    object.configure(state="normal")
    object.delete("1.0", "end")
    if colour:
        object.config(fg='red')
    object.insert(END, choice)
    object.configure(state="disabled")


# Used to find the index positions (if any) of your guessed letter in the secret word
def find_indices(secret, guess):
    indices = []
    for i in range(0, len(secret)):
        if secret[i] == guess:
            indices.append(i)
    return indices


# Used to return an Array of the current characters within the individual Text Widgets
def new_letters(objects):
    newLetters = []
    for i in objects:
        newLetters.append(i.get("1.0", "2.0"))
    return newLetters


# Used to change the Array of characters into a string instead
def new_word(objects):
    newWord = ""
    for i in objects:
        newWord += i[0]
    return newWord


def user_input():
    while True:
        choice = simpledialog.askstring("Hangman", "Guess a Letter")
        if choice is not None and len(choice) == 1:
            break
    return choice


def update_secret_word(root, END, choice, places, objects, secret):
    for j in places:
        change(objects[j], END, choice.upper())
    newLetters = new_letters(objects)
    newWord = new_word(newLetters)
    if newWord == secret.upper():
        simpledialog.messagebox.showinfo("Hangman", "Congratulations! You Won! Thank you for playing")
        root.destroy()


def update_wrong_answers(choice, object, END, wrong):
    if choice.upper() not in wrong:
        wrong += " " + choice.upper()
        change(object, END, wrong)
    return wrong


def update_turn_count(turns, object, END):
    turns -= 1
    updateTurns = f"Turns Left: {turns}"
    change(object, END, updateTurns)
    return turns


def end_game(root, secret, objects, END):
    for k in range(0, len(secret)):
        change(objects[k], END, secret[k].upper(), True)
    simpledialog.messagebox.showinfo("Hangman", "You Lose. Better Luck Next Time!")
    root.destroy()