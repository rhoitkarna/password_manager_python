from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbol

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Can't leave the fields, Email or Password empty.")
    else:
        try:
            with open("information.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("information.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("information.json ", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# -------------------------SEARCH DATA --------------------------#


def search_data():
    search_website = website_entry.get().title()
    try:
        with open("information.json", "r") as file:
            file_contents = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message=f"The information for {search_website} doesn't exist.")
    else:
        if search_website in file_contents:
            required_info = file_contents[search_website]
            password = required_info["password"]
            messagebox.showinfo(title=f"{search_website}", message=f"Email: {email_entry.get()}\nPassword: {password}")
        else:
            messagebox.showerror(title="Oops", message=f"The information for {search_website} doesn't exist.")
    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password  Manager")
window.config(padx=70, pady=70)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search Information", command=search_data)
search_button.grid(row=1, column=2)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "rohitkarn627@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
