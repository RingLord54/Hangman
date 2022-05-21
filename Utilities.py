# Used to Change the Text in the given Text Widget Object
def change(letter, END, choice):
    letter.configure(state="normal")
    letter.delete("1.0", "end")
    letter.insert(END, choice)
    letter.configure(state="disabled")


# Used to find the index positions (if any) of your guessed letter in the secret word
def find_indices(word, letter):
    indices = []
    for i in range(0, len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices


# Used to return an Array of the current characters within the individual Text Widgets
def new_letters(letters):
    newLetters = []
    for i in letters:
        newLetters.append(i.get("1.0", "2.0"))
    return newLetters


# Used to change the Array of characters into a string instead
def new_word(letters):
    newWord = ""
    for i in letters:
        newWord += i[0]
    return newWord
