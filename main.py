import random

logo = """
.------..------.
|Q.--. ||K.--. |
| (\/) || :/\: |
| :\/: || :\/: |
| '--'Q|| '--'K|
`------'`------'
"""

bk = """
__________.__                 __        ____.              __    
\______   \  | _____    ____ |  | __   |    |____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /   |    \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \\  \___|    </\__|    |/ __ \\  \___|    < 
 |______  /____(____  /\___  >__|_ \________(____  /\___  >__|_ \
        \/          \/     \/     \/             \/     \/     \/
"""

# Print the logo and banner
print(logo + bk)

def deal():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    hand = [card1, card2]
    return hand

game = False
u_hand = deal()
c_hand = deal()

# Define a function to check if the user has blackjack
def u_blackjack(u_hand):
    return (11 in u_hand and 10 in u_hand)

# Define a function to check if the computer has blackjack
def c_blackjack(c_hand):
    return (11 in c_hand and 10 in c_hand)

# Define a function to calculate the user's score
def u_calc(u_hand):
    score = sum(u_hand)
    if score > 21 and 11 in u_hand:
        u_hand[u_hand.index(11)] = 1
        return sum(u_hand)
    else:
        return score

# Define a function to calculate the computer's score
def c_calc(c_hand):
    score = sum(c_hand)
    if score > 21 and 11 in c_hand:
        c_hand[c_hand.index(11)] = 1
        return sum(c_hand)
    else:
        return score

# Define a function to let the user draw a card
def hit_user(u_hand):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    u_hand.append(card)
    return u_hand

# Define a function to let the computer draw a card
def hit_computer(c_hand):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    if sum(c_hand) < 17:
        card = random.choice(cards)
        c_hand.append(card)
    return c_hand

# Define a function to calculate the winner
def calc_both(u_hand, c_hand):
    u_score = u_calc(u_hand)
    c_score = c_calc(c_hand)

    if u_score > c_score:
        print("You Win.")
    elif u_score == c_score:
        print("Draw.")
    else:
        print("You Lose.")

while not game:
    print(f"Your cards: {u_hand}")
    print(f"Computer card {c_hand[1]}")

    if u_blackjack(u_hand) and not c_blackjack(c_hand):
        print("You Win, you have Blackjack")
        game = True
    elif not u_blackjack(u_hand) and c_blackjack(c_hand):
        print("You lose, computer has Blackjack")
        game = True
    elif u_blackjack(u_hand) and c_blackjack(c_hand):
        print("Draw, both have Blackjack")
        game = True
    else:
        ask = input("Do you want to draw another card? Y/N ").lower()
        if ask == "y":
            hit_user(u_hand)
            if u_calc(u_hand) > 21:
                print("You Bust. You Lose.")
                game = True
            elif u_calc(u_hand) == 21:
                print("Blackjack! You Win!")
                game = True

            elif c_calc(c_hand) > 21:
                print("Computer bust")
                game = True
        else:
            while sum(c_hand) < 17:
                hit_computer(c_hand)
            calc_both(u_hand, c_hand)
            game = True

print(f"Your final hand: {u_hand}, Value: {u_calc(u_hand)}")
print(f"Computer's final hand: {c_hand}, Value: {c_calc(c_hand)}")
