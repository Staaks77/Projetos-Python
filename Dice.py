# Play a dice

# biblioteca
import random

# validação do valor digitado pelo usuario
def auth_choose():
    while True:

        print("Choose a dice: \n1 - d4 \n2 - d6 \n3 - d8 \n4 - d12 \n5 - d20")    
        choice = int(input("Nº: "))
        
        if choice in[1,2,3,4,5]:
            return choice
        else:
            print("\nSomething it's wrong, please enter a valid number")

# Play
def dice():

    choice = auth_choose()

    role_type = {
        1:4,
        2:6,
        3:8,
        4:12,
        5:20
    }

    valor = random.randint(1,role_type[choice])

    print(f"\nThe dice chose was d{role_type[choice]}")

    print(f"The value is: {valor}")

dice()