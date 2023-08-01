# Imports
import gspread
import json
import os
import random
import readchar
import sys
import time
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from datetime import datetime


# Google drive credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google sheets credentials
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
levels = [1]


def display_text(row, delay=0.012):
    """
    Function displays large portions of text from connected google
    sheet with typewriter effect.
    Function takes number of line as parameter.
    """
    # Call Google sheets and select column A and row from function parametr.
    text_worksheet = SHEET.worksheet("text")
    text_to_write = text_worksheet.cell(row, 1).value
    # Write imported text with 0.012 seconds delay after each character typed.
    print(Fore.GREEN + '')
    for char in text_to_write:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print('' + Style.RESET_ALL)
    return


def update_history():
    """
    Function updates sheet on google drive with players name,
    date, time and perk selected by user.
    """
    # Open Google worksheet
    history_worksheet = SHEET.worksheet("history")
    # Get current time and date
    time_now = str(datetime.now().time())
    date_now = str(datetime.now().date())
    # Update history worksheet with name, date, time and used perks.
    history_worksheet.append_row([
        player_name, date_now, time_now,
        perk_inteligence, perk_luck, perk_charisma
    ])


def word_guess(difficulty, guesses):
    """
    Function randomly takes a word from google sheet.
    Function takes parametr of difficulty = lenght of word selected.
    Function take parametr of guesses = how many gueses does player have.
    """
    # Initail setting for color and value of message returned to player
    # after each letter guess.
    message_color = 3
    message = ''
    # Initial setting of the word has not been guessed yet.
    word_guessed_correctly = False
    letters_guessed = []
    # Initial perks settings.
    difficulty -= perk_inteligence
    guesses += perk_luck
    if perk_charisma == 1:
        perk_charisma_used = 1
    else:
        perk_charisma_used = 0
    # Open Google worksheet.
    words_sheet = SHEET.worksheet("words")
    # Generate random number 1-50 and import a word based on
    # difficulty = lenght of word and genarated number.
    random_number = random.randint(1, 50)
    word_to_guess = words_sheet.cell(random_number, difficulty).value
    # Cycle that runs until word fully guessed or player
    # does not run out of guesses.
    while word_guessed_correctly is False and guesses > 0:
        clear_screen()
        print(f'Your word to guess is {difficulty} letters long.')
        # Initialize list of progress.
        progress_list = []
        # If perk charisma is used, reveal one letter each game.
        if perk_charisma_used == 1:
            charisma_position = random.randint(0, difficulty - 1)
            charisma_letter = word_to_guess[charisma_position]
            letters_guessed.append(charisma_letter)
            perk_charisma_used = 0
        # Append correctly guessed letters to progress list.
        for each in word_to_guess:
            if each in letters_guessed:
                progress_list.append(each)
            else:
                progress_list.append('-')
        # Transform progress list to a string
        progress_word = ''.join(progress_list)
        # If all letters are revealed (progress list has no '-'
        # value left), player wins.
        if '-' not in progress_list:
            return True
        # Player sees the following information.
        print(f'Your progress : {progress_word}')
        print(f'You already tried this letters : {letters_guessed}')
        print(f'You have {guesses} guesses left')
        # Statement that changes color of message depends
        # on the importnace of message.
        if message_color == 1:
            print(Fore.RED + f'{message}' + Style.RESET_ALL)
        elif message_color == 2:
            print(Fore.YELLOW + f'{message}' + Style.RESET_ALL)
        elif message_color == 3:
            print(Fore.GREEN + f'{message}' + Style.RESET_ALL)
        # Players input of a letter or the whole word.
        player_guess = input('Guess a letter or type the whole word : ')
        # If player have inputed only one character.
        if len(player_guess) == 1:
            # Input is not a letter.
            if player_guess not in alphabet:
                message_color = 1
                message = 'Input only letters ...'
            # Input was already selected previously.
            elif player_guess in letters_guessed:
                message_color = 2
                message = 'You already tried this letter'
            # Input is not in the word to guess.
            elif player_guess not in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 1
                message = 'The letter is not in it ...'
            # Correct guess.
            elif player_guess in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 3
                message = "That's correct"
            else:
                message_color = 2
                message = 'Something went wrong'
        # Player guessed the whole word and the lenght of word is correct.
        elif len(player_guess) == len(word_to_guess):
            # Correct word.
            if player_guess == word_to_guess:
                return True
            # Incorrect word.
            else:
                message_color = 1
                message = 'Thats not the word'
                guesses -= 1
        # Player tries to pass in empty string.
        elif len(player_guess) == 0:
            message_color = 2
            message = 'Your guess cannot be empty'
        # The lenght of word to guess and players guess are different.
        else:
            message_color = 1
            message = 'Length of your guess isnt same to the lenght of word'
    return False


def create_charater():
    """
    Function reads player's name and selection of perk.
    Function uses 'readchar' dependency.
    Players name can't be empty otherwise error message is returned.
    Perks selection can be only 'I' or 'L' or 'C' otherwise
    error message is returned.
    """
    # Initial variable of wrong name that's used later in function.
    wrong_name = False
    # Loop that finishes when correct name entered.
    while True:
        clear_screen()
        # Call for global variables.
        global player_name, perk_inteligence, perk_luck, perk_charisma
        print('\n\n')
        # Output on display for user.
        print(Fore.YELLOW + '┌────────────────────', end='')
        print('───────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'│      {MAN_EMOJI}  Create ', end='')
        print(f' character {WOMAN_EMOJI}         │' + Style.RESET_ALL)
        print(Fore.YELLOW + '└────────────────────', end='')
        print('───────────────────┘' + Style.RESET_ALL)
        # Message to display if entered name is not correct.
        if wrong_name is True:
            print(Fore.RED + 'Your name was invalid !', end=' ')
            print('Try again !' + Style.RESET_ALL)
        # Players name input
        print(Fore.BLUE + "What's your name ?" + Style.RESET_ALL)
        player_name = input('')
        # If player tries to pass empty string
        if len(player_name) > 0:
            wrong_perk = False
            # Selection of perk
            while True:
                clear_screen()
                print('\n\n\n')
                print(Fore.YELLOW + '┌───────────────────────────────', end='')
                print('───────────────────────────────────┐' + Style.RESET_ALL)
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'I', end=' ')
                print(Fore.WHITE + '- Inteligent - shortens the leng', end='')
                print('th of guesed word by 1 letter' + Fore.YELLOW + '  │')
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'L', end=' ')
                print(Fore.WHITE + '- Lucky - adds 5 extra guesses', end=' ')
                print('to your guess count' + Fore.YELLOW + '             │')
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'C', end=' ')
                print(Fore.WHITE + '- Charismatic - reveals an ext', end='')
                print('ra letter in guessed word' + Fore.YELLOW + '        │')
                print(Fore.YELLOW + '└──────────────────────────────', end='')
                print('────────────────────────────────────┘')
                print(Fore.BLUE + f"Hello {player_name},The Chosen O", end='')
                print("ne,select your perk.Press i,l or c." + Style.RESET_ALL)
                # Message thats displayed if selection of perk was incorrect.
                if wrong_perk is True:
                    print(Fore.RED + '      Your choice of perk was', end=' ')
                    print('invalid, try again !' + Style.RESET_ALL)
                # Reading players selection of perk
                perk_choice = readchar.readchar()
                # Setting perk based on players selection.
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
            # Calling updating function.
            update_history()
            # Calling function that starts game.
            start_game()
            return
        # Return back to the loop if name was not correct.
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
        # Print menu on screen.
        print('\n\n\n')
        print(Fore.YELLOW + '┌──────────────────', end='')
        print('─────────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'│ {NUCLEAR_EMOJI} Welcome to Fallout Mi', end='')
        print(f'ni - Hangman {NUCLEAR_EMOJI} │' + Style.RESET_ALL)
        print(Fore.YELLOW + '└──────────────────', end='')
        print('─────────────────────┘' + Style.RESET_ALL)
        print(Fore.WHITE + '┌──────────────────', end='')
        print('─────────────────────┐' + Style.RESET_ALL)
        print(Fore.WHITE + '│ ' + Fore.GREEN + 'S' + Fore.WHITE + ' -', end='')
        print(' Start Game                        │' + Style.RESET_ALL)
        print(Fore.WHITE + '│ ' + Fore.GREEN + 'H' + Fore.WHITE + ' -', end='')
        print(' High Scores                       │' + Style.RESET_ALL)
        print(Fore.WHITE + '└──────────────────────', end='')
        print('─────────────────┘' + Style.RESET_ALL)
        # Message to be displayed if selection was wrong.
        if wrong_choice is True:
            print(Fore.RED + 'Your choice was invalid !' + Style.RESET_ALL)
        print('Please make a menu choice, Press S or H.')
        # Reading players selection
        menu_choice = readchar.readchar()
        # calling functions based on players selection.
        if menu_choice.upper() == 'S':
            create_charater()
            break
        elif menu_choice.upper() == 'H':
            break
        # Return back to this loop if players selection was wrong.
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
    Function waits for any key to be pressed so
    user has time to read the text and continue
    when ready.
    """
    print('\n')
    print(Fore.YELLOW + 'Press anything to continue ...' + Style.RESET_ALL)
    # Dummy variable only waiting for any key to be pressed.
    pause_var = readchar.readchar()
    print(pause_var)
    return


def start_game():
    """
    Function starts the game in loop for different levels and difficulty.
    """
    # Loop to iterate through levels.
    for level in levels:
        clear_screen()
        display_text(level)
        wait_until_keypressed()
        clear_screen()
        display_text(level + 1)
        wait_until_keypressed()
        clear_screen()
        word_guess(level + 2, 10)
        level += 1
    return


def main():
    """
    Main program function.
    """
    print_intro()
    end_of_program()


if __name__ == '__main__':
    main()
