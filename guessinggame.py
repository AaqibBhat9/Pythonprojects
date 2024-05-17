from random import randint

lower_number, higher_number = 1,10

random_number : int = randint(lower_number, higher_number)
print(f'Guess the number range from {lower_number} to {higher_number}')

while True:
    try:
        user_guess:int =int(input('Guess :'))
    except ValueError as e:
        print('Enter the valid number :')
        continue
    if user_guess > random_number:
        print('The numebr is smaller')
    elif user_guess < random_number:
         print('The number is higer')
    else:
        print('You guessed right!')
        break
    