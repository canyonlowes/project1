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


wallet = int(100)

def welcome (color): #welcome screen. (Add settings button and more stuff here)
    clear_page()
    window.configure(bg=color)
    welcome_label = tk.Label(window, text = "Enter name below", font = ("georgia", 20))
    welcome_label.pack(pady=20)
    name_entry = tk.Entry(window, bg='brown4', fg='black', font = ("georgia", 20))
    name_entry.pack(pady=30)
    play_button = tk.Button(window, bg="red4", fg='black', text = "Play!", font = ("georgia", 20),command=lambda: pre_bet(name=name_entry.get()))
    play_button.pack(pady=40)
    settings_button = tk.Button(window, text = 'Settings', font = ('georgia', 20), command=lambda:settings_page())
    settings_button.pack(pady=20)

def clear_page(): #clears page when called. (Time saver)
    for widget in window.winfo_children():
        widget.pack_forget()
        


def blind(): #first deal
    def test_bet(bet,next): #checks if your bet is allowed (<= wallet and int)
        global wallet
        try:
            bet_amount = int(bet) #checks if bet can be made an int
            if bet_amount > wallet: #bet more than you have
                not_enough_label = tk.Label(window, text = f'Not enough money. Max bet ${wallet}', font=('georgia', 10))
                not_enough_label.pack(pady=20)
                window.after(2000, not_enough_label.destroy)
            else: #bet less than or equal to what you have
                wallet = wallet - bet_amount
                total_betting_label = tk.Label(window, text = f'Betting ${bet_amount}. ${wallet} remaining', font = ('georgia', 10))
                total_betting_label.pack (pady = 20)
                window.after(1000, total_betting_label.destroy)
                window.after(1000, lambda:next())
        except: #bet was either a decimal or text
            error_label = tk.Label(window, text = 'Invalid number', font = ('georgia', 20)) #bet cannot be made an int
            error_label.pack(pady = 20)
            window.after(2000, error_label.destroy)

    def flop():
        bet_enter_label.destroy()
        bet_amount_entry.destroy()
        bet_button.destroy()
        fold_button.destroy()
        drawn_cards_2 = random.sample(deck, 1)
        for card in drawn_cards_2:
            deck.remove(card)
        cards_label_2 = tk.Label(window, text=", ".join(drawn_cards_2), font=('Georgia', 20))
        cards_label_2.pack(pady=0)
    
    for widget in window.winfo_children():
        widget.pack_forget()
    drawn_cards = random.sample(deck, 3)
    for card in drawn_cards:
        deck.remove(card) 
    cards_label = tk.Label(window, text="\n".join(drawn_cards), font=('Georgia', 20))
    cards_label.pack(pady=0)
    bet_enter_label = tk.Label(window, text = 'enter bet', font = ('georgia', 20))
    bet_enter_label.pack(pady = 20)
    bet_amount_entry = tk.Entry(window, font = ('georgia', 20))
    bet_amount_entry.pack(pady=20)
    bet_button = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_amount_entry.get(),next = flop))
    bet_button.pack(pady=0)
    fold_button = tk.Button(window, text = 'Fold', font = ('georgia', 15), command=lambda:fold())
    fold_button.pack(pady=0)





def fold (): #if player folds
    wallet_fold_label = tk.Label(window, text = f'${wallet} remaining', font = ('georgia', 10))
    wallet_fold_label.pack(pady=20)
    folding_lable=tk.Label(window, text = 'Folding', font = ('georgia', 10))
    folding_lable.pack(pady=20)
    window.after(2,lambda:clear_page())
    window.after(1000, lambda:round_pre_bet())

'''was having trouble getting the pre_bet function to work. Could'nt get it to carry the username variable. Might try to fix, but
this should work for now'''
def round_pre_bet(): #Before you bet after each round after first round 
    lambda:clear_page()
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 20))
    deal_button.pack(pady = 20)


def pre_bet (name): #before you bet after welcome function. 
    username = str(name)
    for widget in window.winfo_children():
        widget.pack_forget()
    name_label = tk.Label(window, text = f'welcome {name}', font = ('georgia', 30))
    name_label.pack(pady=20)
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 20), command=lambda:blind())
    deal_button.pack(pady=20)

def settings_page(): #settings page
    clear_page()
    settings_placeholder_label = tk.Label(window, text = 'Placeholder! Mj is making the real thing.\n right Mj?', font = ('georgia', 20))
    settings_placeholder_label.pack(pady=20)
    back_from_settings_button = tk.Button(window, text = 'Back', font = ('georgia', 20), command=lambda:welcome())
    back_from_settings_button.pack(pady=20)
    color_pick_test = tk.Entry(window, font = ('georgia', 20))
    color_pick_test.pack(pady=20)
    commit_button = tk.Button (window, text = 'commit', font = ('georgia', 20), command=lambda:welcome(color_pick_test.get()))
    commit_button.pack(pady=20)

    



welcome('green')

window.mainloop()
