# Imports
import gspread, json, os, random, readchar, sys, time
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
perk_inteligence = False
perk_luck = False
perk_charisma = False

def display_text(row, delay=0.1):
    """
    Function displays large portions of text with typewriter effect.
    """
    text_worksheet = SHEET.worksheet("text")
    text_to_write = text_worksheet.cell(row, 1).value
    for char in text_to_write:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return


def update_history():
    """
    Function updates sheet on google drive with players name, date, time and perk selected by user.
    """
    history_worksheet = SHEET.worksheet("history")
    time_now = str(datetime.now().time())
    date_now = str(datetime.now().date())
    history_worksheet.append_row([player_name, date_now, time_now, perk_inteligence, perk_luck, perk_charisma])

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
    """
    Function reads player's name and selection of perk.
    Function uses 'readchar' dependency.
    Players name can't be empty otherwise error message is returned.
    Perks selection can be only 'I' or 'L' or 'C' otherwise error message is returned.
    """
    wrong_name = False
    while True:
        clear_screen()
        global player_name, perk_inteligence, perk_luck, perk_charisma
        print('\n\n')
        print(Fore.YELLOW + '         ┌───────────────────────────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'         │      {MAN_EMOJI}  Create new character {WOMAN_EMOJI}      │' + Style.RESET_ALL)
        print(Fore.YELLOW + '         └───────────────────────────────────────┘' + Style.RESET_ALL) 
        if wrong_name == True:
            print(Fore.RED + '         Your name was invalid ! Try again !' + Style.RESET_ALL)
        print(Fore.BLUE + "         What's your name ?" + Style.RESET_ALL)
        player_name = input('         ')
        if len(player_name) > 0:
            wrong_perk = False
            while True:
                clear_screen()
                print('\n\n\n')
                print(Fore.YELLOW + '      ┌──────────────────────────────────────────────────────────────────┐' + Style.RESET_ALL)
                print(Fore.YELLOW + '      │ ' + Fore.GREEN + 'I' + Fore.WHITE + ' - Inteligent - shortens the length of guesed word by 1 letter' + Fore.YELLOW + '  │' + Style.RESET_ALL)
                print(Fore.YELLOW + '      │ ' + Fore.GREEN + 'L' + Fore.WHITE + ' - Lucky - adds 5 extra guesses to your guess count' + Fore.YELLOW + '             │' + Style.RESET_ALL)
                print(Fore.YELLOW + '      │ ' + Fore.GREEN + 'C' + Fore.WHITE + ' - Charismatic - reveals an extra letter in guessed word' + Fore.YELLOW + '        │' + Style.RESET_ALL)
                print(Fore.YELLOW + '      └──────────────────────────────────────────────────────────────────┘' + Style.RESET_ALL)
                print(Fore.BLUE + f"      Hello, the " + Fore.MAGENTA + f"Chosen One {player_name}" + Fore.BLUE +" , select your perk. Press i, l or c." + Style.RESET_ALL)
                if wrong_perk == True:
                    print(Fore.RED + '      Your choice of perk was invalid, try again !' + Style.RESET_ALL)
                perk_choice = readchar.readchar()
                if perk_choice.upper() == 'I':
                    perk_inteligence = True
                    break
                if perk_choice.upper() == 'L':
                    perk_luck = True
                    break
                if perk_choice.upper() == 'C':
                    perk_charisma = True
                    break
                else:
                    wrong_perk = True
            update_history()
            return
        else:
            wrong_name = True
        
def clear_screen():
    """
    Function clears the terminal (screen).
    """
    os.system('clear')
    return

def print_intro():
    """
    Function prints menu to terminal and asks user for menu choice.
    Menu choice is protected against being an empty string.
    Menu choice can be only 'S' or 'H' otherwise error message is returned.
    """
    wrong_choice = False
    while True:
        clear_screen()
        print('\n\n\n\n\n')
        print(Fore.YELLOW + '                    ┌───────────────────────────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'                    │ {NUCLEAR_EMOJI} Welcome to Fallout Mini - Hangman {NUCLEAR_EMOJI} │' + Style.RESET_ALL)
        print(Fore.YELLOW + '                    └───────────────────────────────────────┘' + Style.RESET_ALL)
        print(Fore.WHITE + '                    ┌───────────────────────────────────────┐' + Style.RESET_ALL)
        print(Fore.WHITE + '                    │ ' + Fore.GREEN + 'S' + Fore.WHITE + ' - Start Game                        │' + Style.RESET_ALL)
        print(Fore.WHITE + '                    │ ' + Fore.GREEN + 'H' + Fore.WHITE + ' - High Scores                       │' + Style.RESET_ALL)
        print(Fore.WHITE + '                    └───────────────────────────────────────┘' + Style.RESET_ALL)
        if wrong_choice == True:
            print(Fore.RED + '                    Your choice was invalid !' + Style.RESET_ALL)
        print('                    Please make a menu choice, Press S or H. ')
        menu_choice = readchar.readchar()
        if menu_choice.upper() == 'S':
            create_charater()
            break
        elif menu_choice.upper() == 'H':
            break
        else:
            wrong_choice = True

def end_of_program():
    """
    This is the last function to be executed.
    This function prints "Thank you for playing" message.
    """
    clear_screen()
    print('Thank you for playing.')

def start_game():
    clear_screen()
    display_text(1)
    display_text(2)
    return

def main():
    """
    Main program function.
    """
    print_intro()
    start_game()
    end_of_program()
    return

main()