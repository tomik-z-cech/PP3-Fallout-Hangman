# Imports
import colorama, os
from colorama import Fore, Style

# Emoji list
NUCLEAR_EMOJI = '\u2622'
MAN_EMOJI = '\U0001F468\u200D\U0001F52C'
WOMAN_EMOJI = '\U0001F469\u200D\U0001F52C'

# Global variables
player_name = ''
guesses = 0
lenght_of_word = 0
letters_revealed = 0


def word_guess():
    word_guessed = False
    return word_guessed

def create_charater():
    clear_screen()
    global player_name 
    print(Fore.YELLOW + f'{MAN_EMOJI}  Create new character {WOMAN_EMOJI} \n\n' + Style.RESET_ALL)
    player_name = input("What's your name : ")
    print(f'Hello, {player_name}')

def clear_screen():
    os.system('clear')
    return

clear_screen()
print(Fore.YELLOW + f'{NUCLEAR_EMOJI} Welcome to Fallout Mini - Hangman {NUCLEAR_EMOJI} \n\n' + Style.RESET_ALL)
result = word_guess()
# print(result)
create_charater()
# print(player_name)
