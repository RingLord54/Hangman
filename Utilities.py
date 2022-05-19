def change(letter, END, choice):
    obj = letter
    obj.configure(state="normal")
    obj.delete("1.0", "end")
    obj.insert(END, choice)
    obj.configure(state="disabled")

def find_indices(word, letter):
    indices = []
    for i in range(0, len(word)):
        if word[i] == letter:
            indices.append(i)
    return indices

def isGameWon(letters):
    for i in letters:
        if i.get("1.0", "end") == "_":
            return False
    return True