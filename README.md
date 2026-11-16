# HCAI 121 Final Project: The Class Toolbox

The Class Toolbox is a web app built by the whole class.  Each student adds **one game or one tool** to it.  When your work is accepted, it appears on the live site with your name on it.

Live site: [https://hcai121-toolbox.streamlit.app/](https://hcai121-toolbox.streamlit.app/)

You may use AI tools to help write your code, but you must be able to explain every line.

## The project at a glance

| | Part | Due | Points |
|---|------|-----|--------|
| 1 | **Warm-up:** send your first pull request | Mon 11/30 | 5 |
| 2 | **Proposal:** say what you will build | Mon 11/30 | 5 |
| 3 | **Build:** add your game or tool, and send it as a pull request | Fri 12/4 | 25 |
| 4 | **Evaluation:** explain and evaluate another student's code | Mon 12/7 | 10 |
| 5 | **Demo:** show your work in class and explain your code | Wed 12/9 | 5 |
| | **Total** | | **50** |

## Getting set up (once)

1. **Fork** this repository: click the *Fork* button at the top right of this page.  This makes your own copy of the repository on GitHub.
2. **Clone** your fork to your computer, and go into the folder:
   ```
   git clone https://github.com/YOUR-USERNAME/hcai121-toolbox.git
   cd hcai121-toolbox
   ```
3. **Install** what the app needs:
   ```
   uv venv
   uv pip install -r requirements.txt
   ```
4. **Run the app**:
   ```
   uv run streamlit run Home.py
   ```
   The app opens in your browser.  Press `Ctrl-C` in the terminal to stop it.
5. **Run the tests**:
   ```
   uv run pytest
   ```

## Part 1: Warm-up pull request (due Mon 11/30)

This is practice with the steps you will use in Part 3.

1. Make a branch:
   ```
   git checkout -b warm-up
   ```
2. In the `students` folder, make a file named `YOUR-USERNAME.txt` that contains your name (see `students/epacuit.txt`).
3. Commit and push:
   ```
   git add students
   git commit -m "Add my name"
   git push -u origin warm-up
   ```
4. On GitHub, go to your fork and click **Compare & pull request**, then **Create pull request**.

## Part 2: Proposal (due Mon 11/30)

Choose a project from the lists below, or propose your own idea.  **[PROJECTS.md](PROJECTS.md) describes each project in more detail:** what it does, what the page shows, what code goes in `toolbox/`, and what to test.  At most 3 students may do the same project: first come, first served.

On this repository's **Issues** tab, click **New issue**.  Title it "Proposal: *your project*", and say in a few sentences what you will build, what the user enters, and what the page shows.

**Games**

| Project | What the code in `toolbox/` does |
|---------|----------------------------------|
| Hangman | A `HangmanGame` class: guess a letter, show the word so far (`c_a_e`), count lives. |
| Trivia quiz | A `QuizGame` class that reads questions from a CSV file in `data/` and keeps score. |
| Word scramble | Pick a word from `data/answers.txt`, shuffle its letters, check the player's guess. |
| Tic-tac-toe | A `Board` class: make a move, check for a winner; the computer plays a random legal move. |
| Blackjack (simplified) | A hand value function where an ace counts as 1 or 11. |
| Mastermind | Score a guess against a secret code of colors, like Wordle's `score`. |

**Tools**

| Project | What the code in `toolbox/` does |
|---------|----------------------------------|
| Grade calculator | A weighted average, and the score you need on the final to get a target grade. |
| Unit converter | Conversions (miles and km, °F and °C, cups and ml) using a dictionary of factors. |
| Recipe scaler | Scale a dictionary of ingredient amounts to a new number of servings. |
| Team maker | Shuffle a list of names into groups of a chosen size. |
| Text statistics | Word counts, the longest word, and the reading time of a pasted text. |
| Wordle helper | Enter your guesses and colors, and see which words are still possible (uses our `score`). |
| Ranked-choice ballots: Alaska 2026 | Read the ballots from Alaska's November 2026 election (JSON files) and report first choices, bullet votes, complete rankings, and more. |
| Ranked-choice ballots: PrefLib | The same statistics for a ranked-choice election from PrefLib (text files). |
| Ranked-choice ballots: Otis collection | The same statistics for an American ranked-choice election from the Otis collection (CSV files). |
| Maryland election results | Upload a county results file from the Maryland State Board of Elections and show the votes for an office. |

**Improve a game from class**

Your new page builds on the code from class, without changing it: your file in `toolbox/` imports the class code, for example to make a subclass of `WordleGame` or `RPSMatch`.  (`pages/Wordle_Bots.py` works this way: it uses `toolbox/wordle.py` without changing it.)

| Your page | What it adds |
|-----------|--------------|
| Wordle with a letter board | Shows which letters you have used: green, yellow, gray, or not yet guessed. |
| Wordle with hints | A button that shows how many words are still possible. |
| A better Wordle bot | A new bot (a subclass of `FilterPlayer`) that beats the filter bot, playing on its own page. |
| Rock, paper, scissors with a history | Shows every past round: your move, the computer's move, and who won. |
| Rock, paper, scissors with statistics | Shows wins, losses, ties, and your most common move. |
| Rock, paper, scissors against a learning bot | An opponent that plays the move that beats your most common move. |

Two limits on any project: the code in `toolbox/` must do real work that your tests check, and it must not save data between visits (no to-do lists or trackers), because files saved on the live site are erased whenever it restarts.

## Part 3: Build it (pull request due Fri 12/4)

1. Start a new branch from `main`:
   ```
   git checkout main
   git checkout -b my-project
   ```
2. **Add three new files**, using a name nobody else has used.  Do not change any file that is already in the app.
   - `toolbox/your_project.py`: the Python code that does the work, as functions or a class, with no Streamlit code.
   - `pages/Your_Project.py`: the web page.  It imports your code from `toolbox/`.  Put `st.caption("by Your Name")` under the title.
   - `tests/test_your_project.py`: at least three tests of the code in `toolbox/`.

   Use the existing pages as models.  For a tool, see `pages/Tip_Calculator.py`, `toolbox/tip_calculator.py`, and `tests/test_tip_calculator.py`.  For a game, see `pages/Wordle.py`, `toolbox/wordle.py`, and `tests/test_wordle.py`.  If your game must remember something between clicks, keep it in `st.session_state`, as `pages/Wordle.py` does.
3. **Check it**: run `uv run streamlit run Home.py` and try your page, then run `uv run pytest`.  All tests must pass.  Commit each time something works:
   ```
   git add toolbox pages tests
   git commit -m "Describe what you changed"
   ```
4. **Push** and open a pull request, as in the warm-up:
   ```
   git push -u origin my-project
   ```
5. GitHub then runs all the tests in `tests/` on your code: your own tests, the tests for the existing pages, and a check that every page loads without crashing.  A green check means they all passed.  A red X means something failed: click **Details** to see which test failed and why, fix it, and commit and push again.  Your pull request updates automatically.

## Part 4: Evaluation (due Mon 12/7)

After the pull requests are merged, you will be assigned one game or tool made by another student.  Read its code and try it on the live site.  Then submit your answers to these three questions on ELMS (about 250 words in all):

1. **How it works.**  In your own words, explain how the game or tool works.  What does the code in `toolbox/` do: what is its main function or class, what goes in, and what comes out?  How does the page use it?  Refer to the actual function and variable names.
2. **What you would do differently.**  Pick one thing in the code or the design, and say how you would change it and why.
3. **A feature to add.**  Suggest one new feature and say how you would build it: which function or method you would add or change, and how you would test it.

## Part 5: Demo (Wed 12/9)

Show your game or tool on the live site, and be ready to explain your code and answer questions about it.

## How the app is organized

| Folder | What goes there |
|--------|-----------------|
| `pages/` | One file per game or tool: the web page.  Every file here shows up in the menu on the left. |
| `toolbox/` | The Python code that does the work. |
| `tests/` | Tests for the code in `toolbox/`. |
| `data/` | Data files, such as the Wordle word lists. |
| `students/` | One file per student, from the warm-up. |
