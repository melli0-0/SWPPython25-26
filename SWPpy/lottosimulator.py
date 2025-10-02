import random
import array as array

#generates random picks * numbers from 1 - amount
def random_generator(picks, amount):
    random_numbers = array.array('i', range(1, amount+1))
    for j in range(picks):
        index = random.randint(0, amount-1-j)
        element = random_numbers[index]
        last_element = random_numbers[amount-1-j]
        random_numbers[index] = last_element
        random_numbers[amount-1-j] = element
    return random_numbers

#prints picks * numbers from 1 - amount
def output(picks, amount):
    print('random numbers: ')
    random_numbers = random_generator(picks, amount)
    for j in range(picks):
        print(random_numbers[amount-1-j])

#calls run_times times random_generator()
def statistics(run_times, picks, amount):
    stats = {}
    for j in range(run_times):
        random_numbers = random_generator(picks, amount)
        for k in range(picks):
            if random_numbers[amount - 1 - k] in stats:
                value = stats.get(random_numbers[amount -1 - k])
                stats.update({random_numbers[amount -1 - k]: value+1})
            else:
                stats.update({random_numbers[amount -1 - k]: 1})
    return stats

#print sorted statistics
def table_statistics(run_times, picks, amount):
    dictionary = statistics(run_times, picks, amount)
    print('statistics: ')
    for key, value in sorted(dictionary.items()):
        print('Number ',key, ' was picked ', value, ' times.')


if __name__ == '__main__':
    print('How many runs would you like to simulate?')
    try:
        times = int(input())
    except ValueError:
        print('No integer input')
    else:
        table_statistics(times,6, 45)