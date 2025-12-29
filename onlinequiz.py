import time

QUESTIONS = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "Error"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": "Tuple"
    }
]

TIME_LIMIT = 30  # seconds
SCORE_FILE = "scores.txt"

def start_quiz():
    score = 0
    start_time = time.time()

    for q in QUESTIONS:
        if time.time() - start_time > TIME_LIMIT:
            print("\n⏰ Time's up!")
            break

        print("\n" + q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Enter option number: "))
            if 1 <= choice <= len(q["options"]):
                if q["options"][choice - 1] == q["answer"]:
                    score += 1
            else:
                print("Invalid option. Skipping question.")
        except ValueError:
            print("Invalid input. Skipping question.")

    return score

def save_score(name, score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{name} - {score}\n")

def view_scores():
    print("\n📊 Scoreboard")
    try:
        with open(SCORE_FILE, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No scores available yet.")

def main():
    while True:
        print("\n--- Online Quiz Application ---")
        print("1. Start Quiz")
        print("2. View Scoreboard")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            score = start_quiz()
            print(f"\n✅ Quiz completed! Your score: {score}/{len(QUESTIONS)}")
            save_score(name, score)

        elif choice == "2":
            view_scores()

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Try again.")

main()
