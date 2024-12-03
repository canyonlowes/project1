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

poker_hands_dict={'royal_flush':10,'straight_flush':9,'four_of_a_kind':8,'full_house':7,'flush':6,'straight':5,'three_of_a_kind':4}

def card_to_u():


    com_cards_label = tk.Label(window, text = 'Community Cards',font = ('georgia',15))

    com_cards_label.pack(pady=5)
    
    drawn_cards = random.sample(deck, 3)

    com_frame = tk.Frame(window) #com cards
    com_frame.pack(side='top', pady=10)

    hand_label = tk.Label(window, text = 'Your Hand',font = ('georgia',20))
    hand_label.pack()

    hand_frame=tk.Frame(window) # your hand frame
    hand_frame.pack(pady=10)

    for card in drawn_cards:
        deck.remove(card)
        image_file = card_images.get(card, None)
        
        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            card_photo = ImageTk.PhotoImage(image)
            
            image_label = tk.Label(com_frame,bg='black', image=card_photo)
            image_label.image = card_photo 
            image_label.pack(pady=10,side='left',padx=5)
    
    player_cards = random.sample(deck,2)#player hand
    
    for card in player_cards:
        deck.remove(card)
        image_file=card_images.get(card, None)

        if image_file:
            image = Image.open(image_file)
            image = image.resize((60, 85))
            card_photo = ImageTk.PhotoImage(image)
            
            image_label = tk.Label(hand_frame,bg='black', image=card_photo)
            image_label.image = card_photo  #reference to the image, keeps it from being trashed
            image_label.pack(pady=10,side='left',padx=5)


    bet_enter_label = tk.Label(window, text = 'enter bet', font = ('georgia', 20))
    bet_enter_label.pack()
    bet_amount_entry = tk.Entry(window, font = ('georgia', 20))
    bet_amount_entry.pack()
    bet_button = tk.Button(window, text = 'BET!', font = ('georgia', 20),command=lambda:showdown())
    bet_button.pack()

    comp_frame=tk.Frame(window) #computers hand
    comp_frame.pack(pady=10)

    def showdown ():
                
            bet_enter_label.destroy()
            bet_button.destroy()
            bet_amount_entry.destroy()

            comp_cards_label = tk.Label(comp_frame, text = 'Dealers Cards', font = ('georgia',20))
            comp_cards_label.pack()


            computer_cards = random.sample(deck,2)

            for card in computer_cards: #computer cards-revealed at end of game to determine if you won or lost. 
                deck.remove(card)
                image_file=card_images.get(card, None)

                if image_file:
                    image = Image.open(image_file)
                    image = image.resize((60, 85))
                    card_photo = ImageTk.PhotoImage(image)

                    
                    image_label = tk.Label(comp_frame,bg='black', image=card_photo) 
                    image_label.image = card_photo
                    image_label.pack(pady=10,side='left',padx=5)

card_to_u()

window.mainloop()