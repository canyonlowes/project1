import random

card_types = (['Ace ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','Jack ','Queen ','King '])
suites = (['hearts','diamonds','spades','clubs'])
card = random.choice (card_types) + random.choice (suites)
deck = [f'{rank}of {suit}' for rank in card_types for suit in suites]

import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
window.title('Poker')


wallet = int(100)

from PIL import Image, ImageTk
green = "POKER HOME SCREEN_1.jpg"
gold = "gold1.jpg"


if card_types == 'Ace' and suites == 'hearts':
    image = Image.open('ace_of_hearts.png')
if card_types == 'Ace' and suites == 'spades':
    image = Image.open('ace_of_spades2.png')
if card_types == 'Ace' and suites == 'diamonds':
    image = Image.open('ace_of_diamonds.png')
if card_types == 'Ace' and suites == 'clubs':
    image = Image.open('ace_of_clubs.png')

if card_types == 'Jack' and suites == 'hearts':
    image = Image.open('jack_of_hearts2.png')
if card_types == 'Jack' and suites == 'spades':
    image = Image.open('jack_of_spades2.png')
if card_types == 'Jack' and suites == 'diamonds':
    image = Image.open('jack_of_diamonds2.png')
if card_types == 'Jack' and suites == 'clubs':
    image = Image.open('jack_of_clubs2.png')
        
if card_types == 'King' and suites == 'hearts':
    image = Image.open('king_of_hearts2.png')
if card_types == 'King' and suites == 'spades':
    image = Image.open('king_of_spades2.png')
if card_types == 'King' and suites == 'diamonds':
    image = Image.open('king_of_diamonds2.png')
if card_types == 'King' and suites == 'clubs':
    image = Image.open('king_of_clubs2.png')

if card_types == '2' and suites == 'hearts':
    image = Image.open('2_of_hearts.png')
if card_types == '2' and suites == 'spades':
    image = Image.open('2_of_spades.png')
if card_types == '2' and suites == 'diamonds':
    image = Image.open('2_of_diamonds.png')
if card_types == '2' and suites == 'clubs':
    image = Image.open('2_of_clubs.png')
        
if card_types == '3' and suites == 'hearts':
    image = Image.open('3_of_hearts.png')
if card_types == '3' and suites == 'spades':
    image = Image.open('3_of_spades.png')
if card_types == '3' and suites == 'diamonds':
    image = Image.open('3_of_diamonds.png')
if card_types == '3' and suites == 'clubs':
    image = Image.open('3_of_clubs.png')

if card_types == '4' and suites == 'hearts':
    image = Image.open('4_of_hearts.png')
if card_types == '4' and suites == 'spades':
    image = Image.open('4_of_spades.png')
if card_types == '4' and suites == 'diamonds':
    image = Image.open('4_of_diamonds.png')
if card_types == '4' and suites == 'clubs':
    image = Image.open('4_of_clubs.png')

if card_types == '5' and suites == 'hearts':
    image = Image.open('5_of_hearts.png')
if card_types == '5' and suites == 'spades':
    image = Image.open('5_of_spades.png')
if card_types == '5' and suites == 'diamonds':
    image = Image.open('5_of_diamonds.png')
if card_types == '5' and suites == 'clubs':
    image = Image.open('5_of_clubs.png')
        
if card_types == '6' and suites == 'hearts':
    image = Image.open('6_of_hearts.png')
if card_types == '6' and suites == 'spades':
    image = Image.open('6_of_spades.png')
if card_types == '6' and suites == 'diamonds':
    image = Image.open('6_of_diamonds.png')
if card_types == '6' and suites == 'clubs':
    image = Image.open('6_of_clubs.png')

if card_types == '7' and suites == 'hearts':
    image = Image.open('7_of_hearts.png')
if card_types == '7' and suites == 'spades':
    image = Image.open('7_of_spades.png')
if card_types == '7' and suites == 'diamonds':
    image = Image.open('7_of_diamonds.png')
if card_types == '7' and suites == 'clubs':
    image = Image.open('7_of_clubs.png')

if card_types == '8' and suites == 'hearts':
    image = Image.open('8_of_hearts.png')
if card_types == '8' and suites == 'spades':
    image = Image.open('8_of_spades.png')
if card_types == '8' and suites == 'diamonds':
    image = Image.open('8_of_diamonds.png')
if card_types == '8' and suites == 'clubs':
    image = Image.open('8_of_clubs.png')

if card_types == '9' and suites == 'hearts':
    image = Image.open('9_of_hearts.png')
if card_types == '9' and suites == 'spades':
    image = Image.open('9_of_spades.png')
if card_types == '9' and suites == 'diamonds':
    image = Image.open('9_of_diamonds.png')
if card_types == '9' and suites == 'clubs':
    image = Image.open('9_of_clubs.png')

if card_types == '10' and suites == 'hearts':
    image = Image.open('10_of_hearts.png')
if card_types == '10' and suites == 'spades':
    image = Image.open('10_of_spades.png')
if card_types == '10' and suites == 'diamonds':
    image = Image.open('10_of_diamonds.png')
if card_types == '10' and suites == 'clubs':
    image = Image.open('10_of_clubs.png')




def welcome (): #welcome screen. (Add settings button and more stuff here)
    #window.configure(bg=selected_color)
    clear_page()
    image = Image.open(gold)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image  #Store the image as a part of the window
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_label = tk.Label(window, text = "Enter name below", font = ("georgia", 20))
    welcome_label.pack(pady=20)
    name_entry = tk.Entry(window, bg='snow2', fg='black', font = ("georgia", 20))
    name_entry.pack(pady=20)
    play_button = tk.Button(window, bg="snow2", fg='black', text = "Play!", font = ("georgia", 20),command=lambda: test_name(name=name_entry.get()))
    play_button.pack(pady=20)
    settings_button = tk.Button(window, text = 'Settings', font = ('georgia', 20), command=lambda:settings_page())
    settings_button.pack(pady=20)
    wallet_label = tk.Label(window, text = f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)
    window.bind('<Return>', lambda event: test_name(name=name_entry.get()))

    def test_name(name):
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
            window.after(1,lambda:pre_bet(name=name_entry.get()))
    window.bind('<Escape>', lambda event:window.destroy())

def clear_page(): #clears page when called. (Time saver)
    for widget in window.winfo_children():
        widget.pack_forget()
        


def blind(): #first deal
    global current_color
    global wallet
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
        fold_button_flop = tk.Button(window, text = 'Fold', font = ('georgia', 15), command=lambda:fold())
        fold_button_flop.pack(pady=0)
        wallet_label_2 = tk.Label(window, text = f'Wallet: ${wallet}')
        wallet_label_2.pack(pady=0)
        window.bind('<Escape>',lambda event:fold())
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

            

            def final():
                print('final placeholder :)')





    
    clear_page()
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
    wallet_label = tk.Label(window, text = f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)
    window.bind('<Escape>',lambda event:fold())
    window.bind('<Return>', lambda event:test_bet(bet_amount_entry.get(),next = flop))



def fold (): #if player folds
    global current_color
    wallet_fold_label = tk.Label(window, text = f'${wallet} remaining', font = ('georgia', 10))
    wallet_fold_label.pack(pady=20)
    folding_lable=tk.Label(window, text = 'Folding', font = ('georgia', 10))
    folding_lable.pack(pady=20)
    window.after(2,lambda:clear_page())
    window.after(1000, lambda:round_pre_bet())

'''was having trouble getting the pre_bet function to work. Couldn't get it to carry the username variable. Might try to fix, but
this should work for now'''
def round_pre_bet(): #Before you bet after each round after first round 
    lambda:clear_page()
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 20),command=lambda:blind())
    deal_button.pack(pady = 20)
    home_button = tk.Button(window, text = 'Main Menu', font = ('georgia', 10),command=lambda:welcome())
    home_button.pack(pady = 20)
    window.bind('<Escape>',lambda event:welcome())
    window.bind('<Return>', lambda event:blind())


def pre_bet (name): #before you bet after welcome function.
    image = Image.open(green) 
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image  #Store the image as a part of the window
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    username = str(name)#testing
    print (username) #testing
    clear_page()
    name_label = tk.Label(window, text = f'welcome {username}', font = ('georgia', 30))
    name_label.pack(pady=20)
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 20), command=lambda:blind())
    deal_button.pack(pady=20)
    back_button = tk.Button(window, text = 'Back', font = ('georgia', 10),command=lambda:welcome())
    back_button.pack(pady = 20)
    window.bind('<Escape>',lambda event:welcome())
    window.bind('<Return>',lambda event:blind())

def settings_page(): #settings page
    clear_page()
    settings_placeholder_label = tk.Label(window, text = 'Placeholder! Mj is making the real thing.\n right Mj?', font = ('georgia', 20))
    settings_placeholder_label.pack(pady=20)
    back_from_settings_button = tk.Button(window, text = 'Back', font = ('georgia', 20), command=lambda:welcome())
    back_from_settings_button.pack(pady=20)
    color_pick_test = tk.Entry(window, font = ('georgia', 20))
    color_pick_test.pack(pady=20)
    commit_button = tk.Button (window, text = 'commit', font = ('georgia', 20), command=lambda:commit_color(color_pick_test.get()))
    commit_button.pack(pady=20)

def commit_color(color):
    global selected_color
    selected_color = color
    print (f'running, {selected_color}') #testing purposes
    welcome()


welcome()

window.mainloop()