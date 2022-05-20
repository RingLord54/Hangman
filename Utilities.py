
def change(letter, END, choice):
    letter.configure(state="normal")
    letter.delete("1.0", "end")
    letter.insert(END, choice)
    letter.configure(state="disabled")


def find_indices(word, letter):
    indices = []
    for i in range(0, len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices


def new_letters(letters):
    newLetters = []
    for i in letters:
        newLetters.append(i.get("1.0", "2.0"))
    return newLetters


def new_word(letters):
    newWord = ""
    for i in letters:
        newWord += i[0]
    return newWord