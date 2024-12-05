import random
from PIL import Image, ImageTk
import tkinter as tk
from collections import Counter

window = tk.Tk()
window.geometry("1000x700")
fullscreen = False

# change to make full screen before release (or do something with settings)

window.title('Poker')

card_types = \
    ['Ace', '2', '3', '4', '5', '6', '7', '8',
     '9', '10', 'Jack', 'Queen', 'King']

suits = ['hearts', 'diamonds', 'spades', 'clubs']
deck = [f'{rank} of {suit}' for rank in card_types for suit in suits]

# dictionary to map card names to image files
card_images = {}

# Populates the dictionary with the card images
for rank in card_types:
    for suit in suits:
        card_images[f'{rank} of {suit}'] = f'{rank.lower()}_of_{suit}.png'

poker_hands_dict = {'royal_flush': 10, 'straight_flush': 9,
                    'four_of_a_kind': 8, 'full_house': 7, 'flush': 6,
                    'straight': 5, 'three_of_a_kind': 4, 'two_pair': 3, 'pair':2, 'high_card': 1}


wallet = int(100)
player_bet = int(0)

username = ' '

# this will allow us to remember username.


green = "POKER HOME SCREEN_1.jpg"
gold = "gold1.jpg"   
# this is the default home screen. Only replaced by certain themes like cats

cat_home = "cat1.jpg"
cat_game_background = "cat2.jpg"
christmas_home = "christmasbg4.jpg"
xmas_game_bg = "christmasbg1.jpg"
purple = "purple.jpg"
black = "black1.jpg"
old_f_game = "guns1.jpg"
old_fashioned_home = "brown1.jpg"
red = "red1.jpg"
neon_game = "neon2.jpg"

selected_theme = gold
home_background = gold


def welcome():       # welcome screen.
    global username
    clear_page()
    image = Image.open(home_background)
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image 
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    welcome_label = tk.Label(window, text="Enter name below",
                             font=("georgia", 20))
    welcome_label.pack(pady=20)
    name_entry = tk.Entry(window, font=("georgia", 20))
    name_entry.pack(pady=20)
    play_button = tk.Button(window, text="Play!", font=("georgia", 20),
                            command=lambda: test_name(name=name_entry.get()))
    play_button.pack(pady=20)
    settings_button = tk.Button(window, text='Settings', font=('georgia', 20),
                                command=lambda: settings())
    settings_button.pack(pady=20)
    wallet_label = tk.Label(window, text=f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)

    quit_button = tk.Button(window, text='Quit', font=('georgia', 10),
                            command=lambda: quit_game())
    quit_button.pack(pady=10)

    def quit_game():
        clear_page()
        a_y_s_label = tk.Label(window, text='Are you sure you want to quit?',
                               font=('georgia', 20))
        a_y_s_label.pack()
        ninty_percent = tk.Label(window,
                                 text='99% of gamblers quit before they win big',
                                 font=('georgia', 20))
        ninty_percent.pack()
        yes_button = tk.Button(window, text='Yes Quit', font=('georgia', 15),
                               command=lambda: yes_quit())
        yes_button.pack()
        no_button = tk.Button(window, text='No', font=('georgia', 15),
                              command=lambda: welcome())
        no_button.pack()

        def yes_quit():
            window.destroy()

# checks if name is valid(name must be betweein 1 and 10 letters and no spaces)


def test_name(name):  
    if len(name) == 0:
        bad_username_label = tk.Label(window,
                                      text='Please enter a username between 1-10 character(s)',
                                      font=('georgia', 10))
        bad_username_label.pack(pady=15)
        window.after(2000, bad_username_label.destroy)
    elif len(name) > 10:
        bad_username_label = tk.Label(window,
                                      text='Please enter a username between 1-10 character(s)',
                                      font=('georgia', 10))
        bad_username_label.pack(pady=15)
        window.after(2000, bad_username_label.destroy)
    elif name.count(' ') > 0:
        no_space_username_label = tk.Label(window,
                                           text='Username must not contain spaces',
                                           font=('georgia', 10))
        no_space_username_label.pack(pady=15)
        window.after(2000, no_space_username_label.destroy)
    elif name == 'Ngo':
        Ngo_label = tk.Label(window, text='Welcome Professor',
                             font=('georgia', 15))
        Ngo_label.pack(pady=15)
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Roberson':
        roberson_label = tk.Label(window, text='Welcome Professor',
                                  font=('georgia', 15))
        roberson_label.pack(pady=20)
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Cazalas':
        cazalas_label = tk.Label(window, text='Welcome Dr. Cazalas',
                                 font=('georgia', 15))
        cazalas_label.pack()
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Eicholtz':
        eicholtz_label = tk.Label(window, text='Welcome Dr. Eicholtz',
                                  font=('georgia', 15))
        eicholtz_label.pack()
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Burke':
        burke_label = tk.Label(window, text='Welcome Dr. Burke',
                               font=('georgia', 15))
        burke_label.pack()
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Canyon':
        canyon_label = tk.Label(window, bg='forest green', fg='old lace',
                                text='Welcome Canyon', font=('georiga', 15))
        canyon_label.pack()
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Mj':
        mj_label = tk.Label(window, bg='red4', fg='white', text='Hola MJ',
                            font=('georgia', 15))
        mj_label.pack()
        window.after(2000, lambda: pre_bet(name))
    elif name == 'Franko':
        franko_label = tk.Label(window, bg='cyan2', fg='white',
                                text='Hello Freaky Franko!',
                                font=('georgia', 15))
        franko_label.pack()
        window.after(2000, lambda: pre_bet(name))

    else:
        window.after(1, lambda: pre_bet(name))


def clear_page():  # clears page when called. (Time saver)
    for widget in window.winfo_children():
        widget.pack_forget()


def blind():  # first deal
    global wallet
    global player_bet

    def test_bet(bet, next):  # checks if your bet is allowed
        global wallet
        global player_bet
        try:
            bet_amount = int(bet,)  # checks if bet can be made an int
            if bet_amount > wallet:  # bet more than you have
                not_enough_label = tk.Label(window, 
                                            text=f'Not enough money. Max bet ${wallet}', font=('georgia', 10))
                not_enough_label.pack(pady=10)
                window.after(2000, not_enough_label.destroy)
            elif bet_amount < 1:
                negitve_label = tk.Label(window, text='You must bet at least $1', font=('georgia', 10))
                negitve_label.pack(pady=10)
                window.after(2000, negitve_label.destroy)
            else:  # bet less than or equal to what you have
                wallet -= bet_amount
                player_bet += bet_amount
                total_betting_label = tk.Label(window, 
                                               text=f'Betting ${bet_amount}. ${wallet} remaining',
                                               font=('georgia', 10))
                total_betting_label.pack(pady=10)
                window.after(1000, total_betting_label.destroy)
                window.after(1000, lambda: next())
        except ValueError:  # bet was either a decimal or text
            error_label = tk.Label(window, text='Invalid number',
                                   font=('georgia', 20)) 
            # bet cannot be made an int
            error_label.pack(pady=10)
            window.after(2000, error_label.destroy)

    def flop():
        # bet_enter_label.destroy()
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
           
            image_label = tk.Label(com_frame, bg='black', image=card_photo)
            image_label.image = card_photo  # reference to the image
            image_label.pack(pady=10, side='left', padx=5)

        bet_entry_flop = tk.Entry(window, font=('georgia', 20))
        bet_entry_flop.pack(pady=20)
        bet_button_flop = tk.Button(window, text='BET!', font=('georgia', 20),
                                    command=lambda: test_bet
                                    (bet_entry_flop.get(), next=turn))
        bet_button_flop.pack(pady=0)
        fold_button_flop = tk.Button(window, text='Fold', font=('georgia', 15),
                                     command=lambda: fold())
        fold_button_flop.pack(pady=0)
        wallet_label_2 = tk.Label(window, text=f'Wallet: ${wallet}')
        wallet_label_2.pack(pady=0)

        def turn():
            bet_entry_flop.destroy()
            bet_button_flop.destroy()
            fold_button_flop.destroy()
            wallet_label_2.destroy()
            global drawn_cards3
            drawn_cards3 = random.sample(deck, 1)

            for card in drawn_cards3:
                deck.remove(card)
                image_file = card_images.get(card, None)
            
                if image_file:
                    image = Image.open(image_file)
                    image = image.resize((60, 85))
                    card_photo = ImageTk.PhotoImage(image)
                    
                image_label = tk.Label(com_frame, bg='black', image=card_photo)
                image_label.image = card_photo  # reference to the image
                image_label.pack(pady=10, side='left', padx=5)

            bet_entry_turn = tk.Entry(window, font=('georgia', 20))
            bet_entry_turn.pack(pady=20)
            bet_button_turn = tk.Button(window, text='BET!',
                                        font=('georgia', 20),
                                        command=lambda: test_bet
                                        (bet_entry_turn.get(),
                                            next=showdown))
            bet_button_turn.pack(pady=0)
            fold_button_turn = tk.Button(window, text='Fold',
                                         font=('georgia', 15),
                                         command=lambda: fold())
            fold_button_turn.pack(pady=0)
            wallet_label_3 = tk.Label(window, text=f'Wallet: ${wallet}')
            wallet_label_3.pack(pady=0)

            def showdown():
                bet_entry_turn.destroy()
                bet_button_turn.destroy()
                fold_button_turn.destroy()
                wallet_label_3.destroy()
                bet_enter_label.destroy()

                comp_cards_label = tk.Label(comp_frame, text='Dealers Cards',
                                            font=('georgia', 20))
                comp_cards_label.pack()
                global computer_cards
                computer_cards = random.sample(deck, 2)

                for card in computer_cards:  # computer cards
                    deck.remove(card)
                    image_file = card_images.get(card, None)

                    if image_file:
                        image = Image.open(image_file)
                        image = image.resize((60, 85))
                        card_photo = ImageTk.PhotoImage(image)

                        image_label = tk.Label(comp_frame, bg='black',
                                               image=card_photo)
                        image_label.image = card_photo
                        image_label.pack(pady=10, side='left', padx=5)

                pa_button = tk.Button(window, text='Play Again!',
                                      font=('georgia', 20),
                                      command=lambda: pre_bet(username))
                pa_button.pack()
                home_button_showdown = tk.Button(window, text='Home',
                                                 font=('georgia', 10),
                                                 command=lambda: welcome())
                home_button_showdown.pack(pady=5)

                def get_player_hand_details():
                    global ranks_player
                    global suits_player
                    ranks_player = []
                    suits_player = []
                    for card in drawn_cards3:
                        rank, suit = card.split(' of ')
                        ranks_player.append(rank)
                        suits_player.append(suit)
                    for card in player_cards:
                        rank, suit = card.split(' of ')
                        ranks_player.append(rank)
                        suits_player.append(suit)
                    return ranks_player, suits_player

                def get_computer_hand_details():
                    global ranks_computer
                    global suits_computer
                    ranks_computer = []
                    suits_computer = []
                    for card in drawn_cards3:
                        rank, suit = card.split(' of ')
                        ranks_computer.append(rank)
                        suits_computer.append(suit)
                    for card in computer_cards:
                        rank, suit = card.split(' of ')
                        ranks_computer.append(rank)
                        suits_computer.append(suit)
                    return ranks_computer, suits_computer

                def evaluate_computer_hand():
                    get_computer_hand_details()   # function extract rank and suit and put in lists to be checked for hands
                    global rank_values
                    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                                   '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11,
                                   'Queen': 12, 'King': 13, 'Ace': 14}
                    global computer_rank_values
                    computer_rank_values = \
                        [rank_values[rank] for rank in ranks_computer]
                    # These lines assign integer value to the string value of rank to allow the code to detect straights
                    
                    straight()
                    flush()
                    four_of_kind()
                    full_house()
                    three_of_kind()
                    two_pair()
                    pair()
                    high_card()
                    
                    if straight() and flush():
                        return 'straight_flush'
                    elif four_of_kind():
                        return 'four_of_a_kind'
                    elif full_house():
                        return 'full_house'
                    elif flush():
                        return 'flush'
                    elif straight():
                        return 'straight'
                    elif three_of_kind():
                        return 'three_of_a_kind'
                    elif two_pair():
                        return 'two_pair'
                    elif pair():
                        return 'pair'
                    elif high_card():
                        return 'high_card'
                
                def straight():
                    sorted_values = sorted(player_rank_values)
                    for i in range(1, len(sorted_values)):
                        if sorted_values[i] != sorted_values[i - 1] + 1:
                            return False
                    else:
                        return True
                
                def flush():
                    first_suit = suits_player[0]
                    for suit in suits_player:
                        if suit != first_suit:
                            return False
                    else:
                        return True

                def four_of_kind():
                    rank_counter = Counter(computer_rank_values)
                    if 4 in rank_counter.values():
                        return True
                    else:
                        return False

                def full_house():
                    rank_counter = Counter(computer_rank_values)
                    if 3 in rank_counter.values() and 2 in rank_counter.values():
                        return True
                    else:
                        return False

                def three_of_kind():
                    rank_counter = Counter(computer_rank_values)        
                    if 3 in rank_counter.values():
                        return True
                    else:
                        return False

                def two_pair():
                    rank_counter = Counter(computer_rank_values)
                    pair_counts = list(rank_counter.values())
                    if pair_counts.count(2) >= 2:
                        return True
                    else:
                        return False

                def pair():
                    rank_counter = Counter(computer_rank_values)
                    if 2 in rank_counter.values():
                        return True
                    else:
                        return False

                def high_card():
                    return max(computer_rank_values)        

                def evaluate_player_hand():
                    get_player_hand_details()

                    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                                   '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11,
                                   'Queen': 12, 'King': 13, 'Ace': 14}

                    global player_rank_values
                    player_rank_values = \
                        [rank_values[rank] for rank in ranks_player]

                    straight()
                    flush()
                    four_of_kind()
                    full_house()
                    three_of_kind()
                    two_pair()
                    pair()
                    high_card()

                    if straight() and flush():
                        return 'straight_flush'
                    elif four_of_kind():
                        return 'four_of_a_kind'
                    elif full_house():
                        return 'full_house'
                    elif flush():
                        return 'flush'
                    elif straight():
                        return 'straight'
                    elif three_of_kind():
                        return 'three_of_a_kind'
                    elif two_pair():
                        return 'two_pair'
                    elif pair():
                        return 'pair'
                    else:
                        return 'high_card'

                def straight():
                    sorted_values = sorted(player_rank_values)
                    for i in range(1, len(sorted_values)):
                        if sorted_values[i] != sorted_values[i - 1] + 1:
                            return False
                    else:
                        return True

                def flush():
                    first_suit = suits_player[0]
                    for suit in suits_player:
                        if suit != first_suit:
                            return False
                    else:
                        return True

                def four_of_kind():
                    rank_counter = Counter(player_rank_values)
                    if 4 in rank_counter.values():
                        return True
                    else:
                        return False

                def full_house():
                    rank_counter = Counter(player_rank_values)
                    if 3 in rank_counter.values() and 2 in rank_counter.values():
                        return True
                    return False

                def three_of_kind():
                    rank_counter = Counter(player_rank_values)        
                    if 3 in rank_counter.values():
                        return True
                    else:
                        return False

                def two_pair():
                    rank_counter = Counter(player_rank_values)
                    pair_counts = list(rank_counter.values())
                    if pair_counts.count(2) >= 2:
                        return True
                    return False

                def pair():
                    rank_counter = Counter(player_rank_values)
                    if 2 in rank_counter.values():
                        return True
                    return False

                def high_card():
                    return 'high_card'      

                evaluate_player_hand()
                evaluate_computer_hand()

                player_hand_final = evaluate_player_hand()
                computer_hand_final = evaluate_computer_hand()

                player_hand_value = poker_hands_dict[player_hand_final]
                computer_hand_value = poker_hands_dict[computer_hand_final]

                def player_wins():
                    clear_page()
                    player_wins_label = tk.Label(window, bg='blue',
                                                 text='You Wins',
                                                 font=('georgia', 20))
                    player_wins_label.pack()
                    amount_won_label = tk.Label(window,
                                                text=f'Won ${player_bet*2}!',
                                                font=('georgia', 15))
                    amount_won_label.pack()
                    global wallet
                    wallet = wallet + (player_bet*2)

                def computer_wins():
                    clear_page()
                    computer_wins_label = tk.Label(window, bg='red',
                                                   text='Computer Wins!',
                                                   font=('gorgia', 20))
                    computer_wins_label.pack()
                    amount_lost_label = tk.Label(window,
                                                 text=f'Lost {player_bet}',
                                                 font=('georgia', 15))
                    amount_lost_label.pack()

                def compare_high_cards():
                    global wallet
                    global player_bet
                    player_value_ranks = \
                        sorted([rank_values[rank] for rank in ranks_player],
                               reverse=True)
                    computer_numeric_ranks = sorted([rank_values[rank] for
                                                     rank in ranks_computer],
                                                    reverse=True)
                    for player_rank, computer_rank in zip(player_value_ranks,
                                                          computer_numeric_ranks):
                        if player_rank > computer_rank:
                            player_high_card = tk.Label(window, bg='blue',
                                                        text="You Win!",
                                                        font=("georgia", 20))
                            player_high_card.pack()
                            amount_won_label_chc = tk.Label(window, 
                                                            text=f'Won ${player_bet*2}!',
                                                            font=('georgia', 15))
                            amount_won_label_chc.pack()
                            wallet = wallet + (player_bet*2)
                            return
                        elif computer_rank > player_rank:
                            computer_high_card = tk.Label(window, bg='red',
                                                          text="Computer Wins!",
                                                          font=("georgia", 20))
                            computer_high_card.pack()
                            amount_lost_label_chc = tk.Label(window,
                                                             text=f'Lost {player_bet}',
                                                             font=('georgia', 15))
                            amount_lost_label_chc.pack()
                            return
                    tie_label = tk.Label(window,
                                         text="It's a high card tie!",
                                         font=("georgia", 20))
                    tie_label.pack()
                if player_hand_value > computer_hand_value:
                    player_wins()
                elif computer_hand_value > player_hand_value:
                    computer_wins()
                else:
                    compare_high_cards()

    clear_page()

    com_cards_label = tk.Label(window, text='Community Cards',
                               font=('georgia', 15))

    com_cards_label.pack(pady=5)
    drawn_cards = random.sample(deck, 1)

    com_frame = tk.Frame(window)  # com cards
    com_frame.pack(side='top', pady=10)

    hand_label = tk.Label(window, text='Your Hand', font=('georgia', 20))
    hand_label.pack()

    hand_frame = tk.Frame(window)  # your hand frame
    hand_frame.pack(pady=10)

    for card in drawn_cards:
        deck.remove(card)
        image_file = card_images.get(card, None)

        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            card_photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(com_frame, bg='black', image=card_photo)
            image_label.image = card_photo
            image_label.pack(pady=10, side='left', padx=5)

    global player_cards
    player_cards = random.sample(deck, 2)  # player hand

    for card in player_cards:
        deck.remove(card)
        image_file = card_images.get(card, None)

        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            card_photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(hand_frame, bg='black', image=card_photo)
            image_label.image = card_photo  # reference to the image, keeps it from being trashed
            image_label.pack(pady=10, side='left', padx=5)

    bet_enter_label = tk.Label(window, text='enter bet', font=('georgia', 20))
    bet_enter_label.pack(pady=20)
    bet_amount_entry = tk.Entry(window, font=('georgia', 20))
    bet_amount_entry.pack(pady=20)
    bet_button = tk.Button(window, text='BET!', font=('georgia', 20),
                           command=lambda: test_bet(bet_amount_entry.get(),
                                                    next=flop))
    bet_button.pack(pady=0)
    fold_button = tk.Button(window, text='Fold', font=('georgia', 15),
                            command=lambda: fold())
    fold_button.pack(pady=0)
    wallet_label = tk.Label(window, text=f'Wallet: ${wallet}')
    wallet_label.pack(pady=0)

    comp_frame = tk.Frame(window)  # computers hand
    comp_frame.pack(pady=10)


def fold():  # if player folds
    wallet_fold_label = tk.Label(window, text=f'${wallet} remaining',
                                 font=('georgia', 10))
    wallet_fold_label.pack(pady=20)
    folding_label = tk.Label(window, text='Folding', font=('georgia', 10))
    folding_label.pack(pady=20)
    window.after(2, lambda: clear_page())
    window.after(1000, lambda: pre_bet(username))


def pre_bet(name):  # before you bet after welcome function.
    global username
    global wallet
    global player_bet
    player_bet = 0
    if name != username:
        username = name
    image = Image.open(selected_theme) 
    resized_image = image.resize((1920, 1080), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(resized_image)
    window.bg_image = bg_image   # Stores the image as a part of the window
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    clear_page()
    name_label = tk.Label(window, text=f'welcome {username}',
                          font=('georgia', 30))
    name_label.pack(pady=20)
    deal_button = tk.Button(window, text='DEAL!', font=('georgia', 20),
                            command=lambda: blind())
    deal_button.pack(pady=20)
    back_button = tk.Button(window, text='Back', font=('georgia', 10),
                            command=lambda: welcome())
    back_button.pack(pady=20)


def settings():
    clear_page()
  
    def fullscreen_control():  # enables / disables fullscreen
        global fullscreen
        fullscreen = not fullscreen  # change in and out of full screen
        window.attributes("-fullscreen", fullscreen)  # make full screen
        if fullscreen:
            full_screen_button.config(text="Full Screen: ON")
        else:
            full_screen_button.config(text="Full Screen: OFF")
        welcome()

    settings_label = tk.Label(window, text='Settings', font=('georgia', 20))
    settings_label.pack(pady=20)

    background_button = tk.Button(window, text='Change Background',
                                  font=('georgia', 20),
                                  command=background_menu)
    background_button.pack(pady=10)

    full_screen_button = tk.Button(window, text='Full Screen: OFF',
                                   font=('georiga', 20),
                                   command=lambda: fullscreen_control())
    full_screen_button.pack(pady=10)

    credits_button = tk.Button(window, text="Credits And Attributions",
                               font=('georgia', 20), command=lambda: credits())
    credits_button.pack(pady=10)

    back_button = tk.Button(window, text='Back', font=('georgia', 10),
                            command=lambda: welcome())
    back_button.pack()


def credits():
    clear_page()
    Credits_label = tk.Label(window, text="Credits And Attributions",
                             font=('georgia', 20))
    Credits_label.pack(pady=20)
    devs_label = tk.Label(window, text='Developers', font=('georgia', 15))
    devs_label.pack(pady=5)
    team_label = tk.Label(window, 
                          text='Canyon Lowes\nMJ rodriguez\nFranko Suarez')
    team_label.pack(pady=5)
    back_button = tk.Button(window, text='Back', font=('georgia', 10),
                            command=lambda: settings())
    back_button.pack()


def background_menu():
    clear_page()
    new_background_label = tk.Label(window, text='Choose Background',
                                    font=('Georgia', 20))
    new_background_label.pack(pady=20)
    color_button = tk.Button(window, text='Colors', font=('georgia', 20),
                             command=lambda: colors())
    color_button.pack(pady=20)
    other_button = tk.Button(window, text='Other', font=('georgia', 20),
                             command=lambda: other_bg())
    other_button.pack(pady=20)
    back_button = tk.Button(window, text='Back', font=('georgia', 10),
                            command=lambda: settings())
    back_button.pack()

    def colors():
        clear_page()

        green_button = tk.Button(window, text=' Green', font=('Georgia', 20),
                                 bg='SpringGreen2',
                                 command=lambda: commit_theme(green))
        green_button.pack(pady=0)
        gold_button = tk.Button(window, text=' Gold  ', font=('Georgia', 20),
                                bg='gold', command=lambda: commit_theme(gold))
        gold_button.pack(pady=0)

        purple_button = tk.Button(window, text='Purple', font=('Georgia', 20),
                                  bg='dark orchid',
                                  command=lambda: commit_theme(purple))
        purple_button.pack(pady=0)

        black_button = tk.Button(window, text=' Black ',
                                 font=('georgia', 20),
                                 bg='gray1', fg='gray100',
                                 command=lambda: commit_theme(black))
        black_button.pack(pady=0)

        red_button = tk.Button(window, text=' Red ', font=('georgia', 25),
                               bg='red', command=lambda: commit_theme(red))
        red_button.pack(pady=0)

        back_button = tk.Button(window, text='Back', font=('georgia', 10),
                                command=lambda: background_menu())
        back_button.pack(padyv=50)

    def other_bg():  # themes that are more than colors
        clear_page()

        cat_button = tk.Button(window, bg='DarkGoldenrod1', fg='Black',
                               text=' Cats  ', font=('georgia', 20),
                               command=lambda:
                               commit_theme(cat_game_background))
        cat_button.pack(pady=0)

        christmas_button = tk.Button(window, bg='green2', fg='red2',
                                     text='Christmas', font=('georgia', 20),
                                     command=lambda: commit_theme
                                     (xmas_game_bg))
        christmas_button.pack(pady=0)

        old_fashioned_button = tk.Button(window, bg='bisque2', fg='black',
                                         text='Old Fashioned',
                                         font=('georgia', 20),
                                         command=lambda: commit_theme
                                         (old_f_game))
        old_fashioned_button.pack(pady=0)

        neon_button = tk.Button(window, bg='DarkOrchid2', fg='deep sky blue',
                                text='Neon', font=('Georgia', 20),
                                command=lambda: commit_theme(neon_game))
        neon_button.pack(pady=0)


def commit_theme(theme):
    global selected_theme
    global home_background
    selected_theme = theme
    if selected_theme == cat_game_background:
        home_background = cat_home
        welcome()
    elif selected_theme == xmas_game_bg:
        home_background = christmas_home
        welcome()
    elif selected_theme == old_f_game:
        home_background = old_fashioned_home
        welcome()
    elif selected_theme == neon_game:
        home_background = neon_game
        welcome()
    else:
        home_background = theme
        welcome()


welcome()

window.mainloop()
