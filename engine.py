def run_game(game_module, description):
    print("VD-games")
    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(description)
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if str(user_answer) == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
