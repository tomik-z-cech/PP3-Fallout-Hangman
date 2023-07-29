# Imports
import gspread, json, os, random
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from datetime import datetime


# Google drive credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_info(creds)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fallout_hangman')

# Emoji list
NUCLEAR_EMOJI = '\u2622'
MAN_EMOJI = '\U0001F468\u200D\U0001F52C'
WOMAN_EMOJI = '\U0001F469\u200D\U0001F52C'

# Global variables
player_name = ''


def update_history():
    """
    Function updates sheet on google drive with date and time of user access
    """
    history_worksheet = SHEET.worksheet("history")
    time_now = str(datetime.now().time())
    date_now = str(datetime.now().date())
    history_worksheet.append_row([date_now,time_now])

def word_guess(difficulty, guesses):
    word_hidden = '------------'
    word_guessed = False
    words_sheet = SHEET.worksheet("words")
    random_number = random.randint(1, 50)
    word_to_guess = words_sheet.cell(random_number, difficulty).value
    print('Your word to guess : ')
    print(word_hidden[:difficulty])
    print(f'{difficulty} letters\n')
    print(word_to_guess)
    while True:
        player_guess = input('Type your guess : ')
        if player_guess in word_to_guess:
            print('good')
        else:
            print('not good')
    return word_guessed

def create_charater():
    clear_screen()
    global player_name 
    print(Fore.YELLOW + f'{MAN_EMOJI}  Create new character {WOMAN_EMOJI} \n\n' + Style.RESET_ALL)
    player_name = input("What's your name : ")
    print(f'Hello, {player_name}')

def clear_screen():
    """
    Function clears the terminal (screen)
    """
    os.system('clear')
    return

def print_intro():
    wrong_choice = False
    while True:
        clear_screen()
        print('\n\n\n\n\n')
        print(Fore.YELLOW + '          ┌───────────────────────────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'          │ {NUCLEAR_EMOJI} Welcome to Fallout Mini - Hangman {NUCLEAR_EMOJI} │' + Style.RESET_ALL)
        print(Fore.YELLOW + '          └───────────────────────────────────────┘' + Style.RESET_ALL)
        print(Fore.WHITE + '          ┌───────────────────────────────────────┐' + Style.RESET_ALL)
        print(Fore.WHITE + '          │ ' + Fore.GREEN + 'S' + Fore.WHITE + ' - Start Game                        │' + Style.RESET_ALL)
        print(Fore.WHITE + '          │ ' + Fore.GREEN + 'H' + Fore.WHITE + ' - High Scores                       │' + Style.RESET_ALL)
        print(Fore.WHITE + '          └───────────────────────────────────────┘' + Style.RESET_ALL)
        if wrong_choice == True:
            print(Fore.RED + '          Your choice was invalid !' + Style.RESET_ALL)
        menu_choice = input('          Please make a menu choice : ')
        if menu_choice.upper() in ('S') and len(menu_choice) > 0:
            create_charater()
            break
        elif menu_choice.upper() in ('H') and len(menu_choice) > 0:
            break
        else:
            wrong_choice = True

def main():
    print_intro()
    # update_history()
    # result = word_guess(3, 5)

main()