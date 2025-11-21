import random
from VD_games.engine import run_game

DESCRIPTION = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, correct_answer


def main():
    run_game(generate_question, DESCRIPTION)
if __name__ == '__main__':
    main()
