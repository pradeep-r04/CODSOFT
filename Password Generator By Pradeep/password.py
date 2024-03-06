from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    all = small_alphabets + capital_alphabets + special_characters + numbers
    password_length = int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets + capital_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets + capital_alphabets + numbers,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(small_alphabets+ capital_alphabets + numbers + special_characters,password_length))


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root=Tk()
root.config(bg='cadetblue')
choice=IntVar()
Font=('Ariel',14, 'bold')
passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20,'bold'),
                      bg='cadetblue', fg='white')
passwordLabel.grid(pady=10)

weakradioButton = Radiobutton(root, text='Weak',bg='lightcyan', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)
mediumradioButton = Radiobutton(root, text='Medium',bg='lightcyan', value=2, variable = choice, font=Font)
mediumradioButton.grid(pady=5)
strongradioButton = Radiobutton(root, text='Strong',bg='lightcyan', value=3, variable = choice, font=Font)
strongradioButton.grid(pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='cadetblue', fg='white')
lengthLabel.grid(pady=5)

length_Box= Spinbox(root, from_= 5, to_=18, width=5,bg='lightcyan', font=Font)
length_Box.grid(pady=5)

generateButton = Button(root, text='Generate',bg='lightcyan', font=Font, command = generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(pady=5)

copyButton = Button(root, text='Copy',bg='palegreen', font=Font, command=copy)
copyButton.grid(pady=5)

root.mainloop()