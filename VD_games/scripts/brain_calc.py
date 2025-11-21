

import random


def get_user_input(prompt_text):

    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("Please enter a valid number! Try again.")


def generate_question():

    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])

    question = f"{num1} {operator} {num2}"

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2

    return question, correct_answer


def main():

    print("Welcome to the Brain Games!")
    name = input('May I have your name? ').strip()
    print(f'Hello, {name}!')
    print("What is the result of the expression?")

    rounds_count = 3
    correct_answers = 0

    for _ in range(rounds_count):
        question, correct_answer = generate_question()
        print(f'Question: {question}')

        user_answer = get_user_input('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answers == rounds_count:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
