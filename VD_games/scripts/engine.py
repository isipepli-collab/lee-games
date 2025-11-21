import prompt


def run_game(game_module, description):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    if description:
        print(description)

    rounds_count = 3

    for _ in range(rounds_count):
        question, correct_answer = game_module.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
