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
modulo = 13
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

def check_equal_cards(hand_cards, equal):
    symbols = []
    for card in hand_cards:
        card = card % modulo
        symbols.append(card)
        if symbols.count(card) == equal:
            return True
    return False

def check_two_pairs(hand_cards):
    symbols = []
    pairs = []
    for card in hand_cards:
        card = card % modulo
        symbols.append(card)
        if symbols.count(card) == 2 and card not in pairs:
            pairs.append(card)

    if len(pairs) == 2:
        return True
    return False

def check_full_house(hand_cards):
    symbols = []
    d = None
    for card in hand_cards:
        card = card % modulo
        symbols.append(card)
        if symbols.count(card) == 3:
            d = card

    if d is not None:
        cards_left = [c for c in symbols if c != d]
        if len(cards_left) == 2 and len(set(cards_left)) == 1:
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
        card = card % modulo
        if card < 9: return False
        symbols.append(card)

    for i in symbols:
        if symbols.count(i)!=1:
            return False

    return True

def check_straight(hand_cards):
    symbols = []
    swap = False
    for card in hand_cards:
        card = card % modulo
        if card in symbols:
            return False
        symbols.append(card)

    symbols.sort()
    first = symbols[0]
    for i in range(len(hand_cards)):
        if symbols[i] != first+i:
            # [0, 9, 10, 11, 12]
            if (symbols[i] != 12) or (first != 0):
                return False
    return True

def check_str_flush(hand_cards):
    if check_flush(hand_cards) and check_straight(hand_cards):
        return True
    return False


def percentage(runtimes, cards_nr):
    values = {
        'pair': 0,
        'two_pairs': 0,
        'drilling': 0,
        'four_cards': 0,
        'full_house': 0,
        'straight': 0,
        'flush': 0,
        'straight_flush': 0,
        'royalflush': 0
    }
    checks = {
        'royalflush': (check_royalflush, None),
        'straight_flush': (check_str_flush, None),
        'flush': (check_flush, None),
        'straight': (check_straight, None),
        'four_cards': (check_equal_cards,4),
        'full_house': (check_full_house, None),
        'drilling': (check_equal_cards, 3),
        'two_pairs': (check_two_pairs, None),
        'pair': (check_equal_cards, 2)
    }

    for i in range(runtimes):
        my_cards = take_cards(cards_nr)
        for val, (func, arg) in checks.items():
            if arg is not None:
                if func(my_cards, arg):
                    values[val] += 1
                    break
            else:
                if func(my_cards):
                    values[val] += 1
                    break

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


