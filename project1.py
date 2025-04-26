# quiz = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["Paris", "London", "Berlin", "Madrid"],
#         "answer": "Paris"
#     },
#     {
#         "question": "Who wrote 'Harry Potter'?",
#         "options": ["J.K. Rowling", "J.R.R. Tolkien", "Dan Brown", "Agatha Christie"],
#         "answer": "J.K. Rowling"
#     },
#     {
#         "question": "What is the largest planet in our Solar System?",
#         "options": ["Earth", "Venus", "Jupiter", "Mars"],
#         "answer": "Jupiter"
#     }
# ]
# score = 0

# for q in quiz:
#     print("\n" + q["question"])
#     for i, option in enumerate(q["options"], 1):
#         print(f"{i}. {option}")
    
#     answer = int(input("Enter the option number (1-4): "))
    
#     if q["options"][answer - 1] == q["answer"]:
#         print("Correct! ✅")
#         score += 1
#     else:
#         print(f"Wrong! ❌ The correct answer was: {q['answer']}")



# print("What is the capital of France?")
# print("1: paris")
# print("2: London")
# print("3: Berlin")
# print("4: Madrid")

# answer = int(input("enter your choice (1-4)"))
# if answer ==1:
#     print("sahi jawab")
# else:
#     print("Galat Jawab")



questions = [
    "What is the capital of France?",
    "Who wrote 'Harry Potter'?",
    "Which planet is known as the Red Planet?",
    "What is the largest mammal?",
    "Which ocean is the largest?",
    "Who invented the light bulb?",
    "Which language is used to create Android Apps?",
    "What gas do plants absorb?",
    "Which country gifted the Statue of Liberty to the USA?",
    "What is H2O commonly known as?"
]

options = [
    ["Paris", "London", "Berlin", "Madrid"],
    ["J.K. Rowling", "Dan Brown", "Tolkien", "Agatha Christie"],
    ["Earth", "Mars", "Jupiter", "Venus"],
    ["Elephant", "Blue Whale", "Giraffe", "Shark"],
    ["Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean"],
    ["Thomas Edison", "Albert Einstein", "Isaac Newton", "Nikola Tesla"],
    ["Python", "Kotlin", "Java", "HTML"],
    ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
    ["Germany", "France", "Italy", "Spain"],
    ["Water", "Hydrogen", "Oxygen", "Salt"]
]

answers = [1, 1, 2, 2, 4, 1, 3, 2, 2, 1]  # Correct option numbers (1-based)

score = 0

print("\n🎯 Welcome to the Quiz! 🎯\n")

for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    for j, option in enumerate(options[i], 1):
        print(f"   {j}. {option}")
    
    try:
        user_answer = int(input("👉 Enter your choice (1-4): "))
        
        if user_answer == answers[i]:
            print("✅ Correct!\n")
            score += 1
        else:
            correct_option = options[i][answers[i]-1]
            print(f"❌ Wrong! Correct Answer: {correct_option}\n")
    
    except ValueError:
        print("⚠️ Invalid input! Please enter a number.\n")

print(f"🏆 Your Final Score: {score}/{len(questions)}")
print("\nThanks for playing! 💖")

