
# generate a random number

import random
rand = random.randint(1,100)
antall = 0

print('Gjett et siffer mellom 0 og 100')

while True:
    print(rand)
    guess = int(input("your_guess.\n"))
    antall = antall + 1
    if guess < 1 or guess > 100:
        print('Out of range')
        #continue
    if guess == rand:
        print(f'Right answar, du brukte {antall} forsøk')
        break

    if rand > guess:
        print('Tallet er høyere')
    else:
        print('Tallet er laver')