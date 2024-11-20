
import random
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("500x500")#change to make full screen before relese (or do something with settings)
window.title('Poker')

card_types = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits = ['hearts','diamonds','spades','clubs']

deck = [f'{rank} of {suit}' for rank in card_types for suit in suits]

#dictionary to map card names to image files
card_images = {}

# Populates the dictionary with the card images
for rank in card_types:
    for suit in suits:
        card_images[f'{rank} of {suit}'] = f'{rank.lower()}_of_{suit}.png'

wallet = int(100)

gold="gold1.jpg"
home_background=gold


def clear_page():
    for widget in window.winfo_children():
        widget.pack_forget()

def welcome (): #welcome screen. (Add settings button and more stuff here)
    clear_page()
    image = Image.open(home_background)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image 
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_label = tk.Label(window, text = "Enter name below", font = ("georgia", 20))
    welcome_label.pack(pady=20)
    name_entry = tk.Entry(window, font = ("georgia", 20))
    name_entry.pack(pady=20)
    play_button = tk.Button(window, text = "Play!", font = ("georgia", 20),command=lambda: test_name(name=name_entry.get()))
    play_button.pack(pady=20)
    wallet_label = tk.Label(window, text = f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)
    window.bind('<Return>', lambda event: test_name(name=name_entry.get()))

    def test_name(name): #checks if name is valid (name must be betweein 1 and 10 letters and no spaces)
        if len(name) == 0:
            bad_username_label = tk.Label(window, text = 'Please enter a username between 1 and 10 character(s)', font = ('georgia', 10))
            bad_username_label.pack(pady = 15)
            window.after(2000,bad_username_label.destroy)
        elif len(name) > 10:
            bad_username_label = tk.Label(window, text = 'Please enter a username between 1 and 10 character(s)', font = ('georgia', 10))
            bad_username_label.pack(pady = 15)
            window.after(2000,bad_username_label.destroy)
        elif name.count(' ') > 0:
            no_space_username_label = tk.Label(window, text = 'Username must not contain spaces', font = ('georgia', 10))
            no_space_username_label.pack(pady=15)
            window.after(2000,no_space_username_label.destroy)

        
        else:
            window.after(1,lambda:blind())
    window.bind('<Escape>', lambda event:window.destroy())

def clear_page(): #clears page when called. (Time saver)
    for widget in window.winfo_children():
        widget.pack_forget()
        


def blind(): #first deal
    global wallet
    def test_bet(bet,next): #checks if your bet is allowed (<= wallet and int)
        global wallet
        try:
            bet_amount = int(bet,) #checks if bet can be made an int
            if bet_amount > wallet: #bet more than you have
                not_enough_label = tk.Label(window, text = f'Not enough money. Max bet ${wallet}', font=('georgia', 10))
                not_enough_label.pack(pady=20)
                window.after(2000, not_enough_label.destroy)
            else: #bet less than or equal to what you have
                wallet = wallet - bet_amount
                total_betting_label = tk.Label(window, text = f'Betting ${bet_amount}. ${wallet} remaining', font = ('georgia', 10))
                total_betting_label.pack(pady = 20)
                window.after(1000, total_betting_label.destroy)
                window.after(1000, lambda: next())
        except: #bet was either a decimal or text
            error_label = tk.Label(window, text = 'Invalid number', font = ('georgia', 20)) #bet cannot be made an int
            error_label.pack(pady = 20)
            window.after(2000, error_label.destroy)

    def flop():
        bet_enter_label.destroy()
        bet_amount_entry.destroy()
        bet_button.destroy()
        fold_button.destroy()
        wallet_label.destroy()
        drawn_cards_2 = random.sample(deck, 1)
        for card in drawn_cards_2:
            deck.remove(card)
        cards_label_2 = tk.Label(window, text=", ".join(drawn_cards_2), font=('Georgia', 20))
        cards_label_2.pack(pady=0)
        bet_entry_flop = tk.Entry(window, font = ('georgia', 20))
        bet_entry_flop.pack(pady=20)
        bet_button_flop = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_entry_flop.get(),next = turn))
        bet_button_flop.pack(pady=0)
        fold_button_flop = tk.Button(window, text = 'Fold', font = ('georgia', 15))
        fold_button_flop.pack(pady=0)
        wallet_label_2 = tk.Label(window, text = f'Wallet: ${wallet}')
        wallet_label_2.pack(pady=0)
        window.bind('<Return>', lambda event:test_bet(bet_entry_flop.get(),next = turn))
    
        def turn():
            bet_entry_flop.destroy()
            bet_button_flop.destroy()
            fold_button_flop.destroy()
            wallet_label_2.destroy()
            drawn_cards_3 = random.sample(deck, 1)
            for card in drawn_cards_3:
                deck.remove(card)
            cards_label_3 = tk.Label(window, text=", ".join(drawn_cards_3), font=('Georgia', 20))
            cards_label_3.pack(pady=0)
            bet_entry_turn = tk.Entry(window, font = ('georgia', 20))
            bet_entry_turn.pack(pady=20)
            bet_button_turn = tk.Button(window, text = 'BET!', font = ('georgia', 20), command= lambda:test_bet(bet_entry_turn.get()))
            bet_button_turn.pack(pady=20)

            def final():
                print('final placeholder :)')

    
    clear_page() 
    
    drawn_cards = random.sample(deck, 3)

    for card in drawn_cards:
        deck.remove(card)
        image_file = card_images.get(card, None)
        
        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            photo = ImageTk.PhotoImage(image)
            
            # Create a label to display the image
            image_label = tk.Label(window, image=photo)
            image_label.image = photo  # Keep a reference to the image
            image_label.pack(pady=10)

    bet_enter_label = tk.Label(window, text = 'enter bet', font = ('georgia', 20))
    bet_enter_label.pack(pady = 20)
    bet_amount_entry = tk.Entry(window, font = ('georgia', 20))
    bet_amount_entry.pack(pady=20)
    bet_button = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_amount_entry.get(),next = flop))
    bet_button.pack(pady=0)
    fold_button = tk.Button(window, text = 'Fold', font = ('georgia', 15))
    fold_button.pack(pady=0)
    wallet_label = tk.Label(window, text = f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)
    window.bind('<Return>', lambda event:test_bet(bet_amount_entry.get(),next = flop))



welcome()

window.mainloop()