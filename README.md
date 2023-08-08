# ***Fallout Mini - Hangman - Portfolio Project 3***
---
# **1. Key project information**

- **Description :** This Portfolio Project 3, PYTHON program called **Fallout Mini - Hangman** is an online game (hangman quiz) that allows the user to test their vocabulary, progress through a story line that is based on Fallout 2 RPG game and make an entry to leder board.
- **Key project goal :** To entertain users of this program and test their vocabulary knowledge attempting the **Fallout Mini - Hangman** game.
- **Audience :** There's no age or any other limit to audience of this application. Target audience are any users searching for simple vocabulary games.
- **Live version :** Live version of **Fallout Mini - Hangman** game can be viewed [here](https://fallout-hangman-b9afc22725df.herokuapp.com/) .

![Mock Up](/docs/game.gif)

---

# **2. Table of content**

- [1. Key project information](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#1-key-project-information)
- [2. Table of content](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#2-table-of-content)
- [3. Description of functionality and rules](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#3-description-of-functionality)
- [4. Functions](https://github.com/tomik-z-cech/PP3-Fallout-Hangman#4-functions)

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

*Appendix  - Story line*

![Story line](/docs/storyline.png)

*Appendix 5 - Correct guess*

![Correct guess](/docs/correct_letter.png)

*Appendix 6 - Inorrect guess*

![Incorrect guess](/docs/incorrect_letter.png)

*Appendix 7 - Letter already guessed*

![Letter already guessed](/docs/already_guessed.png)

*Appendix 8 - High Scores*

![High Scores](/docs/highscores.png)

---

# **4. Functions**