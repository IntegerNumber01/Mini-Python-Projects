import random

range_of_numbers = input('What would you like the range of numbers to be? Enter an integer: ')
tries_left = input('How many tries would you like? ')

range_of_numbers = int(range_of_numbers)
tries_left = int(tries_left)

print('The range of numbers is from 0 to', range_of_numbers)

my_number = random.randint(0, range_of_numbers)

user_win = False

for i in range(tries_left):
    guess = input('Guess my number: ')

    if my_number == int(guess):
        user_win = True
        break

if user_win:
    print('Good Job :D')
else:
    print('Better luck next time! My number was', my_number)
