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
SKULL = '\u2620'
LETTER = '\u2753'


# Global variables
player_name = ''
perk_inteligence = 0
perk_luck = 0
perk_charisma = 0
alphabet = ('abcdefghijklmnopqrstuvwxyz')
game_winner = True
levels = [1, 2, 3, 4]
launch_time = 0
numbers_picked = []
# max number of rows in worksheet
# if amount of words incresed, this needs to be updated
max_word_number = 50


def random_word_number():
    """
    Function generates number 1-max_word_number and checks if not
    generated previously.
    """
    # Run this loop until generated number not in
    # already picked numbers
    while True:
        generated = random.randint(1, max_word_number)
        if generated not in numbers_picked:
            numbers_picked.append(generated)
            return generated


def display_text(row, column, delay=0.012):
    """
    Function displays large portions of text from connected google
    sheet with typewriter effect.
    Function takes number of line and column as parameter.
    """
    # Clear screen
    clear_screen()
    # Call Google sheets and select column A and row from function parameter.
    text_worksheet = SHEET.worksheet("text")
    text_to_write = text_worksheet.cell(row, column).value
    text_to_write = text_to_write.replace('PLAYER', player_name)
    text_to_write = text_to_write.replace('BREAK', '\n')
    # Write imported text with 0.012 seconds delay after each character typed.
    print(Fore.YELLOW + '┌────────────────────', end='')
    print('───────────────────┐' + Style.RESET_ALL)
    print(Fore.YELLOW + f'│      {SKULL}  Meantime in ', end='')
    print(f' Wasteland {SKULL}      │' + Style.RESET_ALL)
    print(Fore.YELLOW + '└────────────────────', end='')
    print('───────────────────┘' + Style.RESET_ALL)
    print(Fore.GREEN + '')
    for char in text_to_write:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print('' + Style.RESET_ALL)
    wait_until_keypressed()
    return


def update_history():
    """
    Function updates sheet on google drive with players name,
    date, time and perk selected by user.
    """
    # Open Google worksheet
    history_worksheet = SHEET.worksheet("history")
    # Get current time and date
    start_time = str(datetime.now().time())
    date_now = str(datetime.now().date())
    # Update history worksheet with name, date, time and used perks.
    history_worksheet.append_row([
        player_name, date_now, start_time,
        perk_inteligence, perk_luck, perk_charisma
    ])


def word_guess(difficulty, guesses):
    """
    Function randomly takes a word from google sheet.
    Function takes parameter of difficulty = length of word selected.
    Function take parameter of guesses = how many guesses does player have.
    """
    # Initial setting for color and value of message returned to player
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
    # difficulty = length of word and generated number.
    random_number = random_word_number()
    word_to_guess = words_sheet.cell(random_number, difficulty).value
    # Cycle that runs until word fully guessed or player
    # does not run out of guesses.
    while word_guessed_correctly is False and guesses > 0:
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
            clear_screen()
            print(Fore.GREEN + 'Great, the hidden word was :', end=' ')
            print(f': "{word_to_guess}" !' + Style.RESET_ALL)
            wait_until_keypressed()
            return True
        # Player sees the following information.
        clear_screen()
        print(Fore.YELLOW + '┌────────────────────', end='')
        print('───────────────────┐' + Style.RESET_ALL)
        print(Fore.YELLOW + f'│      {LETTER}    Guess the ', end='')
        print(f' Word   {LETTER}         │' + Style.RESET_ALL)
        print(Fore.YELLOW + '└────────────────────', end='')
        print('───────────────────┘' + Style.RESET_ALL)
        print(Fore.BLUE + '\n')
        print(f'Your word to guess is {difficulty} letters long.')
        print(f'Your progress : {progress_word}')
        print(f'You already tried this letters : {letters_guessed}')
        print(f'Guesses left : {guesses}')
        print('\n' + Style.RESET_ALL)
        # Statement that changes color of message depends
        # on the importance of message.
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
                message = 'You already tried this letter ...'
            # Input is not in the word to guess.
            elif player_guess not in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 1
                message = 'The letter is not in the hidden word ...'
            # Correct guess.
            elif player_guess in word_to_guess:
                letters_guessed.append(player_guess)
                guesses -= 1
                message_color = 3
                message = "That's correct ;)"
            else:
                message_color = 2
                message = 'Something went wrong ...'
        # Player guessed the whole word and the lenght of word is correct.
        elif len(player_guess) == len(word_to_guess):
            # Correct word.
            if player_guess == word_to_guess:
                clear_screen()
                print(Fore.GREEN + 'Great, the hidden word was', end=' ')
                print(f': "{word_to_guess}" !' + Style.RESET_ALL)
                wait_until_keypressed()
                return True
            # Incorrect word.
            else:
                message_color = 1
                message = 'Thats not the word ...'
                guesses -= 1
        # Player tries to pass in empty string.
        elif len(player_guess) == 0:
            message_color = 2
            message = 'Your guess cannot be empty ...'
        # The length of word to guess and players guess are different.
        else:
            message_color = 1
            message = 'Length of your guess isnt same to the lenght of word.'
    clear_screen()
    print(Fore.RED + 'The hidden word was', end=' ')
    print(f': "{word_to_guess}" !' + Style.RESET_ALL)
    wait_until_keypressed()
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
        if wrong_name is True or player_name.isalpha() is True:
            print(Fore.RED + 'Your name was invalid !', end=' ')
            print('Try again !' + Style.RESET_ALL)
        # Players name input
        print(Fore.BLUE + "What's your name ? Only letters." + Style.RESET_ALL)
        player_name = input('')
        # If player tries to pass empty string
        if len(player_name) > 0 and player_name.isalpha() is True:
            player_name = player_name.capitalize()
            wrong_perk = False
            # Selection of perk
            while True:
                clear_screen()
                print('\n\n\n')
                print(Fore.YELLOW + '┌───────────────────────────────', end='')
                print('───────────────────────────────────┐' + Style.RESET_ALL)
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'I', end=' ')
                print(Fore.WHITE + '- Intelligent - shortens the leng', end='')
                print('th of guesed word by 1 letter' + Fore.YELLOW + ' │')
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'L', end=' ')
                print(Fore.WHITE + '- Lucky - adds 5 extra guesses', end=' ')
                print('to your guess count' + Fore.YELLOW + '             │')
                print(Fore.YELLOW + '│ ' + Fore.GREEN + 'C', end=' ')
                print(Fore.WHITE + '- Charismatic - reveals an ext', end='')
                print('ra letter in guessed word' + Fore.YELLOW + '        │')
                print(Fore.YELLOW + '└──────────────────────────────', end='')
                print('────────────────────────────────────┘')
                print(Fore.BLUE + f"Hello {player_name},The Chosen O", end='')
                print("ne, select your perk.Press i,l or c." + Style.RESET_ALL)
                # Message thats displayed if selection of perk was incorrect.
                if wrong_perk is True:
                    print(Fore.RED + 'Your choice of perk was', end=' ')
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
        print(Fore.WHITE + '│ ' + Fore.GREEN + 'E' + Fore.WHITE + ' -', end='')
        print(' Exit                              │' + Style.RESET_ALL)
        print(Fore.WHITE + '└──────────────────────', end='')
        print('─────────────────┘' + Style.RESET_ALL)
        # Message to be displayed if selection was wrong.
        if wrong_choice is True:
            print(Fore.RED + 'Your choice was invalid !' + Style.RESET_ALL)
        print('Please make a menu choice, Press S, H or E.')
        # Reading players selection
        menu_choice = readchar.readchar()
        # calling functions based on players selection.
        if menu_choice.upper() == 'S':
            create_charater()
            break
        elif menu_choice.upper() == 'H':
            display_highscores()
            break
        elif menu_choice.upper() == 'E':
            clear_screen()
            print(Fore.YELLOW + '\nThank you for playing.\n' + Style.RESET_ALL)
            print('This project was creted as student portfolio\n', end='')
            print('project 3 by Tomas Kubancik in 2023.')
            sys.exit()
        # Return back to this loop if players selection was wrong.
        else:
            wrong_choice = True


def update_highscore():
    """
    Function updates Google sheet with game time
    of winner.
    """
    # Read current time
    finish_time = time.time()
    # Calculate game time
    play_time = finish_time - launch_time
    # Open Google worksheet
    highscore_worksheet = SHEET.worksheet("highscores")
    # Update highscores worksheet with name and play_time.
    highscore_worksheet.append_row([player_name, play_time])
    return


def end_of_game():
    """
    This function is called when game is over.
    Function displays text based on winning/loosing.
    Function calls for update_highscore function if user wins.
    """
    clear_screen()
    # Message to display if player wins.
    if game_winner is True:
        update_highscore()
        display_text(4, 1)
    # Message to display if player looses.
    elif game_winner is False:
        display_text(5, 1)
    return


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
    print(Fore.BLACK + pause_var + Style.RESET_ALL)
    return


def start_game():
    """
    Function starts the game in loop for different levels and difficulty.
    """
    # Call global variable.
    global game_winner, launch_time
    # Loop to iterate through levels.
    launch_time = time.time()
    for level in levels:
        row = 1
        # Display text according level.
        display_text(row, level)
        row = 2
        # Display text according level.
        display_text(row, level)
        # Call word_guess function with different level params.
        round_result = word_guess(level + 3, (level * 2) + 10)
        # If round lost = game over.
        if round_result is False:
            game_winner = False
            break
        row = 3
        # Display text according level.
        display_text(row, level)
        # Call word_guess function with different level params.
        round_result = word_guess(level + 3, (level * 2) + 10)
        # If round lost = game over.
        if round_result is False:
            game_winner = False
            break
        continue
    end_of_game()
    return


def display_highscores():
    """
    This function reads the worksheet highscores and pulls all values.
    Sorts out values by time in ascending order and prints first 10.
    If no entries 'No entries yet !' message is displayed.
    """
    clear_screen()
    print(Fore.GREEN + 'Top 10 players\n' + Style.RESET_ALL)
    # Open Google worksheet
    highscore_worksheet = SHEET.worksheet("highscores")
    # Get all values from worksheet
    highscore_data = highscore_worksheet.get_all_values()
    if len(highscore_data) == 0:
        print('No entries yet !')
    # Transform of string time in seconds to float time in seconds
    highsc_floats = [
        [each[0], float(each[1][:5].replace(',', '.'))]
        for each in highscore_data
    ]
    # Sort data from worksheet by the second value + ascending
    sorted_highscs = sorted(highsc_floats, key=lambda x: x[1], reverse=False)
    # For each entry print name and game_time
    # Stop at 10th entry
    position = 1
    for each in sorted_highscs[0:10]:
        # Convert float seconds into minutes with only
        # two decimal places
        time_rounded = round((each[1]) / 60, 2)
        # Print position in leaderboard, name of
        # player and time in minutes
        print(f'{position}. Player: {each[0]} - Time: {time_rounded} minutes.')
        position += 1
    wait_until_keypressed()
    return


def main():
    """
    Main program function.
    """
    while True:
        # Calling global variables
        global player_name, perk_inteligence, perk_luck
        global perk_charisma, game_winner, launch_time, numbers_picked
        # Redefining variables each time game is started
        # to avoid multiple perks and incorrect data used
        player_name = ''
        perk_inteligence = 0
        perk_luck = 0
        perk_charisma = 0
        game_winner = True
        launch_time = 0
        numbers_picked = []
        print_intro()


if __name__ == '__main__':
    main()
