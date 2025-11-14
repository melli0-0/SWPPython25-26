import random


def fill_array(start: int, end: int, nr: int):
    liste = []
    for i in range(1, nr):
        a = random.randint(start, end)
        liste.append(a)
    return liste

def steuer(liste):
    steuergruppe: dict = {'0':0, '1':0, '2':0, '3':0}
    for elem in liste:
        i = None
        match elem:
            case e if e <= 10000:
               i = 0
            case e if e <= 30000: i=1
            case e if e <= 70000: i=2
            case _: i=3
        steuergruppe[f"{i}"] += 1

    return steuergruppe


products = {'a': (4, 24), 'b': (2, 12), 'c': (10, 1)}
# 20 % prozent

def gewinn(dictionary):
    gewinn = 0
    for key, val in dictionary.items():
        gewinn += (val[0] * val[1])
    return gewinn

def my_pass():
    try:
        print("mama")
        pass
        print("Silvana")
    except Exception :
        print(Exception)
    else:
        print("No Exception")
    finally:
        pass

def pair(liste):
    check = set()
    pairs: set = set()
    for x in liste:
        if x in check:
            pairs.add(x)
        else:
            check.add(x)
    print(pairs)


def count_pairs(liste, target):
    pairs = []
    if target % 2 == 0:
        if liste.count(target//2) == 2:
            pairs.append((target//2, target//2))

    for nr in liste:
        rest = target - nr
        if rest in liste:
            if rest < nr:
                pairs.append((rest, nr))
            elif rest > nr:
                pairs.append((nr, rest))

    pairs = set(pairs)
    return pairs

def print_result(liste):
    if len(liste) == 0:
        print("No pairs found")
    else:
        print(liste)

if __name__ == '__main__':
    #steuerzahler = fill_array(5000, 100000, 10)
    #print(steuerzahler)
    #print(steuer(steuerzahler))
    #print(gewinn(products))
    #my_pass()
    #liste = [0,0,1,3,4,1,3,3,5,6,7,9,2,4,8]
    #pair(liste)
    numbers = [1,2,3,4,6,6,7,5,5,10,8,12,11]
    target_sum = 12
    pairs = count_pairs(numbers, target_sum)
    print_result(pairs)