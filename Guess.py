# Guess the number

import random
import time

def guess_number():

    limit = int(input("\nDefine the limit: "))

    number = random.randint(1, limit)

    try_number = 0      # variavel referente a escolha do usuario
    tries = 3           # variavel tentativas
    result = 0          # variavel para definir o resultado

    print("\nAre you ready ?\n")
    time.sleep(1)

    while try_number != number and tries > 0:

        print(f"You have {tries} tries!!!")
        try_number = int(input(f"Choose a number between 0 and {limit}: "))

        if try_number > number:
            print(f"{try_number} is greater than the guess number\n")
        elif try_number < number:
            print(f"{try_number} is less than the guess number\n")
        elif try_number == number:
            result = 1
        else:
            result = 0

        tries = tries - 1         

    else: 
        if result == 0:
            print(f"Oh no :( you lose. The guess number is {number}")
        elif result == 1:
            print(f"Congratulations, you guessed the number {number}")

guess_number()