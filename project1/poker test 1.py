import random

card_types = (['A ','1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ','J ','Q ','K '])
suites = (['hearts','diamonds','spades','clubs'])
card = random.choice (card_types) + random.choice (suites)

def deal():
    deck = [f"{card} of {suit}" for card in card_types for suit in suites]
    random.shuffle(deck)
    
    for i in range(2): #the two cards you see
        card = deck.pop()
        print (f'{card} to you')
    
    print('|---------------------|')
    
    blind = int(input('Enter bet: '))

    print('|---------------------|')
    
    for i in range (3): #first three public cards
        card = deck.pop()
        print (f'{card} shown')

    print('|---------------------|')

    flop = int(input('Enter bet: '))

    print('|---------------------|')

    for i in range (1): #fourth public card
        card = deck.pop()
        print (f'{card} shown')
    
    print('|---------------------|')

    turn = int(input('Enter bet: '))

    print('|---------------------|')

    for _ in range (1): #fifth public card
        card = deck.pop()
        print (f'{card} shown')
    
    print('|---------------------|')

    final_bet = int(input('Enter  final bet: '))

    print('|---------------------|')

    pot = blind + flop + turn + final_bet
    return (pot)


pot = deal()

hand_type = input('enter hand type ') #will change, just for testing rn
if hand_type == 'Royal Flush':
    print ('Heighest hand! You win!')
    print (f'gained {pot}')
else:
    print ('you loose')
    




