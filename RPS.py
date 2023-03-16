# Rock, Paper or Scissors game

import random

# Autenticando o valor digitador pelo usuário
def auth():


    while True:
        choice = input("\n'R' for Rock,'P' for Paper or 'S' for Scissors: ").upper()
        if choice in ['R','P','S']:
            return choice
        else:
            print("\nSomething it's wrong! \nPlease type 'R' for Rock,'P' for Paper or 'S' for Scissors: ")


def play_rps():
    
    
    print("\n********* Welcome to Rock, Paper or Scissors Game *********\n")
    print("********* Let's go!!! *********")

    exit_choice = False

    while exit_choice == False:
 
        user = auth()
        computer = random.choice(['P', 'R', 'S'])

        rps_dic = {
            'R':'Rock',
            'P':'Paper',
            'S':'Scissors'
        }

        print(f"\nYour choice was {rps_dic[user]} and the computer choice was {rps_dic[computer]}")
        
        if user == computer:
            print("Tie!")
            try_again = input("\nWould you like to try again(Y/N)? ").upper()
            if try_again == 'N':
                exit_choice = True
            
        elif (user == 'P' and computer == 'R') or (user == 'T' and computer == 'P') or (user == 'R' and computer == 'T'):
            print("Congrats, you win!")
            try_again = input("\nWould you like to play again(Y/N)? ").upper()
            if try_again == 'N':
                exit_choice = True
        else:
            print("You lose, try again.")
            try_again = input("\nWould you like to try again(Y/N)? ").upper()
            if try_again == 'N':
                exit_choice = True
    else:
        print("\nThank you to play the game!!!")

play_rps()