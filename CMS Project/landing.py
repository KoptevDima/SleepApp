#import modules
import tkinter as tk
import subprocess
from tkinter import *
import os
from PIL import Image, ImageTk


def open_login_page():
    # Open the Login_Page.py file using subprocess
    subprocess.Popen(["python", "Login_Page.py"])
    # Close the main screen
    main_screen.destroy()


def open_register_page():
    # Open the Register_Page.py file using subprocess
    subprocess.Popen(["python", "Register_Page.py"])
    # Close the main screen
    main_screen.destroy()


# Designing Main(first) window
# Adjust the position of the image as needed# Create the main window
main_screen = Tk()
main_screen.geometry("350x500")
main_screen.title("Landing Page")
main_screen.configure(bg="black")


# Load and display the image
image = Image.open("Assets\LogoY13.png")  # Replace "image.jpg" with the path to your image
image = image.resize((100, 100))  # Adjust the size of the image as needed
image_tk = ImageTk.PhotoImage(image)
image_label = Label(main_screen, image=image_tk, bg="black")
image_label.place(x=160, y=10)  


# Create a label to display the app name
app_label = Label(main_screen, text="Sleep \n Genius", bg="black", fg="#FFDE59", width="6", height="2", font=("Blinker", 20, "bold"))
app_label.place(x=75, y=25)


# Create a label to display the welcome message
hi_label = Label(main_screen, text="Hi!", bg="black", fg="white", width="15", height="2", font=("Blinker", 20, "bold"))
hi_label.place(x=0, y=130)


welcome_label = Label(main_screen, text="Welcome", bg="black", fg="#FFDE59", width="20", height="2", font=("Blinker", 20, "bold"))
welcome_label.place(x=0, y=180)


# Create the login button
login_button = Button(main_screen, text="Login", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=open_login_page)
login_button.place(x=60, y=275)


# Create the register button
register_button = Button(main_screen, text="Register", bg="#0CC0DF", fg="white", height="2", width="30", cursor="hand2", command=open_register_page)
register_button.place(x=60, y=325)


main_screen.mainloop()
