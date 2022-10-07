from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

my_label1 = Label(text="is equal to", font=("Arial", 10, "normal"))
my_label1.grid(column=0, row=1)

my_label2 = Label(text="Km", font=("Arial", 10, "normal"))
my_label2.grid(column=2, row=1)

my_label3 = Label(text="Miles", font=("Arial", 10, "normal"))
my_label3.grid(column=2, row=0)

result = Label(text=0, font=("Arial", 10, "normal"))
result.grid(column=1, row=1)


def calculate():
    result["text"] = int(int(input.get()) * 1.6)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

input = Entry()
input.grid(column=1, row=0)

window.mainloop()
