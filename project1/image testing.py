import tkinter as tk
from tkinter import PhotoImage

# Create the main window
root = tk.Tk()
root.title("Background Image Example")
root.geometry("500x400")  # Set window size

# Load the image (image needs to be .png, .gif)
bg_image = PhotoImage(file="POKER HOME SCREEN_1.jpg")

# Create a label to display the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a button on top of the background
button = tk.Button(root, text="Click Me!")
button.place(x=200, y=200)

# Start the Tkinter event loop
root.mainloop()

