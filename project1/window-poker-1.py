import random
from PIL import Image, ImageTk
import tkinter as tk

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

username=''#this will allow us to remember username, idk why i didnt think of this sooner


green = "POKER HOME SCREEN_1.jpg"
gold = "gold1.jpg" #this is the default home screen. Only replaced by certain themes like cats
cat_home = "cat1.jpg"
cat_game_background = "cat2.jpg"
christmas_home = "christmasbg4.jpg"
christmas_game_background = "christmasbg1.jpg"
purple = "purple.jpg"
black = "black1.jpg"
old_fashioned_game = "guns1.jpg"
old_fashioned_home = "brown1.jpg"
red = "red1.jpg"
pink = "pink.jpg"
neon_home = "neon1.jpg"
neon_game = "neon2.jpg"

selected_theme = gold
home_background = gold

print ('franko and mj are lazy and need to contribute to the GROUP project')


#this is where frankos card code was




def welcome (): #welcome screen. (Add settings button and more stuff here)
    global username
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
    settings_button = tk.Button(window, text = 'Settings', font = ('georgia', 20), command=lambda:settings())
    settings_button.pack(pady=20)
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
        elif name =='Ngo':
            Ngo_label = tk.Label(window, text = 'Welcome Professor', font = ('georgia', 15))
            Ngo_label.pack(pady=15)
            window.after(2000,lambda:pre_bet(name))
        elif name == 'Roberson':
            roberson_label=tk.Label(window,text = 'Welcome Professor',font = ('georgia',15))
            roberson_label.pack(pady=20)
            window.after(2000,lambda:pre_bet(name))

        
        else:
            window.after(1,lambda:pre_bet(name))
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
        drawn_cards2 = random.sample(deck, 1)

        for card in drawn_cards2:
            deck.remove(card)
            image_file = card_images.get(card, None)
            
            if image_file:
                image = Image.open(image_file)
                image = image.resize((60, 85))
                card_photo = ImageTk.PhotoImage(image)
                
            image_label = tk.Label(window, image=card_photo)
            image_label.image = card_photo  #reference to the image
            image_label.pack(pady=10)

        bet_entry_flop = tk.Entry(window, font = ('georgia', 20))
        bet_entry_flop.pack(pady=20)
        bet_button_flop = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_entry_flop.get(),next = turn))
        bet_button_flop.pack(pady=0)
        fold_button_flop = tk.Button(window, text = 'Fold', font = ('georgia', 15),command=lambda:fold())
        fold_button_flop.pack(pady=0)
        wallet_label_2 = tk.Label(window, text = f'Wallet: ${wallet}')
        wallet_label_2.pack(pady=0)
        window.bind('<Return>', lambda event:test_bet(bet_entry_flop.get(),next = turn))
    
        def turn():
            bet_entry_flop.destroy()
            bet_button_flop.destroy()
            fold_button_flop.destroy()
            wallet_label_2.destroy()
            drawn_cards3 = random.sample(deck, 1)

            for card in drawn_cards3:
                deck.remove(card)
                image_file = card_images.get(card, None)
            
                if image_file:
                    image = Image.open(image_file)
                    image = image.resize((60, 85))
                    card_photo = ImageTk.PhotoImage(image)
                    
                image_label = tk.Label(window, image=card_photo)
                image_label.image = card_photo  #reference to the image
                image_label.pack(pady=10)

            bet_entry_turn = tk.Entry(window, font = ('georgia', 20))
            bet_entry_turn.pack(pady=20)
            bet_button_turn = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_entry_turn.get(),next = final()))
            bet_button_turn.pack(pady=20)
            fold_button_turn = tk.Button(window, text = 'Fold', font = ('georgia', 15),command=lambda:fold())
            fold_button_turn.pack(pady=0)
            wallet_label_3=tk.Label(window, text = f'Wallet: ${wallet}')
            wallet_label_3.pack(pady=0)

            def final():
                
                bet_entry_turn.destroy()
                bet_button_turn.destroy()
                fold_button_turn.destroy()
                wallet_label_3.destroy()
                drawn_cards4 = random.sample(deck, 1)

                for card in drawn_cards4:
                    deck.remove(card)
                    image_file = card_images.get(card, None)
                
                    if image_file:
                        image = Image.open(image_file)
                        image = image.resize((60, 85))
                        card_photo = ImageTk.PhotoImage(image)
                    
                image_label = tk.Label(window, image=card_photo)
                image_label.image = card_photo  #reference to the image
                image_label.pack(pady=10)

                bet_entry_final = tk.Entry(window, font = ('georgia', 20))
                bet_entry_final.pack(pady=20)
                bet_button_final = tk.Button(window, text = 'BET!', font = ('georgia', 20), command= lambda:test_bet(bet_entry_final.get(),next = test_func))
                bet_button_final.pack(pady=20)
                fold_button_final = tk.Button(window, text = 'Fold', font = ('georgia', 15),command=lambda:fold())
                fold_button_final.pack(pady=0)
                wallet_label_4=tk.Label(window, text = f'Wallet: ${wallet}')
                wallet_label_4.pack(pady=0)

                def test_func ():
                    print ('wondertastic test function :)')


    
    clear_page() 
    
    drawn_cards = random.sample(deck, 3)

    for card in drawn_cards:
        deck.remove(card)
        image_file = card_images.get(card, None)
        
        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            card_photo = ImageTk.PhotoImage(image)
            
            image_label = tk.Label(window, image=card_photo)
            image_label.image = card_photo  #reference to the image
            image_label.pack(pady=10)

    bet_enter_label = tk.Label(window, text = 'enter bet', font = ('georgia', 20))
    bet_enter_label.pack(pady = 20)
    bet_amount_entry = tk.Entry(window, font = ('georgia', 20))
    bet_amount_entry.pack(pady=20)
    bet_button = tk.Button(window, text = 'BET!', font = ('georgia', 20), command=lambda:test_bet(bet_amount_entry.get(),next = flop))
    bet_button.pack(pady=0)
    fold_button = tk.Button(window, text = 'Fold', font = ('georgia', 15),command=lambda:fold())
    fold_button.pack(pady=0)
    wallet_label = tk.Label(window, text = f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)
    window.bind('<Return>', lambda event:test_bet(bet_amount_entry.get(),next = flop))

def fold (): #if player folds
    wallet_fold_label = tk.Label(window, text = f'${wallet} remaining', font = ('georgia', 10))
    wallet_fold_label.pack(pady=20)
    folding_lable=tk.Label(window, text = 'Folding', font = ('georgia', 10))
    folding_lable.pack(pady=20)
    window.after(2,lambda:clear_page())
    window.after(1000, lambda:pre_bet(username))



def pre_bet (name): #before you bet after welcome function.
    global username
    if name != username:
        username = name
    image = Image.open(selected_theme) 
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image  #Stores the image as a part of the window
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    #username = str(name)#We dont necessarily need this, but if I remove it I have to redo a bunch of other stuff, so lets just keep it :) -Canyon
    clear_page()
    name_label = tk.Label(window, text = f'welcome {username}', font = ('georgia', 30))
    name_label.pack(pady=20)
    deal_button = tk.Button(window, text = 'DEAL!', font = ('georgia', 20), command=lambda:blind())
    deal_button.pack(pady=20)
    back_button = tk.Button(window, text = 'Back', font = ('georgia', 10),command=lambda:welcome())
    back_button.pack(pady = 20)
    window.bind('<Escape>',lambda event:welcome())
    window.bind('<Return>',lambda event:blind())



def settings():
    clear_page()
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
    color_button = tk.Button(window, text = 'Colors', font = ('georgia', 20),command=lambda:colors())
    color_button.pack(pady = 20)
    other_button = tk.Button(window, text = 'Other', font = ('georgia', 20),command=lambda:other_bg())
    other_button.pack(pady = 20)
    
    def colors():
        clear_page()  

        green_button = tk.Button(window, text='Green', font=('Georgia', 20), command=lambda: commit_theme(green))
        green_button.pack(pady=0)
    
        gold_button = tk.Button(window, text=' Gold ', font=('Georgia', 20), command=lambda: commit_theme(gold))
        gold_button.pack(pady=0)

        purple_button = tk.Button(window, text='Purple', font=('Georgia', 20), command=lambda: commit_theme(purple))
        purple_button.pack(pady=0)

        black_button = tk.Button(window, text = 'Black', font = ('georgia', 20), command=lambda:commit_theme(black))
        black_button.pack(pady=0)

        red_button = tk.Button(window, text = 'Red', font = ('georgia', 20), command=lambda:commit_theme(red))
        red_button.pack(pady=0)

        pink_button = tk.Button(window, text = 'Pink', font = ('georgia', 20), command=lambda:commit_theme(pink))
        pink_button.pack(pady=0)

        back_button = tk.Button(window, text = 'Back',font = ('georgia', 10),command=lambda:background_menu())
        back_button.pack(pady = 50)
    
    def other_bg ():#themes that are more than colors, like cats 🐈
        clear_page()

        cat_button = tk.Button(window, text = ' Cats  ', font = ('georgia', 20),command=lambda:commit_theme(cat_game_background))
        cat_button.pack(pady = 0)

        christmas_button = tk.Button(window, text = 'Christmas', font = ('georgia', 20),command=lambda:commit_theme(christmas_game_background))
        christmas_button.pack(pady = 0)

        old_fashioned_button = tk.Button(window, text = 'Old Fashioned', font = ('georgia', 20),command=lambda:commit_theme(old_fashioned_game))
        old_fashioned_button.pack(pady = 0)

        neon_button = tk.Button(window, text = 'Neon', font = ('Georgia',20),command=lambda:commit_theme(neon_game))
        neon_button.pack(pady=0)


        back_button = tk.Button(window, text = 'Back',font = ('georgia', 10),command=lambda:background_menu())
        back_button.pack(pady = 50)

def commit_theme(theme):
    global selected_theme
    global home_background
    selected_theme = theme 
    if selected_theme == cat_game_background:
        home_background=cat_home
        welcome()
    elif selected_theme == christmas_game_background:
        home_background=christmas_home
        welcome()
    elif selected_theme == old_fashioned_game:
        home_background=old_fashioned_home
        welcome()
    elif selected_theme == neon_game:
        home_background=neon_game
        welcome()
    else:
        home_background=theme
        welcome()


welcome()

window.mainloop()