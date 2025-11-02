'''
    poker simulation:
        - modulate 52 cards (13 symbols, 4 colors)
        - take 5 cards
        - functions for pair, drilling, flush (same color), royal flush and straight
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
        card = card%13
        if card in symbols:
            return True
        symbols.append(card)
    return False

def check_drilling(hand_cards):
    symbols = []
    for card in hand_cards:
        card = card%13
        symbols.append(card)
        if symbols.count(card) == 3:
            return True

    return False

def check_flush(hand_cards):
    colors = []
    for card in hand_cards:
        match card:
            case c if c < 14:
                colors.append(0)
            case c if c < 27:
                colors.append(1)
            case c if c < 40:
                colors.append(2)
            case c if c >= 40:
                colors.append(3)

    for color in colors:
        if colors.count(color) == 5:
            return True
        elif colors.count(color) != 0:
            return False

def check_royalflush(hand_cards):
    if not check_flush(hand_cards):
        return False
    symbols = []
    for card in hand_cards:
        card = card % 13
        if card < 9: return False
        symbols.append(card)

    for i in symbols:
        if symbols.count(i)!=1:
            return False

    return True

def check_straight(hand_cards):
    symbols = []
    for card in hand_cards:
        card = card % 13
        if card in symbols:
            return False
        symbols.append(card)

    symbols.sort()
    first = symbols[0]
    for i in range(len(hand_cards)):
        if symbols[i] != first+i:
            return False

    return True

def percentage(runtimes, cards_nr):
    values = {
        'pair': 0,
        'drilling': 0,
        'flush': 0,
        'royalflush': 0,
        'straight': 0
    }
    checks = {
        'pair': check_pair,
        'drilling': check_drilling,
        'flush': check_flush,
        'royalflush': check_royalflush,
        'straight': check_straight
    }

    for i in range(runtimes):
        my_cards = take_cards(cards_nr)
        for val, func in checks.items():
            if func(my_cards):
                values[val] += 1

    values = {key: v / runtimes for key,v in values.items() }

    return values

if __name__ == '__main__':
    '''
    my_cards = take_cards(5)
    print(my_cards)
    print('Pair: ', check_pair(my_cards))
    print('Drilling: ', check_drilling(my_cards))
    print('Flush: ', check_flush(my_cards))
    print('Royal Flush: ', check_royalflush(my_cards))
    print('Straight: ', check_straight(my_cards))
    '''
    print('Runtimes: ')
    runtimes = int (input())
    print('Cards: ')
    cards_nr = int(input())
    values = percentage(runtimes, cards_nr)
    for val in values:
        print(val,': ',values[val])


