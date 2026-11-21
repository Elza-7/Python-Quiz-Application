while True:
    print("==============================")
    print("       PYTHON QUIZ GAME")
    print("==============================")
    player_name = input("Enter your name: ")
    print("Welcome ",player_name)
    print("Let's start the quiz ")
    print("==============================")
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Chennai", "B. Mumbai", "C. New Delhi", "D. Kerala"],
            "answer": "C"
        },
        {
            "question": "2. Which is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "B"
        },
        {
            "question": "3. Who is known as the Father of the Indian Constitution?",
            "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B. R. Ambedkar", "D. Sardar Patel"],
            "answer": "C"
        },
        {
            "question": "4. Which is the largest ocean in the world?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "5. Which language are we learning?",
            "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
            "answer": "B"
        },
        {
            "question": "6. How many continents are there in the world?",
            "options": ["A. Five", "B. Six", "C. Seven", "D. Eight"],
            "answer": "C"
        },
        {
            "question": "7. What is the chemical symbol for water?",
            "options": ["A. CO2", "B. O2", "C. H2O", "D. NaCl"],
            "answer": "C"
        },
        {
            "question": "8. Which animal is known as the King of the Jungle?",
            "options": ["A. Tiger", "B. Lion", "C. Elephant", "D. Leopard"],
            "answer": "B"
        },
        {
            "question": "9. What is the national animal of India?",
            "options": ["A. Lion", "B. Elephant", "C. Bengal Tiger", "D. Peacock"],
            "answer": "C"
        },
        {
            "question": "10. What is 25 × 4?",
            "options": ["A. 50", "B. 75", "C. 100", "D. 125"],
            "answer": "C"
        }
    ]
    score = 0

    for question in questions:
        print("\n",question["question"])
        for option in question["options"]:
            print(option)
        user_answer = input("Enter your answer (A/B/C/D): " ).upper()
        if user_answer == question["answer"]:

            score += 1
            print("You answered correctly")
        else:
            print("You answered incorrectly")
    total_questions =len(questions)
    percentage = (score/total_questions)*100
    print("\n========== RESULTS ==========")
    print("Total questions:",total_questions)
    print("Your final score:", score, "/", total_questions)
    print("Your percentage:", percentage, "%")
    if percentage >= 80:
        print("Excellent Performance!")
    elif percentage >= 50:
        print("Well Played!Keep Practising")
    else:
        print("You Tried your Best!Keep Learning")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break


