import random
import tkinter as tk
from PIL import Image, ImageTk  # Import from Pillow

# Create the deck of cards
card_types = (['Ace ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10 ', 'Jack ', 'Queen ', 'King '])
suites = (['hearts', 'diamonds', 'spades', 'clubs'])
deck = [f'{rank} of {suit}' for rank in card_types for suit in suites]

window = tk.Tk()
window.geometry("500x500")
window.title('Poker')

wallet = int(100)

# Load the original image
image = Image.open("POKER HOME SCREEN_1.jpg")

# Global variable for background label
bg_label = None

# Resize image function, triggered when window resizes
def resize_image(event):  
    new_width = event.width
    new_height = event.height
    
    # Resize the image based on the new window size
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    
    # Keep a reference to prevent garbage collection
    window.bg_image = bg_image
    
    # Update the background image in the label
    if bg_label:
        bg_label.config(image=bg_image)

def welcome():  # Welcome screen
    clear_page()
    
    # Create and display the resized background image
    resized_image = image.resize((500, 500), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image  # Store the image as an attribute of the window
    global bg_label  # Make bg_label global so it can be updated in resize_image()
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the window with the background image

    # Center the welcome screen widgets
    welcome_label = tk.Label(window, text="Enter name below", font=("georgia", 20), bg="snow2")
    welcome_label.place(x=(window.winfo_width() - welcome_label.winfo_reqwidth()) / 2, y=50)

    name_entry = tk.Entry(window, bg='snow2', fg='black', font=("georgia", 20))
    name_entry.place(x=(window.winfo_width() - 300) / 2, y=150, width=300)

    play_button = tk.Button(window, bg="snow2", fg='black', text="Play!", font=("georgia", 20), command=lambda: pre_bet(name=name_entry.get()))
    play_button.place(x=(window.winfo_width() - play_button.winfo_reqwidth()) / 2, y=250)

    settings_button = tk.Button(window, text='Settings', font=('georgia', 20), command=lambda: settings_page())
    settings_button.place(x=(window.winfo_width() - settings_button.winfo_reqwidth()) / 2, y=350)

    wallet_label = tk.Label(window, text=f'Wallet: ${wallet}', bg='snow2', font=("georgia", 20))
    wallet_label.place(x=(window.winfo_width() - wallet_label.winfo_reqwidth()) / 2, y=450)

def clear_page():  # Clears the page when called
    for widget in window.winfo_children():
        widget.place_forget()

def pre_bet(name):  # Function before the first bet
    username = str(name)
    clear_page()
    name_label = tk.Label(window, text=f'Welcome {username}', font=('georgia', 30), bg="snow2")
    name_label.place(x=(window.winfo_width() - name_label.winfo_reqwidth()) / 2, y=150)

    deal_button = tk.Button(window, text='DEAL!', font=('georgia', 20), command=lambda: blind())
    deal_button.place(x=(window.winfo_width() - deal_button.winfo_reqwidth()) / 2, y=250)

def settings_page():  # Settings page
    clear_page()
    settings_placeholder_label = tk.Label(window, text='Placeholder! Settings coming soon.', font=('georgia', 20), bg="snow2")
    settings_placeholder_label.place(x=(window.winfo_width() - settings_placeholder_label.winfo_reqwidth()) / 2, y=200)

    back_from_settings_button = tk.Button(window, text='Back', font=('georgia', 20), command=lambda: welcome())
    back_from_settings_button.place(x=(window.winfo_width() - back_from_settings_button.winfo_reqwidth()) / 2, y=350)

def blind():  # First deal
    clear_page()
    drawn_cards = random.sample(deck, 3)
    cards_label = tk.Label(window, text="\n".join(drawn_cards), font=('Georgia', 20), bg="snow2")
    cards_label.place(x=(window.winfo_width() - cards_label.winfo_reqwidth()) / 2, y=150)

# Start the application with the welcome screen
welcome()

# Bind the resize event to the resize_image function
window.bind("<Configure>", resize_image)

window.mainloop()


