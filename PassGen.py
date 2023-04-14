# Gerador de Senhas

# bibliotecas
import random
import string


# complexidade de senha nível I
def complexidade_I():

    senha = ''
    while True:
        if len(senha) < 5:
            senha = senha + str(random.randint(0,9))
        else:
            break
    return senha


# complexidade de senha nível II
def complexidade_II():

    senha = ''
    while True:
        if len(senha) < 10:
            senha = senha + random.choice(string.ascii_lowercase + string.digits)
        else:
            break
    return senha


# complexidade de senha nível III
def complexidade_III():

    senha = ''
    while True:
        if len(senha) < 15:
            senha = senha + random.choice(string.ascii_letters + string.digits + string.punctuation)
        else:
            break
    return senha


# Pergunta que inicia o programa
def pergunta_inicial():

    resposta = None
    while resposta not in['S','s','n','N']:
        resposta = input("\nVocê gostaria de criar uma nova senha (S/N)? ")

    return resposta


# Pergunta de complexidade
def pergunta_complexidade():

    complexidade = None
    while complexidade not in['I','II','III']:
        complexidade = input("\nQual o nível de complexidade que você quer que sua senha tenha (I, II, III)? ")

    return complexidade


# Programa main
def senha_nova():

    resposta = pergunta_inicial()

    if resposta in(['S', 's']):
        
        complexidade = pergunta_complexidade()

        if complexidade in('I'):
            senha = complexidade_I()
            print(f"\nAqui está sua senha de complexidade nível I: {senha}")
        elif complexidade in('II'):
            senha = complexidade_II()
            print(f"\nAqui está sua senha de complexidade nível II: {senha}")
        elif complexidade in('III'):
            senha = complexidade_III()
            print(f"\nAqui está sua senha de complexidade nível III: {senha}")
        
    else:
        print("\nObrigado, até logo!")


senha_nova()



 


