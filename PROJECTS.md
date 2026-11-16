# Project ideas

Each project is three new files: the code in `toolbox/`, the page in `pages/`, and the tests in `tests/`.  Keep the work in `toolbox/` and the display in `pages/`: functions and classes in `toolbox/` take ordinary Python values (strings, numbers, lists, dictionaries) and return results, so you can test them without the web page.

Every description below is a starting point.  You may change the details, as long as you say so in your proposal.

## Games

### Hangman

- **The game:** The computer picks a secret word.  The player guesses one letter at a time and has 6 wrong guesses before losing.
- **The page shows:** the word so far with blanks (`c _ a _ e`), the letters already guessed, and the number of wrong guesses left.
- **Code in `toolbox/`:** a `HangmanGame` class with a `guess(letter)` method, a method that returns the word so far, and methods that say whether the game is won or lost.  The words can come from `data/answers.txt`.
- **Tests:** a correct letter appears in the word so far; a wrong letter costs one guess; guessing every letter wins; 6 wrong guesses loses.

### Trivia quiz

- **The game:** Multiple-choice questions, one at a time, with a score at the end.
- **The page shows:** the question, the choices as buttons, whether the answer was right, and the score.
- **Code in `toolbox/`:** a `QuizGame` class that loads the questions from a CSV file you write and put in `data/` (columns such as `question,a,b,c,d,answer`), with methods to get the current question, answer it, and get the score.
- **Tests:** a right answer adds 1 to the score; a wrong answer does not; the game ends after the last question.

### Word scramble

- **The game:** The computer shuffles the letters of a word from `data/answers.txt`, and the player tries to unscramble it.
- **The page shows:** the scrambled letters, a box for the guess, and whether it is right.  A button gives a new word.
- **Code in `toolbox/`:** a function that scrambles a word, and a function or class that checks a guess.
- **Tests:** the scrambled word has exactly the same letters as the original; a correct guess is accepted; a wrong guess is not.

### Tic-tac-toe

- **The game:** The player (X) plays against the computer (O) on a 3 by 3 board.  The computer plays a random empty square.
- **The page shows:** the board as a grid of buttons, and who won or whether it is a draw.
- **Code in `toolbox/`:** a `Board` class with a method to make a move and a `winner()` method that checks rows, columns, and diagonals.
- **Tests:** three in a row, three in a column, and three on a diagonal each win; a full board with no winner is a draw; you cannot move to a square that is taken.

### Blackjack (simplified)

- **The game:** The player and the dealer each get two cards.  The player can "hit" (take a card) or "stand."  The dealer then takes cards until reaching 17.  The hand closest to 21 without going over wins.
- **The page shows:** both hands, their values, and the winner.
- **Code in `toolbox/`:** a `hand_value(cards)` function where number cards count their number, J, Q, and K count 10, and an ace counts 11 unless that would go over 21, then 1.  A deck can be a shuffled list.
- **Tests:** `hand_value(["A", "K"])` is 21; `hand_value(["A", "A", "9"])` is 21; `hand_value(["K", "Q", "5"])` is 25 (a bust).

### Mastermind

- **The game:** The computer picks a secret code of 4 colors.  The player has 10 guesses.  After each guess, the player learns how many colors are right and in the right place, and how many are right but in the wrong place.
- **The page shows:** the past guesses and their feedback, and whether the player has won.
- **Code in `toolbox/`:** a `score(secret, guess)` function, much like Wordle's `score`, and a class for the game.
- **Tests:** a perfect guess gives 4 in the right place; repeated colors are counted correctly (for example, a secret with one red and a guess with two reds).

## Tools

### Grade calculator

- **The tool:** The user enters scores and weights for each part of a course and sees the overall grade, and what they need on the final to reach a target grade.
- **The page shows:** input boxes for scores and weights, the current grade, and the score needed on the final.
- **Code in `toolbox/`:** a weighted-average function, and a function that computes the final exam score needed.
- **Tests:** scores of 90 and 80 with equal weights give 85; a target that is already reached needs 0; an impossible target is reported as impossible.

### Unit converter

- **The tool:** Convert between units: miles and kilometers, pounds and kilograms, °F and °C, cups and milliliters.
- **The page shows:** a number box, a menu of conversions, and the result.
- **Code in `toolbox/`:** a dictionary of conversion factors and a `convert(value, from_unit, to_unit)` function.  Temperature needs its own formula.
- **Tests:** 212 °F is 100 °C; 1 mile is about 1.609 km (compare with `round`); converting there and back gives the original value.

### Recipe scaler

- **The tool:** The user enters a recipe (ingredients, amounts, and how many people it serves) and a new number of people, and sees the new amounts.
- **The page shows:** the ingredients table and the scaled amounts.
- **Code in `toolbox/`:** a function that takes a dictionary of amounts and the old and new number of servings, and returns a new dictionary.
- **Tests:** doubling 2 eggs gives 4; scaling to the same number of servings changes nothing; the original dictionary is not changed.

### Team maker

- **The tool:** The user pastes a list of names and picks a team size, and the tool makes random teams.
- **The page shows:** the teams, and a button to shuffle again.
- **Code in `toolbox/`:** a function that takes a list of names and a team size and returns a list of teams.  Decide what to do with leftover people, and say so on the page.
- **Tests:** every name appears in exactly one team; 10 names in teams of 3 gives team sizes you expect; no team is empty.

### Text statistics

- **The tool:** The user pastes a piece of text and sees statistics about it.
- **The page shows:** the number of words, the most common words, the longest word, the average word length, and the reading time (at about 200 words per minute).
- **Code in `toolbox/`:** functions that take a string and return each statistic.  Decide how to handle capital letters and punctuation.
- **Tests:** `"the cat the"` has 3 words and `the` appears twice; an empty text has 0 words; if you ignore capital letters, `"The"` and `"the"` count as the same word.

### Wordle helper

- **The tool:** The user enters the guesses they made in today's Wordle and the colors they got, and sees which words are still possible.
- **The page shows:** boxes for each guess and its colors, the number of words still possible, and the words themselves.
- **Code in `toolbox/`:** a function that keeps the words from `data/answers.txt` that match every clue, using `score` from `toolbox/wordle.py`.
- **Tests:** after `slate` with 5 gray letters, no remaining word contains s, l, a, t, or e; the secret word is always still in the list.

### Ranked-choice ballots (three options)

In a ranked-choice election, voters rank the candidates in order.  Many places publish every ballot (without names), called a **cast vote record**.  These projects read real ballots and report what voters did.  There are three options, one for each source of data.  They compute the same statistics; what differs is the kind of file you read.

All three options:

- **The page shows:**
  - the number of ballots;
  - the number of first-choice votes for each candidate;
  - the number of **bullet votes** (ballots that rank exactly one candidate);
  - the number of **complete rankings** (ballots that rank every candidate, or fill every rank);
  - how many ballots rank 0, 1, 2, 3, ... candidates;
  - the number of blank ballots and, if your data records them, of ballots with an overvote (two candidates marked at the same rank).
- **Code in `toolbox/`:** a function that reads the data into a list of ballots (each ballot a list of the names it ranks, in order), and one function per statistic that takes the list of ballots.  Let the user upload another file in the same format with `st.file_uploader`.
- **Tests:** use a few made-up ballots, such as `[["Ana"], ["Ana", "Ben"], ["Ben", "Ana", "Cy", "Di"], []]`: with 4 candidates there is 1 bullet vote, 1 complete ranking, and 1 blank ballot.
- **Going further:** run the instant-runoff count: repeatedly remove the candidate with the fewest first choices and move those ballots to their next choice.

#### Option A: Alaska, November 2026 (JSON files)

Alaska elects its governor, its U.S. senators, its U.S. representative, and its state legislators with ranked-choice voting.  On the [results page](https://www.elections.alaska.gov/election-results/e/), "Download Cast Vote Record" gives a zip file of JSON files, exactly as the voting machines exported them, so you will need Python's `json` module.

- `ContestManifest.json` lists the races, and `CandidateManifest.json` gives each candidate's `Id` and name (`Description`).
- Each `CvrExport_N.json` file holds a list of `Sessions`, one per ballot.  Inside a session, use `Modified` if it is there, and `Original` otherwise; from there, follow `Cards`, then `Contests` (whose `Id` says which race), then `Marks`.
- Each mark has a `CandidateId`, a `Rank`, and `IsVote`.  Count only the marks where `IsVote` is true.
- Start with one `CvrExport` file and one race.  The full zip is too big for the live site, so put the two manifest files and a few `CvrExport` files in `data/`.

#### Option B: PrefLib (text files)

[PrefLib](https://preflib.github.io/PrefLib-Jekyll/) is a library of real election data.  For example, [2009 Minneapolis](https://preflib.github.io/PrefLib-Jekyll/dataset/00018) has ballots from two city races.

- The files are plain text.  Lines starting with `#` describe the election, including the candidates: `# ALTERNATIVE NAME 1: "Carol Becker"`.
- Each later line is a group of identical ballots: `1257: 1,5` means that 1,257 voters ranked candidate 1 first and candidate 5 second.
- Choose the `.soi` files: each ballot ranks some of the candidates, in strict order.

#### Option C: the Otis collection (CSV files)

[Ranked Choice Voting Cast Vote Records](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/AMK8PJ) (Otis, Harvard Dataverse) has CSV files of ballots from many American ranked-choice elections.

- Choose one election and download its file.
- Open the file and look at its header row first, to see how the ranks are stored.
- Read it with the `csv` module.

### Maryland election results

The Maryland State Board of Elections publishes the results of every election as CSV files: see [the 2024 election data files](https://www.elections.maryland.gov/elections/archive/2024/election_data/index.html) and [how to use them](https://elections.maryland.gov/elections/using_election_data_instructions.html).  The files are numbered by county; Prince George's County, where College Park is, is county 17.

- **The tool:** The user uploads a county results file and chooses an office, and sees the results for that office.
- **The page shows:** the candidates, their votes and percentages, the winner, and a bar chart (`st.bar_chart`).
- **Code in `toolbox/`:** a function that reads the file into a list of rows, a function that lists the offices, and a function that returns the votes for each candidate in one office.  Open the file first and look at its header row to see which columns hold the office, the candidate, and the vote total.
- **Tests:** use a few made-up rows in the same format: the votes for each candidate are added correctly, the percentages add up to 100, and the winner is the candidate with the most votes.

## Improve a game from class

For these projects, your file in `toolbox/` imports the code from class and builds on it, for example with a subclass.  Do not change `toolbox/wordle.py` or `toolbox/rps.py`.

### Wordle with a letter board

- **What it adds:** Below the guesses, show every letter of the alphabet in its best color so far: green, yellow, gray, or not yet guessed.
- **Code in `toolbox/`:** a subclass of `WordleGame` with a `letter_status()` method that returns a dictionary from each letter to its color.  A letter that was green once stays green.
- **Tests:** after one guess, its letters have the right colors and the other letters are "not guessed"; green beats yellow.

### Wordle with hints

- **What it adds:** A hint button that shows how many words are still possible, and one of them.
- **Code in `toolbox/`:** a subclass of `WordleGame` with a `possible_words()` method that keeps the words from `answers` that match every guess so far.
- **Tests:** before any guess, every answer is possible; the secret word is always in the list; the list never grows.

### A better Wordle bot

- **What it adds:** A new bot that beats `FilterPlayer`, on its own page where the user can watch it play and compare it with the filter bot.
- **Code in `toolbox/`:** a subclass of `FilterPlayer` that chooses its guess more cleverly, for example the word whose letters are most common among the words still possible.
- **Tests:** every guess is a legal word; it solves `crane`; its average number of turns on 50 secret words is lower than `FilterPlayer`'s.

### Rock, paper, scissors with a history

- **What it adds:** A table of every round so far: your move, the computer's move, and who won.
- **Code in `toolbox/`:** a subclass of `RPSMatch` whose `play_round` calls `super().play_round(...)` and also adds the round to a `history` list.
- **Tests:** after three rounds, the history has three entries in the right order; each entry has the correct winner.

### Rock, paper, scissors with statistics

- **What it adds:** Your wins, losses, and ties, and your most common move.
- **Code in `toolbox/`:** a subclass of `RPSMatch` that counts results and moves in dictionaries.
- **Tests:** after a known sequence of rounds (use `always_rock` as the opponent), the counts are correct; the most common move is right.

### Rock, paper, scissors against a learning bot

- **What it adds:** A new opponent that counts your moves and plays the move that beats the one you have played most often.
- **Code in `toolbox/`:** a subclass of `RPSMatch` that keeps a dictionary counting your moves, and uses `beat` from `toolbox/rps.py` to choose the computer's move.
- **Tests:** after you play rock three times, it plays paper; with no history yet, it still returns a legal move.
