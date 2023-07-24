import tkinter as tk
from tkinter import messagebox
import subprocess
import os
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import re

def open_login_page():
    # Open the Login_Page.py file using subprocess
    subprocess.Popen(["python", "Login_Page.py"])
    # Close the main screen
    registration_screen.destroy()

def register_user():
    # Get the username and password entered by the user
    username = username_login_entry.get()
    password = password_login_entry.get()


    # Connect to the database or create a new one if it doesn't exist
    conn = sqlite3.connect(r'DB\user_credentials.db')


    # Create a table to store user credentials if it doesn't exist
    table_create_query = '''CREATE TABLE IF NOT EXISTS UsersLogin
            (User_Name TEXT, Password TEXT)
    '''
    conn.execute(table_create_query)


    # Check if the username already exists
    check_query = 'SELECT User_Name FROM UsersLogin WHERE User_Name = ?'
    cursor = conn.cursor()
    cursor.execute(check_query, (username,))
    existing_user = cursor.fetchone()


    # Validate the username to allow only letters
    if not re.match("^[a-zA-Z]+$", username):
        # Show an error message if the username contains non-letter characters
        messagebox.showerror('Registration', 'Username should only contain letters!')
        return
    
    # Validate the password to contain a capital letter and a number
    if not (re.search(r"[A-Z]", password) and re.search(r"\d", password)):
        # Show an error message if the password doesn't meet the criteria
        messagebox.showerror('Registration', 'Password must contain a capital letter and a number!')
        conn.close()
        return
    
    # Validate the password to not contain spaces
    if ' ' in password:
        # Show an error message if the password contains spaces
        messagebox.showerror('Registration', 'Password cannot contain spaces!')
        conn.close()
        return
    
        # Validate the password to contain at least 8 characters
    if len(password) < 8:
        # Show an error message if the password is too short
        messagebox.showerror('Registration', 'Password must contain at least 8 characters!')
        conn.close()
        return

    if existing_user:
        # Show an error message if the username already exists
        messagebox.showerror('Registration', 'Username already exists!')
    else:
        # Insert the new user into the database
        insert_query = 'INSERT INTO UsersLogin (User_Name, Password) VALUES (?, ?)'
        insert_data = (username, password)
        cursor.execute(insert_query, insert_data)
        conn.commit()
        # Show a success message
        messagebox.showinfo('Registration', 'Registration successful!')
        # take user to login page after they created an account
        open_login_page()


    # Close the database connection
    conn.close()


registration_screen = tk.Tk()
registration_screen.title("Registration")
registration_screen.geometry("350x500")
registration_screen.configure(bg="black")


# Load and display the image
image = Image.open("Assets\LogoY13.png")  # Replace "image.jpg" with the path to your image
image = image.resize((75, 75))  # Adjust the size of the image as needed
image_tk = ImageTk.PhotoImage(image)
image_label = Label(registration_screen, image=image_tk, bg="black")
image_label.place(x=275, y=5)  


# Create a label to display the app name
app_label = Label(registration_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
app_label.place(x=200, y=15)


# Create a label to display the welcome message
hi_label = Label(registration_screen, text="Hi!", bg="black", fg="white", width="5", height="2", font=("Blinker", 20, "bold"))
hi_label.place(x=25, y=110)


welcome_label = Label(registration_screen, text="Welcome", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
welcome_label.place(x=25, y=160)


username_verify = tk.StringVar()
password_verify = tk.StringVar()


tk.Label(registration_screen, text="Please enter details below to register", bg="black", fg="#0CC0DF").place(x=50, y=230)


tk.Label(registration_screen, text="Username * ", bg="black", fg="white").place(x=50, y=285)
username_login_entry = tk.Entry(registration_screen, textvariable=username_verify)
username_login_entry.place(x=160, y=285)


tk.Label(registration_screen, text="Password * ", bg="black", fg="white").place(x=50, y=315)
password_login_entry = tk.Entry(registration_screen, textvariable=password_verify, show='*')
password_login_entry.place(x=160, y=315)


tk.Button(registration_screen, text="Register", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=register_user).place(x=50, y=365)


# switch to register page message
tk.Label(registration_screen, text="Have an account?", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold")).place(x=30, y=440)

# Create the button to switch to register page
tk.Button(registration_screen, text="Login", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command=open_login_page).place(x=190, y=440)


registration_screen.mainloop()
