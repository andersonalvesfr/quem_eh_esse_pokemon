import random

def texto_de_inicializacao():
    print("##############################################")
    print("### Bem-vindo ao jogo: Quem é esse pokemón ###")
    print("##############################################")

def carregar_nome_secreto_do_pokemon():
    arquivo = open("Base_de_nomes.txt", "r") #abre o arquivo no modo de leitura
    lista_com_nome_dos_pokemon = [] #cria a lista para carregar os nomes

    for i in arquivo:
        i = i.strip() #tira o \n
        lista_com_nome_dos_pokemon.append(i)

    arquivo.close()
    #print(lista_com_nome_dos_pokemon)

    escolher_o_nome_aleatório = random.randrange(0,len(lista_com_nome_dos_pokemon))
    nome_secreto_do_pokemon = lista_com_nome_dos_pokemon[escolher_o_nome_aleatório].upper()
    return nome_secreto_do_pokemon


def principal():
    texto_de_inicializacao()
    nome_secreto_do_pokemon = carregar_nome_secreto_do_pokemon()
    #print(nome_secreto_do_pokemon)

    sublinhado_pokemon = ["_" for j in nome_secreto_do_pokemon] #lista que gera os sublinhados com o nome do pokemon
    print(sublinhado_pokemon)

    tentativas = 0
    tentativas_totais = 0
    acertou = False

    while (not acertou):
        chute= input("Digite o seu palpite de letra: ")
        chute = chute.strip().upper()
        tentativas = tentativas + 1
        tentativas_totais = tentativas_totais + 1

        if chute in nome_secreto_do_pokemon:

            posicao_da_letra = 0
            for k in nome_secreto_do_pokemon:
                if (k.upper() == chute.upper()):
                    sublinhado_pokemon[posicao_da_letra] = k
                posicao_da_letra = posicao_da_letra + 1

            print(sublinhado_pokemon)
            acertou = "_" not in sublinhado_pokemon
            tentativas = 0

        elif (tentativas == 3):
            print("Você merece uma dica do professor Carvalho")
            numero_aleatório = random.randrange(0, len(nome_secreto_do_pokemon))
            print("O nome deste pokémon contém a seguinte letra {}".format(nome_secreto_do_pokemon[numero_aleatório]))
            tentativas = 0

        if (tentativas_totais == 10):
            print("Você esgotou o número de 10 tentativas, treine mais da próxima vez")
            print("O pokémon secreto era: {}". format(nome_secreto_do_pokemon))
            break

    if (acertou == True):
        print("#######################################")
        print("## Parabéns você é um mestre pokémon ##")
        print("#######################################")



if(__name__ == "__main__"):
    principal()