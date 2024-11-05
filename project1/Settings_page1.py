import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('300x300')

# Path to your images
green = "POKER HOME SCREEN_1.jpg"
gold = "gold1.jpg"
cat = "cat1.jpg"

selected_theme = gold 

def clear_page(): 
    for widget in window.winfo_children():
        widget.pack_forget()

def testpage():
    image = Image.open(selected_theme)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    setting_button = tk.Button(window, text='Settings', font=('Georgia', 20), command=settings)
    setting_button.pack(pady=10)

def settings():
    image = Image.open(selected_theme)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    settings_label = tk.Label(window, text='Settings', font=('Georgia', 20))
    settings_label.pack(pady=20)
    
    background_button = tk.Button(window, text='Change Background', font=('Georgia', 20), command=background_menu)
    background_button.pack(pady=20)

def background_menu():
    clear_page()  
    new_background_label = tk.Label(window, text='Choose Background', font=('Georgia', 20))
    new_background_label.pack(pady=20)
    
    green_button = tk.Button(window, text='Green', font=('Georgia', 20), command=lambda: commit_theme(green))
    green_button.pack(pady=20)
    
    gold_button = tk.Button(window, text='Gold', font=('Georgia', 20), command=lambda: commit_theme(gold))
    gold_button.pack(pady=20)

    cat_button = tk.Button(window, text = 'Cat', font = ('georgia', 20),command=lambda:commit_theme(cat))
    cat_button.pack(pady = 20)

def commit_theme(theme):
    global selected_theme
    selected_theme = theme 
    testpage()

testpage()

window.mainloop()