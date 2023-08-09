# ***Fallout Mini - Hangman - Portfolio Project 3***
---
# **1. Key project information**

- **Description :** This Portfolio Project 3, PYTHON program called **Fallout Mini - Hangman** is an online game (hangman quiz) that allows the user to test their vocabulary, progress through a story line that is based on Fallout 2 RPG game and make an entry to leder board.
- **Key project goal :** To entertain users of this program and test their vocabulary knowledge attempting the **Fallout Mini - Hangman** game.
- **Audience :** There's no age or any other limit to audience of this application. Target audience are any users searching for simple vocabulary games.

## **Live version :** Live version of **Fallout Mini - Hangman** game can be viewed [here](https://fallout-hangman-b9afc22725df.herokuapp.com/) .

![Mock Up](/docs/game.gif)

---
---

# **2. Table of content**

- [1. Key project information](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#1-key-project-information)
- [2. Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)
- [3. Description of functionality and rules](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#3-description-of-functionality)
- [4. Functions](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#4-functions)
- [5. Overall logical flow](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#5-overall-logical-flow)
- [6. Imports](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#6-imports)
    - [6.1. Modules](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#61-modules)
    - [6.2. requirements.txt](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#62-requirementstxt)
- [7. Google sheet](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#7-google-sheet)
- [8. Testing](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#8-testing)
    - [8.1. Developer testing](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#81-developer-testing)
    - [8.2. User testing](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
    - [8.2. Validator testing](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
    - [8.2. Bugs](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
- [9. Deployment](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#9-deployment)
    - [9.1. Transfer of progress from IDE](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
    - [9.2. Offline cloning](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
    - [9.3. Heroku](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#82-user-testing)
- [10. Technologies](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#10-technologies)
- [11. Credits](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#11-credits)

---
---

# **3. Description of functionality**

- After starting the program, user is prompted with `Main menu` with 3 options (Start the game, Highscores, Exit) *(appendix 1)*.
- If users selects "S" - Start Game, user is prompted with input of their name *(appendix 2)*.
- In next step, user is prompted with perk selection *(appendix 3)*:
  - **Intelligent** - shortens the hidden word by 1 letter
  - **Lucky** - adds extra 5 guesses each round of guessing
  - **Charismatic** - reveals 1 letter from each hidden word
- After selecting the perk, game starts inform the user of the story line and quests *(appendix 4)*.
- As the user completes the word guessing each time, story line moves on and length of hidden word increses. The output of each guess could be :
  - **Correct guess** - user is notified, number of guesses is decreased by 1,list of already guessed letters is updated, correctly guessed letter is revealed in the hidden word, if this was last hidden letter, user goes to next level *(appendix 5)*.
  - **Incorrect guess** - user is notified, number of guesses is decreased by 1,list of already guessed letters is updated, if this was last guess left game ends *(appendix 6)*.
  - **Letter already guessed** - user is notified *(appendix 7)*.
- If user fails to guess any of the hidden words, game finishes and program returns to `Main menu`
- If users guess all the hidden words correctly, game time based on starting and finishing the game is recorded and program returns to `Main menu`
- If users selects "H" - High Scores, list of 10 best players is displayed to user, user can return to `Main menu` after *(appendix 8)*.
- If users selects "E" - Exit, the program ends.

*Appendix 1 - Main menu*

![Main menu](/docs/main_menu.png)

*Appendix 2 - Name input*

![Name input](/docs/name_input.png)

*Appendix 3 - Perk selection*

![Perk selection](/docs/perk_selection.png)

*Appendix 4 - Story line*

![Story line](/docs/storyline.png)

*Appendix 5 - Correct guess*

![Correct guess](/docs/correct_letter.png)

*Appendix 6 - Inorrect guess*

![Incorrect guess](/docs/incorrect_letter.png)

*Appendix 7 - Letter already guessed*

![Letter already guessed](/docs/already_guessed.png)

*Appendix 8 - High Scores*

![High Scores](/docs/highscores.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **4. Functions**

- **Name :** `display_text(row, column, delay=0.012)`
- **Parameters :** `row` `column`
- **Goal :** Function is designed to display large amount of text with a type-writer effect.
- **Function :** Function calls `clear_screen()` first and then connects to Google worksheet - sheet 'text *(appendix 9)* and targets cell stated as parameters. Function reads this cell and replaces string `PLAYER` with variable `player_name` and string `BREAK` with `\n` to wrap lines in Heroku terminal in suitable positions.
- **Flow Chart :** *Appendix 10*

*Appendix 9 - Connected Google sheet - worksheet `text`**

![display_text()](/docs/text.png)

*Appendix 10 - display_text()*

![display_text()](/docs/display_text.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `clear_screen()`
- **Parameters :** None
- **Goal :** Function is designed to clear the terminal screen before next text is displayed. This scrren was made for compatibility between Windows and Unix systems, instead of changing multiple lines of code if enviroment is changed, the code needs to be only changed iside of this function.
- **Function :** Function only performs one line of code.
- **Flow Chart :** *Appendix 11*

*Appendix 11 - clear_screen()*

![clear_screen()](/docs/clear_screen.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `update_highscore()`
- **Parameters :** None
- **Goal :** Function is designed to update high score sheet in connected Google sheet `highscore` *(appendix 12)*.
- **Function :** Function reads current time and saves it, based on that function then claculates play time (Play Time = Finish Time - Start Time). Function then connects to Google sheet and appends row with player's name and play time in seconds (variables `player_name` and `play_time`)
- **Flow Chart :** *Appendix 13*

*Appendix 12 - Connected Google sheet - worksheet `highscores`*

![Worksheet highscores](/docs/worksheet_highscores.png)

*Appendix 13 - update_highscore()*

![update_highscore()](/docs/update_highscores.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `update_history()`
- **Parameters :** None
- **Goal :** Function is designed to update history sheet in connected Google sheet *(appendix 14)* for analytics purposes every time someone plays the game.
- **Function :** Function reads current date and time, opens Google sheet (worksheet `history`) and appends new row to the worksheet with player's name, date, time, perk (variables `player_name`, `date_now`, `start_time`, `perk_inteligence`, `perk_luck`, `perk_charisma`).
- **Flow Chart :** *Appendix 15*

*Appendix 14 - Connected Google sheet - worksheet `history`*

![Worksheet history](/docs/worksheet_history.png)

*Appendix 15 - update_history()*

![update_history()](/docs/update_history.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `wait_until_keypressed()`
- **Parameters :** None
- **Goal :** Function is designed to make a pause in program run and wait until user presses any key.
- **Function :** Function reads character pressed into variable `pause_var`. This variable is then "displayed" in black color so it is not visible in black backgrounded terminal. Priniting the variable `pause_var` is not neccessary, but it does avoid error message in code.
- **Flow Chart :** *Appendix 16*

*Appendix 16 - wait_until_keypressed()*

![wait_until_keypressed()](/docs/wait.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `display_highscores()`
- **Parameters :** None
- **Goal :** Function is designed to read high score sheet in connected Google sheet `highscore` *(appendix 11)* and display accordingly.
- **Function :** Function reads all values in `highscore' Google sheet, if any, displays first 10 in ascending order, if none message "No entries yet" is displayed.
- **Flow Chart :** *Appendix 17*

*Appendix 17 - display_highscores()*

![display_highscores()](/docs/display_highscores.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `end_of_game()`
- **Parameters :** None
- **Goal :** Function is designed to display winning/loosing meessage and call `update_highscore()` if user wins.
- **Function :** Function contains if/else statement determining if variable `game_winner` is True. If `game_winner` is True, highscores are update and congratulations message is displayed. If `game_winner` is False, then only loosing message is displayed.
- **Flow Chart :** *Appendix 18*

*Appendix 18 - end_of_game()*

![end_of_game()](/docs/end_of_game.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `random_word_number()`
- **Parameters :** None
- **Goal :** Function is designed to randomly generate number between 1 and variable `max_word_number`.
- **Function :** Function runs in loop. Each cycle function geneartes number between 1 and value of variable `max_word_number`. This variable is currently set to 50 as the database of words contain 50 entries for each word length. Variable `max_word_number` needs to be adjusted if the database of words is made broader. This function also contains if/else statement to ensure the randomly generated number was not generated already. The cycle is exited only if newly genearted number isn't inluded in `numbers_picked` list.
- **Flow Chart :** *Appendix 19*

*Appendix 19 - random_word_number()*

![random_word_number()](/docs/random.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `word_guess(difficulty, guesses)`
- **Parameters :** `difficulty` = length of guessed word, `guesses` = the amount of guesses per word
- **Goal :** Function prepares a hidden word and user needs to guess all the letters correctly or guess the whole word.
- **Function :** This function resets all the necessary variables first.`message_color = 3`, `message = ''`, `word_guessed_correctly = False`, `letters_guessed = []`.
After they are all reset, function recalculates variables `difficulty` and `guesses` based on perks lucks or inteligence were used, also if perk charisma was used, variable `perk_charisma_used` is set to 1.Function random_word_number is called and number returned. Function then opens Google worksheet ('words') and based on `difficulty` and returned random number targets a specific cell with a word in it. Then this function runs in cycle until either the word is guessed correctly or user runs out of guesses. All letters of hidden word are initially replaced with `'-'`, unless perk cahrisma was used, then one letter is left unhidden. User is prompted to guess a letter or type whe whole word. Depends on the letter being in hidden word or not, the next cycle is determined wirh message and all displayed information. 
- **Flow Chart :** *Appendix 20*

*Appendix 20 - word_guess(difficulty, guesses)*

![word_guess(difficulty, guesses)](/docs/word_guess.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `print_intro()`
- **Parameters :** None
- **Goal :** Function is designed to display Main Menu *(appendix 1)* and validate user choice between `S - Start Game` , `H - High Scores` or `E - Exit`.
- **Function :** Function prints Main menu and waits for a key to be pressed (`readchar` function). If users selection is between the letters S, H or E, program calls next function depending on selection, otherwise error message is displayed.
- **Flow Chart :** *Appendix 21*

*Appendix 21 - print_intro()*

![print_intro()](/docs/print_intro.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `create_character()`
- **Parameters :** None
- **Goal :** Function is designed to get user's name and perk selection, also to validate that `player_name` are only alphabetical characters and the perk selection is between the characters `I - Intelligence` , `L - Luck` or `C - Charisma`.
- **Function :** Likewise the previous function `print-intro()`, this function prints Perks menu and waits for a key to be pressed (`readchar` function). If users selection is between the letters I, L or C, program calls next function depending on selection, otherwise error message is displayed.
- **Flow Chart :** *Appendix 22*

*Appendix 22 - create_character()*

![create_character()](/docs/create_character.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

- **Name :** `start_game()`
- **Parameters :** None
- **Goal :** Function runs in loops (4 loops for full game). Thsi function calls the `word_guess` with parameters increasing every loop to make the game harder each loop. After each game, this function determies if user can go to next stage or should the game ends in case of user didn't guess the word correctly.
- **Function :** Function iterates through list `levels`. This list has currently 4 positions. Based on the next number in the `levels` list, parameters for `word_guess` function are determined. After each call for `word_guess` function, this function goes through if/else statement `game_winner` = True or False, `end_of_game` function is called then.
- **Flow Chart :** *Appendix 23*

*Appendix 23 - start_game()*

![start_game()](/docs/start_game.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **5. Overall Logical Flow**

*Appendix 24 - Overall flow chart*

![Overall Flowchart](/docs/overall.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **6. Imports**

## **6.1. Modules**

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

To ensure functionality of this program, variable modules had to be imported.

- **Name of module:** `readchar`
- **Function :** This module reads one character as user input, returning it as string with lenght 1. Waits until character is available.
- **Version used :** 4.0.5
- **Link to documentation:** [readchar](https://pypi.org/project/readchar/)

---

- **Name of module:** `colorama`
- **Function :** The Python colorama module is a cross-platform library that simplifies the process of adding color to terminal text. It provides a simple and convenient way to add ANSI escape codes to text, making it possible to color text output on Windows as well as other platforms.
- **Version used :** 0.4.6
- **Link to documentation:** [colorama](https://pypi.org/project/colorama/)

---

- **Name of module:** `googleauth`
- **Function :** This module, google-auth is the Google authentication library for Python. This library provides the ability to authenticate to Google APIs using various methods. It also provides integration with several HTTP libraries.
- **Version used :** 2.22.0
- **Link to documentation:** [google-auth](https://pypi.org/project/google-auth/)

---

- **Name of module:** `gspread`
- **Function :** This module, gspread is a Python API for Google Sheets. Opens a spreadsheet by title, key or url.
- **Version used :** 5.10.0
- **Link to documentation:** [gspread](https://docs.gspread.org/en/latest/)

---

- **Name of module:** `json`
- **Function :** This module enables Python programs to effortlessly communicate with web services, exchange data, and store structured information.
- **Version used :** built-in
- **Link to documentation:** [json](https://www.json.org/json-en.html)

---

- **Name of module:** `os`
- **Function :** This module provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system-dependent functionality.
- **Version used :** built-in
- **Link to documentation:** [os](https://docs.python.org/3/library/os.html)

---

- **Name of module:** `random`
- **Function :** This module is an in-built module of Python that is used to generate random numbers in Python. These are pseudo-random numbers means they are not truly random.
- **Version used :** built-in
- **Link to documentation:** [random](https://docs.python.org/3/library/random.html)

---

- **Name of module:** `sys`
- **Function :** This module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment. It lets us access system-specific parameters and functions.
- **Version used :** built-in
- **Link to documentation:** [sys](https://docs.python.org/3/library/sys.html)

---

- **Name of module:** `time`
- **Function :** This module provides many ways of representing time in code, such as objects, numbers, and strings. It also provides functionality other than representing time, like waiting during code execution.
- **Version used :** built-in
- **Link to documentation:** [time](https://docs.python.org/3/library/time.html)

---

- **Name of module:** `datetime`
- **Function :** This module supplies classes for manipulating dates and times. While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation
- **Version used :** built-in
- **Link to documentation:** [datetime](https://docs.python.org/3/library/datetime.html)

---

## **6.2. requirements.txt**

In order for the program to work in Heroku terminal, file `requirements.txt` needs to be created with all third party imported modules. This is done with command `pip freeze > requirements. txt`. This command ensures that up-to-date `requirements.txt` *(appendix 25)* file is generated.

*Appendix 25 - requirements.txt*

![requirements.txt](/docs/requirements.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **7. Google sheet**

This project uses Google sheets.

**Reasons :** 
- Save large protions of text - sheet `(text)`
- Database of hidden words - sheet `(words)`
- Database of High Scores - sheet `(highscores)`
- Record of history of accesses - sheet `(history)`

It is necessary to implement the following code to access the file with given credentials *(appnedix 26)*.

[Google sheet credentials documentation](https://cloud.google.com/docs/authentication/provide-credentials-adc)

*Appendix 26 - Google sheets credentials*

![Google sheets credentials](/docs/credentials.png)

Also, very importandly, the same credentials need to be passed onto Heroku apllication *(appendix 27)*, including the `PORT = 8000` as config vars.

*Appendix 27 - Heroku settings*

![Heroku settings](/docs/heroku_settings.png)


[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **8. Testing**

## **8.1. Developer testing**

**Steps :** 
- Main Menu *(appendix 28)*
- Name Input *(appendix 29)*
- Perk Input *(appendix 30)*
- Guess Word *(appendix 31)*

*Appendix 28 - Main Menu test*

![Main Menu test](/docs/main_menu_test.png)

*Appendix 29 - Name Input test*

![Name Input test](/docs/name_input_test.png)

*Appendix 30 - Perk Input test*

![Perk Input test](/docs/perk_test.png)

*Appendix 31 - Guess Word test*

![Guess Word Input test](/docs/guess_word_test.png)

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

## **8.2. User testing**


|User|Nessa Bourke  |
|--|--|
| Feedback given | I really enjoyed using the program, instructions were clear and easy to follow and I especially loved the high score feature! It would be good to return to the main menu at any stage.|
| Applied changes | Added "0" as an option to all inputs to return to main menu. Commit [91c8830](https://github.com/tomik-z-cech/PP3-Fallout-Hangman/commit/91c8830299d6047dcf648f16d00cd7ed7a77bb64)  |
---
|User|Julie Carroll  |
|--|--|
| Feedback given | All functionality is good, please do spelling check. |
| Applied changes | Spelling check performed. Commit [fb2802d](https://github.com/tomik-z-cech/PP3-Fallout-Hangman/commit/fb2802df3ee5a27ce4358714909e4a4fbac1e8e8). |

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

## **8.3. Validator testing**

### PEP8 validator
- **Method :** Project (`run.py`) was tested by  [PEP8 validator](https://pep8ci.herokuapp.com/).
- **Result :** No errors were found when tested (*appendix 32*).

*Appendix 32 - PEP8 validator*

![PEP8 validator](/docs/pep8.png)

## **8.4. Bugs**

### Fixed bugs
Throughout testing, various bugs were discovered, especially with 79 characters long line. They were all fixed, committed and documented via GitHub.
 - Bug with inability to return to main menu from the game.
 - **Fix :** Add if/else statement to all user input. If `input = "0"` run function `print_intro`.
 - Error with line length of more than 79 characters.
 - **Fix :** Wrap lines using `end=''` code. 
 - In higher levels, the amount of guesses exceeded amount of letters in alphabet.
 - **Fix :** Introduce `round_result = word_guess(level + 3, (level * 2) + 10)` multiplication of 2 instead of 3.
 - When user plays game multiple times, perks are adding and user can avail of multiple perks.
 - **Fix :** Introduce `reset of all perk variables` in `main()` function.  

### Unfixed bugs
There are no know unfixed bugs as of 9.8.2023.

---
---

# **9. Deployment**

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

## **9.1. Transfer of progress from IDE**

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub
- **Finding :** CodeAnywhere IDE only holds up to 3 commitments in queue, regular `git push` needed to be used.

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

## **9.2. Offline cloning**

- **Task :** To use repository on local machine.
- **Method :** 
   - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . After those steps open your local coding environment and type `git clone [copied link]` .  
- **Finding :** Git Windows application needs to be installed.

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

## **9.3. Heroku

- **Task :** Enable users to acces the program via Heroku terminal.
- **Method :** 
   - Once the Heroku account and URL is linked with GitHub repository, the live program does update automatically.  
- **Finding :** Heroku termainl freezer after 1 minute inactivity.

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---


# **10. Technologies**

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---

# **11. Credits**

[Back to Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)

---
---