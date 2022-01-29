from random import choice

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ['♠', '♥', '♦', '♣']

hande = []  # Hands do be exhibited, with suits and numbers
handi = []  # Hand's integral values, using for calculating game values
hands = []  # Hand's suits, useful in certain games, such as a straight flush in poker

card_values = {14: 'A', 11: 'J', 12: 'Q', 13: 'K'}  # Dictionary to turn Jester, Queen and King into functional Numbers


# In certain games, these values must be altered. Eg: In blackjack, these three cards hold the value 10

def card_gen():
    global suits, numbers, hande

    suit = choice(suits)  # Generates an suit for the card and appends it to the matching list
    hands.append(suit)

    number = choice(numbers)  # Generates a number for the card and appends it to the matching list
    handi.append(number)
    # Places the J, Q, K and A based on their integral values. (Must be reworked for blackjack-like cases) [WIP]
    if number in card_values:
        number = card_values[number]

    card = (str(number) + suit)  # Actually generates the card and appends it to the exhibition hand
    hande.append(str(card))

    if card in hande is True:  # Prevents card repetition
        hande.remove(card)


x = int(input('Quantas cartas gerar? '))

for r in range(0, x):
    card_gen()
