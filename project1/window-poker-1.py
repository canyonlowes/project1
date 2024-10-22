import random

card_types = (['Ace ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','Jack ','Queen ','King '])
suites = (['hearts','diamonds','spades','clubs'])
card = random.choice (card_types) + random.choice (suites)
deck = [f'{rank}of {suit}' for rank in card_types for suit in suites]

import tkinter as tk
window = tk.Tk()
window.configure(bg='green4')
window.geometry("500x500")
window.title('Poker')

wallet = 100

def deal1():
    for widget in window.winfo_children():
        widget.pack_forget()
    drawn_cards = random.sample(deck, 2)
    for card in drawn_cards:
        deck.remove(card) 
    cards_label = tk.Label(window, text=", ".join(drawn_cards), font=('Georgia', 20))
    cards_label.pack(pady=20)
    bet_enter_label = tk.Label(window, text = 'enter bet', font = ('georgia', 20))
    bet_enter_label.pack(pady = 20)
    bet_amount_entry = tk.Entry(window, font = ('georgia', 20))
    bet_amount_entry.pack(pady=20)

def first_bet (name):
    for widget in window.winfo_children():
        widget.pack_forget()
    name_label = tk.Label(window, text = f'welcome {name}', font = ('georgia', 20))
    name_label.pack(pady=20)
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 40), command=lambda:deal1())
    deal_button.pack(pady=20)

    
    

def welcome ():
    welcome_label = tk.Label(window, text = "Enter name below", font = ("georgia", 20))
    welcome_label.pack(pady=20)
    name_entry = tk.Entry(window, font = ("georgia", 20))
    name_entry.pack(pady=30)
    play_button = tk.Button(window, text = "Play!", font = ("georgia", 20), command=lambda: first_bet(name=name_entry.get()))
    play_button.pack(pady=40)

welcome()

window.mainloop()

