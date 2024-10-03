'''
class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            return amount
        else:
            raise ValueError("Not enough chips!")

def main_game():
    player = Player("Alice", 1000)
    while True:
        print(f"Player {player.name}, you have {player.chips} chips.")
        action = input("Choose your action (bet/fold): ").lower()
        if action == "bet":
            bet_amount = int(input("Enter bet amount: "))
            player.bet(bet_amount)
            print(f"{player.name} bets {bet_amount} chips.")
        elif action == "fold":
            print(f"{player.name} folds!")
            break
        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main_game()
'''

import tkinter as tk

class PokerGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Game")
        
        self.label = tk.Label(root, text="Welcome to Poker!")
        self.label.pack()

        self.bet_button = tk.Button(root, text="Bet", command=self.bet_action)
        self.bet_button.pack()

        self.fold_button = tk.Button(root, text="Fold", command=self.fold_action)
        self.fold_button.pack()

    def bet_action(self):
        # Code to handle bet
        self.label.config(text="You bet!")

    def fold_action(self):
        # Code to handle fold
        self.label.config(text="You fold!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerGameGUI(root)
    root.mainloop()
