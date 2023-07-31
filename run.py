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
perk_inteligence = 0
perk_luck = 0
perk_charisma = 0
alphabet = ('abcdefghijklmnopqrstuvwxyz')

def display_text(row, delay=0.012):
    """
    Function displays large portions of text from connected google sheet with typewriter effect.
    Function takes number of line as parameter.
    """
    text_worksheet = SHEET.worksheet("text")
    text_to_write = text_worksheet.cell(row, 1).value
    print(Fore.GREEN + '')
    for char in text_to_write:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print('' + Style.RESET_ALL)
    return


def update_history():
    """
    Function updates sheet on google drive with players name, date, time and perk selected by user.
    """
    history_worksheet = SHEET.worksheet("history")
    time_now = str(datetime.now().time())
    date_now = str(datetime.now().date())
    history_worksheet.append_row([player_name, date_now, time_now, perk_inteligence, perk_luck, perk_charisma])

def word_guess(difficulty, guesses, revealed):
    message_color = 3
    message = ''
    word_guessed_correctly = False
    letters_guessed = []
    difficulty -= perk_inteligence
    guesses += perk_luck
    revealed += perk_charisma
    words_sheet = SHEET.worksheet("words")
    random_number = random.randint(1, 50)
    word_to_guess = words_sheet.cell(random_number, difficulty).value
    while word_guessed_correctly == False and guesses > 0:
        clear_screen()
        print(f'Your word to guess is {difficulty} letters long.')
        print(word_to_guess)
        progress_list = []
        for each in word_to_guess:
            if each in letters_guessed:
                progress_list.append(each)
            else:
                progress_list.append('-')
        progress_word = ''.join(progress_list)
        if '-' not in progress_list:
            return True
        print(f'Your progress : {progress_word}')
        print(f'You already tried this letters : {letters_guessed}')
        print(f'You have {guesses} left')
        if message_color == 1:
            print(Fore.RED + f'{message}' + Style.RESET_ALL)
        elif message_color == 2:
            print(Fore.YELLOW + f'{message}' + Style.RESET_ALL)
        elif message_color == 3:
            print(Fore.GREEN + f'{message}' + Style.RESET_ALL)
        player_guess = input('Guess a letter or type the whole word : ')
        if len(player_guess) == 1:
            if player_guess not in alphabet:
                message_color = 1
                message = 'Input only letters ...'
            elif player_guess in letters_guessed:
                message_color = 2
                message = 'You already tried this letter'
            elif player_guess not in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 1
                message = 'The letter is not in it ...'
            elif player_guess in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 3
                message = "That's correct"
            else:
                message_color = 2
                message = 'Something went wrong'
        elif len(player_guess) == len(word_to_guess):
            if player_guess == word_to_guess:
                return True
            else:
                message_color = 1
                message = 'Thats not the word'
        elif len(player_guess) == 0:
            message_color = 2
            message = 'Your guess cannot be empty'
        else:
            message_color = 1
            message = 'Length of your guess isnt same to the lenght of word'
    return False

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
                    perk_inteligence = 1
                    break
                if perk_choice.upper() == 'L':
                    perk_luck = 5
                    break
                if perk_choice.upper() == 'C':
                    perk_charisma = 1
                    break
                else:
                    wrong_perk = True
            update_history()
            start_game()
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

def wait_until_keypressed():
    """
    Function waits for any key to be pressed so user has time to read the text and continue when ready.
    """
    print('\n')
    print(Fore.YELLOW + 'Press anything to continue ...'+ Style.RESET_ALL)
    pause_var = readchar.readchar()
    return

def start_game():
    clear_screen()
    display_text(1)
    wait_until_keypressed()
    clear_screen()
    display_text(2)
    wait_until_keypressed()
    word_guess(3, 10, 1)
    return

print_intro()
end_of_program()