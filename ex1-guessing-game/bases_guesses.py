import random

def suffix(num):
    if num == 1:
        return ''
    return 'es'

def guessing_game():
  my_number = random.randint(0,100)
  guesses = 3

  print('Guessing Game!')
  print('I''m thinking of a number between 0 and 100 - can you guess it?')

  while True:
    if guesses == 0:
        print(f'You''re all out of guesses...')
        break

    print(f'You have {guesses} guess{suffix(guesses)} left')
    your_guess = input('What is your guess?\n')

    if not your_guess.isdigit():
        print(f'That isn''t a number... ')
        continue

    your_guess_int = int(your_guess)

    if your_guess_int == my_number:
        print(f'Yay! You guessed it! It was {your_guess}')
        break

    if your_guess_int > my_number:
        print(f'{your_guess} is too high')
    else:
        print(f'{your_guess} is too low')

    guesses = guesses - 1


if __name__ == "__main__":
  guessing_game()