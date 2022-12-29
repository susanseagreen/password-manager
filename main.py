from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    password_list = []

    for _ in range(random.randint(8, 10)):
        password_list.append(random.choice(letters))

    for _ in range(random.randint(2, 4)):
        password_list += random.choice(symbols)

    for _ in range(random.randint(2, 4)):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    password = password_input.get()

    if not website or not password:
        messagebox.showwarning(title="Missing Data", message="Please double check the form.\n\nSome fields have been left empty")
    else:
        can_save = messagebox.askokcancel(title=website, message=f"{website}\n\nWould you like to save your password as '{password}'?")

        if can_save:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", width=10)
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

password_label = Label(text="Password", width=10)
password_label.grid(column=0, row=3)
password_input = Entry(width=20)
password_input.grid(column=1, row=3)

generate_password_btn = Button(text="Generate Password", width=11, command=generate)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=8, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
