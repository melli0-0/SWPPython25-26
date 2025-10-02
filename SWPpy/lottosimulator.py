import random
import array as array
from turtledemo.chaos import g


def randomgenerator(n):
    randomNumbers = array.array('i', range(1,46))
    for j in range(n):
        index = random.randint(0,len(randomNumbers)-j-1)
        element = randomNumbers[index]
        #print('Element = ', element)
        lastelement = randomNumbers[len(randomNumbers)-j-1]
        #print('Last element = ', lastelement)
        randomNumbers[index] = lastelement
        randomNumbers[len(randomNumbers)-j-1] = element
        #print('Index',randomNumbers[index])
        #print('Last',randomNumbers[len(randomNumbers)-j-1])
        #print('-------------------------------')
    return randomNumbers

def output(n):
    print('random numbers: ')
    randomNumbers = randomgenerator(n)
    for j in range(n):
        print(randomNumbers[len(randomNumbers)-j-1])

#output(6)

def statistics(run_times, numbers):
    #dictionary
    stats = {}
    for j in range(run_times):
        #for every run - array
        randomNumbers = randomgenerator(numbers)
        for k in range(numbers):
            #safe last numbers*values in dict
            if randomNumbers[len(randomNumbers) - k - 1] in stats:
                #checks keys
                value = stats.get(randomNumbers[len(randomNumbers) - k - 1])
                #increase value by 1
                stats.update({randomNumbers[len(randomNumbers) - k - 1]: value+1})
            else:
                stats.update({randomNumbers[len(randomNumbers) - k - 1]: 1})
    return stats

def tableStatistics(run_times, numbers):
    dict = statistics(run_times, numbers)
    print('statistics: ')
    for key, value in sorted(dict.items()):
        print('Number ',key, ' was picked ', value, ' times.')

tableStatistics(1000,6)