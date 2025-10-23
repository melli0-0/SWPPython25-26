'''
    poker simulation:
        - modulate 52 cards (13 symbols, 4 colors)
        - take 5 cards
        - functions for pair, drilling, flush, royal flush and straight
        - play 100000 times - calculate percentage for different combinations
        - compare with correct percentages (internet)
'''
import array as array
import random

# typecode 'i' - int values
cards_number = 52
cards = array.array('i', range(0,cards_number))

def take_cards(taking):
    hand_cards = array.array('i', range(0, taking))
    for take in range(taking):
        index = random.randint(0, len(cards)-take-1)
        card = cards[index]
        last_card = cards[-1-take]
        # swop random card with last one
        cards[index] = last_card
        cards[-1-take] = card
        hand_cards[take] = card
    return hand_cards

def check_pair(hand_cards):
    symbols = []
    for card in hand_cards:
        index = hand_cards.index(card)
        card = card%13
        if card in symbols:
            return True
        symbols.append(card)
    return False

if __name__ == '__main__':
    my_cards = take_cards(5)
    print(my_cards)
    print('Pair: ', check_pair(my_cards))