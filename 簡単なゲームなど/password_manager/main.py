from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    generated_password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
                }
            }

    if website and email and password:
        is_ok = messagebox.askokcancel(title="Confirm Information", message=f"These are the details entered:"
                                                                            f" \nWebsite: {website} \nEmail: {email} "
                                                                            f"\nPassword: {password} \nClick ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as data:
                    json_data = json.load(data)
                    print(json_data)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)

            else:
                json_data.update(new_data)

                with open("data.json", "w") as data:
                    json.dump(json_data, data, indent=4)

            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty!")


def find_password():

    try:
        with open("data.json", "r") as data:
            json_data = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title=" File Not Found", message="No Data File Found\nYou haven't made a password ")
    else:

        website = website_input.get()
        if website in json_data:
            email = json_data[website]["email"]
            password = json_data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the website exists.\nYou typed {website}\nPlease Check spell and case")

    # messagebox.showinfo(title=f"{website}", message=f"Website: {website}\nEmail: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, sticky=EW)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky=EW)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()
