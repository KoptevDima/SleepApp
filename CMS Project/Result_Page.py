import tkinter as tk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

from Login_Page import username
from SleepData_Input import hours_slept

def give_result():
        reference_hours = 8
        if hours_slept > reference_hours:
            messagebox.showinfo("Result", f"{username}, You slept {hours_slept} hours, which is more than the recommended {reference_hours} hours.")
        elif hours_slept < reference_hours:
            messagebox.showinfo("Result", f"{username}, You slept {hours_slept} hours, which is less than the recommended {reference_hours} hours.")
        else:
             messagebox.showinfo("Result", f"{username}, You slept {hours_slept} hours, which is the recommended amount of sleep.")

Result_screen = tk.Tk()
Result_screen.title("Login")
Result_screen.geometry("350x500")
Result_screen.configure(bg="black")


# Load and display the image
image = Image.open("Assets\LogoY13.png")
image = image.resize((75, 75))  # Adjust the size of the image as needed
image_tk = ImageTk.PhotoImage(image)
image_label = tk.Label(Result_screen, image=image_tk, bg="black")
image_label.place(x=275, y=5)  


# Create a label to display the app name
app_label = tk.Label(Result_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 15, "bold"))
app_label.place(x=200, y=15)


# Create a label to display the thanks message
Thanks_label = tk.Label(Result_screen, text="Thanks!", bg="black", fg="white", width="10", height="2", font=("Blinker", 20, "bold"))
Thanks_label.place(x=20, y=75)


Result_label = tk.Label(Result_screen, text="Here's your result", bg="black", fg="#FFDE59", width="20", height="2", font=("Blinker", 20, "bold"))
Result_label.place(x=0, y=125)


tk.Label(Result_screen, text="This is your sleep result", bg="black", fg="#0CC0DF").place(x=55, y=185)


# Create login button
tk.Button(Result_screen, text="Submit", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2").place(x=50, y=360)

Result_screen.mainloop()