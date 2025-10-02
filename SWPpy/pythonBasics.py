import random
from random import randrange

print('a: ')
a = input()
print('b: ')
b = input()

c = randrange(1, 101)
print('c: ',c)
try:
    a = int(a) # convert str input to int
    b = int(b)
except ValueError:
    print('a or b need to be integer')

if a < 5:
    print("a < 5")
elif a == 5:
    print("a == 5")
else:
    print("a > 5")

for i in range(1,30,3): # from 1 to 30 all 3 steps
    if i % 2 == 0:
        pass #pass is a placeholder and 'ignores' if statement
    if i == 3:
        continue # next loop run
    if i == 5:
        break # loop ends right here
    print(i)

# var = (20 if x == 1 else 30)

try:
    print('while')
    while b<5:
        b=b+1
        print(b)
except Exception as e: # for all Exceptions -> Exception or just except
    print(e)
else:
    print('no exception')
finally:
    print('always')
