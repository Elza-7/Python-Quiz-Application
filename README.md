# 🧠 Python Quiz Game

A simple command-line multiple-choice quiz game written in Python. Test your general knowledge with 10 questions, get your score and percentage, and play again as many times as you like.

## Features

- Personalized welcome using the player's name
- 10 multiple-choice questions (A/B/C/D)
- Instant feedback after every answer
- Final score and percentage
- Performance message based on your result
- Input validation: invalid answers (anything other than A/B/C/D), empty names and invalid yes/no replies are rejected and re-asked
- Option to replay the quiz without restarting the program

## Requirements

- Python 3.6 or higher

No external libraries are needed.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Run the game:

   ```bash
   python main.py
   ```

   If you are using PyCharm, open the project and click **Run ▶** on `main.py`.

## How to Play

1. Enter your name when prompted.
2. Read each question and type the letter of your answer (`A`, `B`, `C`, or `D`). Lowercase letters also work.
3. See your result at the end.
4. Type `yes` to play again, or anything else to exit.

## Sample Output

```
==============================
       PYTHON QUIZ GAME
==============================
Enter your name: Arun
Welcome  Arun
Let's start the quiz
==============================

 1. What is the capital of India?
A. Chennai
B. Mumbai
C. New Delhi
D. Kerala
Enter your answer (A/B/C/D): c
You answered correctly

...

========== RESULTS ==========
Total questions: 10
Your final score: 9 / 10
Your percentage: 90.0 %
Excellent Performance!
Do you want to play again? (yes/no):
```

## Scoring

| Percentage | Message |
|------------|---------|
| 80% and above | Excellent Performance! |
| 50% – 79% | Well Played! Keep Practising |
| Below 50% | You Tried your Best! Keep Learning |

## Project Structure

```
.
├── main.py      # Quiz game source code
└── README.md    # Project documentation
```

## Possible Improvements

- Shuffle the questions randomly
- Add a timer for each question
- Load questions from a JSON file
- Save high scores

## Author

Created by **Elza**

## License

This project is open source and free to use for learning purposes.