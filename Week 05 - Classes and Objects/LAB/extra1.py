
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Dealer went over. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 21 and computer_score != 21:
        return "Blackjack! You win!"
    elif computer_score == 21 and user_score != 21:
        return "Dealer has Blackjack. You lose!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

class Hand:
    def __init__(self):
        """Create an empty hand of cards."""
        self.cards = []

    def add_card(self):
        """Deal one card and add it to this hand."""
        self.cards.append(deal_card())

    def score(self):
        """Calculate the score using Blackjack rules."""
        if sum(self.cards) == 21 and len(self.cards) == 2:
            return 21

        score = sum(self.cards)

        while score > 21 and 11 in self.cards:
            self.cards[self.cards.index(11)] = 1
            score = sum(self.cards)

        return score

def play_game():
    user_hand = Hand()
    computer_hand = Hand()

    for i in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    game_over = False

    while not game_over:
        user_score = user_hand.score()
        computer_score = computer_hand.score()

        print(f"Your cards: {user_hand.cards}, score: {user_score}")
        print(f"Dealer's first card: {computer_hand.cards[0]}")

        if user_score == 21 or user_score > 21:
            game_over = True
        else:
            choice = input("Type 'hit' to draw a card or 'stand' to stop: ").lower()

            if choice == "hit":
                user_hand.add_card()
            elif choice == "stand":
                game_over = True
            else:
                print("Please type hit or stand.")

    if user_hand.score() <= 21:
        while computer_hand.score() < 17:
            computer_hand.add_card()

    user_score = user_hand.score()
    computer_score = computer_hand.score()

    print(f"\nYour final hand: {user_hand.cards}, score: {user_score}")
    print(f"Dealer's final hand: {computer_hand.cards}, score: {computer_score}")
    print(compare(user_score, computer_score))

while input("\nDo you want to play Blackjack? Type 'yes' or 'no': ").lower() == "yes":
    play_game()
