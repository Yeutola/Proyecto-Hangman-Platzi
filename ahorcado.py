import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.swapcase()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Te quedan', lives, 'vidas y has usado estas cartas: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palabra actual: ', ' '.join(word_list))

        user_letter = input('Adivina una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nTu letra,', user_letter, 'no esta en la palabra.')

        elif user_letter in used_letters:
            print('\nYa usaste esa carta. Adivina otra letra.')

        else:
            print('\nEsa no es una carta válida.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Moriste, lo siento. La palabra era', word)
    else:
        print('¡QUE BIEN! Adivinaste la palabra', word, '!!')


if __name__ == '__main__': 
  hangman()
