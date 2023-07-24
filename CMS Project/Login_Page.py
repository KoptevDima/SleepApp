import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

def open_register_page():
    # Open the Register_Page.py file using subprocess
    subprocess.Popen(["python", "Register_Page.py"])
    # Close the main screen
    login_screen.destroy()

def open_input_page():
    # Open the Register_Page.py file using subprocess
    subprocess.Popen(["python", "SleepData_Input.py"])
    # Close the main screen
    login_screen.destroy()
    

def login(username_entry, password_entry):
    global username
    
    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect(r'DB\user_credentials.db')

    # Execute a SELECT query to check if the username and password match
    query = 'SELECT * FROM UsersLogin WHERE User_Name = ? AND Password = ?'
    cursor = conn.cursor()
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    # Check if a matching user is found
    if user:
        # Show a success message
        messagebox.showinfo('Login', 'Login successful!')
        # Take the user to the input page after they logged in
        open_input_page()
    else:
        # Show an error message if the login credentials are invalid
        messagebox.showerror('Login', 'Invalid username or password!')

    # Close the database connection
    conn.close()


login_screen = tk.Tk()
login_screen.title("Login")
login_screen.geometry("350x500")
login_screen.configure(bg="black")


# Load and display the image
image = Image.open("Assets\LogoY13.png")
image = image.resize((75, 75))  # Adjust the size of the image as needed
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(login_screen, image=image_tk, bg="black")
image_label.place(x=275, y=5)  


# Create a label to display the app name
app_label = tk.Label(login_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
app_label.place(x=200, y=15)


# Create a label to display the welcome message
hi_label = tk.Label(login_screen, text="Hi!", bg="black", fg="white", width="5", height="2", font=("Blinker", 20, "bold"))
hi_label.place(x=25, y=100)


welcome_label = tk.Label(login_screen, text="Welcome", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
welcome_label.place(x=25, y=150)


username_verify = tk.StringVar()
password_verify = tk.StringVar()


tk.Label(login_screen, text="Please enter details below to login", bg="black", fg="#0CC0DF").place(x=50, y=220)


tk.Label(login_screen, text="Username * ", bg="black", fg="white").place(x=50, y=280)
username_login_entry = tk.Entry(login_screen, textvariable=username_verify)
username_login_entry.place(x=160, y=280)


tk.Label(login_screen, text="Password * ", bg="black", fg="white").place(x=50, y=310)
password_login_entry = tk.Entry(login_screen, textvariable=password_verify, show='*')
password_login_entry.place(x=160, y=310)


# Create login button
tk.Button(login_screen, text="Login", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=lambda: login(username_login_entry, password_login_entry)).place(x=50, y=360)


# switch to register page message
tk.Label(login_screen, text="Don't have an account?", bg="black", fg="#0CC0DF", width="20", height="1", font=("Blinker", 10, "bold")).place(x=35, y=435)

# Create the button to switch to register page
tk.Button(login_screen, text="Register", bg="#FFDE59", fg="#0CC0DF", height="1", width="10", cursor="hand2", command=open_register_page).place(x=200, y=435)


login_screen.mainloop()
