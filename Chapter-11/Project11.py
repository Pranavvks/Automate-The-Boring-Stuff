import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
if 'tails' or 'heads' in guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if 'tails' or'heads' in guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')