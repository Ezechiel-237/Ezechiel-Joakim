import tkinter as tk
from tkinter import messagebox
from openpyxl import workbook, load_workbook
import csv
import os

excel_file = "registration_data.xlsx"

filename = "users.csv"

# Make sure the CSV file exists if not create one
if not os.path.isfile(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password", "contact", "email"])

# --- Function to register user ---
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    contact= entry_contact.get()
    email= entry_email.get()

    if username == "" or password == ""  or contact == "" or email == "":
        messagebox.showwarning("Input Error", "Both fields are required.")
        return

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                messagebox.showerror("Error", "Username already exists.")
                return

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, contact, email ])
        messagebox.showinfo("Success", "Registration successful!")

   


# --- Function to login user ---
def login_user():
    username = entry_username.get()
    password = entry_password.get()
    contact= entry_contact.get()
    email= entry_email.get()


    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password and row["Number"] == contact and row["Email"] == email:
                messagebox.showinfo("Success", "Login successful!")
                return
        messagebox.showerror("Failed", "Invalid username or password.")

# --- GUI Window ---
root = tk.Tk()
root.title("Login Form")
root.geometry("500x500")
root.configure(bg="#f0f4f7")

# Labels
label_title = tk.Label(root, text="", font=("Arial", 20))
label_title.pack(pady=10)
title_font= ("Arial",20 ,"bold")
label_title= tk.Label(root, text="CONTACT FORM",font=title_font, bg="#f0f4f7",)
label_title.pack(pady=20)

label_user = tk.Label(root, text="Username:")
label_color= ("#333")
label_font= ("Arial",12)
label_user.pack()
entry_username = tk.Entry(root)
entry_font= ("Arial",12)
entry_username.pack()

label_pass = tk.Label(root, text="Password:")
label_color= ("#333")
label_font= ("Arial",12)
label_pass.pack()
entry_password = tk.Entry(root, show="*")
entry_font= ("Arial",12)
entry_password.pack()

label_contact = tk.Label(root, text="contact:")
label_color= ("#333")
label_font= ("Arial",12)
label_contact.pack()
entry_contact = tk.Entry(root, show="*")
entry_font= ("Arial",12)
entry_contact.pack()

label_email = tk.Label(root, text="email")
label_color= ("#333")
label_font= ("Arial",12)
label_email.pack()
entry_email = tk.Entry(root, show="*")
entry_font= ("Arial",12)
entry_email.pack()

# Buttons

button_frame= tk.Frame(root, bg="#f0f4f7")
button_frame.pack(pady=20)

btn_login = tk.Button(root, text="Login", command=login_user)
btn_login.pack(pady=5,padx=10)
button_color=("#007acc")
button_text_color=("#fff")
btn_login= tk.Button(button_frame, text="Login",font=label_font, bg=button_color, fg=button_text_color, width=10)
btn_login.grid(row=0, column=0, padx=10)

btn_register = tk.Button(root, text="Register", command=register_user)
btn_register.pack(pady=5,padx=10)
button_color=("#007acc")
button_text_color=("#fff")
btn_register= tk.Button(button_frame, text="Register", font=label_font, bg=button_color, fg=button_text_color, width=10)
btn_register.grid(row=0, column=0, padx=10)


# font and color









#  title


# button frame to flex




# Run the app
root.mainloop()