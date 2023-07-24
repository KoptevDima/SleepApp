import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

from Login_Page import username

def open_result_page():
    # Open the Login_Page.py file using subprocess
    subprocess.Popen(["python", "SleepData_Input.py"])
    # Close the main screen
    Input_screen.destroy()

def save_sleep_data():
    global hours_slept

    hours_slept = hours_entry.get()

    try:
        hours_slept = float(hours_entry.get())
        if 0 <= hours_slept <= 24:
            messagebox.showinfo({username}, "your result has been recorded")
            open_result_page()
        else:
            messagebox.showwarning("Invalid Input", "The number of hours slept should be between 0 and 24.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


Input_screen = tk.Tk()
Input_screen.title("Login")
Input_screen.geometry("350x500")
Input_screen.configure(bg="black")


# Load and display the image
image = Image.open("Assets\LogoY13.png")
image = image.resize((75, 75))  # Adjust the size of the image as needed
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(Input_screen, image=image_tk, bg="black")
image_label.place(x=275, y=5)  


# Create a label to display the app name
app_label = tk.Label(Input_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
app_label.place(x=200, y=15)


# Create a label to display the let's message
lets_label = tk.Label(Input_screen, text="Let's", bg="black", fg="white", width="10", height="2", font=("Blinker", 20, "bold"))
lets_label.place(x=5, y=100)


start_label = tk.Label(Input_screen, text="Get started", bg="black", fg="#FFDE59", width="10", height="2", font=("Blinker", 20, "bold"))
start_label.place(x=45, y=150)


tk.Label(Input_screen, text="Please enter your sleep data below", bg="black", fg="#0CC0DF").place(x=60, y=220)


tk.Label(Input_screen, text="Number of hours \n slept* ", bg="black", fg="white").place(x=50, y=290)
hours_entry = tk.Entry(Input_screen)
hours_entry.place(x=160, y=290)


# Create login button
tk.Button(Input_screen, text="Submit", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=lambda: save_sleep_data()).place(x=50, y=380)

Input_screen.mainloop()
