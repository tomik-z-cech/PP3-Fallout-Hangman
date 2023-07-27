# Imports
import colorama, os
from colorama import Fore, Style

# Emoji list
NUCLEAR_EMOJI = '\u2622'

# Global variables
player_name = ''

def word_guess(guesses, lenght_of_word):
    word_guessed = False
    return word_guessed



os.system('clear')
print(Fore.YELLOW + f'{NUCLEAR_EMOJI} Welcome to Fallout Mini - Hangman {NUCLEAR_EMOJI} \n\n' + Style.RESET_ALL)
result = word_guess(7, 7)
print(result)
