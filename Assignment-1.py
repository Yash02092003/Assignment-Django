import tkinter as tk
from tkinter import Label, Entry, Button
import csv

root = tk.Tk()
root.title("Registration Form")

with open("formData.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "email", "contact", "address"])


name = Label(root, text="Name")
name.grid(row=0, column=0, padx=10, pady=10)
email = Label(root, text="Email")
email.grid(row=1, column=0, padx=10, pady=10)
contact = Label(root, text="Contact No")
contact.grid(row=2, column=0, padx=10, pady=10)
address = Label(root, text="Address")
address.grid(row=3, column=0, padx=10, pady=10)

nameEntry = Entry(root)
nameEntry.grid(row=0, column=1, padx=10, pady=10)
emailEntry = Entry(root)
emailEntry.grid(row=1, column=1, padx=10, pady=10)
contactEntry = Entry(root)
contactEntry.grid(row=2, column=1, padx=10, pady=10)
addressEntry = Entry(root)
addressEntry.grid(row=3, column=1, padx=10, pady=10)


def submitForm(): 
    name = nameEntry.get()
    email = emailEntry.get()
    contact = contactEntry.get()
    address = addressEntry.get()

    nameEntry.delete(0, tk.END)
    emailEntry.delete(0, tk.END)
    contactEntry.delete(0, tk.END)
    addressEntry.delete(0, tk.END)

    with open("formData.csv", "a+", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, contact, address])

btn = Button(text="Submit", command=submitForm)
btn.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
